from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence , RunnableParallel , RunnablePassthrough , RunnableLambda , RunnableBranch
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(
    model='deepseek-r1-distill-llama-70b'
)   

parser=StrOutputParser()

prompt=PromptTemplate(
    template='make a details about {topic}',
    input_variables=["topic"],
)

prompt1=PromptTemplate(
    template='make a summary about {topic}',
    input_variables=["topic"],
)   

chain1=RunnableSequence(prompt, llm, parser)

chain2=RunnableBranch(
    (lambda x: len(x.split())>10,RunnableSequence(prompt1, llm, parser)),
    RunnablePassthrough()
)

chain3=RunnableSequence(chain1, chain2)
output=chain3.invoke({"topic": "terror attack"})    
print(output)