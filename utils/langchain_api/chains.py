from langchain_openai import ChatOpenAI

from utils.config import (
    OPENAI_API_KEY,
    OPENAI_MODEL_NAME,
    OPENAI_TEMPERATURE_MODEL,
)
from utils.langchain_api.prompts import game_description_prompt


model = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model=OPENAI_MODEL_NAME,
    temperature=OPENAI_TEMPERATURE_MODEL
)


def get_game_description(game_title: str) -> str:
    llm = model
    response = llm.invoke(game_description_prompt.format(game_title=game_title))
    if response:
        result = response.content.strip()
        return result
    return None
