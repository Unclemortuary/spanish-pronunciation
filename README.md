# Spanish Pronunciation Project

This project generates audio files with the pronunciation of specified Spanish words using the `gtts` (Google Text-to-Speech) package.

## Project Structure

```
spanish-pronunciation
├── src
│   ├── main.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/spanish-pronunciation.git
   cd spanish-pronunciation
   ```

2. **Create a virtual environment (optional but recommended):**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Open `src/main.py` and modify the list of words you want to generate audio for.
2. Run the script:
   ```
   python src/main.py
   ```

3. The audio files will be saved in the same directory as the script.

## Dependencies

- `gtts`: Google Text-to-Speech library for Python.