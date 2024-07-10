import streamlit as st

# Add a title to your app
st.title("Image Display in Streamlit")

image_options = {
    "MSE for Best features": "/Users/josh2369/Downloads/image1.jpg",
    "Map showing Violent Crime Per Pop": "/Users/josh2369/Downloads/image2.jpg",
    "Histogram showing Violent Crimes Per Pop": "/Users/josh2369/Downloads/image3.jpg",
    "Q-Q plot showing Violent Crimes Per Pop": "/Users/josh2369/Downloads/image4.jpg",
    "States with highest Violent Crimes Per Pop": "/Users/josh2369/Downloads/image5.jpg",
    "Communities with highest Violent Crimes Per Pop": "/Users/josh2369/Downloads/image6.jpg",
    "Actual vs Real Values for best Feature": "/Users/josh2369/Downloads/image7.jpg",
    "Residual vs Fitted Values for best Feature": "/Users/josh2369/Downloads/image8.jpg",
}


selected_image = st.selectbox("Select an image:", list(image_options.keys()))

st.image(image_options[selected_image], caption=selected_image, use_column_width=True)