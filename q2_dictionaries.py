#!/usr/bin/env python3

import re

def word_frequency(sentence):
    word_counts = {}
    words = re.findall(r'\b\w+\b', sentence.lower())

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

# Test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
