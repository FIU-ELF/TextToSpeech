import os
import json
import ntpath
import requests
import azure.cognitiveservices.speech as speechsdk
#input your key from Azure Cognitive Services
key="" 
speech_config = speechsdk.SpeechConfig(subscription=key, region="eastus2")

# The language of the voice that speaks.
speech_config.speech_synthesis_voice_name='en-US-AmberNeural'
#speech_config.speech_synthesis_voice_name='es-ES-ElviraNeural'


Text_dir="text"
Wav_dir="wav"
Text_array=[]
Wav_array=[]
Speech_files=[]
for filename in os.listdir(Text_dir):
    f=filename.strip(".txt")
    Text_array.append(f)

for filename in os.listdir(Wav_dir):
    f=filename.strip(".wav")
    Wav_array.append(f)

for file in Text_array:
    if file not in Wav_array:
       Speech_files.append(file) 

if not Speech_files:
    print("Your wav files are complete, please delete the wav file you wish to redo. If your Text directory is empty, please add content.")
    exit()
else:
    print("Starting your batch")


for file in Speech_files:
    my_wav="".join([Wav_dir,"\\",file, ".wav"])
    my_txt="".join([Text_dir,"\\",file, ".txt"])
    file=open(my_txt,"r")
    lines=file.readlines()
    print(lines)
    audio_config = speechsdk.audio.AudioOutputConfig(filename=my_wav)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    text = lines
    speech_synthesis_result = speech_synthesizer.speak_text_async(str(text)).get()
    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")

   