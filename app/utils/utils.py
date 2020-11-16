import streamlit as st
from PIL import Image

import numpy as np
import plotly.express as px
import pandas as pd

import os
import json

from .preprocessing import cleaning


def load_local_image(image_path, image_resize=None):
    """ Helper function to load/resize an image from the local.

    Args:
        image_path (str): The image path.
        image_resize (tuple): The image-resize in a tuple form of (width, height)

    Returns:
        return Pillow.Image object
    """
    if not os.path.exists(image_path):
        return None

    try:
        image = Image.open(image_path)
        if isinstance(image_resize, tuple):
            image.resize(image_resize)

        return image
    except Exception as e:
        print(f'E [load_local_image]: {e}')

    return None


def load_local_text(text_path):
    """ Helper function to load a text file from the local.

    Args:
        text_path (str): The text file path.

    Returns:
        return string text!
    """
    if not os.path.exists(text_path):
        return ''

    with open(text_path) as f:
        text = f.read()

    return text


def load_local_css(css_path):
    """ Helper function to load a css file from the local.

    Args:
        css_path (str): The css file path.
    """
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def load_remote_css(css_url):
    """ Helper function to load a css file from the url.

    Args:
        css_url (str): The css url path.
    """
    st.markdown(f'<link href="{css_url}" rel="stylesheet">', unsafe_allow_html=True)


def load_json(json_path):
    """ Helper function to load a json.

    Args:
        json_path (str): The json path.
    """
    data = {}
    if not os.path.exists(json_path):
        return data

    try:
        with open(json_path, 'r') as fj:
            data = json.load(fj)
            return data
    except:
        return data


def load_examples(example_path, custom_text="متن خودت رو وارد کن"):
    df = pd.read_json(example_path)
    names = df.name.values.tolist()
    names = [cleaning(name) for name in names]
    mapping = {cleaning(df['name'].iloc[i]): (
        df['text'].iloc[i],
        df['link'].iloc[i],
    ) for i in range(len(names))}
    names.append(custom_text)
    mapping[custom_text] = ('', '')
    return names, mapping
