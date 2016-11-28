def calculate_total_entropy(example_group, key):
    total_entropy = 0
    for value in valus[key]:
        with_value = []
        num_positive = 0
        num_negative = 0
        for example in example_group:
            if example[key] == value:
                with_value.append(example)
                if example['class']:
                    num_positive = num_positive + 1
                else:
                    num_negative = num_negative + 1

        coeff = len(with_value) / (len(example_group) * 1.0)
        total_entropy = total_entropy + coeff * entropy(with_value)
    return total_entropy

def gain(example_group, key):
    total_entropy = calculate_total_entropy(example_group, key)
    return (entropy(example_group) - total_entropy)

def entropy(examples):
    num_positive = 0
    num_negative = 0
    for example in examples:
        if example['class']:
            num_positive = num_positive + 1
        else:
            num_negative = num_negative + 1
    total = num_positive + num_negative
    if num_positive:
        first_exp = -1 * (num_positive / total) * math.log2(num_positive / total)
    else:
        first_exp = 0
    if num_negative:
        second_exp = -1 * (num_negative / total) * math.log2(num_negative / total)
    else:
        second_exp = 0
    return first_exp + second_exp
