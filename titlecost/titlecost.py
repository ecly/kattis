title, cost_cap = input().split()
cost_cap = float(cost_cap)
print(len(title) if len(title) < cost_cap else cost_cap)
