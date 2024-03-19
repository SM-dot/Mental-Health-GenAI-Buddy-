import openai
import gradio
import langchain
from langchain.document_loaders import PyPDFLoader # import the correct loader
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter

openai.api_key = "#### Enter your own API Key ####"

system_message = f"""
You are a mental health assisstant that answers any questions about mental health in a firendly manner, always let the user know that you are there to loisten to them.\
    In case you notice anyone talking about dying or comiting a suicide please immeditely guide them to a suicide control helpline and provide comforting words.\
    Pursuade the user to not commit suidcide. \
    """
messages = [{"role": "system", "content": system_message}]

#SPDM and etc needs to be fixed, proper technical discussion needs to be done and sorted 
#sorted - make it into chunks, make it more better, text split at 5, chunk split it aned then comprehend it into a list
#then make it more context aware by telling it to read more, no prompt fine tune it and then incorprorate, hard launch it into GM 
#Plan - tonight have it working by toight 

loader = PyPDFLoader("C:/Users/kaylab/Desktop/ChatGPT API/MachineLearning-Lecture01.pdf") # put the document in the loader
pages = loader.load() # call the documents fromt the loader 
chunk_size = 26
chunk_overlap = 4
r_splitter = RecursiveCharacterTextSplitter(chunk_size = chunk_size, chunk_overlap = chunk_overlap)
c_splitter = CharacterTextSplitter(chunk_size = chunk_size, chunk_overlap = chunk_overlap)
text1 = "fscvchbgfS hfi/j 3;o8yrli7tGQE KHi ehd"
r_splitter.split_text(text1)


def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = messages
    )
    
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT,  inputs = "text", outputs = "text", title = "The Mental Health Assisstant: Talk about anything with me!")

demo.launch(share=True)
