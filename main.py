
import streamlit as st
from file_manager import FileManager
from api_interaction import ApiInteraction
from letter_formatter import LetterFormatter

def main():
    st.title("Patient Follow-Up Letter Generator")

    # File uploader for different types of files
    uploaded_file = st.file_uploader("Upload a Transcript File (TXT, PDF, DOCX)", type=["txt", "pdf", "docx"])
    
    if uploaded_file is not None:
        # Save uploaded file using FileManager
        file_path = FileManager.save_uploaded_file(uploaded_file)
        
        # Extract the text from the file
        transcript = FileManager.extract_text_from_file(file_path)

        if transcript:
            # Generate the patient follow-up letter
            api_interaction = ApiInteraction()
            letter = api_interaction.generate_patient_letter(transcript)

            # Format the letter (Optional)
            formatted_letter = LetterFormatter.format_letter(letter)

            # Display the formatted letter
            st.subheader("Generated Patient Letter")
            st.text_area("Patient Letter", value=formatted_letter, height=300)

            # Provide an option to download the generated letter
            output_path = "generated_patient_letter.txt"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(formatted_letter)

            st.download_button("Download Patient Letter", data=open(output_path, "rb"), file_name=output_path, mime="text/plain")
        else:
            st.error("Failed to extract content from the file.")
    else:
        st.info("Please upload a transcript file to generate the patient letter.")

if __name__ == "__main__":
    main()
