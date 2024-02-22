from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = Ollama(model='llama2')
output_parser = StrOutputParser()

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant of the Best Orthopaedic Surgeon in the world. You are responsible for writing detailed medical reports which include the following sections <TYPE OF FRACTURE> <TREATMENT PLAN> <COST BREAKUP> <ADDITIONAL RECOMMENDATIONS>. Assume any other details like Patient Name, Total Cost etc whenever necessary."),
        ("human", "Hello! I have been experiencing some pain in {fracture_type}"),
        ("ai", "Oh, Let me take a so that I can make a report. How certain are you of the pain?"),
        ("human", "I'm {confidence}% certain. Please make a report. " )
        
    ]
)

chain = chat_template | llm | output_parser

def make_report(result):
    
    report = chain.invoke({
        "fracture_type": result.get("condition"),
        "confidence": result.get("confidence")
    })
    
    return report
    
    