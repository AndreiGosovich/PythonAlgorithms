
# Закодируйте любую строку из трех слов по алгоритму Хаффмана.

from collections import Counter


class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(head, codes=dict(), code=''):
    if head is None:
        return None
    if isinstance(head.value, str):
        codes[head.value] = code
        return codes
    else:
        get_code(head.value, codes, code)
    get_code(head.left, codes, code+'0')
    get_code(head.right, codes, code+'1')

    return codes


def get_tree(temp):
    count_str = Counter(temp)

    if len(count_str) <= 1:
        node = Node(None)

        if len(count_str) == 1:
            node.left = Node(count_str[0])
            node.right = None
        count_str = {node: 1}

    while len(count_str) != 1:
        node = Node(None)
        spam = count_str.most_common()[:-3:-1]

        node.left = Node(spam[0][0])
        node.right = Node(spam[1][0])

        count_str.pop(spam[0][0])
        count_str.pop(spam[1][0])

        count_str.setdefault(node, spam[0][1] + spam[1][1])

    return node


def get_code_string(original_string, codes):
    return ''.join(codes[i] for i in original_string)


def get_decode_string(encoded_string, codes):
    new_codes = dict()
    result = ''
    for key, val in codes.items():
        new_codes[val] = key
    j = 0
    for i in range(len(encoded_string) + 1):
        if encoded_string[j: i] in new_codes:
            result += new_codes[encoded_string[j: i]]
            j = i
    return result


original_st = 'beep boop beer!'
print(f'Исходная строка: {original_st}')
tree = get_tree(original_st)
cds = get_code(tree)
print(f'Коды символов: {cds}')
encoded_str = get_code_string(original_st, cds)
print('Закодированная строка: ', end='')
for i in range(0, len(encoded_str), 4):
    print(encoded_str[i: i + 4], end=' ')
print()

decoded_str = get_decode_string(encoded_str, cds)
print(f'Раскодированная строка: {decoded_str}')


# Кодировка: Сложность O(n * log(n)), пространственная сложность O(2n)
# Декодирование: Сложность O(2n), пространственная сложность O(n)
