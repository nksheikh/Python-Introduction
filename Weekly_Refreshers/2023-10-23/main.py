import re
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')

from nltk.corpus import comtrans

try:
    stop_words = stopwords.words("english")
except LookupError:
    print('Resource not found. Downloading now...')
    nltk.download('stopwords')
    stop_words = stopwords.words("english")
    
try:
    nltk.data.find('tokenizers/punkt.zip')
except LookupError:
    print('Resource not found. Downloading now...')
    nltk.download('punkt')