from abc import ABC, abstractmethod
from exceptions.employee_exceptions import ProjectAllocationError

class Employee(ABC):
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary
        self.projects = []
        self.performance = 0

    # ➤ Thêm dự án
    def add_project(self, project):
        if len(self.projects) >= 5:
            raise ProjectAllocationError("Nhân viên đã có tối đa 5 dự án")
        self.projects.append(project)

    # ➤ Đánh giá hiệu suất
    def set_performance(self, score):
        if score < 0 or score > 10:
            raise ValueError("Điểm phải từ 0-10")
        self.performance = score

    # ➤ Tính đền bù khi nghỉ việc
    def calculate_compensation(self):
        base = len(self.projects) * 5000000
        if self.performance >= 8:
            return base * 0.5
        return base

    # ➤ Giảm lương theo số tiền
    def decrease_salary(self, amount):
        if amount <= 0:
            raise ValueError("Số tiền giảm phải > 0")
        if self.salary - amount <= 0:
            raise ValueError("Lương không thể <= 0")
        self.salary -= amount

    # ➤ Giảm lương theo %
    def decrease_salary_percent(self, percent):
        if percent <= 0 or percent > 100:
            raise ValueError("Phần trăm không hợp lệ")
        self.salary *= (1 - percent / 100)

    # ➤ Hàm trừu tượng tính lương
    @abstractmethod
    def calculate_salary(self):
        pass

    # ➤ Hiển thị
    def __str__(self):
        return (
            f"ID: {self.emp_id} | "
            f"Tên: {self.name} | "
            f"Lương: {self.calculate_salary()} | "
            f"Dự án: {len(self.projects)} | "
            f"Hiệu suất: {self.performance}"
        )