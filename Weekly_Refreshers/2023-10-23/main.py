import re
import pandas as pd
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, confusion_matrix, roc_auc_score
        
class Preprocess():

    # 1. Remove HTML formatting
    # 2. Remove non-alphabet characters such as punctuation or numbers and replace with ' '
    #     You may refer back to the slides for this part (We implement this for you)
    # 3. Remove leading or trailing white spaces including any newline characters
    # 4. Convert to lower case
    # 5. Tokenize and remove stopwords using nltk's 'english' vocabulary
    # 6. Rejoin remaining text into one string using " " as the word separator

    # Initialize the preprocessor
    def __init__(self):
        # nltk.download("stopwords")
        # nltk.download ('wordnet')
        # nltk.download("punkt")
        pass
            
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
    def clean_text(self, text, html_flag = False, norm_method = None):
        
        # Copy the provided text
        cleaned_text = text
        
        # If text is HTML, parse and remove formatting
        if html_flag:
            soup = BeautifulSoup(cleaned_text, features = "html.parser")
            cleaned_text = soup.get_text()
        
        # Convert all text to lower case
        cleaned_text = cleaned_text.lower()
        
        # Remove punctuation/accent marks, special characters, numeric digits and replace with " "
        #  and remove leading and trailing spaces and newlines
        cleaned_text = re.sub('^\s+|\W+|[0-9]|\s+$', ' ', cleaned_text)
        cleaned_text = cleaned_text.strip()
        
        # Tokenize text, modify them, and remove stopwords using nltk's 'english' vocabulary
        tokens = word_tokenize(cleaned_text)
        stop_words = set(stopwords.words("english"))
        
        # Select the text normalization method
        normalize = None
        if norm_method is None:
            normalize = lambda arg: arg
        elif norm_method == "stem":
            porter_stemmer = PorterStemmer()
            normalize = porter_stemmer.stem
        elif norm_method == "lemmatize":
            wordnet_lemmatizer = WordNetLemmatizer()
            normalize = wordnet_lemmatizer.lemmatize
        else:
            raise ValueError("Inappropriate Noramlization Method Provided")
        
        # Normalize all the non-stopword tokens and conjoin them
        norm_words = [normalize(token) for token in tokens if token not in stop_words]
        cleaned_text = " ".join(norm_words)
        return cleaned_text

class TextRepresentation():

    # Contruct the class initialzied with a corpus
    def __init__(self, corpus):
        self.corpus = corpus
    
    # Use the sklearn module to produce a one hot encoding representation for a corpus (collection of documents)
    def getonehotencoding(self, verbose = False):
        onehot_vectorizer = CountVectorizer(binary = True)
        onehot_vectorizer.fit(self.corpus)
        onehotencoded = onehot_vectorizer.transform(self.corpus).toarray()
        if verbose:
            print(f"The One Hot Encoding representation is:\n{onehotencoded}")
        
        # onehotencoded : (N, D) one hot encoded numpy array
        return onehotencoded
    
    # Use the sklearn module to produce a bag of words representation for a corpus
    def getbagofwords(self, verbose = False):        
        bow_vectorizer = CountVectorizer()
        bow_vectorizer.fit(self.corpus)
        bagofwords = bow_vectorizer.transform(self.corpus).toarray()
        if verbose:
            print(f"The Bag of Words representation is:\n{bagofwords}")
            
        # bagofwords : (N, D) bag of words numpy array
        return bagofwords

    # Use the sklearn module to produce a TF-IDF representation for a corpus
    def gettfidf(self, verbose = False):
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_vectorizer.fit(self.corpus)
        tfidf = tfidf_vectorizer.transform(self.corpus).toarray()
        if verbose:
            print(f"The TF-IDF representation is:\n{tfidf}")
        
        # tfidf : (N, D) tf-idf numpy array
        return tfidf

class NaiveBayesClassifications():
    
    # Construct the class with the encoded corpus representation and true labels
    def __init__(self, encoded_corpus, true_labels):

        # encoded_corpus: (N, D) numpy array of numerically encoded sentences
        # y : (N, ) numpy vector of labels
        
        self.encoded_corpus = encoded_corpus
        self.true_labels = true_labels
    
    def multinomnial_naivebayes(self):
        mnb_clf = MultinomialNB(force_alpha = True)
        mnb_clf.fit(self.encoded_corpus, self.true_labels.ravel())
        y_hat = mnb_clf.predict(self.encoded_corpus)
        
        # y_hat: (N,) numpy vector of labels
        return y_hat
        
    def guassian_naivebayes(self):
        gnb_clf = GaussianNB()
        gnb_clf.fit(self.encoded_corpus, self.true_labels.ravel())
        y_hat = gnb_clf.predict(self.encoded_corpus)
        
        # y_hat: (N,) numpy vector of labels
        return y_hat

class Metrics():
    
    # Initalize the metrics with the true and predicted values of classification
    def __init__(self):        
        pass
        
    def displaymetrics(self, y_true, y_pred, average = None):
        # average: None or string 'macro'
        
        # Compute the metrics
        accuracy = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred, average = average)
        recall = recall_score(y_true, y_pred, average = average)
        f1 = f1_score(y_true, y_pred, average = average)
        roc_auc = roc_auc_score(y_true, y_pred, average = average)
        matrix = confusion_matrix(y_true, y_pred)
        
        # Print the results
        metrics_mappings = {
            "accuracy score": accuracy,
            "precision score": precision,
            "recall score": recall,
            "f1 score": f1,
            "roc_auc": roc_auc,
            "confusiuon matrix": matrix
        }
        for metric in metrics_mappings:
            print(f"The {metric} was calcualted to be: {metrics_mappings[metric]}")

if __name__ == "__main__":
    
    split_ratio = 0.75
    df_data = pd.read_csv("G:/My Drive/Personal_Development/Programming_Projects/Python-Introduction/Weekly_Refreshers/2023-10-23/data/data.csv")
    threshold = round(split_ratio * df_data.shape[0])
    train = df_data.iloc[:threshold,]
    test = df_data.iloc[threshold:,]
    
    train_corpus = train["headline"].values.tolist()
    test_corpus = test["headline"].values.tolist()
    train_labels = train["label"].to_numpy().reshape(-1, 1)
    test_labels = test["label"].to_numpy().reshape(-1, 1)
    
    # Perform pre-processing
    pp = Preprocess()
    std_norm_corpus = [pp.clean_text(document, html_flag = False, norm_method = None) for document in train_corpus]
    stem_norm_corpus = [pp.clean_text(document, html_flag = False, norm_method = "stem") for document in train_corpus]
    lemma_norm_corpus = [pp.clean_text(document, html_flag = False, norm_method = "lemmatize") for document in train_corpus]
    
    # # Print the results
    # print(f"The original corpus is: {train_corpus}")
    # print(f"The standard text preprocessing yielded the corpus: {std_norm_corpus}")
    # print(f"The stemmed text preprocessing yielded the corpus: {stem_norm_corpus}")
    # print(f"The lemmatized text preprocessing yielded the corpus: {lemma_norm_corpus}")
    
    # Encode and display the different text representations
    tr = TextRepresentation(lemma_norm_corpus)
    ohe = tr.getonehotencoding()
    bow = tr.getbagofwords()
    tfidf = tr.gettfidf()
    
    # Perform Naive Bayes predictions
    nb = NaiveBayesClassifications(tfidf, train_labels)
    mb_pred_labels = nb.multinomnial_naivebayes()
    gn_pred_labels = nb.guassian_naivebayes()
    
    # Display the metrics
    m = Metrics()
    print("Display Mulinomnial NB Results...")
    m.displaymetrics(y_true = train_labels, y_pred = mb_pred_labels)
    print("Display Guassian NB Results...")
    m.displaymetrics(y_true = train_labels, y_pred = gn_pred_labels)