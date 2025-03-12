meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "PRO": "Muy bueno en algo",
            "NOOB": "Muy malo en algo",
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
    
else:
    print("Lo sentimos, su palabra no se encuentra en el diccionario")
