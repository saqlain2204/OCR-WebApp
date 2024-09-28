# Optical Character Recognition (OCR) Web Application

This project is a web-based prototype that demonstrates Optical Character Recognition (OCR) functionality. The application allows users to upload images containing both Hindi and English text, extracts the text using the **General OCR Theory (GOT)** model, and provides a basic keyword search feature. 

Due to the GOT model's requirement for GPU support, the application must be run in an environment with a GPU, such as Kaggle notebooks, where a P100 GPU is used.

## Features

- **Image Upload:** Users can upload an image file (JPEG, PNG, etc.).
- **Text Extraction:** Extracts Hindi and English text from the uploaded image using the GOT OCR model.
- **Keyword Search:** Users can search for specific keywords within the extracted text.
- **Search Results:** Displays search results on the same page, highlighting the matching sections.

## Tech Stack

- **Backend:** Python, Huggingface Transformers, PyTorch
- **Frontend:** Streamlit
- **OCR Model:** General OCR Theory (GOT), a 580M end-to-end OCR 2.0 model
- **Deployment:** Streamlit app for UI; GPU support via Kaggle Notebook

## Prerequisites

To run this project locally or in a notebook environment, you will need:

- Python 3.8+
- PyTorch (with GPU support)
- Huggingface Transformers library
- Streamlit (for the web interface)

## How to Run the Application

### 1. Clone the Repository

```bash
git clone https://github.com/saqlain2204/ocr-webapp.git
cd ocr-webapp
```
2. Set Up Python Environment
Create a virtual environment and install the required packages:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
3. Running Locally (With GPU Support)
Since the GOT model requires GPU support, you can run this project in a Kaggle notebook or another environment that provides a GPU. Follow the steps below for Kaggle:

Upload the project files to a Kaggle notebook.
Ensure that GPU is enabled in the notebook settings.
Execute the notebook cells to start the backend OCR processing.
If running locally, make sure that your system has a compatible GPU and the required CUDA libraries are installed.

4. Access the Web Interface
Once the application is running, launch the Streamlit interface by running:

```bash
streamlit run app.py
```

5. Using the Application
Upload a supported image file (JPEG, PNG).
The extracted text from the image will be displayed below the upload section.
Enter a keyword to search within the extracted text.
The application will highlight the matching sections of the text.

Project Structure
```plaintext
├── app.py                # Streamlit app for the frontend
├── backend.py            # Handles the backend OCR processing
├── notebook.ipynb        # The notebook used in a GPU environment
├── requirements.txt      # Required dependencies
├── README.md             # Project documentation
```

app.py: The frontend of the web application using Streamlit.
backend.py: Contains all the OCR model integration and text extraction logic.
requirements.txt: Lists all the required Python packages and dependencies.

Deployment Notes
Important: The GOT OCR model **only works with GPU support**. As a result, the application may **not** function correctly on a Streamlit deployment that does not provide GPU support. For a working demonstration, please refer to the [Kaggle Notebook](https://www.kaggle.com/code/saqlain22/notebookeb74771db9).

The Streamlit version of the app is accessible at the following URL, but it may not work fully due to the lack of GPU: [Live Demo] (Streamlit).

To test the functionality with GPU, please use the Kaggle notebook link, which has been configured with GPU support.

Future Enhancements
Implement fallback logic for non-GPU environments.
Explore other OCR models that support CPU inference.
Add support for additional languages and more complex search functionalities.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Demo Video:
A demo on the working of the application can be viewed [here](https://drive.google.com/file/d/1UmCSfSBN_Xy7Wr8fC9rRBaDyEfWo6VyH/view?usp=sharing)

## Author

- **Mohammed Saqlain**  
  [LinkedIn](https://www.linkedin.com/in/saqlain2204) | [GitHub](https://github.com/saqlain2204)

For any questions or issues, feel free to raise an issue or contact me via email at saqlain.contact@gmail.com.