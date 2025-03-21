
#Implementimi i Kodit pa matplotlib, ne Terminal me shfaq Listen e rastesishme, Rezultatet e performances edhe Analizen e Performances

import heapq
import time
import random
import timeit
from collections import Counter

def top_k_frequent_heap(nums, k):
    """
    Gjen K elementet me te shpeshta duke perdorur Min-Heap
    """
    freq_map = Counter(nums)  # Numërojmë frekuencat
    return [num for num, _ in heapq.nlargest(k, freq_map.items(), key=lambda x: x[1])]

def top_k_frequent_bucket_sort(nums, k):
    """
    Gjen K elementet me te shpeshta duke perdorur Bucket Sort
    """
    freq_map = Counter(nums)
    max_freq = max(freq_map.values())
    buckets = [[] for _ in range(max_freq + 1)]
    
    for num, freq in freq_map.items():
        buckets[freq].append(num)
    
    result = []
    for freq in range(max_freq, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result

def generate_random_data(size, max_value):
    """
    Gjeneron nje liste me numra te rastesishem me madhesi te dhene
    """
    return [random.randint(1, max_value) for _ in range(size)]

def benchmark_algorithm(algorithm, nums, k):
    """
    Mat kohën e ekzekutimit të një algoritmi për një dataset të caktuar
    """
    return timeit.timeit(lambda: algorithm(nums, k), number=10)

def evaluate_performance():
    """
    Teston performancën e algoritmeve me dataset të ndryshëm
    """
    sizes = [1000 * i for i in range(1, 11)]  # 100 dataset-e me madhësi të ndryshme
    unique_elements = 10000  # Numri maksimal i vlerave unike në dataset
    k = 10  # Numri i elementeve më të shpeshta që kërkojmë

    print("--- Rezultatet e testimit të performancës ---")
    for size in sizes:
        test_data = generate_random_data(size, unique_elements)
        
        time_heap = benchmark_algorithm(top_k_frequent_heap, test_data, k)
        time_bucket = benchmark_algorithm(top_k_frequent_bucket_sort, test_data, k)
        
        print(f"Dataset size: {size}")
        print(f"Heap Sort Time: {time_heap:.5f} sec")
        print(f"Bucket Sort Time: {time_bucket:.5f} sec")
        print("-" * 10)

def main1():
    """
    Kryen testimin e algoritmeve dhe shfaq rezultatet
    """
    # Shembull testimi me 60 elemente për krahasim
    nums = [random.randint(1, 30) for _ in range(60)]
    k = 5
    print("Lista e rastësishme me 60 elemente:", nums)
    print("Top 7 elementet me te shpeshta (Heap):", top_k_frequent_heap(nums, k))
    print("Top 3 elementet me te shpeshta (Heap):", top_k_frequent_heap(nums, k))
    print("Top 7 elementet me te shpeshta (Bucket Sort):", top_k_frequent_bucket_sort(nums, k))
    print("Top 4 elementet me te shpeshta (Bucket Sort):", top_k_frequent_bucket_sort(nums, k))
    
    nums = [random.randint(1, 20) for _ in range(40)]
    k = 5
    print("Lista e rastësishme me 60 elemente:", nums)
    print("Top 5 elementet me te shpeshta (Heap):", top_k_frequent_heap(nums, k))
    print("Top 3 elementet me te shpeshta (Heap):", top_k_frequent_heap(nums, k))
    print("Top 6 elementet me te shpeshta (Bucket Sort):", top_k_frequent_bucket_sort(nums, k))
    print("Top 2 elementet me te shpeshta (Bucket Sort):", top_k_frequent_bucket_sort(nums, k))
    
    # Testimi i performancës me 10 dataset-e
    evaluate_performance()
    
    # Analiza e Performancës
    print("\nAnaliza e Performancës (18 teste të ndryshme):")
    for i in range(1, 19):
        size = random.randint(1000, 500000)
        test_data = generate_random_data(size, 5000)
        time_heap = benchmark_algorithm(top_k_frequent_heap, test_data, k)
        time_bucket = benchmark_algorithm(top_k_frequent_bucket_sort, test_data, k)
        print(f"Test {i}: Dataset me {size} elemente -> Heap: {time_heap:.6f} sec, Bucket: {time_bucket:.6f} sec")


#Implementimi i Kodit me matplotlib, ne Terminal me shfaq Listen e rastesishme, Rezultatet e performances Vizualizimin amo spo ma shfaq Analizen e performances

import heapq
import time
import random
import timeit
import matplotlib.pyplot as plt
from collections import Counter
from queue import PriorityQueue
import sys
sys.stdout.flush()


def top_k_frequent_hashmap_sort(nums, k):
    """
    Gjen K elementet më të shpeshta duke përdorur HashMap dhe renditje
    """
    freq_map = Counter(nums)
    sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
    return [num for num, _ in sorted_items[:k]]

def top_k_frequent_heap(nums, k):
    """
    Gjen K elementet me te shpeshta duke perdorur Min-Heap
    """
    freq_map = Counter(nums)
    return [num for num, _ in heapq.nlargest(k, freq_map.items(), key=lambda x: x[1])]

def top_k_frequent_bucket_sort(nums, k):
    """
    Gjen K elementet me te shpeshta duke perdorur Bucket Sort
    """
    freq_map = Counter(nums)
    max_freq = max(freq_map.values())
    buckets = [[] for _ in range(max_freq + 1)]
    
    for num, freq in freq_map.items():
        buckets[freq].append(num)
    
    result = []
    for freq in range(max_freq, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result

def top_k_frequent_priority_queue(nums, k):
    """
    Gjen K elementet me te shpeshta duke perdorur Priority Queue
    """
    freq_map = Counter(nums)
    pq = PriorityQueue()
    
    for num, freq in freq_map.items():
        pq.put((-freq, num))
    
    result = [pq.get()[1] for _ in range(k)]
    return result

def generate_random_data(size, max_value):
    """
    Gjeneron nje liste me numra te rastesishem me madhesi te dhene
    """
    return [random.randint(1, max_value) for _ in range(size)]

def benchmark_algorithm(algorithm, nums, k):
    """
    Mat kohën e ekzekutimit të një algoritmi për një dataset të caktuar
    """
    return timeit.timeit(lambda: algorithm(nums, k), number=10)

def evaluate_performance():
    """
    Teston performancën e algoritmeve me 10 dataset-e të ndryshëm
    """
    sizes = [1000 * i for i in range(1, 4)]
    unique_elements = 10000
    k = 10

    results = {"HashMap": [], "Heap": [], "Bucket": [], "PQ": []}
    
    print("--- Rezultatet e testimit të performancës ---")
    sys.stdout.flush()
    plt.show(block=False)  # Hap grafikun pa bllokuar ekzekutimin
    plt.pause(3)  # Shfaq grafikun për 3 sekonda
    plt.close()  # Mbyll grafikun automatikisht
    
    for size in sizes:
        test_data = generate_random_data(size, unique_elements)
        
        time_hashmap = benchmark_algorithm(top_k_frequent_hashmap_sort, test_data, k)
        time_heap = benchmark_algorithm(top_k_frequent_heap, test_data, k)
        time_bucket = benchmark_algorithm(top_k_frequent_bucket_sort, test_data, k)
        time_pq = benchmark_algorithm(top_k_frequent_priority_queue, test_data, k)
        
        results["HashMap"].append(time_hashmap)
        results["Heap"].append(time_heap)
        results["Bucket"].append(time_bucket)
        results["PQ"].append(time_pq)
        
        print(f"Dataset size: {size}")
        print(f"HashMap Sort Time: {time_hashmap:.5f} sec")
        print(f"Heap Sort Time: {time_heap:.5f} sec")
        print(f"Bucket Sort Time: {time_bucket:.5f} sec")
        print(f"Priority Queue Time: {time_pq:.5f} sec")
        print("-" * 10)
    
    # Vizualizimi i rezultateve
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, results["HashMap"], marker='o', label='HashMap Sort')
    plt.plot(sizes, results["Heap"], marker='s', label='Heap')
    plt.plot(sizes, results["Bucket"], marker='^', label='Bucket Sort')
    plt.plot(sizes, results["PQ"], marker='d', label='Priority Queue')
    
    plt.xlabel("Dataset Size")
    plt.ylabel("Execution Time (sec)")
    plt.title("Performance Comparison of Top-K Frequent Algorithms")
    plt.legend()
    plt.grid()
    plt.show()

def main2():
    """
    Kryen testimin e algoritmeve dhe shfaq rezultatet
    """
    nums = [random.randint(1, 20) for _ in range(40)]
    k = 5
    print("Lista e rastësishme me 60 elemente:", nums)
    print("Top 5 elementët me te shpeshta (HashMap Sort):", top_k_frequent_hashmap_sort(nums, k))
    print("Top 5 elementët me te shpeshta (Heap):", top_k_frequent_heap(nums, k))
    print("Top 5 elementët me te shpeshta (Bucket Sort):", top_k_frequent_bucket_sort(nums, k))
    print("Top 5 elementët me te shpeshta (Priority Queue):", top_k_frequent_priority_queue(nums, k))
    
    nums = [random.randint(1, 10) for _ in range(20)]
    k = 5
    print("Lista e rastësishme me 60 elemente:", nums)
    print("Top 5 elementet me te shpeshta (Heap):", top_k_frequent_heap(nums, k))
    print("Top 3 elementet me te shpeshta (Heap):", top_k_frequent_heap(nums, k))
    print("Top 6 elementet me te shpeshta (Bucket Sort):", top_k_frequent_bucket_sort(nums, k))
    print("Top 2 elementet me te shpeshta (Bucket Sort):", top_k_frequent_bucket_sort(nums, k))
    
    # Testimi i performancës me 10 dataset-e
    evaluate_performance()
    
      # Analiza e Performancës
    
    print("\nAnaliza e Performancës (18 teste të ndryshme):")
    sys.stdout.flush()
    
    for i in range(1, 19):
        size = random.randint(1000, 500000)
        test_data = generate_random_data(size, 5000)
        time_heap = benchmark_algorithm(top_k_frequent_heap, test_data, 5)
        time_bucket = benchmark_algorithm(top_k_frequent_bucket_sort, test_data, 5)
        print(f"Test {i}: Dataset me {size} elemente -> Heap: {time_heap:.6f} sec, Bucket: {time_bucket:.6f} sec")
        sys.stdout.flush()
        
    
    """Kryen testimin e metodave dhe teston performancën"""
    nums = [random.randint(1, 30) for _ in range(60)]
    k = 5
    print("Lista e rastësishme me 60 elemente:", nums)
    
    print("\n HashMap Sort:", top_k_frequent_hashmap_sort(nums, k))
    print(" Min-Heap:", top_k_frequent_heap(nums, k))
    print(" Bucket Sort:", top_k_frequent_bucket_sort(nums, k))
    print(" Priority Queue:", top_k_frequent_priority_queue(nums, k))
    
    evaluate_performance()
    
if __name__ == "__main__":
    main1()
    main2()


