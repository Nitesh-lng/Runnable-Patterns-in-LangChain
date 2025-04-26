from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence , RunnableParallel , RunnablePassthrough
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm=ChatGroq(
    model='meta-llama/llama-4-scout-17b-16e-instruct'
)

prompt1=PromptTemplate(
    template='make a joke about({topic}',
    input_variables=["topic"],
)

prompt2=PromptTemplate(
    template='exlpain the joke{joke}',
    input_variables=["joke"],
)

parser=StrOutputParser()

chain=RunnableSequence(prompt1, llm, parser)

chain2=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2, llm, parser)
})

chain3=RunnableSequence(chain, chain2)

print(chain3.invoke({"topic": "job"}))



