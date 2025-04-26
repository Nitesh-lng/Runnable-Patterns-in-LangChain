from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
import os

load_dotenv()   
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm=ChatGroq(
    model='meta-llama/llama-4-scout-17b-16e-instruct'
)

prompt=PromptTemplate(
    template="make a joke about {topic}",
    input_variables=["topic"],
)

prompt1=PromptTemplate(
    template='exlpain the joke{joke}',
    input_variables= ["joke"]
)

parser=StrOutputParser()

chain=RunnableSequence(
    prompt,
    llm,
    parser,
    prompt1,
    llm,
    parser
)

print(chain.invoke({"topic": "job"}))