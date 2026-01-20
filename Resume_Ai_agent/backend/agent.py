import os
from pydantic_ai import Agent
from pydantic_ai.models.openrouter import OpenRouterModel
from pydantic_ai.providers.openrouter import OpenRouterProvider

provider = OpenRouterProvider(
    api_key=os.environ.get("OPENROUTER_API_KEY")
)

model = OpenRouterModel(
    model_name="mistralai/mistral-7b-instruct",
    provider=provider
)

agent = Agent(
    model=model,
    system_prompt="You are an AI interview coach."
)
