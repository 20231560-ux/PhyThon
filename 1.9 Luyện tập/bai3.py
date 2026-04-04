# Bài 3: Tạo 2 list mới từ list ban đầu, một list chẵn và một list lẻ
_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
_even_numbers = list(filter(lambda n: n % 2 == 0, _numbers))
_odd_numbers = list(filter(lambda n: n % 2 != 0, _numbers))

print("List ban đầu:", _numbers)
print("List chẵn:", _even_numbers)
print("List lẻ:", _odd_numbers)
