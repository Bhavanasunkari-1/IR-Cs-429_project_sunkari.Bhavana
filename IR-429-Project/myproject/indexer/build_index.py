import json
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

def build_index(json_file, pickle_file):
    # Load data from JSON
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
        documents = [item['title'] for item in data]  # Adjust if your data structure differs

        # Create the TF-IDF representation
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(documents)

        # Save the vectorizer and matrix to a pickle file
        with open(pickle_file, 'wb') as f:
            pickle.dump((vectorizer, tfidf_matrix), f)

        print("Index has been built and saved successfully.")
    except Exception as e:
        print(f"An error occurred while building the index: {e}")

# Adjust the paths as necessary
json_path = '/mnt/c/users/pamid/Downloads/nws/myproject/data/destinations.json'  # Path to your JSON data file
pickle_path = '/mnt/c/users/pamid/Downloads/nws/myproject/data/tfidf_model.pkl'
  # Path to save the pickle file

if __name__ == '__main__':
    build_index(json_path, pickle_path)
