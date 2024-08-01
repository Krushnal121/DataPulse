"""# Set up translation credentials
from azure.cognitiveservices.speech.translation import SpeechTranslationConfig

translation_config = SpeechTranslationConfig(subscription=speech_key, region=service_region)
translation_config.speech_recognition_language = "en-US"
translation_config.add_target_language("fr")

# Create a translation recognizer
audio_config = speechsdk.audio.AudioConfig(filename="path_to_audio.wav")
translation_recognizer = speechsdk.translation.TranslationRecognizer(translation_config=translation_config, audio_config=audio_config)

# Perform translation
result = translation_recognizer.recognize_once()

# Display translation
if result.reason == speechsdk.ResultReason.TranslatedSpeech:
    print(f"Translated Text: {result.translations['fr']}")
"""