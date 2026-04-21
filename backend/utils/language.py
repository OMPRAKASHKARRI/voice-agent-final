from deep_translator import GoogleTranslator


def detect_language(text):
    try:
        return GoogleTranslator(source='auto', target='en').detect(text)
    except:
        return "en"


def translate_to_english(text, lang):
    if lang == "en":
        return text
    try:
        return GoogleTranslator(source=lang, target='en').translate(text)
    except:
        return text


def translate_from_english(text, lang):
    if lang == "en":
        return text
    try:
        return GoogleTranslator(source='en', target=lang).translate(text)
    except:
        return text