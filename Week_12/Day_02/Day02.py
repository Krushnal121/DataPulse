# Question Answering using transformers library
from transformers import pipeline

# Load pre-trained model
qa_pipeline = pipeline("question-answering")

# Sample context and question
context = "The capital of France is Paris."
question = "What is the capital of France?"

# Get the answer
result = qa_pipeline(question=question, context=context)
print(f"Answer: {result['answer']}")

# Conversational Language Understanding using Rasa
from rasa.nlu.model import Interpreter

# Load the Rasa model
interpreter = Interpreter.load("path_to_your_model")

# Sample user message
message = "I want to book a flight to New York"

# Get the model's response
result = interpreter.parse(message)
print(result)
