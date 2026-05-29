import os
import json
from groq import Groq
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from loguru import logger
from dotenv import load_dotenv

load_dotenv()

class GroqClient:
    """
    Handles connection, retry logic, and error handling for the Groq API.
    """
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            logger.error("GROQ_API_KEY not found in environment variables")
            raise ValueError("GROQ_API_KEY is required")
        
        self.client = Groq(api_key=self.api_key)
        self.model = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")
        logger.info(f"GroqClient initialized with model: {self.model}")

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type(Exception),
        before_sleep=lambda retry_state: logger.warning(f"Retrying Groq API call... Attempt {retry_state.attempt_number}")
    )
    async def call_groq(self, system_prompt: str, user_prompt: str):
        """
        Calls the Groq API with the optimized single-call strategy.
        """
        try:
            logger.info(f"Calling Groq API for prompt: {user_prompt[:50]}...")
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                response_format={"type": "json_object"},
                temperature=0.2,
            )
            logger.info("Groq API call successful")
            return completion.choices[0].message.content
        except Exception as e:
            logger.error(f"Error calling Groq API: {str(e)}")
            raise

groq_client = GroqClient()
