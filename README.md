# Summary Generator

## Overview
This is a simple **Summary Generator** built using **Streamlit**. Users input a blog URL and select the type of content (**News, Blog, Article, or Research Paper**). Upon submission, the system extracts the article using **LangChain**, processes it with **LLaMA**, and generates a concise summary while ensuring the token limit is not exceeded.

## Features
- **Streamlit UI:** Simple and interactive web interface.
- **Content Extraction:** Uses **LangChain** to retrieve the article.
- **AI Summarization:** Generates structured summaries using **LLaMA**.
- **Tokenization Handling:** Ensures the summary remains within the allowed limit.

## Installation
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/summary-generator.git
   cd summary-generator
   ```
2. **Create and Activate Virtual Environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. **Run the application:**
   ```sh
   streamlit run main.py
   ```
2. **Enter the blog/news/article URL.**
3. **Select the content type.**
4. **Hit Submit** to generate the summary.

## Project Structure
```
./summary-generator
│── main.py               # Streamlit app logic
│── summarizer.py         # LangChain + LLaMA summarization logic
│── requirements.txt      # Dependencies
│── ./assets/image.png    # Reference image
```

## Screenshot
![](/assets/image.png)

## Notes
- This is a **dummy project** for demonstration purposes.
- Future improvements may include **better prompt engineering** and **fine-tuned models** for different content types.

