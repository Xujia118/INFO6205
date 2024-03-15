import heapq


def min_max_heapify(coins):
    # Convert the coins list into a min-max heap
    heapq.heapify(coins)
    return coins


def find_fake_coin(coins):
    heap = min_max_heapify(coins)
    is_min_level = True

    while heap:
        if is_min_level:
            # Pop the minimum element (lighter coin)
            fake_coin = heapq.heappop(heap)
        else:
            # Pop the maximum element (heavier coin)
            fake_coin = heapq.heappop(heap)

        # Toggle the level
        is_min_level = not is_min_level

    return fake_coin

coins = [2, 2, 2, 1, 2, 2, 2, 2]
fake_coin = find_fake_coin(coins)
print("Fake coin:", fake_coin)