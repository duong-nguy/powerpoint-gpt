# PowerPoint GPT (Using Mistral)

## Overview
**PowerPoint GPT** is an interactive project that allows you to **converse with your PowerPoint presentations** using natural language processing (NLP). Despite the name, this project leverages **Mistral**—a high-performance NLP model—rather than GPT, to provide an engaging and insightful experience by helping users navigate and extract content from their PowerPoint slides.

## Features
- **Natural Language Queries:** Ask questions about your presentation, and get relevant answers.
- **Content Summarization:** Summarize slide content quickly without needing to read through the entire presentation.

## Why Mistral?
While the name suggests "GPT," Mistral was chosen for its state-of-the-art performance, efficiency, and ability to handle complex queries with ease. This ensures that you get faster and more accurate responses while interacting with your presentations.

## Getting Started

### Prerequisites
- Python 3.x
- `pip` package manager
- PowerPoint file (`.pptx`) to interact with
- [Mistral](https://mistral.ai/) model integration

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/powerpoint-gpt.git
    cd powerpoint-gpt
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
3. Set up your environment variables:

    On Linux/macOS:
    ```bash
    export OPENAI_API_KEY="your_openai_api_key"
    export MISTRAL_API_KEY="your_mistral_api_key"
    ```

    On Windows:
    ```cmd
    set OPENAI_API_KEY=your_openai_api_key
    set MISTRAL_API_KEY=your_mistral_api_key
    ```

### Usage

1. Run the application:

    ```bash
    python main.py 
    ```

2. Interact with your PowerPoint using natural language queries:

    - **Example Queries:**
        - Query: Hello, what can you tell me about Barrier Free It?
        - Answer: Barrier Free IT is a company or product that focuses on making technology accessible to everyone, regardless of physical or cognitive barriers.



## Acknowledgments
- **Mistral AI** for providing the powerful model that drives this project.
- The **OpenAI GPT** family for inspiring the original idea.
- The open-source community for providing the tools and libraries to build this project.

---

Enjoy **PowerPoint GPT** (powered by Mistral) to make working with presentations smarter and more interactive!

