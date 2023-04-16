meme_sozlugu = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "SAD": "üzgün olduğunu belirtmek",
            "CREEPY": "korkunç"
            }
    
kelime = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if kelime in meme_sozlugu.keys():
    print("Kelime sözlükte var")
else:
 print("kelime sözlükte yok")
