students = []

def is_valid_score(score):
    return 0 <= score <= 100

def add_student(name, score):
    if not is_valid_score(score):
        print("Invalid score")
        return False
    students.append((name, score))
    return True

def calculate_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"

def show_students():
    for name, score in students:
        grade = calculate_grade(score)
        print(f"Name: {name}, Score: {score}, Grade: {grade}")

if __name__ == "__main__":
    add_student("Alice", 85)
    add_student("Bob", 150)
    show_students()
