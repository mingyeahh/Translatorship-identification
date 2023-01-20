import six
from google.cloud import translate_v2 as translate
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# Translate skeleton function code from google cloud translation: https://cloud.google.com/translate/docs/basic/translate-text-basic
def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    # print(u"Text: {}".format(result["input"]))
    # print(u"Translation: {}".format(result["translatedText"]))
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
    return result['translatedText']

IN_DIR_PO = Path('po')
OUT_DIR_PO = Path('po-en-goo')
IN_DIR_FR = Path('fr')
OUT_DIR_FR = Path('fr-en-goo')


# for i in IN_DIR_PO.iterdir():
#     with open(i) as f:
#         txt = f.read()

#     out = translate_text("en", txt)

#     with open(OUT_DIR_PO / i.name, 'w') as f:
#         f.write(out)

for i in IN_DIR_FR.iterdir():
    with open(i) as f:
        txt = f.read()

    out = translate_text("en", txt)

    with open(OUT_DIR_FR / i.name, 'w') as f:
        f.write(out)
