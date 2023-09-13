# Text To Speech
Example of using Azure Cognitive Services Text to Speech to convert various text files to speech.

## Python Requirements
pip install azure-cognitiveservices-speech

## Create A Cognitive Service in your resource group

## Add key to speech_loop.py

## Instructions
One approach to slide making can be creating slides and then creating narrations for those slides. Azure's Text to Speech is a convenient way of creating voice overs for slides. With this script, we have a folder called "text" which contains the text files we want to use for our slides. In our example, slide1.txt corresponds to the text we want for slide 1.

Another folder called "wav" stores the output of the text files. It will read slide1.txt and convert it to slide1.wav containing your text to speech. For all unique txt file names it will do this.
To rerun the text to speech, assuming you wanted to make edits, just delete the wav file that you want to redo and alter your text. Rerunning the script will generate the missing wave file. 

This is a convenient way to batch create slide voiceovers.






