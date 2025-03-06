import os
from PyPDF2 import PdfReader
from docx import Document
import streamlit as st

class FileManager:
    @staticmethod
    def save_uploaded_file(uploaded_file, folder="uploads"):
        """
        Saves the uploaded file to the specified folder and returns the file path.
        """
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return file_path

    @staticmethod
    def extract_text_from_file(file_path):
        """
        Extracts and returns the text content from a file based on its type.
        Supports PDF, DOCX, and TXT formats.
        """
        if file_path.endswith('.pdf'):
            with open(file_path, 'rb') as f:
                reader = PdfReader(f)
                return "".join([page.extract_text() for page in reader.pages])
        elif file_path.endswith('.docx'):
            doc = Document(file_path)
            return "\n".join([para.text for para in doc.paragraphs])
        else:
            with open(file_path, 'r') as file:
                return file.read()
