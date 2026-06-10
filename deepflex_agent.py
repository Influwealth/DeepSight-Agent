from transformers import pipeline
from sentence_transformers import SentenceTransformer, util
import json

class DeepFlexAgent:
    def __init__(self, model_name="mistralai/Mistral-7B-Instruct-v0.2"):
        self.llm = pipeline("text-generation", model=model_name, device=0)
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
        self.memory = []

    def save_context(self, user_input, response):
        self.memory.append({"input": user_input, "response": response})
        with open("memory_log.json", "w") as f:
            json.dump(self.memory, f)

    def recall_context(self, query):
        if not self.memory:
            return ""
        query_embed = self.embedder.encode(query)
        similarities = [util.pytorch_cos_sim(query_embed, self.embedder.encode(mem["input"])) for mem in self.memory]
        best_match = self.memory[similarities.index(max(similarities))]
        return best_match["response"]

    def generate_response(self, user_input):
        context = self.recall_context(user_input)
        prompt = f"Previous: {context}\nNow: {user_input}"
        result = self.llm(prompt, max_length=200)[0]['generated_text']
        self.save_context(user_input, result)
        return result
