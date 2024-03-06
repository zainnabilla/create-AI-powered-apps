import gradio as gr
from langchain.prompts import PromptTemplate
import os
from langchain_openai import ChatOpenAI

openai_api_key = "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"
os.environ["OPENAI_API_KEY"] = openai_api_key

# Mendefinisikan model AI
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key= openai_api_key
)

# Mendefinisikan PromptTemplate sebagai format prompt untuk input dari user
prompt = PromptTemplate(
    input_variables=["nama", "posisi", "perusahaan", "keterampilan"],
    template="Yang terhormat HRD Manajer {perusahaan},\n\nDengan surat ini, saya {nama}, ingin melamar untuk posisi {posisi} di {perusahaan}. Saya memiliki pengalaman di bidang {keterampilan}. Terima kasih telah mempertimbangkan lamaran saya.\n\nHormat saya,\n {nama}",
)

# Define a function to generate a cover letter using the llm and user input
def generate_cover_letter(nama: str, posisi: str, perusahaan: str, keterampilan: str) -> str:
    formatted_prompt = prompt.format(nama=nama, posisi=posisi, perusahaan=perusahaan, keterampilan=keterampilan)
    response = llm.invoke(formatted_prompt).content
    return response

# Define the Gradio interface inputs
inputs = [
    gr.Textbox(label="Nama"),
    gr.Textbox(label="Posisi"),
    gr.Textbox(label="Perusahaan"),
    gr.Textbox(label="Keterampilan")
]

# Define the Gradio interface output
output = gr.Textbox(label="Template Surat")

# Launch the Gradio interface
gr.Interface(fn=generate_cover_letter, inputs=inputs, outputs=output).launch(server_name="0.0.0.0", server_port= 7860, share=True)