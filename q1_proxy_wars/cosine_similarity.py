from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define the filenames
file_names = [
    "deepseek-llm_response.txt",
    "phi_response.txt",
    "dolphin-phi_response.txt",
    "qwen_response.txt",
    "gemma_response.txt",
    "llama2-chinese_response.txt",
    "stable-beluga_response.txt",
    "stablelm2_response.txt",
    "llama3_response.txt",
    "starling-lm_response.txt",
    "mistrallite_response.txt",
    "wizardlm-uncensored_response.txt",
    "mistral-openorca_response.txt",
    "mistral_response.txt",
    "wizard-vicuna_response.txt",
    "wizard-vicuna-uncensored_response.txt",
    "openchat_response.txt",
    "xwinlm_response.txt",
    "orca2_response.txt",
    "yi_response.txt",
    "solar_response.txt"
]

# Load the content of llama2_response.txt
with open("llama2_response.txt", "r") as f:
    llama2_content = f.read()

# Create a CountVectorizer object
vectorizer = CountVectorizer().fit([llama2_content])

# Transform llama2_response.txt and calculate its vector representation
llama2_vector = vectorizer.transform([llama2_content])

# Open/create cosine_results.txt to write results
with open("cosine_results.txt", "w") as result_file:
    for filename in file_names:
        # Load content of each file
        with open(filename, "r") as f:
            content = f.read()

        # Transform content and calculate vector representation
        content_vector = vectorizer.transform([content])

        # Calculate cosine similarity
        similarity = cosine_similarity(llama2_vector, content_vector)[0][0]

        # Write similarity value to file
        result_file.write(f"Similarity between llama2_response.txt and {filename}: {similarity}\n")

        print(f"Similarity between llama2_response.txt and {filename}: {similarity}")

print("Cosine similarities have been calculated and written to cosine_results.txt.")

