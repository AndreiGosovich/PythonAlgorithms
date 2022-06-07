
# Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком
import hashlib


def dz_8_1(s):
    result = set()
    s_hexdigest = hashlib.sha1(s.encode('utf-8')).hexdigest()
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_str = hashlib.sha1(s[i:j+1].encode('utf-8')).hexdigest()
            if s_hexdigest != sub_str:
                result.add(sub_str)
    return len(result)


if __name__ == '__main__':
    s = 'lorem ipsum dolor sit amet'
    print(f'Количество уникальных подстрок = {dz_8_1(s)}')
