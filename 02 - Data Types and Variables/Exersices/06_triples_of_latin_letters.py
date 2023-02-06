def main():
    n = int(input())
    latin_letters = [chr(x) for x in range(ord("a"), ord("a") + n)]
    triples = [(x, y, z) for x in latin_letters for y in latin_letters for z in latin_letters]
    triples.sort()
    for triple in triples:
        print("".join(triple))


if __name__ == "__main__":
    main()
