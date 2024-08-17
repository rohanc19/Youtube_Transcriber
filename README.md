# Advanced YouTube Video Summarizer

## 🎥 Description

The Advanced YouTube Video Summarizer is a Streamlit-based web application that leverages Google's Generative AI to provide comprehensive summaries and analysis of YouTube video content. This tool extracts video transcripts, offers translation capabilities, generates summaries in various styles, and allows users to ask questions about the video content.

## 🌟 Features

- **Video Transcript Extraction**: Automatically fetches the transcript from any YouTube video URL.
- **Multi-language Support**: Translates video content to various languages.
- **Customizable Summaries**: Generate summaries in different styles (Detailed Notes, Key Points, ELI5).
- **Adjustable Summary Length**: Control the word count of generated summaries.
- **Q&A Functionality**: Ask questions about the video content and receive AI-generated answers.
- **User-friendly Interface**: Clean and intuitive Streamlit-based UI.
- **Download and Copy Options**: Easy sharing of generated summaries.

## 🛠 Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/advanced-youtube-summarizer.git
   cd advanced-youtube-summarizer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the project root and add your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## 🚀 Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and navigate to the provided local URL (usually `http://localhost:8501`).

3. Enter a YouTube video URL in the input field.

4. Choose your desired summary options (type, word limit, language).

5. Click "Generate Summary" to view the AI-generated summary.

6. Use the Q&A section to ask specific questions about the video content.

## 📚 Dependencies

- streamlit
- python-dotenv
- google-generativeai
- youtube_transcript_api
- googletrans
- pandas

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/advanced-youtube-summarizer/issues).

## 📝 License

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.

## 🙏 Acknowledgements

- Google Generative AI
- YouTube Transcript API
- Streamlit
