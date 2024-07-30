# This is to  translate the sentence
from openai import OpenAI
import random


def translate(sentence, from_lang, to_lang):
    api_key = open(".env", mode="r").read()
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": f"I will provide you with a text in {from_lang}. Your task is to translate it accurately into {to_lang}, while preserving the original meaning, tone, and style as closely as possible. The translation should read naturally in the target language and maintain any cultural nuances or contextual elements present in the source text. Write only the translation, nothing else."
            },
            {
                "role": "user",
                "content": f"{sentence}"
            }
        ]
    )
    result = completion.choices[0].message.content
    return result

"""
lang_list = ["Spanish", "German", "French", "Hindi", "Marathi", "Gujarati", "Chinese", "Japanese", "Persian", "Greek"]

sentence = "Why don't scientists trust atoms? Because they make up everything!"
from_lang = "English"

for i in range(9):
    to_lang = random.choice(lang_list)
    sentence = translate(sentence, from_lang, to_lang)
    from_lang = to_lang
    print(sentence)
"""
if __name__ == "__main__":
    print(translate("Ajax my beloved", "English", "Spanish"))
    print(translate("I love pizza", "English", "Italian"))
    print(translate("Coding is fun", "English", "French"))
    print(translate("Cats are awesome", "English", "Japanese"))
    print(translate("Books are great", "English", "German"))
    print(translate("Music is life", "English", "Portuguese"))
    print(translate("Je t'aime", "French", "German"))
    print(translate("Ich liebe Programmieren", "German", "Spanish"))
    print(translate("La vida es bella", "Spanish", "Italian"))
    print(translate("私は猫が好きです", "Japanese", "Korean"))
    print(translate("Amo la musica", "Italian", "Portuguese"))

    print(translate("Les étoiles brillent plus quand le ciel est sombre", "French", "Russian"))
    print(translate("La tecnología avanza más rápido de lo que imaginamos hoy", "Spanish", "Chinese"))
    print(translate("编程中的每一个错误都是学习新事物的机会", "Chinese", "French"))
    print(translate("Man sollte jeden Tag etwas Neues ausprobieren und lernen", "German", "Italian"))
    print(translate("Studiare la programmazione richiede pazienza, dedizione e molta pratica", "Italian", "Japanese"))
