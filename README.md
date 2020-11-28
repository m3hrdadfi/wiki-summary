# Wiki Summary

This [paper](https://arxiv.org/abs/1907.12461) introduced the opportunity to use available pre-trained LMs (BERT, GPT-2, and RoBERTa) to achieve state-of-the-art results on some interesting NLP tasks like Text Summaziration.
So, I trained an EncoderDecoder model based on parsBERT on [WikiSummary](http://github.com/m3hrdadfi/wiki-summary) (A summarization dataset extracted from Wikipedia).
The model achieved an 8.47 ROUGE-2 score.

[![Wiki Summarization](assets/screenshot.png)](https://youtu.be/sBEIcP9Eipo)

## Dataset information
The dataset extracted from Persian Wikipedia into the form of articles and highlights. I cleaned the dataset into pairs of articles and highlights and reduced the articles' length (only version 1.0.0) and highlights' length to a maximum of 512 and 128, respectively, suitable for parsBERT. 
Also, for making things simple, converted the dataset into the [HuggingFace' datasets](https://github.com/m3hrdadfi/wiki-summary/tree/master/datasets), which is available in the [repo](https://github.com/m3hrdadfi/wiki-summary/tree/master/datasets). 
Or you can access the `csv` format here:

**Version 1.0.0**
- [Train Set](https://drive.google.com/uc?id=1-CaP3xHgZxOGjQ3pXC5tr9YnIajmel-t)
- [Dev Set](https://drive.google.com/uc?id=1-2g2gkDeNaN-vth-8Mgit_ovmSkVh91u)
- [Test Set](https://drive.google.com/uc?id=1-9G4yYP6YO8oMA-o4cTe9NJpEyr7x5jg)

**Version 2.0.0**
- [Train Set](https://drive.google.com/uc?id=1-DDO0tYW-NIJ5b94W8R7ynltUPNC6LPu)
- [Dev Set](https://drive.google.com/uc?id=1-2NN4OAdTnEI6Ul5EqQ8ISG0BhcbxWGB)
- [Test Set](https://drive.google.com/uc?id=1-AWPStfvTQKSwQiAR0fCjzK4eMK1Ww4W)


| Version 	|  Train 	| Validation 	|  Test 	|
|:-------:	|:------:	|:----------:	|:-----:	|
|  1.0.0  	| 45,653 	|    5,073   	| 5,637 	|
|  2.0.0  	| 34,153 	|    3,795   	| 3,754 	|


### Example
An example ID is `c291771f3b7d6dbc229fda944b7c03a7a1834263`. These are heximal formated SHA1 hashes of the urls where the stories were retrieved from.
For each ID, there is a string for the article, a string for the highlights, and a string for the id.

|                    ID                    	|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Article                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    	|                                                                                                                                                                                                                                                                          Hightlights                                                                                                                                                                                                                                                                          	|
|:----------------------------------------:	|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:	|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:	|
| `c291771f3b7d6dbc229fda944b7c03a7a1834263` 	| قبل از به وجود آمدن دی سی، در خلا و فضایی عاری از هرگونه حیات که تنها پرایمال مانیتور بود، یهوه بوسیله قدرت های نامحدود دو برادر خلق کرد؛ یکی از آن ها میکائیل دمیورگوس، و دیگری سمائیل نام گرفت که بعدها با عنوان لوسیفر مورنینگ استار شناخته شد. پس از شکل گیری این دو تن، یهوه آن ها را هدایت نمود و به آن ها چگونگی استفاده از قدرت هایشان را آموخت، در نتیجه آن ها شکلی از خلقت را ایجاد کردند که هم اکنون به عنوان فرضیه چندجهانی دی سی شناخته می شود. میلیاردها سال پیش، لوسیفر فرشته مقرب دست به شورشی علیه پادشاهی بهشت زد و در نتیجه به فضایی عاری از ماده و فاقد هر گونه شکل تحت عنوان چائوپلازم تبعید شد. سپس چائوپلازم تبدیل بهک فضای متروک، ویران و گستره ای تهی با عنوان دوزخ شد، مقصد نهایی برای ارواح ملعون، جایی که مورنینگ استار فرمانروایی می کرد و در انتظار روزی بود تا بتواند دوباره آزاد شود. زمانی که تاریکی اعظم (شیطان وحشی بزرگ) بیدار شده و بازگشت، لوسیفر مجبور شد قدرت خود را با او سهیم شود و فرمانروایی خود را با بعل الذباب و عزازیل به اشتراک گذاشت. بدین سبب سه قدرت مثلثی شکل گرفتند، اما با این حال لوسیفر بخش کثیر قدرت را برای خود نگاه داشت. زمانی فرار رسید که دیریم یکی از اندلس برای جستجوی سکان خود که از او به سرقت رفته بود وارد دوزخ شد. دیریم پس از ورود به جهنم در یک نبرد ذهنی با یک دیو خبیث قدرتمند شرکت کرد و خواستار سکان دزدیده شده خود بود. دیریم پس از اینکه سکان خود را بازیافت لوسیفر را در مقابل تمام شیاطین دوزخ تحقیر کرد، و مورنینگ استار در آن روز سوگند به نابودی دیریم نمود 	| لوسیفر مورنینگ استار یک شخصیت خیالی در کتاب های کمیک آمریکایی منتشر شده توسط دی سی کامیکس است که در درجه اول به عنوان شخصیت مکمل در مجموعه کمیک سندمن و سپس در نقش شخصیت اصلی در اسپین آف ، که هر دو توسط ورتیگو منتشر می شدند . لوسیفر زمانی در بین قدرتمندترین و زیباترین فرشتگان عالم هستی قرار داشت و یکی از دو شخصیت خیالی به شمار می رود که با خلق فرضیه چندجهانی دی سی در ارتباط است . لوسیفر پس از شورشی که در بهشت بر پا کرد ، توسط پرزنس جهت حکومت به جهنم فرستاده شد . پیتر استورماره نقش شخصیت لوسیفر را در فیلم کنستانتین (۲۰۰۵) ایفا کرده است . 	|


## Evaluation
The following table summarizes the ROUGE scores obtained by the Bert2Bert model.

### Version 1.0.0
|    %    | Precision | Recall | FMeasure |
|:-------:|:---------:|:------:|:--------:|
| ROUGE-1 |   28.14   |  30.86 |   27.34  |
| ROUGE-2 |   07.12   | 08.47* |   07.10  |
| ROUGE-L |   28.49   |  25.87 |   25.50  |

### Version 2.0.0 (coming soon)
|    %    | Precision | Recall | FMeasure |
|:-------:|:---------:|:------:|:--------:|
| ROUGE-1 |   x   |  x |   x  |
| ROUGE-2 |   x   | x |   x  |
| ROUGE-L |   x   |  x |   x  |

## How to use

### HuggingFace Transformers
```python
from transformers import (
    BertTokenizerFast,
    EncoderDecoderConfig,
    EncoderDecoderModel
)

model_name = 'm3hrdadfi/bert2bert-fa-wiki-summary'
tokenizer = BertTokenizerFast.from_pretrained(model_name)
config = EncoderDecoderConfig.from_pretrained(model_name)
model = EncoderDecoderModel.from_pretrained(model_name, config=config)

sequence = """YOUR TEXT COMES HERE"""
inputs = tokenizer([sequence], padding="max_length", truncation=True, max_length=512, return_tensors="pt")
input_ids = inputs.input_ids
attention_mask = inputs.attention_mask

outputs = model.generate(input_ids, attention_mask=attention_mask)
generated = tokenizer.batch_decode(outputs, skip_special_tokens=True)
print(f'YOUR GENERATED TEXT: {generated}')
```

### Streamlit Application on Google-Colab
Follow the block steps on this Colab notebook.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/m3hrdadfi/wiki-summary/blob/master/notebooks/How_to_use_app.ipynb) 

## Cite 
I didn't publish any paper about this work. Please cite this repository in publications as the following:

```markdown
@misc{Bert2BertWikiSummaryPersian,
  author = {Mehrdad Farahani},
  title = {Summarization using Bert2Bert model on WikiSummary dataset},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {https://github.com/m3hrdadfi/wiki-summary},
}
```

## Releases
v1.0.0: Hello World!

Available by: [m3hrdadfi/bert2bert-fa-wiki-summary](https://huggingface.co/m3hrdadfi/bert2bert-fa-wiki-summary)


## License
[Apache License 2.0](LICENSE)
