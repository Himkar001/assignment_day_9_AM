records = [
    ["Aman", "Math", 88],
    ["Priya", "Physics", 91],
    ["Rahul", "Math", 76],
    ["Neha", "Chemistry", 85],
    ["Karan", "Physics", 67],
    ["Simran", "Math", 95],
    ["Riya", "Chemistry", 78],
    ["Arjun", "Physics", 82],
    ["Meera", "Math", 73],
    ["Kabir", "Chemistry", 89]
]


def add_student(name, subject, marks):

    for r in records:
        if r[0] == name and r[1] == subject:
            print("Duplicate record!")
            return

    records.append([name, subject, marks])


def get_toppers(subject):

    filtered = [r for r in records if r[1] == subject]

    toppers = sorted(filtered, key=lambda x: x[2], reverse=True)

    return toppers[:3]


def class_average(subject):

    marks = [r[2] for r in records if r[1] == subject]

    if len(marks) == 0:
        return 0

    return sum(marks) / len(marks)


def above_average_students():

    avg = sum([r[2] for r in records]) / len(records)

    return [r for r in records if r[2] > avg]


def remove_student(name):

    global records

    records = [r for r in records if r[0] != name]


def save_records():

    with open("students.txt", "w") as f:

        for r in records:

            f.write(f"{r[0]}, {r[1]}, {r[2]}\n")


while True:

    print("\n1 Add student")
    print("2 Show toppers")
    print("3 Show class average")
    print("4 Above average students")
    print("5 Remove student")
    print("6 Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        name = input("Name: ")
        subject = input("Subject: ")
        marks = int(input("Marks: "))

        add_student(name, subject, marks)

    elif choice == "2":

        subject = input("Subject: ")
        print(get_toppers(subject))

    elif choice == "3":

        subject = input("Subject: ")
        print(class_average(subject))

    elif choice == "4":

        print(above_average_students())

    elif choice == "5":

        name = input("Name: ")
        remove_student(name)

    elif choice == "6":

        save_records()

        print("Records saved to students.txt")

        break