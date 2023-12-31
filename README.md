# Text To Speech
Example of using Azure Cognitive Services Text to Speech to convert various text files to speech for Hackathon 2022 and 2023 using Python.

## Python Requirements
pip install azure-cognitiveservices-speech

## Create A Cognitive Service in your resource group
First, create a cognitive speech service in Azure. Note, the python script is setup for region EastUS2. 
<p align="middle">
      <img src="/images/cog.png" alt="cognitive services" width="80%" height="80%">
</p>

## Add key to speech_loop.py

In the cognitive service, there will be a key. Copy it.
<p align="middle">
      <img src="/images/key.png" alt="cognitive services" width="80%" height="80%">
</p>

Then paste that key into this part of the python script.
<p align="middle">
      <img src="/images/pythonkey.png" alt="cognitive services" width="80%" height="80%">
</p>

## Instructions
One approach to slide making can be creating slides and then creating narrations for those slides. Azure's Text to Speech is a convenient way of creating voice overs for slides. With this script, we have a folder called "text" which contains the text files we want to use for our slides. In our example, slide1.txt corresponds to the text we want for slide 1.

Another folder called "wav" stores the output of the text files. It will read slide1.txt and convert it to slide1.wav containing your text to speech. For all unique txt file names it will do this.
To rerun the text to speech, assuming you wanted to make edits, just delete the wav file that you want to redo and alter your text. Rerunning the script will generate the missing wave file. 

This is a convenient way to batch create slide voiceovers.

To change the voice, update the below code from these choices: https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts#supported-languages

<p align="middle">
      <img src="/images/speech.png" alt="cognitive services" width="80%" height="80%">
</p>




