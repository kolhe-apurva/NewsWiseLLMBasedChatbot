# NewsWiseLLMBasedChatbot
### A Collaborative Project by Apurva Kolhe & Vishrutha Reddy

## Overview
The NewsWiseLLMBasedChatbot is an innovative amalgamation of two advanced models: the T5 Summarization Model and the Llama 2 Model. Crafted by Apurva Kolhe and Vishrutha Reddy, this sophisticated chatbot excels in summarizing news articles and providing insightful answers to queries based on those summaries. The project unfolds in three distinct yet interconnected phases: the training and evaluation of the T5 Summarization Model, the fine-tuning and assessment of the Llama 2 Model, and their eventual convergence into an integrated, multifunctional chatbot.

## Part 1: T5 Summarization Model

### Overview
The T5 Summarization Model is designed to summarize news articles using the "cnn_dailymail" dataset. The process includes data preprocessing, model training, and evaluation.

### Installation
```
pip install transformers==4.20.0
pip install keras_nlp==0.3.0
pip install datasets
pip install huggingface-hub
pip install nltk
```

### Usage
- Data Loading and Preprocessing: Load and preprocess the CNN/DailyMail dataset.
- Model Setup: Initialize and configure the T5 small model using Hugging Face Transformers.
- Training: Train the model on the processed dataset.
- Evaluation: Evaluate the model's performance using the Rouge-L metric.
  
### Code Structure
- **Dependency Installation**: Importing necessary libraries and modules.
- **Data Loading**: Using the 'datasets' library to load the 'cnn_dailymail' dataset.
- **Data Preprocessing**: Tokenization and splitting of the dataset.
- **Model Initialization**: Setting up the T5 small model.
- **Model Training**: Training the model on the processed dataset.
- **Model Evaluation**: Evaluating the model using the Rouge-L metric.

### Additional Notes
- The project uses specific versions of libraries, so ensure compatibility by installing the specified versions.
- Adjustments might be necessary depending on the computing resources available.

---

## Part 2: Fine-Tuning - Llama 2 7B Model

### Overview
The Llama 2 Model is trained to answer questions based on news articles, using a dataset from Hugging Face. Post-training, the model is uploaded to Hugging Face for evaluation and integration into the chatbot.

### Installation
```
pip install autotrain-advanced
pip install huggingface_hub
# Additional dependencies for updating torch on Google Colab and others as required
```

### Process
1. **Model Training**: Train the Llama 2 Model using the `autotrain` utility from Hugging Face.
2. **Model Upload**: Upload the trained model to Hugging Face.

### Usage
- **Data Preparation**: Using a custom dataset for news question-answering from Hugging Face (Follow the README.md in the Dataset folder)
- **Training Configuration**: Setting up training parameters such as learning rate, batch size, and number of epochs.
- **Model Initialization and Training**: Using the `autotrain` utility for streamlined training and setup.
- **Post-Training Actions**: Uploading the trained model to Hugging Face.

### Evaluation
- Model Loading: Load the trained Llama 2 Model from Hugging Face.
- Data Loading: Prepare the evaluation data.
- Evaluation Metrics: Evaluate the model using BLEU score, ROUGE, and semantic similarity.

### Usage
- **Model Evaluation Setup**: Configuring the model for evaluation.
- **Performance Measurement**: Using different metrics to assess the model's performance on the test dataset.
- **Result Analysis**: Analyzing and visualizing the results obtained from the evaluation metrics.

## Additional Notes
- Ensure compatibility by installing the specified versions of the libraries.
- Adjust the training and evaluation parameters based on your specific requirements and the computing resources available.

---

## Part 3: Combined T5 and Llama Models into a Chatbot - NEWS-WISE

### Overview
This section integrates the T5 Summarization and Llama 2 Models into a Gradio-based chatbot.

### Installation
```
pip install autotrain-advanced
pip install huggingface_hub
pip install gradio
```

### Process
1. **Model Loading**: Load both the T5 Summarization Model and the Llama 2 Model from Hugging Face.
2. **Gradio Interface**: Set up a Gradio interface for the chatbot.
3. **Chatbot Functionality**: Enable the chatbot to summarize news articles (T5 Model) and answer questions (Llama 2 Model).

### Usage
- Users input a news article to get a summary and ask questions related to the summary.
- The Gradio interface facilitates interaction with the chatbot.

### Code Structure
- **Model Initialization**: Loading the T5 summarization model and the Llama2 question-answering model.
- **Gradio Interface Setup**: Configuring the Gradio interface for user interaction.
- **Summarization and Question Answering**: Integrating both models to provide a seamless chatbot experience.

### Additional Notes
- Update Gradio interface as needed.
- Ensure access to the Hugging Face hosted models.

### Chatbot Interactions

Here are some screenshots of the chatbot in action:

**Chatbot Summarizing A Given News Article**
![Chatbot Interaction Summarizer](/chatbot_interaction_images/summarizer)  

<br>
<br>

**Chatbot Generating Answers To The Given Questions, Based On The Previous Article**

<br>
<br>

![Chatbot Interaction Question1](/chatbot_interaction_images/question1)

![Chatbot Interaction Question2](/chatbot_interaction_images/question2)
