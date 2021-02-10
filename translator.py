from translate import Translator
translator = Translator(to_lang="es")

with open("test.txt", mode="r") as myFile:
    text = myFile.read()
    translation = translator.translate(text)
    print(translation)
    with open("trans.txt", mode="w") as myFile1:
        myFile1.write(translation)
