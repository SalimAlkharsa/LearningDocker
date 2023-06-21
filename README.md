# Sentiment Analysis Web App

The purpose of this was to familiarize myself with Docker more so than anything else. The model here used is an imported open source model.

This is a Python application that performs sentiment analysis on text input and provides the sentiment analysis results through a web interface.

## Requirements

- Python 3.9 or later
- Docker

## Setup and Usage

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/sentiment-analysis-web-app.git
   cd sentiment-analysis-web-app

2. Build the docker image:
   
   ```docker build -t sentiment-analysis-app .```
  
4. Run the Docker container:
   
   ```docker run -p 3000:3000 sentiment-analysis-app```


## Technologies Used

- Python
- Flask
- Transformers (Hugging Face)
- Docker


