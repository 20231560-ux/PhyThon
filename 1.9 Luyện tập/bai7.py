def remove_all_duplicates(lst):
    """Trả về danh sách chỉ chứa phần tử xuất hiện đúng một lần."""
    return [item for item in lst if lst.count(item) == 1]


def keep_one_duplicate(lst):
    """Trả về danh sách giữ một lần xuất hiện cho mỗi phần tử trùng lặp."""
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


if __name__ == "__main__":
    raw = input("Nhập các phần tử cách nhau bằng dấu phẩy (hoặc nhấn Enter để dùng ví dụ): ")
    if raw.strip():
        _list = [x.strip() for x in raw.split(",") if x.strip()]
    else:
        _list = ["abc", "xyz", "abc", "12", "ii", "12", "5a"]

    print("Danh sách ban đầu:", _list)
    print("Loại bỏ tất cả phần tử trùng:", remove_all_duplicates(_list))
    print("Giữ một phần tử cho mỗi giá trị trùng:", keep_one_duplicate(_list))
