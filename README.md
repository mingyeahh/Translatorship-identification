# Translatorship-identification

## About the project
This is a translatorship identification modelling project for human and machine translations. The research question is: Can we distinguish machine translation from human translation at the document level? The analysis object is Solaris by Stainslaw Lem. The main method for the project is by Machine Learning, Principal Component Analysis (PCA) and n-gram analysis.

## Dataset construction
Text documents are the chapters from each translation/book source.
* directory __`original`__ stores 
    * `fr-h`, `po-h`, `fr` -> human translations in different languages
    * `po` -> the orginal book in Polish (po)
    * `deepl-t.py` and `google-t.py` -> programs to autogenerate translations by DeepL and Google (API keys required)
    * `fr-dl`, `fr-goo` -> generated English translation from the French human translation by machines
    * `po-dl`, `po-goo` -> generated English translation from the French human translation by machines

* directory __`cleaned`__ stores the relavant data after data cleaning and processing


## Getting Started
Here is how you could utilise the code.

### Prerequisites
*  Python3 (pip included)

### Installation

```sh
pip install -r requirements.txt
```

## Usage

### Retranslate and reclean the dataset (optional)

1. Get API keys from [Google Translation AI](https://cloud.google.com/translate/docs/setup) and [DeepL AI](https://www.deepl.com/pro-api?cta=header-pro-api/)

2. Create a file in the `original/` directory called `.env` containing:

```
GOOGLE_APPLICATION_CREDENTIALS="path/to/credentials.json"
deepl_key = "123abc..."
```

3. Run
```
python3 deepl-t.py
```
```
python3 google-t.py
```

4. Open jupyter lab (or notebook) and navigate to the `Translatorship-identification` directory.

5. Open `data-processing.ipynb`.

6. Run all cells in `data-processing.ipynb`.




### Run analysis
1. Open jupyter lab (or notebook) and navigate to the `Translatorship-identification` directory.

2. Open `unigram`, `bigram`, or `trigram.ipynb`.

3. Run all cells in the notebook.
