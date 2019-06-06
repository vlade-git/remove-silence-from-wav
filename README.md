# remove-silence-from-wav
silence_removal.py is a python3 script that removes the silence in sound files at the beggining and the end of the sound file.

It uses the pydub library:
	https://github.com/jiaaro/pydub

Usage:
Run the script in open terminal in the folder containing the script with the command:
	python3 silence_removal.py

The script asks for input folder (where unprocessed files are) and output folder (where processed files should be saved) destination:

	Please specify the input folder :
	<destination to input folder>

	Please specify the output folder :
	<destination to output folder>

The script reads all the files from the input folder, but procceses only the sound files defined in 'sound_types' list.

Dependencies:
pydub library needs ffmpeg or libav to be installed prior to using the library.
More info:	https://github.com/jiaaro/pydub#dependencies
