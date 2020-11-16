import streamlit as st
import torch
from transformers import (
    BertTokenizerFast,
    EncoderDecoderConfig,
    EncoderDecoderModel
)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


@st.cache(allow_output_mutation=True, show_spinner=False)
def load_tokenizer(model_name_or_path):
    return BertTokenizerFast.from_pretrained(model_name_or_path)


@st.cache(allow_output_mutation=True, show_spinner=False)
def load_config(model_name_or_path):
    return EncoderDecoderConfig.from_pretrained(model_name_or_path)


@st.cache(allow_output_mutation=True, show_spinner=False)
def load_model(model_name_or_path, config=None):
    if config:
        model = EncoderDecoderModel.from_pretrained(model_name_or_path, config=config)
    else:
        model = EncoderDecoderModel.from_pretrained(model_name_or_path)

    return model.to(device)


# @st.cache(allow_output_mutation=True, show_spinner=False)
def generate_output(
        model,
        tokenizer,
        text,
        max_length=512):
    inputs = tokenizer([text], padding="max_length", truncation=True, max_length=max_length, return_tensors="pt")
    input_ids = inputs.input_ids.to(device)
    attention_mask = inputs.attention_mask.to(device)

    outputs = model.generate(input_ids, attention_mask=attention_mask)
    output_str = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    output_str = [op.replace('هه', 'ه‌ه') for op in output_str]
    return output_str
