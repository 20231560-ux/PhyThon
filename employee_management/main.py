from models.manager import Manager
from models.developer import Developer
from models.intern import Intern
from services.company import Company
from services.payroll import total_salary
from utils.validators import *

company = Company()

def menu():
    print("\n===== MENU =====")
    print("1. Thêm nhân viên")
    print("2. Hiển thị danh sách")
    print("3. Tính lương từng nhân viên")
    print("4. Tìm nhân viên theo ID")
    print("5. Xóa nhân viên")
    print("6. Phân công dự án")
    print("7. Đánh giá hiệu suất")
    print("8. Thống kê tổng lương")
    print("9. Sắp xếp theo số dự án")
    print("10. Nhân viên có dự án")
    print("11. Nghỉ việc (đền bù)")
    print("12. Giảm lương nhân viên")
    print("0. Thoát")

while True:
    try:
        menu()
        choice = int(input("Chọn: "))

        # 1. Thêm nhân viên
        if choice == 1:
            emp_id = input("ID: ")
            name = input("Tên: ")
            age = int(input("Tuổi: "))
            salary = float(input("Lương: "))

            validate_age(age)
            validate_salary(salary)

            print("1.Manager 2.Dev 3.Intern")
            t = int(input("Chọn loại: "))

            if t == 1:
                emp = Manager(emp_id, name, age, salary)
            elif t == 2:
                emp = Developer(emp_id, name, age, salary)
            else:
                emp = Intern(emp_id, name, age, salary)

            company.add_employee(emp)
            print("✔ Thêm thành công")

        # 2. Hiển thị danh sách
        elif choice == 2:
            for e in company.list_employees():
                print(e)

        # 3. Tính lương từng nhân viên
        elif choice == 3:
            for e in company.list_employees():
                print(f"{e.name} => {e.calculate_salary()}")

        # 4. Tìm nhân viên
        elif choice == 4:
            emp = company.find_employee(input("ID: "))
            print(emp)

        # 5. Xóa nhân viên
        elif choice == 5:
            company.delete_employee(input("ID: "))
            print("✔ Đã xóa")

        # 6. Phân công dự án
        elif choice == 6:
            emp = company.find_employee(input("ID: "))
            project = input("Tên dự án: ")
            emp.add_project(project)
            print("✔ Đã thêm dự án")

        # 7. Đánh giá hiệu suất
        elif choice == 7:
            emp = company.find_employee(input("ID: "))
            score = float(input("Điểm: "))
            emp.set_performance(score)
            print("✔ Đã cập nhật")

        # 8. Tổng lương
        elif choice == 8:
            print("Tổng lương:", total_salary(company.employees))

        # 9. Sắp xếp theo số dự án
        elif choice == 9:
            for e in company.sort_by_projects():
                print(e)

        # 10. Nhân viên có dự án
        elif choice == 10:
            for e in company.employees_with_projects():
                print(e)

        # 11. Nghỉ việc
        elif choice == 11:
            comp = company.resign_employee(input("ID: "))
            print("✔ Đền bù:", comp)

        # 12. Giảm lương
        elif choice == 12:
            emp_id = input("Nhập ID: ")
            emp = company.find_employee(emp_id)

            print("1. Giảm theo số tiền")
            print("2. Giảm theo %")
            c = int(input("Chọn: "))

            if c == 1:
                amount = float(input("Nhập số tiền giảm: "))
                emp.decrease_salary(amount)
            elif c == 2:
                percent = float(input("Nhập % giảm: "))
                emp.decrease_salary_percent(percent)
            else:
                print("❌ Chọn sai")
                continue

            print("✔ Đã giảm lương")

        # 0. Thoát
        elif choice == 0:
            print("Bye 👋")
            break

        else:
            print("❌ Chọn sai")

    except Exception as e:
        print("❌ Lỗi:", e)