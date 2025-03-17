Top K Frequent Element

	Porject overview
Ky projekt fokusohet në zhvillimin dhe analizën e një algoritmi për gjetjen e K elementeve më të shpeshta në një grup të dhënash. Një nga problemet klasike të përpunimit të të dhënave është se ka aplikime në analiza të mëdha të të dhënave.

	Project Objectives 
Qëllimet kryesore të projektit janë:
Zhvillimi i një algoritmi efikas për gjetjen e K elementeve më të shpeshta në një grup të dhënash të dhënë.
Krahasimi i metodave të ndryshme për zgjidhjen e problemit, duke përfshirë përdorimin e Heap, HashMap, dhe Bucket Sort.
Analiza e kompleksitetit kohor dhe hapësinor të algoritmeve për të përcaktuar metodën më të mirë për skenarë të ndryshëm.
Implementimi i zgjidhjes në Python, me përdorimin e strukturave të të dhënave si priority queue (heapq).
Vlerësimi i performancës së algoritmit duke përdorur grupe të dhënash reale ose të gjeneruara.

	Project Requirements 
Për të realizuar projektin, nevojiten:
Mjedisi i Zhvillimit: Python 3.x, Jupyter Notebook ose një IDE si PyCharm/VS Code.
Libraritë Kryesore: heapq, collections, dhe numpy për krijimin e të dhënave.
Të dhëna për testim: Të dhëna sintetike ose të dhëna reale nga burime publike (p.sh. fjalët më të përdorura në një tekst të madh).
Metoda të vlerësimit: Matje e kohës së ekzekutimit për dataset të madhësive të ndryshme dhe krahasimi i saktësisë së metodave.

	Deliverables
Rezultatet që do të dorëzohen në fund të projektit përfshijnë:
Kod i dokumentuar i algoritmit për gjetjen e K elementeve më të shpeshta.
Raport Analitik, duke përfshirë krahasimin e metodave të ndryshme dhe analizën e kompleksitetit.
Visualizime dhe grafikë, që tregojnë performancën e algoritmit për dataset të ndryshëm.
Prezantim (Slides/Poster) me përmbledhjen e metodave, rezultateve dhe konkluzioneve.

	Implementation Steps 
1.	Algorithm Design 
Në këtë hap do të analizohen dhe zhvillohen disa qasje për zgjidhjen e problemit. Alternativat kryesore janë:
Përdorimi i HashMap dhe Min Heap: 
Përdorim një HashMap për të numëruar frekuencën e secilit element.
Më pas përdorim një Min Heap (priority queue) për të ruajtur K elementet me frekuencë më të lartë.
Ky algoritëm ka kompleksitet O(N log K).
Bucket Sort: 
Përdorim një listë (bucket) për të organizuar elementët sipas frekuencës së tyre.
Ky algoritëm ka kompleksitet O(N) në rastin optimal.

2.	Implementation 
Në këtë hap do të implementohet algoritmi në Python. Do të krijohen funksione për:
Numërimin e frekuencës së elementeve duke përdorur collections.Counter.
Ruajtjen dhe përpunimin e të dhënave në Heap ose Bucket Sort.
Testimin e metodave me grupe të dhënash të ndryshme.

3.	Performance Evaluation – Vlerimi i performances
• Do të matet koha e ekzekutimit për secilin algoritëm duke përdorur time ose timeit. 
• Do të krahasohen performancat për dataset të madhësive të ndryshme (p.sh. 10K, 100K, 1M elemente). 
• Do të analizohet kompleksiteti teorik dhe praktik i algoritmeve.



Disa pseudocode:

Pseudokodi për Metodën me Heap
FUNCTION TopKFrequentBucketSort(nums, k):
    // Hap 1: Krijo një hartë për numërimin e frekuencave
    frequency_map ← empty map
    FOR each num IN nums:
        IF num EXISTS in frequency_map THEN
            frequency_map[num] ← frequency_map[num] + 1
        ELSE
            frequency_map[num] ← 1

    // Hap 2: Gjej frekuencën maksimale për të krijuar "bucket"-at
    max_frequency ← MAXIMUM value among all frequency_map values

    // Hap 3: Krijo një listë me bucket-e; çdo bucket korrespondon me një frekuencë
    buckets ← list of (max_frequency + 1) empty lists

    // Hap 4: Vendos secilin numër në bucket-in përkatës sipas frekuencës së tij
    FOR each (num, frequency) IN frequency_map:
        APPEND num TO buckets[frequency]

    // Hap 5: Fillimisht nga bucket me frekuencën më të madhe, grumbullo numrat derisa të mblidhen k elemente
    result ← empty list
    FOR freq FROM max_frequency DOWN TO 1:
        FOR each num IN buckets[freq]:
            APPEND num TO result
            IF LENGTH(result) EQUALS k THEN
                RETURN result

    RETURN result
Fillimisht ndërtojmë një hartë të frekuencave duke kaluar nëpër të gjitha elementet e listës.
Pastaj, përdorim një qasje me heap për të marrë K çiftet (element, frekuencë) më të mëdha.
Në fund, nxjerrim vetëm vlerat (elementet) dhe i kthejmë ato.

Pseudokodi për Metodën me Bucket Sort
FUNCTION TopKFrequentBucketSort(nums, k):
    // Hap 1: Krijo një hartë për numërimin e frekuencave
    frequency_map ← empty map
    FOR each num IN nums:
        IF num EXISTS in frequency_map THEN
            frequency_map[num] ← frequency_map[num] + 1
        ELSE
            frequency_map[num] ← 1

    // Hap 2: Gjej frekuencën maksimale për të krijuar "bucket"-at
    max_frequency ← MAXIMUM value among all frequency_map values

    // Hap 3: Krijo një listë me bucket-e; çdo bucket korrespondon me një frekuencë
    buckets ← list of (max_frequency + 1) empty lists

    // Hap 4: Vendos secilin numër në bucket-in përkatës sipas frekuencës së tij
    FOR each (num, frequency) IN frequency_map:
        APPEND num TO buckets[frequency]

    // Hap 5: Fillimisht nga bucket me frekuencën më të madhe, grumbullo numrat derisa të mblidhen k elemente
    result ← empty list
    FOR freq FROM max_frequency DOWN TO 1:
        FOR each num IN buckets[freq]:
            APPEND num TO result
            IF LENGTH(result) EQUALS k THEN
                RETURN result

Së pari ndërtojmë një hartë të frekuencave.
Më pas, përcaktojmë frekuencën maksimale për të ndërtuar një listë (array) me bucket-e, ku indeksi i secilit bucket përfaqëson një frekuencë.
Pastaj, çdo element vendoset në bucket-in përkatës bazuar në frekuencën e tij.
Duke filluar nga bucket me frekuencën më të lartë, nxjerrim elementet derisa të arrijmë K elemente.


Pseudokodi për Gjenerimin e Të Dhënave të Rastësishme dhe Matjen e Performancës
•	Gjenerimi i të Dhënave të Rastësishme
FUNCTION GenerateRandomData(size, max_value):
    data ← empty list
    FOR i FROM 1 TO size:
        APPEND (random integer between 1 and max_value) TO data
    RETURN data

FUNCTION Main():
    // Testim me dataset të vogël
    nums ← GenerateRandomData(60, 30)
    k ← 5
    PRINT "Lista e rastësishme me 60 elemente:", nums
    PRINT "Top 5 elementet me frekuenca më të lartë (Heap):", TopKFrequentHeap(nums, k)
    PRINT "Top 5 elementet me frekuenca më të lartë (Bucket Sort):", TopKFrequentBucketSort(nums, k)
    // Testo performancën me dataset të ndryshëm
    CALL EvaluatePerformance()
    
    // Testime shtesë për analizë të performancës
    FOR test_number FROM 1 TO 18:
        size ← RANDOM integer between 1000 and 500000
        test_data ← GenerateRandomData(size, 5000)
        time_heap ← BenchmarkAlgorithm(TopKFrequentHeap, test_data, k)
        time_bucket ← BenchmarkAlgorithm(TopKFrequentBucketSort, test_data, k)
        PRINT "Test", test_number, ": Dataset me", size, "elemente -> Heap:", time_heap, "sec, Bucket:", time_bucket, "sec"


