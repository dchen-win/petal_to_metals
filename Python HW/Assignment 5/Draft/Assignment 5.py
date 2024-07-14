

class Student:
   
    def __init__(self, id, first_name, last_name): 
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.assignment = {}
    # Method
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}" 

    assignments = []
    def get_assignments(self):
        return self.assignments
    
    def get_assignment(self, name):
        return self.assignments[0]
        # count = 0
        # for i in range (len(self.assignments)):
        #     count += 1
        #     if self.assignments[i] == name:
        #         print(count)
        #         return name
        #     else:
        #         print(count)
        #     return None

    # def get_average(self. *args):
    #     pass

    def submit_assignment(self, assignment):
        # insert() function inserts an element to the given index of an existing list
        self.assignments.insert(0, assignment)
        print("--------Submitted SUccessfully--------")

    def remove_assignment(self, name):
        if f"{self.first_name} {self.last_name}" == name:
            self.assignments.pop(0)
            print("-----------Removed Successfully-------")

    
class Assignments:

    def __init__(self, name, max_score):
        self.name = name
        self.max_score = max_score
        self.grade = None    # grade an integer representing the actual score on the assignment

#         Methods
    def assign_grade(self, grade):
        self.grade = grade  # sets the grade to the supplied integer grade value.
        if self.grade > self.max_score:
            self.grade = None 

    # def get_average(self):
    #     self.grade / self.max_score
     

std1 = Student(1, "smith", "jay")
std2 = Student(2, "john", "black")

fullname_of_std1 = std1.get_full_name()
fullname_of_std2 = std2.get_full_name()
print(f"Name: {fullname_of_std1}")
print(f"Name: {fullname_of_std2}")






# Submit the assignment
std1.submit_assignment("Biolody")
std1.submit_assignment("Programming")
std1.submit_assignment("History")

# Get all the assignment
print(f"List of all the assignments: {std1.get_assignments()}")

std2.submit_assignment("History")
std2.submit_assignment("Programming")
std2.submit_assignment("Biolody")

# get all the assignements
print(f"List of all the assignments: {std2.get_assignments()}")

# Create the Assginement Object 1
assign1 = Assignments(fullname_of_std1, 10)   # Assignment 1
grade1 = assign1.assign_grade(8)
print("Std 1 Assignment 1 Grade: ")
print(assign1.grade)

assign1 = Assignments(fullname_of_std2, 10)   # Assignment 1
grade1 = assign1.assign_grade(7)
print("Std 2 Assignment 1 Grade: ")
print(assign1.grade)


# Create the Assginement Object 2
assign2 = Assignments(fullname_of_std1, 10)   # Assignment 2
grade2= assign2.assign_grade(5)
print("Std1 Assignment 2 Grade: ")
print(assign2.grade)

assign2 = Assignments(fullname_of_std2, 10)   # Assignment 2
grade2= assign2.assign_grade(4)
print("Std 2 Assignment 2 Grade: ")
print(assign2.grade)

# Create the Assginement Object 3
assign3 = Assignments(fullname_of_std1, 10)   # Assignment 3
grade3= assign3.assign_grade(4)
print("Std 1 Assignment 3 Grade: ")
print(assign3.grade)

assign3 = Assignments(fullname_of_std2, 10)   # Assignment 3
grade3= assign3.assign_grade(3)
print("Std 1 Assignment 3 Grade: ")
print(assign3.grade)


#get the average
# print(std1.get_average())

# get assignment by name
print(f"Most recent assignment submitted by {fullname_of_std1} is: ", std1.get_assignment("name"))
print(f"Most recent assignment submitted by {fullname_of_std2} is: ", std2.get_assignment("name"))
# Remove assignment
std1.remove_assignment(fullname_of_std1)
print(std1.get_assignments())
std2.remove_assignment(fullname_of_std2)
print(std2.get_assignments())

