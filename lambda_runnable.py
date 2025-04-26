from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence , RunnableParallel , RunnablePassthrough , RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(
    model='deepseek-r1-distill-llama-70b'
)   

prompt = PromptTemplate(
    template='make a tweet about {topic}',
    input_variables=["topic"],
)

parser= StrOutputParser()
def number_of_words(text):
    return len(text)

chain = RunnableSequence(prompt,llm,parser)

chain1=RunnableParallel({
    'joke':RunnablePassthrough(),
    'words':RunnableLambda(number_of_words)
})

main_chain=RunnableSequence(chain, chain1)
output=main_chain.invoke({"topic": "terror attack"})
print(output)