from langchain_community.llms import Ollama
llm = Ollama(model='llama2')

print(llm.invoke('what is your name?'))