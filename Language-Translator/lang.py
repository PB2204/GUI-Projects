from google_trans_new import google_translator

translator = google_translator()
text = input("Enter a text: ")
translate = translator.translate(text, lang_tgt='fr')
print(translate)