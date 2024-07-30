# AI will take topic from player and generate 5 sentences
from openai import OpenAI


def get_lines(yo_topic: str, word_count: int = 10):
    api_key = open(".env", mode="r").read()
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": f"please generate 5 sentences, each one is about {word_count} words long, on {yo_topic}. Only write the sentences one after another. Sentences should be separated by line breaks, each sentence on a separate line. Write only the {yo_topic} sentences, nothing else."}
        ]
    )
    result = completion.choices[0].message.content
    return result.split("\n")


if __name__ == "__main__":
    print(get_lines("cat"))
    print(get_lines("AI"))
    print(get_lines("chloric acid"))
    print(get_lines("Sargon of Akkad"))
    print(get_lines("bulletproof vest"))
    print(get_lines("trilobites"))
    print(get_lines("meow"))
    print(get_lines("abracadabra"))
