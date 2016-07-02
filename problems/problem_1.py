prompt = "If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000."

def get_multiples_less_than(multiples_of, less_than):
    multiples = []
    if type(multiples_of) == list:
        for i in multiples_of:
            multiples.extend(get_multiples_less_than(i, less_than))
        return list(set(multiples))

    for i in range(less_than):
        if i % multiples_of == 0:
            multiples.append(i)
    return multiples

def solution():
    multiples = get_multiples_less_than([3, 5], 1000)
    print multiples
    return sum(multiples)

print solution()
