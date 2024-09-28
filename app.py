import streamlit as st
from PIL import Image
import tempfile
import os
from backend import OCRUsingGOT

st.set_page_config(
    page_title="OCR Using GOT",
    layout="centered",
    initial_sidebar_state="auto",
)

@st.cache_resource
def initialize_ocr():
    return OCRUsingGOT()

ocr_extractor = initialize_ocr()

st.title("🖼️ OCR Using GOT")
st.write("Upload an image, and the model will extract the text for you.")

image_file = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'])

if image_file is not None:
    try:
        pil_image = Image.open(image_file).convert('RGB') 
        st.image(pil_image, caption='Uploaded Image', use_column_width=True)

        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_file:
            pil_image.save(tmp_file.name)
            temp_file_path = tmp_file.name

        with st.spinner('Extracting text from the image...'):
            extracted_text = ocr_extractor.extract_text(temp_file_path)  

        st.subheader("📝 Extracted Text:")
        if extracted_text:
            st.write(extracted_text)
            
            search_term = st.text_input("Search for text:", "")
            if search_term:
                highlighted_text = extracted_text.replace(
                    search_term, f'<span style="background-color: rgba(0, 255, 0, 0.3);">{search_term}</span>'
                )
                st.markdown(highlighted_text, unsafe_allow_html=True)  
            else:
                st.write("No search term provided.")
        else:
            st.write("No text found in the image.")

    except Exception as e:
        st.error(f"An error occurred while processing the image: {e}")
    finally:
        if 'temp_file_path' in locals() and os.path.exists(temp_file_path):
            os.remove(temp_file_path)
