import re
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

# 1. Remove HTML formatting
# 2. Remove non-alphabet characters such as punctuation or numbers and replace with ' '
#     You may refer back to the slides for this part (We implement this for you)
# 3. Remove leading or trailing white spaces including any newline characters
# 4. Convert to lower case
# 5. Tokenize and remove stopwords using nltk's 'english' vocabulary
# 6. Rejoin remaining text into one string using " " as the word separator

class Preprocess():
    
    # 
    def __init__(self):
        self.download_resources()
    
    # Download English stopwords and punkt for nltk word_tokenize
    def download_resources(self):
        try:
            self.stop_words = stopwords.words("english")
            nltk.data.find("tokenizers/punkt.zip")
        except LookupError:
            print("Resource(s) not found. Downloading now...")
            nltk.download("stopwords")
            nltk.download("punkt")
            self.stop_words = stopwords.words("english")
            
	# STEP 1 - Noise Removal
    # -HTML formatting
	# -Punctuation and accent marks
	# -Special characters
	# -Numeric digits or replacing with word
	# -Leading, ending, and vertical whitespace
    # STEP 2 - Tokenization
    # STEP 3 - Text Normalization
    # -Convert all letters to lower or upper case
    # -Remove stop words, sparse terms, and particular words
    # -Stemming: reducing words to their word stem
    # -Lemmatization: reduces inflectional forms to a common base form
    def clean_text(self, text, html_flag = False):
        
        # Copy the provided text
        cleaned_text = text
        
        # If text is HTML, parse and remove formatting
        if html_flag:
            soup = BeautifulSoup(cleaned_text, features = "html.parser")
            cleaned_text = soup.get_text()
        
        # Convert all text to lower case
        cleaned_text = cleaned_text.lower()
        
        # Remove punctuation/accent marks, special characters, numeric digits, and extraneous spaces
        cleaned_text = re.sub('^\s+|\W+|[0-9]|\s+$',' ',cleaned_text).strip()
        
        # Tokenize text and remove stop words
        tokens = word_tokenize(cleaned_text)
        stop_words = list(stopwords.words("english"))
        cleaned_text = " ".join([token for token in tokens if token not in stop_words])
        
        # Stem and lemmatize words
        porter_stemmer = PorterStemmer()
        wordnet_lemmatizer = WordNetLemmatizer()
        stemmed_text = [porter_stemmer.stem(word) for word in cleaned_text]
        lemmatized_text = [wordnet_lemmatizer.lemmatize(word) for word in cleaned_text]
        