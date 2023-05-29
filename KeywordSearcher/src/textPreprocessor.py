import spacy
import nltk
# nltk.download('wordnet')

from spacy.lang.en.stop_words import STOP_WORDS
from nltk.stem import WordNetLemmatizer
class TextPreprocessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def preprocess_text(self, text):
        doc = self.nlp(text)
        tokens = []

        for token in doc:
            #remove stop words, punctuation and convert to lowercase
            if not token.is_stop and not token.is_punct:
                token_text = token.lemma_.lower().strip()

                if token_text != '\n\n' and token_text != ' ' and len(token_text) > 1:
                    tokens.append(token_text)
        
        #Lemmantization
        lemmatizer =  WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]

        #join the tokens back into a single string
        preprocessedText = ' '.join(tokens)
        return preprocessedText