bids = int(input())
bid_names = []
bid_amnts = []
for j in range(bids):
    bid_names.append(input())
    bid_amnts.append(int(input()))

print(bid_names[bid_amnts.index(max(bid_amnts))])