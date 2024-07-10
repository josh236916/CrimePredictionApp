import streamlit as st

# Add a title to your app
st.title("Results For Classification and Regression")

image_options = {
    "Classification": "/Users/josh2369/Downloads/image9.jpg",
    "Regression": "/Users/josh2369/Downloads/image10.jpg",
   
}


selected_image = st.selectbox("Select an image:", list(image_options.keys()))

st.image(image_options[selected_image], caption=selected_image, use_column_width=True)