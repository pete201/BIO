import time

target = list("1234567")

order = list(input())

start = time.time()

pending = [(order, 0)]

ans = set()
seen = set()
while True:
    item, d = pending.pop(0)

    # code for part b
    """
    if d == 6:
        ans.add("".join(item))
    if d > 6: break
    """

    if item == target:
        print(d)
        break

    # 1
    q = list(item)
    a = q.pop(0)
    q.insert(3, a)
    if "".join(q) not in seen:
        seen.add("".join(q))
        pending.append((q, d+1))

    # 2
    q = list(item)
    a = q.pop(-1)
    q.insert(3, a)
    if "".join(q) not in seen:
        seen.add("".join(q))
        pending.append((q, d+1))

    # 3
    q = list(item)
    a = q.pop(3)
    q.insert(0, a)
    if "".join(q) not in seen:
        seen.add("".join(q))
        pending.append((q, d+1))

    # 4
    q = list(item)
    a = q.pop(3)
    q.append(a)
    if "".join(q) not in seen:
        seen.add("".join(q))
        pending.append((q, d+1))

#print(len(ans))
print("Time:", time.time() - start)
