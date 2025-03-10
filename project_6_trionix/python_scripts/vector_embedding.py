import numpy as np 
import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os

def load_transcript(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text
def preprocess_text(text):
    text = text.lower()  
    text = re.sub(r'\s+', ' ', text) 
    return text
def process_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text) 
    sentences = [preprocess_text(sentence) for sentence in sentences if sentence.strip()]
    return sentences

def generate_embeddings(sentences, model_name='all-MiniLM-L6-v2'):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(sentences)
    return embeddings, model

def save_embeddings_and_sentences(embeddings, sentences, embeddings_file, sentences_file):
    np.save(embeddings_file, embeddings)
    with open(sentences_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(sentences))

def search_transcript(query, sentences, embeddings, model, top_n=5):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, embeddings)[0]
    top_indices = similarities.argsort()[-top_n:][::-1] 
    results = [(sentences[idx], similarities[idx]) for idx in top_indices]
    return results


def myquery(query,loaded_sentences,loaded_embeddings,model):
    # query = input("\nEnter your search query (or type 'exit' to quit): ")
    # if query.lower() == 'exit':
    #     print("Exiting...")
    #     return True
    
    print("\nSearching for relevant sentences...")
    results = search_transcript(query, loaded_sentences, loaded_embeddings, model)
    print(f"\nSearch results for query: '{query}'\n")
    the_results = []
    for i, (sentence, score) in enumerate(results, start=1):
        the_results.append(f"{i}. {sentence}")
    return the_results
def main(transcript_file):
    embeddings_file = os.path.join(os.getcwd(),'data','processed','transcript_embeddings.npy')
    sentences_file = os.path.join(os.getcwd(), 'data','processed','processed_transcript.txt')
   
    print("Loading and processing the transcript...")
    text = load_transcript(transcript_file)
    sentences = process_sentences(text)
    
    print("Generating embeddings...")
    embeddings, model = generate_embeddings(sentences)
    
    print("Saving embeddings and processed sentences...")
    save_embeddings_and_sentences(embeddings, sentences, embeddings_file, sentences_file)
    
    print("Loading saved embeddings and sentences...")
    loaded_embeddings = np.load(embeddings_file)
    with open(sentences_file, 'r', encoding='utf-8') as file:
        loaded_sentences = file.read().split('\n')
    print("Loaded",loaded_sentences)
    print("Loaded",loaded_embeddings)
    print("Loaded",model)
    return loaded_sentences,loaded_embeddings,model
    # while True:
    #     if(myquery(query,loaded_sentences,loaded_embeddings,model)):
    #         break

if __name__ == "__main__":
    main()
