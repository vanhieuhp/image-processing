from unidecode import unidecode

text = "Văn Hiếu"
transliterated_text = unidecode(text)
converted_text = transliterated_text.lower().replace(" ", "")
print(converted_text)  # This will print: "vanhieu"
