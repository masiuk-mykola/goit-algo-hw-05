import timeit
from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search


with open("article1.txt", "r", encoding="utf-8") as f:
    text1 = f.read()
with open("article2.txt", "r", encoding="utf-8") as f:
    text2 = f.read()


pattern_exist = "алгоритм"
pattern_fake = "вигаданийрядок"

algorithms = {
    "KMP": kmp_search,
    "Boyer-Moore": boyer_moore_search,
    "Rabin-Karp": rabin_karp_search,
}

for name, func in algorithms.items():
    for idx, text in enumerate([text1, text2], start=1):
        for pat in [pattern_exist, pattern_fake]:
            time = timeit.timeit(lambda: func(text, pat), number=10)
            print(f"{name} | Article {idx} | Pattern: {pat} | Time: {time:.6f} sec")
