

#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
# Code for hugging face


import requests

# Replace with your Hugging Face API key
API_KEY = "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"

# Hugging Face Inference API URL for Code Llama - Instruct
API_URL = "https://api-inference.huggingface.co/models/codellama/CodeLlama-7b-hf"

# Assembly code input
asm_code = """
section .text
    global _start
_start:
    mov eax, 1
    mov ebx, 0
    int 0x80
"""

# Create the prompt for Code Llama
prompt = f"Convert the following x86 assembly code into an equivalent C code:\n\n{asm_code}\n\nC code:"

# Request payload
headers = {"Authorization": f"Bearer {API_KEY}"}
payload = {"inputs": prompt}

# Send request to Hugging Face API
response = requests.post(API_URL, headers=headers, json=payload)

# Check response
if response.status_code == 200:
    c_code = response.json()[0]["generated_text"]
    print("\n🔥 Converted C Code:\n")
    print(c_code)
else:
    print("Error:", response.status_code, response.text)
