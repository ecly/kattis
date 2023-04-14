text = input()
happy_count = text.count(":)")
sad_count = text.count(":(")
if happy_count and not sad_count:
    print("alive")
elif sad_count and not happy_count:
    print("undead")
elif sad_count and happy_count:
    print("double agent")
else:
    print("machine")
