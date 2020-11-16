import hazm
from cleantext import clean
import emoji
import re

normalizer = hazm.Normalizer()


def upper_repl(match):
    """ Convert mask-special tokens to real special tokens """
    return " [" + match.group(1).upper().replace('-', '_') + "] "


def convert_emoji_to_text(text, delimiters=('[', ']')):
    """ Convert emojis to something readable by the vocab and model """
    text = emoji.demojize(text, delimiters=delimiters)
    return text


def clean_html(raw_html):
    """ Remove all html tags """
    cleaner = re.compile('<.*?>')
    cleaned = re.sub(cleaner, '', raw_html)
    return cleaned


def clean_text(
        raw_text,
        fix_unicode=True,
        to_ascii=False,
        lower=True,
        no_line_breaks=True,
        no_urls=True,
        no_emails=True,
        no_phone_numbers=True,
        no_numbers=False,
        no_digits=False,
        no_currency_symbols=True,
        no_punct=False,
        replace_with_url="",
        replace_with_email="",
        replace_with_phone_number="",
        replace_with_number="",
        replace_with_digit="0",
        replace_with_currency_symbol=""):
    """ Preprocessing and normalization the text a the low level """
    cleaned = clean(
        raw_text,
        fix_unicode=fix_unicode,
        to_ascii=to_ascii,
        lower=lower,
        no_line_breaks=no_line_breaks,
        no_urls=no_urls,
        no_emails=no_emails,
        no_phone_numbers=no_phone_numbers,
        no_numbers=no_numbers,
        no_digits=no_digits,
        no_currency_symbols=no_currency_symbols,
        no_punct=no_punct,
        replace_with_url=replace_with_url,
        replace_with_email=replace_with_email,
        replace_with_phone_number=replace_with_phone_number,
        replace_with_number=replace_with_number,
        replace_with_digit=replace_with_digit,
        replace_with_currency_symbol=replace_with_currency_symbol
    )
    return cleaned


def cleaning(
        text,
        default_cleaning=True,
        normalize_cleaning=True,
        half_space_cleaning=True,
        html_cleaning=True,
        emoji_convert=False,
        username_cleaning=True,
        hashtag_cleaning=True,
        fix_unicode=True,
        to_ascii=False,
        lower=True,
        no_line_breaks=True,
        no_urls=True,
        no_emails=True,
        no_phone_numbers=True,
        no_numbers=False,
        no_digits=False,
        no_currency_symbols=True,
        no_punct=False,
        replace_with_url="",
        replace_with_email="",
        replace_with_phone_number="",
        replace_with_number="",
        replace_with_digit="0",
        replace_with_currency_symbol=""):
    """ A hierarchy of normalization and preprocessing """
    text = text.strip()

    if username_cleaning:
        text = re.sub(r"\@[\w.-_]+", " ", text)

    if hashtag_cleaning:
        text = text.replace('#', ' ')
        text = text.replace('_', ' ')

    if emoji_convert:
        text = emoji.emojize(text)
        text = convert_emoji_to_text(text)

    # regular cleaning
    if default_cleaning:
        text = clean_text(
            text,
            fix_unicode,
            to_ascii,
            lower,
            no_line_breaks,
            no_urls,
            no_emails,
            no_phone_numbers,
            no_numbers,
            no_digits,
            no_currency_symbols,
            no_punct,
            replace_with_url,
            replace_with_email,
            replace_with_phone_number,
            replace_with_number,
            replace_with_digit,
            replace_with_currency_symbol
        )

    # cleaning HTML
    if html_cleaning:
        text = clean_html(text)

    # normalizing
    if normalize_cleaning:
        text = normalizer.normalize(text)

    # removing weird patterns
    weird_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u'\U00010000-\U0010ffff'
        u"\u200d"
        u"\u2640-\u2642"
        u"\u2600-\u2B55"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\u3030"
        u"\ufe0f"
        u"\u2069"
        u"\u2066"
        u"\u2013"
        u"\u2068"
        u"\u2067"
        "]+", flags=re.UNICODE)

    text = weird_pattern.sub(r'', text)

    # removing extra spaces, hashtags
    text = re.sub("#", "", text)
    # text = re.sub("\s+", " ", text)

    if emoji_convert:
        text = re.sub(r"\[(\w.+)\]", upper_repl, text)
        # text = re.sub("\s+", " ", text)

    if half_space_cleaning:
        text = text.replace('\u200c', ' ')
        # text = re.sub("\s+", " ", text)

    return text
