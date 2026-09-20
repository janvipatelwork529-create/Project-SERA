# Changelog

All notable changes to Project SERA will be documented here.

## [v0.1.0] - The Awakening

### Planned
- Initial SERA program
- Basic user interaction
- Welcome message
- User name input
- Basic menu
- Study section
- Motivation section
- About SERA section
- Exit option

## [v0.2.0] - Infinite Assistant

### Added
- Continuous menu using a while loop
- Repeated user interaction
- Exit functionality
- Invalid choice handling
- Improved program flow

## [v0.3.0] - First Memory

### Added
- SERA can remember the user's name
- File-based memory using `memory.txt`
- Reading and writing files
- `try/except` error handling
- First-launch handling
- Welcome-back message for returning users

## [v0.4.0] - Study Companion

### Added
- Dedicated Study menu
- Separate Study loop
- Add subjects
- View subjects
- Remove subjects
- Subject numbering
- Subject validation
- Persistent subject storage using `subjects.txt`
- Automatic loading of saved subjects when SERA starts
- Automatic updating of `subjects.txt` after adding or removing subjects
- Used Python lists to manage subjects
- Used `readlines()` and `strip()` to process saved subjects
- Improved interaction between the Main Menu and Study Menu

## [v0.5.0] - Personal Organizer

### Added
- Dedicated Organizer menu
- Add tasks
- View tasks
- Remove tasks
- Add task date and time
- Date and time handling using `datetime`
- Persistent task storage using `tasks.json`
- Automatic loading of saved tasks when SERA starts
- JSON data handling using `json`
- Conversion between JSON strings and Python `datetime` objects
- Basic due-time reminder checking
- Date and time input validation
- Task-number validation
- Subject-number validation
- Improved error handling for invalid inputs
- Improved task management and organization

## [v0.6.0] - SERA Speaks

### Added
- Voice Assistant mode
- Speech-to-text using SpeechRecognition
- Microphone input using sounddevice
- Text-to-speech using edge-tts
- Audio playback using playsound3
- SERA can listen to spoken commands
- SERA can respond using voice
- Added support for basic voice commands
- Added Windows ARM64 FLAC converter workaround

### Improved
- Integrated voice features with the existing v0.5.0 Personal Organizer
- Preserved name memory from v0.3.0
- Preserved subject management from v0.4.0
- Preserved task and reminder management from v0.5.0
- Added a dedicated Voice Assistant option to the main menu

### Technical
- Added microphone recording and audio processing
- Added speech recognition error handling
- Added speech recognition service error handling
- Added asynchronous text-to-speech generation
- Added unique audio filenames for multiple spoken responses

### Status
- v0.6.0 completed and tested