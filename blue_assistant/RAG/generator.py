from transformers import AutoTokenizer, AutoModelForCausalLM

class Generator:
    def __init__(self, model_name="gpt2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate(self, prompt, max_length=300):
        inputs = self.tokenizer(prompt, return_tensors='pt')
        outputs = self.model.generate(
            inputs.input_ids, 
            max_length=max_length, 
            num_return_sequences=1, 
            no_repeat_ngram_size=2,
            early_stopping=True
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)