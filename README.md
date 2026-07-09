안녕하세요!

This repo is a collection of small, random ML projects built around the Korean language -
speech, OCR, NLP 🇰🇷

## Projects

### 1. Korean ASR test - `KOR_ASR.ipynb`

Tested OpenAI Whisper on Korean speech recognition.

**Conclusion:** Whisper works well on Korean out of the box - good enough to use
in future projects without fine-tuning.

### 2. Korean Photo Reader - read Korean with your own voice 📷🔊

Upload a photo of Korean text, tap a word, and hear it read aloud **in your own voice** —
zero Korean knowledge needed.

**How it works:**
- [EasyOCR](https://github.com/JaidedAI/EasyOCR) detects and reads the text in the photo
- [OmniVoice](https://github.com/k2-fsa/OmniVoice) clones your voice from a short audio clip (3–10 s) and reads the tapped word instantly

**Try it:** [Korean Photo Reader on Hugging Face Spaces](https://huggingface.co/spaces/coolbambook/KOR_Speaking_test)
A grade from speaking test
