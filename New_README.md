
# ChatBot Document Processor System

## Overview
This repository contains a Python application that integrates document processing capabilities with a chatbot system to provide document-based question answering. The system processes documents, creates a vector database, and uses this to generate responses to user queries.

## Repository Structure
- `merge.py`: Main script combining all functionalities.
- `.gitignore`: Specifies intentionally untracked files to ignore.
- `api_key.py`: Manages API keys for external services.
- `chat_bot.py`: Implements the chatbot functionality for answering user queries.
- `content.pdf`: Sample document to be processed and used for query answering.
- `document_processor.py`: Processes documents and builds a vector database for retrieval.
- `main.py`: Main entry point of the application.
- `prompt_creator.py`: Handles the creation of prompts for the chatbot.

## Features
- **Document Loading and Splitting**: Load PDF documents and split them into manageable sections.
- **Vector Database Creation**: Build a vector database from processed text to support document retrieval.
- **Query Answering**: Use the document context to generate relevant responses to user queries.
- **Prompt Management**: Dynamically create and manage prompt templates for the chatbot based on the document content.

## How to Run
1. Install the required dependencies:
   ```bash
   pip install langchain-community langchain-google-genai IPython
   ```
2. Execute the main script:
   ```bash
   python main.py
   ```
3. Follow the command line prompts to input questions and receive answers.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
