import streamlit as st

def main():
    st.title("Simple Streamlit App")
    
    # Add a text input
    user_input = st.text_input("Enter your name:", "")
    
    # Add a button
    if st.button("Greet"):
        if user_input:
            st.write(f"Hello, {user_input}!")
        else:
            st.write("Please enter your name.")
    
    # Add a slider
    age = st.slider("Select your age:", 0, 100, 25)
    st.write(f"You selected: {age} years old")
    
    # Add a selectbox
    option = st.selectbox(
        "What's your favorite color?",
        ("Red", "Green", "Blue", "Yellow")
    )
    st.write(f"Your favorite color is {option}")

if __name__ == "__main__":
    main()
