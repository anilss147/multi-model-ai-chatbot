# 🤖 Multi-Model AI Chatbot (Google Colab & Local)

This project is a **Gradio-based chatbot** powered by **state-of-the-art AI models** like **LLaMA-3, Mistral-7B, Falcon-7B**, and more.  
It allows you to interact with **multiple AI models dynamically** without requiring an API key. The chatbot is designed for ease of use, whether you're running it on **Google Colab** or your **local machine**.

---

## 🚀 Features

### 1. **Supports Multiple AI Models**
   - Choose from a variety of pre-trained models, including:
     - **LLaMA-3** (8B and 70B variants)
     - **Mistral-7B** and **Mistral-7B-Instruct**
     - **Falcon-7B** and **Falcon-40B**
     - **LLaMA-2** (7B, 13B, and 70B variants)
     - **Mixtral-8x7B**
     - **RedPajama-INCITE-7B**
     - **MPT-7B**
   - Each model is optimized for specific tasks like conversational AI, instruction following, or general-purpose language generation.

### 2. **Dynamic Model Switching**
   - Seamlessly switch between models during a conversation without restarting the application.
   - Enables users to experiment with different models and compare their responses in real-time.

### 3. **Customizable Response Length**
   - Adjust the maximum response length using a slider in the interface.
   - Provides flexibility for generating short or detailed responses.

### 4. **Clear Chat History**
   - Reset the conversation with a single click.
   - Useful for starting fresh conversations or testing new models.

### 5. **Token Limit Management**
   - Automatically handles token limits for large models to prevent errors.
   - Ensures that input prompts and responses stay within the model's maximum token capacity.

### 6. **Runs on Google Colab or Locally**
   - **Google Colab**: Leverage free GPU resources for faster inference.
   - **Local Setup**: Run the chatbot on your own machine with GPU support for better control and privacy.

### 7. **Gradio Chat UI**
   - A clean and intuitive user interface built with **Gradio**.
   - Features include:
     - Dropdown menu for model selection.
     - Input box for user messages.
     - Chat history display for ongoing conversations.
     - Buttons to send messages and clear chat history.

### 8. **No API Key Required**
   - Fully open-source and free to use.
   - No need to sign up for external services or pay for API access.

---

## 📥 Installation & Setup

### **1️⃣ Run on Google Colab**
1. Open **[Google Colab](https://colab.research.google.com/)** and create a new notebook.
2. Install the required dependencies by running the following command in a Colab cell:
   ```sh
   !pip install torch transformers accelerate gradio
   ```
3. Clone this repository:
   ```sh
   !git clone    https://github.com/anilss147/multi-model-ai-chatbot.git
   ```
4. Navigate to the project directory and run the app:
   ```sh
   %cd multi-model-chatbot
   !python app.py
   ```

### **2️⃣ Run Locally**
1. Clone this repository:
   ```sh
   git clone    https://github.com/anilss147/multi-model-ai-chatbot.git
   ```
2. Navigate to the project directory:
   ```sh
   cd multi-model-chatbot
   ```
3. Install the required dependencies:
   ```sh
   pip install torch transformers accelerate gradio
   ```
4. Run the application:
   ```sh
   python app.py
   ```

---

## 🖥️ Usage

1. **Launch the Gradio Interface**:
   - When you run the app, the Gradio interface will automatically open in your browser.
2. **Select an AI Model**:
   - Use the dropdown menu to choose from the available AI models.
3. **Type Your Message**:
   - Enter your message in the input box and click the **Send** button.
4. **View AI Responses**:
   - The AI's response will appear in the chat window along with the conversation history.
5. **Clear Chat History**:
   - Use the **Clear Chat History** button to reset the conversation.
6. **Adjust Response Length**:
   - Use the slider to set the maximum response length (in tokens) for the AI.

---

## 🛠️ Technologies Used

- **Python**: The core programming language for the application.
- **Gradio**: A Python library for building interactive web interfaces.
- **Transformers**: Hugging Face library for loading and interacting with pre-trained AI models.
- **Torch**: A deep learning framework for GPU-accelerated model inference.
- **Accelerate**: A library for efficient model deployment on GPUs.

---

## 🌟 Key Highlights

- **Dynamic Model Selection**:
  - Switch between models in real-time without restarting the app.
- **Error Handling**:
  - Gracefully handles errors during model loading or response generation.
- **Customizable Settings**:
  - Allows users to adjust response length and clear chat history easily.
- **Open-Source**:
  - Fully transparent and free to use for personal or educational purposes.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🌟 Acknowledgments

- **Hugging Face**: For providing pre-trained models and the Transformers library.
- **Gradio**: For the easy-to-use UI framework.
- **Open-Source Community**: For making this project possible through contributions and support.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project, feel free to fork the repository and submit a pull request.

---

## 📧 Contact

For questions or feedback, please reach out to [anilsherika207@gmail.com].

---

### Why This README is Beginner-Friendly:
1. **Clear Feature Descriptions**: Each feature is explained in detail, making it easy for new users to understand the chatbot's capabilities.
2. **Step-by-Step Installation**: Instructions for both Google Colab and local setups are provided with clear commands.
3. **Usage Instructions**: A detailed guide on how to interact with the chatbot, including selecting models, sending messages, and clearing chat history.
4. **Technologies Section**: Highlights the tools and libraries used, helping developers understand the tech stack.
5. **Contributing Section**: Encourages community involvement and provides a pathway for contributions.
6. **Contact Section**: Offers a way for users to reach out for support or feedback.

Let me know if you need further refinements or additional sections!# 🤖 Multi-Model AI Chatbot (Google Colab & Local)

This project is a **Gradio-based chatbot** powered by **state-of-the-art AI models** like **LLaMA-3, Mistral-7B, Falcon-7B**, and more.  
It allows you to interact with **multiple AI models dynamically** without requiring an API key. The chatbot is designed for ease of use, whether you're running it on **Google Colab** or your **local machine**.

---

## 🚀 Features

### 1. **Supports Multiple AI Models**
   - Choose from a variety of pre-trained models, including:
     - **LLaMA-3** (8B and 70B variants)
     - **Mistral-7B** and **Mistral-7B-Instruct**
     - **Falcon-7B** and **Falcon-40B**
     - **LLaMA-2** (7B, 13B, and 70B variants)
     - **Mixtral-8x7B**
     - **RedPajama-INCITE-7B**
     - **MPT-7B**
   - Each model is optimized for specific tasks like conversational AI, instruction following, or general-purpose language generation.

### 2. **Dynamic Model Switching**
   - Seamlessly switch between models during a conversation without restarting the application.
   - Enables users to experiment with different models and compare their responses in real-time.

### 3. **Customizable Response Length**
   - Adjust the maximum response length using a slider in the interface.
   - Provides flexibility for generating short or detailed responses.

### 4. **Clear Chat History**
   - Reset the conversation with a single click.
   - Useful for starting fresh conversations or testing new models.

### 5. **Token Limit Management**
   - Automatically handles token limits for large models to prevent errors.
   - Ensures that input prompts and responses stay within the model's maximum token capacity.

### 6. **Runs on Google Colab or Locally**
   - **Google Colab**: Leverage free GPU resources for faster inference.
   - **Local Setup**: Run the chatbot on your own machine with GPU support for better control and privacy.

### 7. **Gradio Chat UI**
   - A clean and intuitive user interface built with **Gradio**.
   - Features include:
     - Dropdown menu for model selection.
     - Input box for user messages.
     - Chat history display for ongoing conversations.
     - Buttons to send messages and clear chat history.

### 8. **No API Key Required**
   - Fully open-source and free to use.
   - No need to sign up for external services or pay for API access.

---

## 📥 Installation & Setup

### **1️⃣ Run on Google Colab**
1. Open **[Google Colab](https://colab.research.google.com/)** and create a new notebook.
2. Install the required dependencies by running the following command in a Colab cell:
   ```sh
   !pip install torch transformers accelerate gradio
   ```
3. Clone this repository:
   ```sh
   !git clone    https://github.com/anilss147/multi-model-ai-chatbot.git
   ```
4. Navigate to the project directory and run the app:
   ```sh
   %cd multi-model-chatbot
   !python app.py
   ```

### **2️⃣ Run Locally**
1. Clone this repository:
   ```sh
   git clone   https://github.com/anilss147/multi-model-ai-chatbot.git
   ```
2. Navigate to the project directory:
   ```sh
   cd multi-model-chatbot
   ```
3. Install the required dependencies:
   ```sh
   pip install torch transformers accelerate gradio
   ```
4. Run the application:
   ```sh
   python app.py
   ```

---

## 🖥️ Usage

1. **Launch the Gradio Interface**:
   - When you run the app, the Gradio interface will automatically open in your browser.
2. **Select an AI Model**:
   - Use the dropdown menu to choose from the available AI models.
3. **Type Your Message**:
   - Enter your message in the input box and click the **Send** button.
4. **View AI Responses**:
   - The AI's response will appear in the chat window along with the conversation history.
5. **Clear Chat History**:
   - Use the **Clear Chat History** button to reset the conversation.
6. **Adjust Response Length**:
   - Use the slider to set the maximum response length (in tokens) for the AI.

---

## 🛠️ Technologies Used

- **Python**: The core programming language for the application.
- **Gradio**: A Python library for building interactive web interfaces.
- **Transformers**: Hugging Face library for loading and interacting with pre-trained AI models.
- **Torch**: A deep learning framework for GPU-accelerated model inference.
- **Accelerate**: A library for efficient model deployment on GPUs.

---

## 🌟 Key Highlights

- **Dynamic Model Selection**:
  - Switch between models in real-time without restarting the app.
- **Error Handling**:
  - Gracefully handles errors during model loading or response generation.
- **Customizable Settings**:
  - Allows users to adjust response length and clear chat history easily.
- **Open-Source**:
  - Fully transparent and free to use for personal or educational purposes.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🌟 Acknowledgments

- **Hugging Face**: For providing pre-trained models and the Transformers library.
- **Gradio**: For the easy-to-use UI framework.
- **Open-Source Community**: For making this project possible through contributions and support.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project, feel free to fork the repository and submit a pull request.

---

## 📧 Contact

For questions or feedback, please reach out to [anilsherikar207@gmail.com].

---

### Why This README is Beginner-Friendly:
1. **Clear Feature Descriptions**: Each feature is explained in detail, making it easy for new users to understand the chatbot's capabilities.
2. **Step-by-Step Installation**: Instructions for both Google Colab and local setups are provided with clear commands.
3. **Usage Instructions**: A detailed guide on how to interact with the chatbot, including selecting models, sending messages, and clearing chat history.
4. **Technologies Section**: Highlights the tools and libraries used, helping developers understand the tech stack.
5. **Contributing Section**: Encourages community involvement and provides a pathway for contributions.
6. **Contact Section**: Offers a way for users to reach out for support or feedback.

Let me know if you need further refinements or additional sections!