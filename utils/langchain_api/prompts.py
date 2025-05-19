from langchain.prompts import ChatPromptTemplate

from utils.config import (
    PROMPT_SYSTEM_GAME_DESCRIPTION,
    PROMPT_USER_GAME_DESCRIPTION,
)

game_description_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", PROMPT_SYSTEM_GAME_DESCRIPTION),
        ("user", PROMPT_USER_GAME_DESCRIPTION),
    ]
)
