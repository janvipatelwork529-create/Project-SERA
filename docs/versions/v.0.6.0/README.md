# SERA v0.6.0 — SERA Speaks

## Overview

SERA v0.6.0 introduces voice interaction.

In this version, SERA can listen to the user's voice, convert speech into text, process basic commands, and respond using generated speech.

## Features

- 🎤 Voice input using microphone
- 📝 Speech-to-text using SpeechRecognition
- 🔊 Text-to-speech using edge-tts
- ▶️ Audio playback using playsound3
- 🎙️ Voice Assistant mode
- 🧠 Retains previous memory features
- 📚 Retains Study Companion features
- 📅 Retains Personal Organizer features

## Voice Flow

User speaks
↓
Microphone records audio
↓
Speech recognition
↓
Text
↓
SERA processes command
↓
Text-to-speech
↓
SERA speaks

## Basic Voice Commands

Currently supported:

- `hello`
- `how are you`
- `stop`

## Technologies Used

- Python
- SpeechRecognition
- sounddevice
- edge-tts
- playsound3

## Version Status

**v0.6.0 — Completed and tested**

## Next Version

**v0.7.0 — SERA Understands**

Focus: APIs, JSON, and information retrieval.