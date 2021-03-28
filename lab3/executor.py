import random
from concurrent.futures import as_completed
from concurrent.futures.thread import ThreadPoolExecutor

DNA = ['A', 'T', 'C', 'G']
NO_THREADS = 25


def look_substr(index, substr, samples):
    if samples[index].find(substr) != -1:
        print("DNA sequence found în sample %d" % index)
    else:
        print("")


def main():
    random.seed(1998)

    samples = [''.join([random.choice(DNA) for _ in range(10000)]) for _ in range(100)]
    substr = random.choice(samples)
    with ThreadPoolExecutor(max_workers=NO_THREADS) as executor:
        future = [executor.submit(look_substr, i, substr, samples) for i in range(100)]
        for res in as_completed(future):
            result = res.result()
            if result != '':
                print(result)


if __name__ == '__main__':
    main()
