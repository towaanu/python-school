def create_hoorspool_memo(pattern):
    memo = {}
    pattern_length = len(pattern)

    for i in range(len(pattern) - 2, -1, -1):
        current_char = pattern[i]
        memo[current_char] = len(pattern) - i - 1
    
    memo[pattern[-1]] = pattern_length
    return memo



def boyermoore_hoorspool(text, pattern):
    memo = create_hoorspool_memo(pattern)
    pattern_length = len(pattern)
    cursor = 0

    while cursor <= len(text) - pattern_length:

        i = pattern_length - 1
        while text[cursor + i] == pattern[i] and i >= 0:
            i = i - 1
        
        if i == -1:
            return cursor # found it !
        
        char_to_align = text[cursor + pattern_length - 1]
        cursor += memo.get(char_to_align, pattern_length)
    
    return None


if __name__ == "__main__":
    print("Hello search text tmp")
    text = "stadia is released, now ! You can play, yeaaaaaaahhhh !!!!"
    pat = "cann"

    print(f"TEXT: {text}")
    print(f"PATTERN: {pat}")
    print(f"RESULT: {boyermoore_hoorspool(text, pat)}")
