t = int(input())
for case_number in range(1, t + 1):
    print("Recipe #", case_number)
    r, p, d = map(int, input().split())
    scaling_factor = d / p
    ingredients = []
    for _ in range(r):
        name, weight, percentage = input().split()
        ingredient = name, float(weight), float(percentage)
        ingredients.append(ingredient)

    main_weight = next(w for _, w, p in ingredients if p == 100)
    main_weight_scaled = main_weight * scaling_factor
    for name, _, percentage in ingredients:
        print(name, main_weight_scaled * percentage / 100)

    print("-" * 40)
