gcvwr, truck_weight, _ = map(int, input().split())
item_weight = sum(map(int, input().split()))
capacity = int((gcvwr - truck_weight) * 0.9)
trailer_weight_limit = capacity - item_weight
print(trailer_weight_limit)
