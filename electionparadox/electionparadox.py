n = int(input())
ps = sorted(map(int, input().split()))
lost_region_count = (len(ps)//2)+1
lost_regions = ps[:lost_region_count]
won_regions = ps[lost_region_count:]
votes = sum(won_regions) + sum(v // 2 for v in lost_regions)
print(votes)
