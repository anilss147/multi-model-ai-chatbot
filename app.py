import torch
import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer

# Full list of AI models
AVAILABLE_MODELS = {
    "LLaMA-3-8B": "meta-llama/Meta-Llama-3-8B",
    "LLaMA-3-70B": "meta-llama/Meta-Llama-3-70B",
    "LLaMA-2-7B": "meta-llama/Llama-2-7b-chat-hf",
    "LLaMA-2-13B": "meta-llama/Llama-2-13b-chat-hf",
    "LLaMA-2-70B": "meta-llama/Llama-2-70b-chat-hf",
    "Mistral-7B": "mistralai/Mistral-7B-Instruct-v0.1",
    "Mistral-7B-Instruct": "mistralai/Mistral-7B-Instruct",
    "Mixtral-8x7B": "mistralai/Mixtral-8x7B-Instruct-v0.1",
    "Falcon-7B": "tiiuae/falcon-7b-instruct",
    "Falcon-40B": "tiiuae/falcon-40b-instruct",
    "RedPajama-INCITE-7B": "togethercomputer/RedPajama-INCITE-7B-Chat",
    "MPT-7B": "mosaicml/mpt-7b-chat"
}

# Cache loaded models to avoid reloading
loaded_models = {}

def load_model(model_name):
    """Load the selected model only if not already loaded."""
    if model_name not in loaded_models:
        try:
            print(f"🔄 Loading model: {model_name}...")
            tokenizer = AutoTokenizer.from_pretrained(AVAILABLE_MODELS[model_name])
            model = AutoModelForCausalLM.from_pretrained(
                AVAILABLE_MODELS[model_name], torch_dtype=torch.float16, device_map="auto"
            )
            loaded_models[model_name] = (model, tokenizer)
        except Exception as e:
            print(f"❌ Error loading model {model_name}: {e}")
            raise RuntimeError(f"Failed to load model: {e}")
    return loaded_models[model_name]

def chat_with_ai(model_name, message, chat_history, max_tokens=200):
    """Generate response from the selected model."""
    if not message.strip():
        return "⚠️ Please enter a valid message.", chat_history

    model, tokenizer = load_model(model_name)
    
    chat_history_text = "\n".join([f"User: {m[0]}\nAI: {m[1]}" for m in chat_history])
    prompt = f"{chat_history_text}\nUser: {message}\nAI:"

    # Ensure token limit is respected
    max_input_tokens = model.config.max_position_embeddings - max_tokens
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_input_tokens).to("cuda")
    
    try:
        output = model.generate(**inputs, max_new_tokens=max_tokens)
        response = tokenizer.decode(output[0], skip_special_tokens=True)
        response = response.split("AI:")[-1].strip()
    except Exception as e:
        response = f"❌ Error generating response: {e}"

    chat_history.append((message, response))
    return response, chat_history

# Gradio UI
with gr.Blocks() as chat_ui:
    gr.Markdown("# 🤖 Multi-Model AI Chatbot (ALL Models)")

    with gr.Row():
        model_selector = gr.Dropdown(
            choices=list(AVAILABLE_MODELS.keys()),
            value="Mistral-7B",
            label="Choose AI Model"
        )
        max_tokens_slider = gr.Slider(
            minimum=50, maximum=500, value=200, step=10, label="Max Response Tokens"
        )
        clear_button = gr.Button("Clear Chat History")

    chat_history = gr.State([])

    def clear_history():
        return []

    chat_interface = gr.ChatInterface(
        fn=lambda message, chat_history: chat_with_ai(
            model_selector.value, message, chat_history, max_tokens_slider.value
        ),
        title="Multi-Model Chatbot",
        description="Select an AI model and chat!",
    )

    clear_button.click(fn=clear_history, inputs=[], outputs=[chat_history])

chat_ui.launch(debug=True, share=True)