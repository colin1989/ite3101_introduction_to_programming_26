from typing import List

n = ["Michael", "Lieberman"]
# Add your function here
def join_string(words: List[str]):
    result = ""
    for w in words:
        result += w
    return result

print(join_strings(n))
