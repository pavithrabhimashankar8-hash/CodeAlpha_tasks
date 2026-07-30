from deep_translator import GoogleTranslator

print("=" * 50)
print("      AI LANGUAGE TRANSLATION TOOL")
print("=" * 50)

text = input("Enter text to translate: ")

source = input("Enter source language (en, kn, hi): ")
target = input("Enter target language (en, kn, hi): ")

translated = GoogleTranslator(
    source=source,
    target=target
).translate(text)

print("\nTranslated Text:")
print(translated)
