import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import os
from huggingface_hub import login

login(token="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")

torch.classes.__path__ = [os.path.join(torch.__path__[0], torch.classes.__file__)] 

# # Setting up the model and tokenizer
# torch.random.manual_seed(666)
# model = AutoModelForCausalLM.from_pretrained(
#     "microsoft/Phi-3-mini-4k-instruct",
#     device_map="mps",
#     torch_dtype="auto",
#     trust_remote_code=True,
# )

# tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")

# pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

# def get_output(input_text: str) -> str:
#     messages = [
#         {"role": "system", "content": "You are a writer at English proficiency C2."},
#         {"role": "user", "content": "Rewrite the following sentence to C2 proficiency: I am in the leftmost lane on a multi-lane road. I am proceeding forward because my path is clear."},
#         {"role": "assistant", "content": "OUTPUT: I am in the leftmost lane of a multi-lane road, continuing forward as my path is clear."},
#         {"role": "user", "content": f"Rewrite the following sentence to C2 proficiency: {input_text}"},
#     ]
    
#     generation_args = {
#         "max_new_tokens": 128,
#         "return_full_text": False,
#         "do_sample": False,
#     }

#     output = pipe(messages, **generation_args)
#     return output[0]['generated_text']

model_id = "meta-llama/Llama-3.2-1B-Instruct"

print("Loading model!")
pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype=torch.bfloat16,
    device_map="cpu",
)
print("Model loaded!")

def get_output(input_text: str):
    messages = [{"role": "system", "content": f"Text: {input_text}"},
                {"role": "user", "content": 'Rewrite the text with a C2 proficiency.'},
                ]
    outputs = pipe(
        messages,
        max_new_tokens=128,
    )
    output_text = outputs[0]["generated_text"][-1]['content']
    return output_text