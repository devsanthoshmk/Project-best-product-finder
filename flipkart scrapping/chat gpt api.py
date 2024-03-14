import textwrap

import google.generativeai as genai

from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key="AIzaSyCI-_EvYzkVMH6yRjrWwhDRGGyUXSIj1Fo")

model = genai.GenerativeModel('gemini-pro')
product="https://www.amazon.in/Exide-150Ah-Instabrite-Inveter-Battery/dp/B015B5454A/ref=sr_1_47?dib=eyJ2IjoiMSJ9.qRrhVYUVURy0LKDL-cTunRbrXYNqVLhJWDoiyNKW7f8pLeFzoEoPiSeLskKcUjVAPgnrlkFmrORRw9szzFP6aDSkGjqH6JUh1HUIJTZSPh90mahZCvO0b4Hs70O5l791PQI2cbPqQV4PDB76TUMidecj5jDwd5h76KuUxGH2sYV8v2Nie3jKk1CCzAgCGcAFLzRkeNLEJo3UK4OEOUnfTeF7vc5yZ7_PufP1lZQjdvw5fRy0KkEEbhQtv-Fctp0Mac7vbNhIkCy_gc9jk5AeFcZ0ijQHjNA68cj76GU4IOo.O8OoXfVRcHNzc2R3IUB8L5KndEKnwno25dwQz4_yrG4&dib_tag=se&keywords=ups+battery&qid=1710374745&sr=8-47"#"TechSupreme SMPS Battery Charger for Bike, UPS Clip Battery Charger Worldwide Adaptor12 Volt 7 amp Battery Charger"
response = model.generate_content(f"Provide a concise opinion on {product} 11 after analyzing customer reviews on amazon.simply Opinion score for 5 in the last line based on your opinion")
print(response.text)
print(to_markdown(response.text))