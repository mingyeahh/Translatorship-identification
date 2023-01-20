import deepl
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

auth_key = os.getenv("deepl_key") 
translator = deepl.Translator(auth_key)

IN_DIR_PO = Path('po')
OUT_DIR_PO = Path('po-en-dl')
IN_DIR_FR = Path('fr')
OUT_DIR_FR = Path('fr-en-dl')

# for i in IN_DIR_PO.iterdir():
#     with open(i) as f:
#         txt = f.read()

#     out = translator.translate_text(txt, target_lang="EN-GB").text

#     with open(OUT_DIR_PO / i.name, 'w') as f:
#         f.write(out)

for i in IN_DIR_FR.iterdir():
    with open(i) as f:
        txt = f.read()

    out = translator.translate_text(txt, target_lang="EN-GB").text

    with open(OUT_DIR_FR / i.name, 'w') as f:
        f.write(out)

