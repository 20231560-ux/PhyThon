def min_in_list(numbers):
    """Trả về số nhỏ nhất trong danh sách numbers."""
    if not numbers:
        raise ValueError("Danh sách không được rỗng")
    return min(numbers)


if __name__ == "__main__":
    raw = input("Nhập các số nguyên cách nhau bằng dấu cách (hoặc nhấn Enter để dùng ví dụ): ")
    if raw.strip():
        nums = [int(x) for x in raw.split()]
    else:
        nums = [11, 2, 23, 45, 6, 9]

    print("Danh sách:", nums)
    print("Số nhỏ nhất là:", min_in_list(nums))
