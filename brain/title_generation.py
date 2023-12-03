import torch
from torch.utils.data import DataLoader, Dataset
from transformers import BertTokenizer, BertModel, GPT2LMHeadModel, AdamW

# Define a simple dataset class
class BlogTitleDataset(Dataset):
    def __init__(self, blog_texts, titles, tokenizer, max_length=512):
        self.blog_texts = blog_texts
        self.titles = titles
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.blog_texts)

    def __getitem__(self, idx):
        blog_text = self.blog_texts[idx]
        title = self.titles[idx]
        
        inputs = self.tokenizer.encode_plus(
            blog_text,
            title,
            add_special_tokens=True,
            max_length=self.max_length,
            padding='max_length',
            return_tensors='pt'
        )
        
        return {
            'input_ids': inputs['input_ids'].squeeze(),
            'attention_mask': inputs['attention_mask'].squeeze(),
            'labels': inputs['input_ids'].squeeze()
        }

# Example blog texts and corresponding titles (you should replace these with your data)
blog_texts = [
    "In this blog post, we'll explore fine-tuning a BERT model for title generation.",
    "Text generation is a fascinating field in natural language processing.",
    # Add more blog texts as needed
]
titles = [
    "Fine-Tuning BERT for Title Generation",
    "Exploring Text Generation in NLP",
    # Add more titles corresponding to the blog texts
]

# Initialize BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
encoder_model = BertModel.from_pretrained('bert-base-uncased')
decoder_model = GPT2LMHeadModel.from_pretrained('gpt2')

# Create a dataset and data loader
dataset = BlogTitleDataset(blog_texts, titles, tokenizer)
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# Define optimizer and loss function
optimizer = AdamW(decoder_model.parameters(), lr=1e-5)
criterion = torch.nn.CrossEntropyLoss()

# Training loop
encoder_model.eval()
decoder_model.train()
for epoch in range(5):  # Adjust the number of epochs as needed
    total_loss = 0.0
    for batch in dataloader:
        input_ids = batch['input_ids']
        attention_mask = batch['attention_mask']
        labels = batch['labels']
        
        optimizer.zero_grad()
        
        # Encode the blog text with BERT
        with torch.no_grad():
            encoder_outputs = encoder_model(input_ids, attention_mask=attention_mask)
            encoder_embeddings = encoder_outputs.last_hidden_state
        
        # Generate titles with the decoder
        outputs = decoder_model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
        
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1}, Loss: {total_loss}")

# Save the fine-tuned decoder model
decoder_model.save_pretrained('fine-tuned-title-generator')

# Inference (title generation)
encoder_model.eval()
decoder_model.eval()
for i, blog_text in enumerate(blog_texts):
    input_text = blog_text
    input_ids = tokenizer.encode(input_text, add_special_tokens=True, max_length=512, return_tensors='pt')
    generated_title_ids = decoder_model.generate(input_ids, max_length=50, num_return_sequences=1)
    generated_title = tokenizer.decode(generated_title_ids[0], skip_special_tokens=True)
    
    print(f"Blog Text {i+1}:\n{input_text}\nGenerated Title {i+1}:\n{generated_title}\n")
