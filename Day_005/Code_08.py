#  Dictionary to store student info

student = {
    "name": "Yash Tayade",
    "roll_no": 101,
    "branch": "IT",
    "passed": True
}

print("Student Info:", student)
print("Name:", student["name"])
print("Branch:", student.get("branch"))
