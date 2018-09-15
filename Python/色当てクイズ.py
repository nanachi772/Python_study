colors = ["purple", "orange", "green"]

guess = input("何色でしょう？（入力してください）:")
if guess in colors:
    print ("大当たり")
else:
    print ("ハズレ！また挑戦してね。")