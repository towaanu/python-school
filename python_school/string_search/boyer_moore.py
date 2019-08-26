def make_pattern_dict(pattern):
    pattern_length = len(pattern)
    tuple_list = [(pattern[i], i) for i in range(pattern_length)]
    return dict(tuple_list)


def boyer_moore_search(text, pattern):
    pattern_length = len(pattern)
    text_length = len(text)

    pattern_dict = make_pattern_dict(pattern)
    print(pattern_dict)

    shift = 0
    while shift <= (text_length - pattern_length):
        j = pattern_length - 1

        print(f"Shift: {shift}")

        while j >= 0  and pattern[j] == text[shift + j]:
            j -= 1
        
        if j < 0:
            print(f"Found it ! shift: {shift}")
            shift += pattern_length
        
        else:
            shift += pattern_length - pattern_dict.get(text[shift + j], 0) - 1



if __name__ == '__main__':
    # print(make_pattern_dict("Hello"))
    txt = "ABAAABCD"
    pat = "ABC"
    print(boyer_moore_search(txt, pat))
