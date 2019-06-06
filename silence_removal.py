import os
from pydub import AudioSegment


#path variables
print('Please specify the input folder :')
in_path=input()
if in_path=='':
    in_path='/home/HDD/voice2voice/tacotron2/female_lin_voice/female/'
elif in_path[-1:] != '/':
    in_path=in_path+'/'

print('Please specify the output folder :')
out_path=input()
if out_path=='':
    out_path='/home/HDD/voice2voice/tacotron2/female_lin_voice/female/'
elif out_path[-1:] != '/':
    out_path=out_path+'/'

#defined sound types
sound_types=['mp3','wav','ogg','aac','wma']

files=os.listdir(in_path)#reads the filenames from input folder

#function that finds the silence based on DB value
def detect_silence(sound):
    trim_ms = 0 # ms
    silence_threshold=-50.0
    chunk_size=10
    assert chunk_size > 0 # to avoid infinite loop
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size
    return trim_ms

for sound_file in files:
    try:
        print('In: ',sound_file)
        file_type=sound_file[sound_file.index('.')+1:]
        if file_type in sound_types:#proceed if sound type
            sound_type=file_type
            
            os.chdir(in_path)

            sound=AudioSegment.from_file(sound_file,sound_type)#load sound
            
            start_trim = detect_silence(sound)#find the silence in the begining of the sound
            end_trim = detect_silence(sound.reverse())#find the silence at the end of the sound
            duration = len(sound)#lenght of the sound without silence 
   
            trimmed_sound = sound[start_trim:duration-end_trim]
            
            os.chdir(out_path)

            trimmed_sound.export('trimmed-'+sound_file,format=sound_type)#save sound

            print('Out: ','trimmed-',sound_file,'\n')
            
    except:
        print('ERROR: ', sound_file)
        pass