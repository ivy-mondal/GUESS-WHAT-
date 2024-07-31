# DA GAME
# from openai import OpenAI
from gibb_topic_get_lines import get_lines
import random
from translate_yo_line import translate
from gotta_latinize_em_all import transliterate

if __name__ == "__main__":
    print("So yo playing a  game eh! Aight gimme yo topic ^_^")
    yo_topic = input()
    yo_lines = get_lines(yo_topic)
    filtered_lines = [string for string in yo_lines if string]

    for line in filtered_lines:
        print(f"\t {line}")

    choice = "nay"
    while choice != "yay":
        print("Sooooo, which line do we hit em with ?! Options are 1234&5 btw")
        line_no = int(input())
        da_line = yo_lines[line_no - 1]
        print("Are yo sure you want this one to be the one?" + " " + da_line + "\n" + "yay or nay?")

        choice = input()

    print("Okie, we go with " + da_line)



    all_languages = [
        "Afrikaans", "Arabic", "Armenian", "Azerbaijani",
        "Belarusian", "Bengali", "Bosnian", "Bulgarian",
        "Chinese", "Croatian", "Czech", "Danish",
        "Dutch", "English", "Esperanto", "Estonian", "Filipino", "Finnish", "French",
        "German", "Greek", "Gujarati",
        "Hawaiian", "Hebrew", "Hindi", "Hungarian", "Icelandic",
        "Indonesian", "Irish", "Italian", "Japanese", "Kannada",
        "Kazakh", "Korean", "Kurdish", "Latin", "Malay", "Malayalam",
        "Marathi", "Mongolian", "Nepali", "Norwegian",
        "Odia", "Pashto", "Persian", "Polish", "Portuguese", "Punjabi", "Romanian",
        "Russian", "Serbian", "Sindhi",
        "Sinhala", "Slovak", "Somali", "Spanish", "Sundanese",
        "Swedish", "Tamil", "Telugu", "Thai", "Turkish", "Turkmen",
        "Ukrainian", "Urdu", "Vietnamese"
    ]

    sentence = da_line
    from_lang = "English"

    for i in range(9):
        to_lang = random.choice(all_languages)
        sentence = translate(sentence, from_lang, to_lang)
        from_lang = to_lang

    lang_list_01 = [
        "Hindi", "Marathi", "Gujarati", "Tamil", "Telugu", "Kannada", "Malayalam", "Punjabi", "Bengali", "Odia", "kannada", "Assamese",
        "Armenian", "Chinese", "Filipino", "Greek", "Hebrew", "Indonesian", "Japanese", "Korean", "Persian",
        "Thai", "Urdu", "Vietnamese"]  # to screw mr fluffy
    lang_list_02 = [
        "Russian", "Belarusian", "Ukrainian", "Polish", "Czech", "Slovak", "Bulgarian", "Macedonian", "Croatian", "Slovene",
        "Arabic", "Afrikaans", "Czech", "Danish", "Dutch", "Finnish", "French",
         "Icelandic", "Irish",  "Latin", "Norwegian", "Polish",  "Swedish"
    ]
    print("which list do you want to proceed with, 1 or 2? (1 to screw mr meow)")
    choice = input()

    if choice == "1":
        last_list = lang_list_01
    if choice == "2":
        last_list = lang_list_02
    last_one = random.choice(last_list)
    final_line = translate(sentence, to_lang, last_one)

    not_latin = ["Hindi", "Marathi", "Gujarati","Tamil", "Telugu", "Kannada", "Malayalam", "Punjabi", "Bengali", "Odia", "kannada", "Assamese",
        "Armenian", "Chinese", "Filipino", "Greek", "Hebrew", "Indonesian", "Japanese", "Korean", "Persian",
        "Thai", "Urdu", "Vietnamese","Russian", "Belarusian", "Ukrainian", "Polish", "Czech", "Slovak", "Bulgarian", "Macedonian", "Croatian",
         "Slovene","Arabic", "Afrikaans", "Czech", "Danish", "Dutch", "Finnish", "French",
         "Icelandic", "Irish",  "Latin", "Norwegian", "Polish",  "Swedish" ]

    if last_one not in not_latin:
        print("Here it comes @_@:  " + "\n" + final_line)
    else:
        spain_without_s = transliterate(final_line, last_one)
        print("Here it comes @_@:  " + "\n" + spain_without_s)


