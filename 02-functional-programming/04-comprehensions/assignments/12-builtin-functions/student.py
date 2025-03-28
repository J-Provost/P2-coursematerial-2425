def movie_count(movies, director):
    return len([movie for movie in movies if movie.director == director])

def longest_movie_runtime_with_actor(movies, actor):
    return max([movie.runtime for movie in movies if actor in movie.actors], default=0)

def has_director_made_genre(movies, director, genre):
    return any(genre in movie.genres and movie.director == director for movie in movies)

def is_prime(n):
    return all(n % k != 0 for k in range(2, int(n**0.5) + 1)) and n >= 2

def is_increasing(ns):
    return all(x <= y for x, y in zip(ns, ns[1:]))

def count_matching(xs, ys):
    return sum(1 for x, y in zip(xs, ys) if x == y)

def weighted_sum(ns, weights):
    return sum(n * w for n, w in zip(ns, weights))

def alternating_caps(string):
    chars = [char.upper() if index % 2 == 0 else char.lower() for index, char in enumerate(string)]
    return "".join(chars)

def find_repeated_words(sentence):
    import re
    words = [word.lower() for word in re.findall(r'\b\w+\b', sentence)]
    return {word1 for word1, word2 in zip(words, words[1:]) if word1 == word2}