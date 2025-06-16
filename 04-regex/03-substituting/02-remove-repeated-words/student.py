# Write your code here
import re

def remove_repeated_words(string):
    # Replace consecutive repeated words with a single instance
    return re.sub(r'\b(\w+)(?:\s+\1\b)+', r'\1', string)