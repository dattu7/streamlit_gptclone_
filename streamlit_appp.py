import streamlit as st
from openai import OpenAI

# Function to generate response
def generate_response(prompt, api_key):
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional skilled in explaining complex concepts in simple way"},
            {"role": "user", "content": prompt}
        ]
    )
    generated_content = completion.choices[0].message.content
    return generated_content

# Streamlit UI
def main():
    st.set_page_config(page_title="Dattu's GPT", page_icon="🧠")
    st.title("Dattu's AI-3.5 Turbo Response Generator")

    # Add instructions to the sidebar with different style and font
    st.sidebar.title("Instructions:")
    st.sidebar.markdown(
        """
        This is a GPT-3.5 Turbo response generator by Dattu.
        
        1. Enter your prompt in the text area on the right.
        2. Click the 'Generate Response' button to generate a response.
        3. The generated response will appear below the text area.
        4. You can exit the application by typing 'exit' in the prompt.
        """
    )

    # Create a container to hold the API key input field and position it on the right side
    api_key_container = st.sidebar.empty()

    # Ask for OpenAI API key
    api_key = api_key_container.text_input("Enter your OpenAI API key:", type="password")

    prompt = st.text_input("Enter the prompt ('exit' to quit):")
    
    if prompt.lower() == 'exit':
        st.write("Exiting...")
    elif st.button("Generate Response"):
        with st.spinner("Generating..."):
            response = generate_response(prompt, api_key)
        st.write("Generated Content:", response)
    
    # Add footer
    st.markdown(
        """
        <style>
            .footer {
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                background-color: grey;
                padding: 8px 0;
                text-align: center;
                text-size:30px;
            }
        </style>
        <div class="footer">
            <p  style="color:white";>Powered by OpenAI • Icons by Font Awesome</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
