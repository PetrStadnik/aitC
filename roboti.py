def calculate_quality(N, D1, D2, T1, T2):
    svetlo_1 = [[] for _ in range(N)]
    svetlo_2 = [[] for _ in range(N)]


    time = 0
    for i in range(N):
        for d in range(-D1, D1 + 1):
            pos = i + d
            if 0 <= pos < N:
                for dt in range(T1[i]):
                    t = time + dt
                    if t not in svetlo_1[pos]:
                        svetlo_1[pos].append(t)
        time += T1[i]


    time = 0
    for i in range(N):
        pos1 = N - 1 - i
        for d1 in range(-D2, D2 + 1):
            pos = pos1 + d1
            if 0 <= pos < N:
                for dt in range(T2[pos1]):
                    t = time + dt
                    if t not in svetlo_2[pos]:
                        svetlo_2[pos].append(t)
        time += T2[pos1]  


    kvality = []
    for i in range(N):
        o1 = 0
        o2 = 0
        for t in svetlo_1[i]:
            if t in svetlo_2[i]:
                o2 += 1
            else:
                o1 += 1
        for t in svetlo_2[i]:
            if t not in svetlo_1[i]:
                o1 += 1
        kvalita = 2 * o1 + 3 * o2
        kvality.append(kvalita)

    k_min = kvality[0]
    k_max = kvality[0]
    for k in kvality:
        if k < k_min:
            k_min = k
        if k > k_max:
            k_max = k

    return k_min, k_max


def monkey():
    print("ručně nebo soubor?")
    volba = input().strip().lower()

    if volba == "soubor":
        print("název souboru")
        nazev = input().strip()
        try:
            with open(nazev, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("soubor nenalezen")
            return
    else:
        print("zadej vstupní data")
        lines = [input(), input(), input()]

    if len(lines) < 3:
        print("málo")
        return

    try:
        N, D1, D2 = map(int, lines[0].split())
        T1 = list(map(int, lines[1].split()))
        T2 = list(map(int, lines[2].split()))
    except:
        print("chybný vstup")
        return

    if len(T1) != N or len(T2) != N:
        print("nesedí délky")
        return

    k_min, k_max = calculate_quality(N, D1, D2, T1, T2)
    print(k_min, k_max)


if __name__ == "__main__":
    monkey()
