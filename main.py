import streamlit as st
import google.generativeai as gen_ai

# Configure Streamlit page settings
st.set_page_config(
    page_title="SEO Content Converter",
    page_icon=":rocket:",  # Favicon emoji
    layout="centered",  # Page layout option
)

# Directly set the API key here (not recommended for production)
GOOGLE_API_KEY = "AIzaSyBz4zZKA2H3djpB4_rn9kBejPZn2ytedRM"

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Streamlit app layout
st.title("SEO Content Converter")

# User input
ordinary_content = st.text_area("Enter your ordinary content")

# SEO optimization level
optimization_level = st.selectbox(
    "Select the level of SEO optimization needed:",
    ["Basic", "Standard", "Advanced"]
)

# Combine user input with the prompt for generating advanced SEO content
if st.button("Convert to SEO Optimized Content"):
    prompt = f"""
    Take the following ordinary content and convert it into {optimization_level} SEO-optimized content. Make sure to include relevant keywords, meta descriptions, headers, and any other elements appropriate for the selected level of optimization:

    Content: '{ordinary_content}'
    """

    with st.spinner("Optimizing content..."):
        # Generate SEO content using the Gemini-Pro model
        response = model.generate_content([prompt])
        seo_content = response.text

    # Display the SEO optimized content
    st.subheader(f"{optimization_level} SEO Optimized Content")
    st.write(seo_content)
