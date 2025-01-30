import numpy as np 
import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load the Transcript
def load_transcript(file_path):
    """Loads the transcript from a .txt file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Step 2: Preprocess the Text
def preprocess_text(text):
    """Cleans the input text."""
    text = text.lower()  
    text = re.sub(r'\s+', ' ', text) 
    return text

# Step 3: Split and Process Sentences
def process_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text) 
    sentences = [preprocess_text(sentence) for sentence in sentences if sentence.strip()]
    return sentences

# Step 4: Generate Embeddings
def generate_embeddings(sentences, model_name='all-MiniLM-L6-v2'):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(sentences)
    return embeddings, model

# Step 5: Save Embeddings and Processed Sentences
def save_embeddings_and_sentences(embeddings, sentences, embeddings_file, sentences_file):
    """Saves embeddings and processed sentences to files."""
    np.save(embeddings_file, embeddings)
    with open(sentences_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(sentences))

# Step 6: Search the Transcript
def search_transcript(query, sentences, embeddings, model, top_n=5):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, embeddings)[0]
    top_indices = similarities.argsort()[-top_n:][::-1]  # Get top N results
    results = [(sentences[idx], similarities[idx]) for idx in top_indices]
    return results


def myquery(query,loaded_sentences,loaded_embeddings,model):
    query = input("\nEnter your search query (or type 'exit' to quit): ")
    if query.lower() == 'exit':
        print("Exiting...")
        return True
    
    print("\nSearching for relevant sentences...")
    results = search_transcript(query, loaded_sentences, loaded_embeddings, model)
    print(f"\nSearch results for query: '{query}'\n")
    the_results = []
    for i, (sentence, score) in enumerate(results, start=1):
        the_results.append(f"{i}. {sentence} (Score: {score:.4f})")
    return the_results

# Step 7: Main Function
def main(transcript_file):
    
    embeddings_file = os.path.join(os.getcwd(),'project_6_trionix', 'data', 'transcript_embeddings.npy')
    sentences_file = os.path.join(os.getcwd(), 'project_6_trionix', 'data', 'processed_transcript.txt')
   
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
    return loaded_sentences,loaded_embeddings,model
    # while True:
    #     if(myquery(query,loaded_sentences,loaded_embeddings,model)):
    #         break

if __name__ == "__main__":
    main()