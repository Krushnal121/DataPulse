"""#Speech to Text
# Install required libraries
!pip install azure-cognitiveservices-speech

import azure.cognitiveservices.speech as speechsdk

# Set up Speech SDK credentials
speech_key = "<your-speech-key>"
service_region = "your-region"

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
audio_config = speechsdk.AudioConfig(filename="path_to_audio.wav")

# Recognize speech
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
result = speech_recognizer.recognize_once()

# Display result
print(f"Recognized: {result.text}")

#Text to Speech
# Set up Speech SDK credentials
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
audio_config = speechsdk.audio.OutputFormat()

# Create a synthesizer
synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# Synthesize text to speech
text = "Hello, this is a text to speech conversion."
result = synthesizer.speak_text_async(text).get()

# Check result
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized successfully.")
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print(f"Speech synthesis canceled: {cancellation_details.reason}")
"""