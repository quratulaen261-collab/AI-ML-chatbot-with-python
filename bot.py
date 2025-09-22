import streamlit as st 
responses = {
    "hi": "Hello! How are you?",
    "hello": "Hi there!",
    "how are you": "I'm doing great, thanks for asking!",
    "bye": "Goodbye! Have a nice day.",
    "what is ai": "AI (Artificial Intelligence) is the simulation of human intelligence by machines.",
    "what is machine learning": "Machine Learning is a subset of AI that allows systems to learn from data without explicit programming.",
    "difference between ai and ml": "AI is the broader concept of machines being able to carry out tasks smartly, while ML is a subset of AI focused on learning from data.",
    "what is deep learning": "Deep Learning is a type of ML that uses neural networks with many layers to model complex patterns in data.",
    "what is nlp": "NLP (Natural Language Processing) is a branch of AI that helps computers understand, interpret, and generate human language.",
    "what is computer vision": "Computer Vision is a field of AI that enables machines to interpret and process visual data like images and videos.",
    "what is supervised learning": "Supervised Learning is an ML technique where models are trained on labeled data (input-output pairs).",
    "what is unsupervised learning": "Unsupervised Learning is an ML technique where models find patterns in data without labeled outputs.",
    "what is reinforcement learning": "Reinforcement Learning is an ML approach where an agent learns by interacting with an environment and receiving rewards or penalties.",
    "what is neural network": "A Neural Network is a set of algorithms modeled after the human brain, designed to recognize patterns."
}
st.title("AI ML Chatbot")
user_input = st.text_input("Ask me anything about AI ML")
if st.button("Submit"):
    if user_input.lower() in responses:
        st.write(responses[user_input.lower()])
    else:
        st.write("I'm sorry, I don't understand that question")
