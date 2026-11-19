class Person:
    def __init__(self, name, age, email, person_id, **kwargs):
        self.name = name
        self.age = age
        self.email = email
        self.__person_id = person_id

        # Store additional information
        self.additional_info = kwargs

    # Getter for private ID
    def get_person_id(self):
        return self.__person_id

    # Display basic information
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Email:", self.email)
        print("ID:", self.__person_id)


class Student(Person):
    def __init__(self, name, age, email, person_id,
                 grade, major, average_score, **kwargs):

        # Initialize parent class
        super().__init__(name, age, email, person_id)

        self.grade = grade
        self.major = major
        self.__average_score = 0

        # Set initial score using setter
        self.set_average_score(average_score)

        # Store additional information
        self.additional_info = kwargs

    # Getter for average score
    def get_average_score(self):
        return self.__average_score

    # Setter for average score
    def set_average_score(self, score):
        if 0 <= score <= 100:
            self.__average_score = score
            print("Score updated successfully!")
        else:
            print("Invalid score! Score must be between 0 and 100.")

    # Check pass or fail
    def check_result(self):
        if self.__average_score >= 75:
            print("Result: PASS")
        else:
            print("Result: FAIL")

    # Display student information (method overriding)
    def display_info(self):
        print("\n===== STUDENT INFORMATION =====")

        super().display_info()

        print("Grade:", self.grade)
        print("Major:", self.major)
        print("Average Score:", self.__average_score)

        print("Additional Information:", self.additional_info)

        self.check_result()


class Teacher(Person):
    def __init__(self, name, age, email, person_id,
                 subject, department, salary, **kwargs):

        # Initialize parent class
        super().__init__(name, age, email, person_id)

        self.subject = subject
        self.department = department
        self.salary = salary

        # Store additional information
        self.additional_info = kwargs

    # Display teacher information (method overriding)
    def display_info(self):
        print("\n===== TEACHER INFORMATION =====")

        super().display_info()

        print("Subject:", self.subject)
        print("Department:", self.department)
        print("Salary:", self.salary)

        print("Additional Information:", self.additional_info)

    # Display teaching subject
    def display_subject(self):
        print(self.name, "teaches", self.subject)

    # Display department and salary
    def display_work_info(self):
        print("Department:", self.department)
        print("Salary:", self.salary)

# OBJECT CREATION
# Three Student objects

student1 = Student(
    "Alice", 16, "alice@gmail.com", "S001",
    "Grade 11", "Science", 85,
    Club="Science Club",
    Scholarship="Yes",
    Nationality="Indonesian"
)

student2 = Student(
    "Bob", 17, "bob@gmail.com", "S002",
    "Grade 12", "Engineering", 70,
    Club="Robotics Club",
    Scholarship="No",
    Nationality="Singaporean"
)

student3 = Student(
    "Charlie", 16, "charlie@gmail.com", "S003",
    "Grade 11", "Business", 92,
    Club="Debate Club",
    Scholarship="Yes",
    Nationality="Malaysian"
)


# Two Teacher objects

teacher1 = Teacher(
    "Mr. John", 35, "john@gmail.com", "T001",
    "Mathematics", "Science", 5000,
    Experience="10 years",
    Certification="Master's Degree",
    Office="Room 101"
)

teacher2 = Teacher(
    "Ms. Sarah", 29, "sarah@gmail.com", "T002",
    "Chemistry", "Science", 4500,
    Experience="5 years",
    Certification="Bachelor's Degree",
    Office="Room 205"
)

# DISPLAY INFORMATION
# Display students
student1.display_info()
student2.display_info()
student3.display_info()

# Display teachers
teacher1.display_info()
teacher2.display_info()

# Update student score
print("\n===== UPDATING STUDENT SCORE =====")
student2.set_average_score(80)

# Check updated result
student2.check_result()

# Test invalid score
student1.set_average_score(120)

# Retrieve private information using getters
print("\n===== GETTER METHODS =====")
print("Student Name:", student1.name)
print("Student ID:", student1.get_person_id())
print("Student Average Score:", student1.get_average_score())

# Display teacher subject
print("\n===== TEACHER SUBJECT =====")
teacher1.display_subject()

# Display teacher department and salary
print("\n===== TEACHER WORK INFORMATION =====")
teacher2.display_work_info()