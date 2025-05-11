from dotenv import load_dotenv
from logger import logging
from dataclasses import dataclass
from google import genai
from mistralai import Mistral
import os

load_dotenv()

@dataclass(kw_only=True)
class QnA:
    gemini_api_key: str = os.getenv('GEMINI_API_KEY')
    mistral_api_key: str = os.getenv('MISTRAL_API_KEY')
    

    def create_prompt(self, query):
        return prompt = f"""

          {query}
        """


    def generate_gemini_response(self, prompt):
        client = genai.Client(api_key=self.gemini_api_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash", # best gemini model
            contents=prompt
        )
        logging.info('Response received.')
        return response.text


    def generate_mistral_response(self, prompt):
        client = Mistral(api_key=self.mistral_api_key)
        response = client.chat.complete(
            model="mistral-large-latest", # best mistral ai model
            context=prompt
        )
        logging.info('Response received.')
        return response.choices[0].message.content


if __name__=="__main__":
    qna_object = QnA()
    qna_object.create_prompt