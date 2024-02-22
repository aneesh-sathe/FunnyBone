from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = Ollama(model='llama2')
output_parser = StrOutputParser()

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant of the Best Orthopaedic Surgeon in the world. You are responsible for writing detailed medical reports which include the following sections <FRACTURE DETECTED> <TREATMENT PLAN> <COST BREAKUP> <ADDITIONAL RECOMMENDATIONS>. If no fracture is detected, you should forward the case to the doctor for special attention."),
        ("human", "Hello! I have been experiencing some pain in {fracture_type}"),
        ("ai", "Oh, Let me take a so that I can make a report. How certain are you of the pain?"),
        ("human", "I'm {confidence}% certain. Please make a report. " )
        
    ]
)

chain = chat_template | llm | output_parser

def make_report(result):
    report = chain.invoke({
        "fracture_type": result.condition,
        "confidence": result.confidence
    })
    
    return report
    
    