#o(k^2) algo
def get_kth_multiple(k):
    res = [3,5,7]
    is_number_seen= set()
    is_number_seen.add(1)
    is_number_seen.add(3)
    is_number_seen.add(5)
    if k<=3:
        return res[k-1]

    for i in range(k-3):
        choices = []
        for j in range(len(res)):
            if 3*res[j] not in is_number_seen:
                choices.append(3*res[j])
            if 5*res[j] not in is_number_seen:
                choices.append(5 * res[j])
            if 7*res[j] not in is_number_seen:
                choices.append(7 * res[j])
        ans = min(choices)
        res.append(ans)

        is_number_seen.add(ans)
    print(res)
    return res[-1]

k = 1000
import time
tic = time.time()
# for i in range(k):
#     print(get_kth_multiple(i))
res1 = get_kth_multiple(k)
toc = time.time()
toc = time.time()
first_algo_time =toc-tic

########################################
#second algorithm
def get_kth_multiple_via_heap(k):
    res = []
    is_number_seen = set()
    import heapq
    heap = [3,5,7]
    heapq.heapify(heap)
    for i in range(k):
        next_el = heapq.heappop(heap)
        #is_number_seen.add(next_el)
        res.append(next_el)
        if (next_el*3) not in is_number_seen:
            is_number_seen.add(next_el*3)
            heapq.heappush(heap,next_el*3)
        if (next_el * 5) not in is_number_seen:
            is_number_seen.add(next_el*5)
            heapq.heappush(heap, next_el * 5)
        if (next_el * 7) not in is_number_seen:
            is_number_seen.add(next_el*7)
            heapq.heappush(heap, next_el * 7)
    print(res)
    return res[-1]

tic = time.time()
res2=get_kth_multiple_via_heap(k)
toc = time.time()
second_algo_time =toc-tic
print("first algo time",first_algo_time)
print("second algo time",second_algo_time)
print("check if two algos are equal",res1==res2)