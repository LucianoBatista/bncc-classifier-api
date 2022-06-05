import html
from nltk.tokenize import word_tokenize

import pandas as pd

from project.app.bncc_classifier import cleaning


class PreProcessing:
    def __init__(self, text: str) -> None:
        self.text = text
        self.clean_text = ""
        self.clean_df = None

    def prepro(self):
        df = pd.DataFrame({"item": [self.text]})
        df["clean_item"] = (
            df["item"]
            .astype(str)
            .apply(html.unescape)
            .apply(lambda x: cleaning.remove_html(x))
            .apply(lambda x: x.lower())
            .apply(lambda x: cleaning.remove_punctuation_2(x))
            .apply(cleaning.remove_italic_quotes)
            .apply(cleaning.remove_open_quotes)
            .apply(cleaning.remove_end_quotes)
            .apply(cleaning.remove_italic_dquotes)
            .apply(cleaning.remove_open_dquotes)
            .apply(cleaning.remove_quote)
            .apply(lambda x: cleaning.remove_pt_stopwords(x))
            .apply(lambda x: cleaning.remove_en_stopwords(x))
            .apply(word_tokenize)
            .apply(lambda x: cleaning.remove_frq_words(x))
            .apply(lambda x: cleaning.remove_rare_words(x))
        )

        self.clean_text = df["clean_item"].values[0]
        self.clean_df = df.copy()
