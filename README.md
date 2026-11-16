# Magic 8-Ball

An interactive Python application that generates randomized responses to yes-or-no questions through a command-line interface or Streamlit web application.

## Features

- Generates one of nine randomized responses to user-submitted questions.
- Accepts optional names and custom questions.
- Validates empty questions and supports multiple questions per session.
- Provides command-line and browser-based interfaces.

## Tech Stack

- **Language:** Python 3.9+
- **Standard Library:** `random`
- **Web Framework:** Streamlit

## Getting Started

**Requirements:** Python 3.9 or later.

### Clone the Repository

```bash
git clone https://github.com/edauys/magic-8-ball.git
cd magic-8-ball
```

### Command-Line Version

```bash
python3 magic8.py
```

### Web Application

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Launch the application:

```bash
python3 -m streamlit run app.py
```

The application runs locally at `http://localhost:8501`.

## Project Structure

```text
magic-8-ball/
├── app.py
├── magic8.py
├── requirements.txt
└── README.md
```

## About

A Python project demonstrating randomization, functions, input validation, and interactive application development.
