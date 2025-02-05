def solve():
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        preferred = []
        married_princes = set()
        unmarried_daughters = set(range(1, n + 1))

        for daughter in range(1, n + 1):
            data = list(map(int, input().strip().split()))
            k, kingdoms = data[0], data[1:]
            preferred.append(kingdoms)

            for kingdom in kingdoms:
                if kingdom not in married_princes:
                    married_princes.add(kingdom)
                    unmarried_daughters.discard(daughter)
                    break

        if not unmarried_daughters:
            print("OPTIMAL")
            continue

        all_princes = set(range(1, n + 1))
        unmarried_princes = all_princes - married_princes

        if unmarried_princes:
            unmarried_daughter = next(iter(unmarried_daughters))
            unmarried_prince = next(iter(unmarried_princes))
            print("IMPROVE")
            print(unmarried_daughter, unmarried_prince)
        else:
            print("OPTIMAL")

solve()