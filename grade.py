students = []

def add_student(name, score):
    students.append((name, score))

def show_students():
    for name, score in students:
        print(f"Name: {name}, Score: {score}")

if __name__ == "__main__":
    add_student("Alice", 85)
    show_students()
