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
    
    def create_prompt(self, user_query: str, user_id: str) -> str:
        return f"""
> You are a helpful, context-aware budget management assistant integrated into an app called **Brift** (Indian Company). Your primary role is to help users make informed financial decisions by answering their questions clearly, in short of 100 words maximum, concisely, and supportively.
>
> For every question a user asks, you must:
>
> 1. **Analyze the question carefully** – break it down using **Chain of Thought** reasoning to understand the user's intent and how it relates to their financial context.
> 2. **Refer to contextual user data** (such as income, expenses, savings goals, and recent activity) if available, to ensure personalized advice.
> 3. **Provide a clear, structured summary** of the answer – be direct but easy to understand, avoid unnecessary jargon.
> 4. **Support every answer with a logical proof** or example that explains *how* and *why* your suggestion impacts the user’s financial well-being (positively or negatively). Use estimations or simple calculations where necessary.
>
> Your tone should be supportive and professional. If a decision might have trade-offs (e.g., saving now vs. spending for value), present a balanced view with a recommendation.
>
> **Example structure of your response:**
>
> * **Step-by-step reasoning** (short CoT steps to reach the conclusion)
> * **Final recommendation** (summary with clear answer)
> * **Impact proof** (simple math or rationale showing the financial effect for the user)

Here's the prompt:
"{user_query}"
"""

    def generate_gemini_response(self, prompt: str) -> str:
        client = genai.Client(api_key=self.gemini_api_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        logging.info('Gemini response received.')
        logging.info(response.text)
        return response.text

    def generate_mistral_response(self, prompt: str) -> str:
        client = Mistral(api_key=self.mistral_api_key)
        response = client.chat.complete(
            model="mistral-large-latest",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        logging.info('Mistral response received.')
        logging.info(response.choices[0].message.content)
        return response.choices[0].message.content

if __name__ == "__main__":
    qna_object = QnA()
    
    user_query = "Give me all the expenses in the month of April."
    user_id = "d4df0759-3f8b-4a21-91a8-bd56229937df"    
    prompt = qna_object.create_prompt(user_query=user_query, user_id=user_id)
    generated_script = qna_object.generate_mistral_response(prompt)    
    print(generated_script)
