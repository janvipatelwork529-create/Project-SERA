SERA Bug Tracker

This file records bugs, errors, and technical problems encountered during SERA development.

---

v0.6.0 — SERA Speaks

BUG-001 — PyAudio installation failed

Status: Fixed
Version: v0.6.0

Problem:
Installing "SpeechRecognition[audio]" failed because PyAudio could not be built/installed successfully.

Solution:
Instead of using PyAudio, SERA was switched to "sounddevice" for microphone recording.

---

BUG-002 — NumPy was missing

Status: Fixed
Version: v0.6.0

Problem:
"sounddevice" required NumPy for recording audio, but NumPy was not installed.

Error:

ModuleNotFoundError: No module named 'numpy'

Solution:
Installed NumPy.

---

BUG-003 — FLAC converter not available

Status: Fixed
Version: v0.6.0

Problem:
SpeechRecognition could record audio, but converting the audio for Google Speech Recognition produced:

OSError: FLAC conversion utility not available

Investigation:
SpeechRecognition already contained "flac-win32.exe", but the library was not finding it correctly.

Solution:
The bundled FLAC converter was located and explicitly supplied to SpeechRecognition.

---

BUG-004 — Windows ARM64 was not recognized by SpeechRecognition

Status: Fixed
Version: v0.6.0

Problem:
The computer uses Windows ARM64, while SpeechRecognition's automatic FLAC converter detection did not properly handle this architecture.

Solution:
A workaround was added to manually point SpeechRecognition to:

flac-win32.exe

---

BUG-005 — pyttsx3 repeated speech failed

Status: Replaced
Version: v0.6.0

Problem:
"pyttsx3" successfully produced speech during an initial test, but repeated speech calls did not work reliably.

Investigation:
The problem continued even when creating a fresh engine for repeated speech.

Solution:
Replaced "pyttsx3" with "edge-tts".

---

BUG-006 — "await" used outside an async function

Status: Fixed
Version: v0.6.0

Problem:
An early "edge-tts" test attempted to use "await" outside an asynchronous function.

Error:

SyntaxError: 'await' outside function

Solution:
Created an "async" function and used:

asyncio.run(...)

---

BUG-007 — Incorrect Edge-TTS voice name

Status: Fixed
Version: v0.6.0

Problem:
The voice name was typed incorrectly.

Incorrect:

en-Us-AiraNeural

Correct:

en-US-AriaNeural

Solution:
Corrected the voice name and verified the available voices.

---

BUG-008 — Same MP3 file was reused

Status: Fixed
Version: v0.6.0

Problem:
When multiple responses were saved to and played from the same MP3 filename, only the first response played correctly.

Solution:
Each generated speech response was given a unique filename:

speech1.mp3
speech2.mp3
speech3.mp3

---

BUG-009 — Delay between spoken responses

Status: Known limitation
Version: v0.6.0

Problem:
There is a noticeable delay between responses because SERA must:

Generate speech
↓
Save MP3
↓
Load MP3
↓
Play MP3

Current status:
Accepted temporarily for v0.6.0.

Possible future improvement:
Optimize or replace the speech-generation/playback pipeline.

---

BUG-010 — "NoAudioReceived" during integrated testing

Status: Resolved
Version: v0.6.0

Problem:
The microphone produced a "NoAudioReceived" error when the speech system was first integrated into the larger SERA program, even though the microphone worked in isolated tests.

Investigation:
The isolated recording and speech-recognition tests worked correctly.

Solution:
The voice functions were tested separately, corrected, and then integrated into the v0.5 codebase.

---

BUG-011 — Python code typo during speech integration

Status: Fixed
Version: v0.6.0

Problem:
Some of the early integrated tests failed because of human typing/code-entry mistakes.

Solution:
The code was corrected and the individual components were tested independently before combining them.

---

BUG-012 — VS Code used the wrong Python environment

Status: Fixed
Version: v0.6.0

Problem:
The required packages were installed correctly, but running the SERA file from VS Code produced:

ModuleNotFoundError: No module named 'speech_recognition'

However, the package was installed and could be imported successfully from the terminal.

Cause:
VS Code was using a different Python interpreter/environment when running the file.

Solution:
Selected the correct Python interpreter:

C:\Users\janvi\AppData\Local\Python\pythoncore-3.14-64\python.exe

After selecting the correct interpreter, SERA worked normally.

---

Summary

v0.6.0 involved several technical problems involving:

- Microphone input
- Audio recording
- Speech recognition
- FLAC conversion
- Windows ARM64 compatibility
- Text-to-speech
- Asynchronous Python
- Audio file generation
- Audio playback
- Python environments
- VS Code interpreter configuration

All critical issues required for v0.6.0 have been resolved. 