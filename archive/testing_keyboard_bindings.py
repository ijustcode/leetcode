def veryBigSorter(s: str) -> str:
    for i in s:
        print(i)

    list_string = [s[i] for i in range(len(s))]
    print(list_string)

veryBigSorter("parichehr")
