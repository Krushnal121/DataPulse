'''# Recognize speech (same as speech to text example)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
result = speech_recognizer.recognize_once()

# Display result
print(f"Recognized: {result.text}")
'''