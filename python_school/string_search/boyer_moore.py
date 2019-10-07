def offset_memo(text):
    memo = {}
    text_length = len(text)
    for i in range(text_length - 1):
        current_char = text[i]
        memo[current_char] = text_length - i - 1
    print(f"Memo : {memo}")
    return memo

def boyer_moore_horspool(text, search_text):
    memo = offset_memo(search_text)
    text_offset = 0
    while text_offset <= (len(text) - len(search_text)):

        i = len(search_text) - 1

        while i >= 0 and search_text[i] == text[text_offset + i]:
            i -= 1
        
        if i < 0:
            # found it !
            return text_offset
        else:
            current_text_char = text[text_offset + len(search_text) - 1]
            
            text_offset += memo.get(current_text_char, len(search_text))

    return -1

if __name__ == "__main__":
    print('Hello boyer moore :D')

    text = "Bonjour josianne, comment ça va ?"
    search_text = "comment"
    print(f"boyer_moore_horspool({text}, {search_text}) {boyer_moore_horspool(text, search_text)}")

    text_b = "AACBC"
    search_text_b = "CBC"
    print(f"boyer_moore_horspool({text_b}, {search_text_b}) {boyer_moore_horspool(text_b, search_text_b)}")