from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import gradio as gr

# initialize the models
openai = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key="KODE_API_KAMU"
)

def chatbot(input_pertanyaan):
    # defining a template
    template = """pertanyaan: {pertanyaan}
    Tolong berikan langkah langkahnya:
    """
    prompt = PromptTemplate(template=template, input_variables=["pertanyaan"])
    formated_prompt =prompt.format(pertanyaan=str(input_pertanyaan))
    return openai.invoke(formated_prompt).content

demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")

demo.launch(share=True)
