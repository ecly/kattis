words = input().split()
ostgotska_words = [w for w in words if "ae" in w]
if len(ostgotska_words) >= len(words) * 0.4:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")
