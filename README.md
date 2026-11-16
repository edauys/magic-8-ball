# 🎱 Magic 8-Ball

An interactive Python Magic 8-Ball that answers yes-or-no questions with one of nine random fortunes. Built as an extension of the **Codecademy Magic 8-Ball** introductory Python exercise.

## Features
- Enter your name (optional) and any yes-or-no question.
- Receive one of nine randomly selected fortunes.
- Friendly handling of empty questions.
- Play repeatedly in the terminal, or use the Streamlit web interface.

## Run in the terminal
Requires Python 3.9 or newer. No third-party dependencies are needed.

```bash
python magic8.py
```

## Run the web app locally

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Publish on GitHub
Create a new public repository named `magic-8-ball`, then upload these files through **Add file → Upload files**. Do not upload credentials, `.env` files, or other secrets.

## Deploy the web app
In [Streamlit Community Cloud](https://share.streamlit.io/), connect the GitHub repository and choose `app.py` as the entry point. Follow the platform's prompts to deploy. Free hosting has availability and resource limitations.

## Attribution
Based on Codecademy's **Magic 8-Ball** Python learning project. The terminal interaction, validation, reusable fortune function, and Streamlit interface are extensions to the original exercise.

## License
No license has been selected. Add a license if you want to grant reuse permissions.
