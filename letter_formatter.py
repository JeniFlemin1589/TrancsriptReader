class LetterFormatter:
    @staticmethod
    def format_letter(letter):
        """
        Format the generated letter to ensure proper structure and style,
        making it look professional and branded for Chairsyde Dental Clinic.
        """
        # Define the clinic header and footer
        clinic_header = """
                                                            Chairsyde Dental Clinic          
                                                            Your Smile, Our Priority!            
                                                            www.chairsyddentalclinic.com           
                                                            Call Us: (555) 123-4567\n\n\n"""
        
        clinic_footer = """
        
                        Thank you for trusting Chairsyde Dental Clinic with your oral health! 
                        If you have any questions, don't hesitate to contact us."""

        # Apply header and footer to the letter
        formatted_letter = clinic_header + letter + clinic_footer
        
        # Enhance formatting: make sections bold and clearly separated
        formatted_letter = formatted_letter.replace("**Summary of Findings:**", "**SUMMARY OF FINDINGS**:\n")
        formatted_letter = formatted_letter.replace("**Treatment Plan:**", "**TREATMENT PLAN**:\n")
        formatted_letter = formatted_letter.replace("**Next Steps:**", "**NEXT STEPS**:\n")
        
        # Add some spacing between sections for clarity
        formatted_letter = formatted_letter.replace("\n", "\n")

        return formatted_letter
