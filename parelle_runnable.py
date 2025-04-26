from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence , RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(
    model='meta-llama/llama-4-scout-17b-16e-instruct'
)   

prompt = PromptTemplate(
    template='make a tweet about {topic}',
    input_variables=["topic"],
)

prompt1 = PromptTemplate(
    template='make a linkedin post about {topic}',
    input_variables=["topic"]
)

parser= StrOutputParser()

parellel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt, llm, parser),
    'linkedin_post': RunnableSequence(prompt1, llm, parser)
})

output=parellel_chain.invoke({"topic": "terror attack"})
print(output)