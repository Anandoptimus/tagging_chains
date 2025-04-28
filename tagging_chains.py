from pydantic import BaseModel, Field 
from typing import TypedDict, List
from langchain.utils.openai_functions import convert_pydantic_to_openai_function
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser

class Tagging(BaseModel):
    """Tag the piece of text into particular info"""
    sentiment: str = Field(description = "sentiment of text should be 'pos', 'neg', or 'neutral'")
    language: str = Field(description = "language of text (should be in ISO-639-1 code) ") 
    gender: str = Field(description = "gender of text should be in 'I or my or single person or self' or 'he or him or man', 'she or her or woman', 'we or they or group of people' or 'it or animal or non-living things'")

tagging_functions = [convert_pydantic_to_openai_function(Tagging)]

model = ChatOpenAI(model = "gpt-3.5-turbo")

model_function = model.bind(functions = tagging_functions, function_call = {"name": "Tagging"})

prompt = ChatPromptTemplate.from_messages([
    ("system", "Think carefully, and then tag the text as instructed"),
    ("user", "{input}")
])

chain = prompt | model_function | JsonOutputFunctionsParser()

chain.invoke({"input": "good morning everybody"})

chain.invoke({"input": "i love to read "})
