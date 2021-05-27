n, k = map(int, input().split())
sum_existing_ratings = sum(int(input()) for _ in range(k))
judges_to_vote = n - k
min_rating = (sum_existing_ratings + (judges_to_vote * -3)) / n
max_rating = (sum_existing_ratings + (judges_to_vote * 3)) / n
print(min_rating, max_rating)
