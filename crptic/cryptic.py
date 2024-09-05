import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from collections import Counter
from cryptography.fernet import Fernet
import os
import zipfile

# Set the correct directory path
file_path = os.path.join('C:\\Users\\sankh\\OneDrive\\Desktop\\whitesea\\crptic\\data')

# Function to read cipher text file
def read_cipher_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()

# Function to extract character frequency
def char_frequency(cipher_text: str) -> Counter:
    return Counter(cipher_text)

# Function to create bigrams
def create_bigrams(cipher_text: str) -> list:
    return [cipher_text[i:i+2] for i in range(len(cipher_text)-1)]

# Function to calculate entropy
def calculate_entropy(cipher_text: str) -> float:
    probs = [cipher_text.count(c) / len(cipher_text) for c in set(cipher_text)]
    return -sum(p * np.log2(p) for p in probs)

# Load cipher text files
cipher_texts = []
labels = []
for i in range(1, 9):
    # Use the correct file path
    file_path = os.path.join('C:\\Users\\sankh\\OneDrive\\Desktop\\whitesea\\crptic\\data', f'data{i}.txt')
    cipher_text = read_cipher_file(file_path)
    cipher_texts.append(cipher_text)
    labels.append(f'Algorithm{i}')  # Replace with actual algorithm labels if known

# Extract features
vectorizer = CountVectorizer(analyzer='char', ngram_range=(1, 2))
X = vectorizer.fit_transform(cipher_texts)
X_bigrams_array = np.array([bigrams for bigrams in X_bigrams])
X_entropy_array = np.array(X_entropy)

X_all = np.column_stack((X.toarray(), X_bigrams_array, X_entropy_array))
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_all, labels, test_size=0.2, random_state=42)

# Train SVM model
model = SVC()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Decode cipher text
def decode_cipher(cipher_text: str, algorithm: str) -> str:
    try:
        if algorithm == 'AES':
            # Implement AES decryption using cryptography library
            key = b'your_aes_key'  # Replace with your actual AES key
            fernet = Fernet(key)
            plain_text = fernet.decrypt(cipher_text.encode())
            return plain_text.decode()
        elif algorithm == 'Caesar':
            # Implement Caesar cipher decryption
            shift = 3
            plain_text = ''.join(chr((ord(char) - shift - 97) % 26 + 97) for char in cipher_text.lower())
            return plain_text
        else:
            raise ValueError('Unsupported algorithm')
    except Exception as e:
     print(f'Error decoding cipher text: {e}')