import gradio as gr
from transformers import pipeline

asr = pipeline("automatic-speech-recognition",
               model="coolbambook/whisper-small-korean-kss")

def transcribe(audio):
    if audio is None:
        return "Record or upload something first."
    return asr(audio)["text"]

demo = gr.Interface(
    fn=transcribe,
    inputs=gr.Audio(sources=["microphone", "upload"], type="filepath"),
    outputs=gr.Textbox(label="Transcript"),
    title="Korean ASR — Whisper-small fine-tuned on KSS",
    description="Fine-tuned on the Korean Single Speaker dataset. CER 3.8% on held-out clips.",
)
demo.launch()