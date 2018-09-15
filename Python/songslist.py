songs = {"1": "fun",
        "2": "blue",
        "3": "me",
        "4": "floor",
        "5": "live"
}

n = input("数を入力してください:")
for n in songs:
    song = songs[n]
    print (song)
    break
else:
    print ("見つかりません")