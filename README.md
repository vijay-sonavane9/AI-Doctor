# 🩺 AI Doctor Voice Bot (Multimodal)
An advanced, multimodal AI assistant that acts as a medical consultant. This project integrates Computer Vision, Speech-to-Text, Large Language Models (LLM), and Text-to-Speech to create a seamless "Doctor-Patient" interaction.

The AI can "see" medical images (like X-rays or symptoms), "hear" patient queries, analyze the data using medical logic, and "speak" back with a realistic human voice.

## 🚀 Features
🗣️ Voice Interaction: Talk to the AI naturally; no typing required.

👁️ Vision Capabilities: Upload medical images for analysis (skin issues, X-rays, reports).

⚡ Ultra-Fast Inference: Powered by Groq for near-instantaneous LLM responses.

🧠 Medical Persona: Custom system prompts designed to mimic a professional, empathetic doctor.

🔊 Realistic Voice: Uses ElevenLabs for high-quality, lifelike speech output.

🖥️ Interactive UI: Clean web interface built with Gradio.

## 🛠️ Tech Stack
Python: Core programming language.

Groq API: Runs Llama 3 (Logic) and Whisper (Transcription) with extreme speed.

ElevenLabs: Generates realistic AI speech.

Gradio: Front-end user interface.

## 🔮 Future Scope
RAG Implementation: Connecting the bot to a Vector Database (Pinecone/ChromaDB) loaded with real medical textbooks for higher accuracy.

History Memory: Allowing the bot to remember previous turns in the conversation.

Deployment: Hosting the app on AWS or HuggingFace Spaces.

## ⚠️ Disclaimer
This project is for educational purposes only. The AI is not a licensed medical professional and should not be used for real medical emergencies or diagnoses.

## 👤 Author
Vijay Sonavane - Ai Engineer

FFmpeg: Handles audio recording and playback processing.

SpeechRecognition & Pydub: Audio capture and manipulation.
