# This is to make the final input latin script
from openai import OpenAI


def transliterate(yo_sentence, current_lang):
    api_key = open(".env", mode="r").read()
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages= [
            {"role": "system",
             "content": f" I wil give you a sentence.Your task is to transliterate the given sentence, which is in {current_lang} language to Latin script. Only give the transliterated sentence, nothing else."
             },
            {"role": "user",
             "content": f"{yo_sentence}"}
        ]
    )
    result = completion.choices[0].message.content
    return result
if __name__ == "__main__":
    print(transliterate("私は猫が好きです"))
    print(transliterate("编程中的每一个错误都是学习新事物的机会"))
    print(transliterate("アンドロイドは人間らしさを持つように設計されています。", "Japanese"))
    print(transliterate("寿限無寿限無五劫の擦り切れ海砂利水魚の水行末雲来末風来末食う寝るところに住むところ", "Japanese"))
