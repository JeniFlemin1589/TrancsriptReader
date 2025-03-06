
from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

# Load the environment variables from .env file
load_dotenv()

_ = load_dotenv(find_dotenv())
client = OpenAI(
    api_key=os.environ.get('open_api_key'),
)

temperature = 0.3
max_tokens = 1000
top_p = 0.9

class ApiInteraction:
    def __init__(self):
        self.api_key = os.environ.get('open_api_key')
        if not self.api_key:
            raise ValueError("API key is missing from the environment variables")

        # Set the OpenAI API key
        client.api_key = self.api_key

    def generate_patient_letter(self, transcript, tone="empathetic"):
        """
        Generate a detailed and structured patient follow-up letter from a consultation transcript.
        The letter should be accurate, comprehensive, and easy for patients to understand, with tone variation.
        """

        tone_styles = {
            "empathetic": "Use a gentle, caring, and supportive tone, reassuring the patient and expressing empathy for their concerns.",
            "formal": "Maintain a polished, professional tone, focusing on clinical accuracy and straightforward explanations.",
            "casual": "Adopt a friendly, conversational tone to make the patient feel comfortable and at ease.",
        }

        selected_tone = tone_styles.get(tone.lower(), tone_styles["casual"])

        system_message = f"""
        You are an expert dentist and medical writer. Your task is to draft a personalized, patient-friendly follow-up letter based on the provided consultation transcript. 
        Carefully extract and organize relevant details, ensuring completeness and accuracy. Match the letter’s tone to the user's request.
        
        Tone: {selected_tone}
        
        Guidelines:
        - Extract doctor or physician's name and the patient's name and use it in the place holder 
        - If the the name or details of the doctor or patient are missing then omit it or leave the space.
        - If the date is given then use in th eplace holde or else place it as on you last visit 
        - Extract names, dates, symptoms, and observations from the transcript.
        - Summarize findings and treatments concisely but comprehensively.
        - Avoid section titles or headings to match real-world dental letters.
        - Fill in missing details wisely with general advice or omit sections if unavailable.
        - Ensure a smooth, natural flow with clear transitions.
        """

        user_message = f"""
        Dear [Patient Name],

        Thank you for visiting our dental practice on [Date of Appointment]. It was a pleasure meeting you and addressing your dental health concerns.

        Thank you for sharing your symptoms with us. Based on your consultation, we noted the following: 
        Main symptoms: [List main symptoms or omit if not mentioned]. Clinical observations revealed [describe clinical findings, including any inflammation, decay, plaque, or bone loss, or omit if not mentioned]. Relevant X-ray findings include [summarize results or omit if not available].

        Regarding your treatment, we recommend the following procedures: [List recommended treatments, e.g., filling replacement, deep cleaning, root canal, etc., or suggest common preventive measures]. We also suggest maintaining good oral hygiene through [specific hygiene advice or general tips like brushing twice daily and flossing]. Lifestyle adjustments, such as [reducing smoking or modifying diet, or skip if not discussed], may further improve your oral health.

        For your next steps, your scheduled appointment is on [next appointment date, or recommend scheduling one if missing]. In the meantime, we advise [short-term advice, like using desensitizing toothpaste, or provide general comfort measures].

        Please remember that your oral health is our top priority. If you have any questions or experience worsening symptoms, don’t hesitate to contact our office.

        Best wishes for your continued dental health,

        [Physician's Name]
        Physician - Chairsyde 
        ---
        
        Transcript:
        {transcript}
        
        Fill in the structure with extracted information, ensuring coherence and a natural flow.
        """

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
        )

        return completion.choices[0].message.content
