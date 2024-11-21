import streamlit as st
from transformers import pipeline

# Load AI model
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")  # Free AI model from Hugging Face

# Main application
def main():
    st.title("Math Basics Learning App")
    st.subheader("Learn Arithmetic, Algebra, and Geometry")

    # Sidebar for topics
    topic = st.sidebar.selectbox(
        "Select a Math Topic",
        ["Arithmetic Basics", "Algebra Basics", "Geometry Basics"]
    )

    st.markdown(f"### {topic}")

    if topic == "Arithmetic Basics":
        arithmetic_section()
    elif topic == "Algebra Basics":
        algebra_section()
    elif topic == "Geometry Basics":
        geometry_section()

def arithmetic_section():
    st.write("Learn the basics of arithmetic like fractions, percentages, and operations.")
    example_query = st.text_input("Ask about arithmetic concepts (e.g., 'What is a fraction?')")
    if example_query:
        st.write("AI Response:")
        model = load_model()
        response = model(example_query, max_length=100, num_return_sequences=1)
        st.write(response[0]['generated_text'])

def algebra_section():
    st.write("Learn the basics of algebra like expressions and equations.")
    example_query = st.text_input("Ask about algebra concepts (e.g., 'What is a variable?')")
    if example_query:
        st.write("AI Response:")
        model = load_model()
        response = model(example_query, max_length=100, num_return_sequences=1)
        st.write(response[0]['generated_text'])

def geometry_section():
    st.write("Learn the basics of geometry like angles, triangles, and circles.")
    example_query = st.text_input("Ask about geometry concepts (e.g., 'What is a right angle?')")
    if example_query:
        st.write("AI Response:")
        model = load_model()
        response = model(example_query, max_length=100, num_return_sequences=1)
        st.write(response[0]['generated_text'])

if __name__ == "__main__":
    main()
