1. Word Order Invariance: Why does the sentence "Dog bites man" have the exact same Bag of Words representation as
"Man bites dog"? How does this impact sentiment analysis?
ANS: BoW represents text strictly by counting word frequencies while completely ignoring grammar and word order. Because "Dog bites man" and "Man bites dog" contain the exact same set of words ("dog", "bites", "man"), their numerical vectors end up identical. This is a major limitation for sentiment analysis because word arrangement changes meaning completely—such as "not good" versus "good, not bad"—and BoW completely misses that context.
2. Sparsity Issue: What happens to the memory size and density of the BoW matrix when the corpus contains 100,000
unique vocabulary words?
ANS: When a corpus scales up to 100,000 unique vocabulary words, every single document vector has to expand to a dimension of 100,000. Since a typical sentence or document only uses a tiny handful of those words, the vast majority of the matrix entries become zeros. This causes massive memory bloat and very low matrix density, which is why machine learning libraries use compressed sparse formats to save RAM.

3. Zero Similarity: Explain why Document 3 in Task 2 receives a Cosine Similarity score of 0.0000 when queried against
"machine learning algorithms for data"?
ANS: Document 3 focuses entirely on natural language processing ("Natural language processing helps computers understand human language"). When it is queried against "machine learning algorithms for data", there is zero token overlap between the document and the query terms. Since the dot product in the numerator of the cosine similarity formula evaluates to 0, the final similarity score drops to 0.0000.


TASK1 OUTPUT:
<img width="844" height="296" alt="Capture1" src="https://github.com/user-attachments/assets/101b0ac1-356f-4471-83ad-4339ee60535b" />

TASK2 OUTPUT:
<img width="1366" height="768" alt="Capture2" src="https://github.com/user-attachments/assets/430ce7ef-166b-4025-bb52-870aeb505d03" />



