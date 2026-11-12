class student:
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major
        
    def introduce_student(self):
        return f"Hi, I am {self.name} with (ID: {self.student_id}) and I am majoring in {self.major}."
    
    def is_same_major(self, other_student):
        return self.major == other_student.major
    
# Create Objects:
student1 = student("Kayvan", "12345", "Computer Science")
student2 = student("Payman", "67890", "Computer Science")

# Call methods:
print(student1.introduce_student())
print(student2.introduce_student())

print("Same major or not!?")
print(student1.is_same_major(student2))