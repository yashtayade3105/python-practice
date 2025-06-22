from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Name", "Age", "Pofession"]
table.add_row(["Yash", 25, "Student"])
table.add_row(["Ravi" , 31, "Developer"])
table.add_row(["Sai", 19, "Designer"])
print(table)
print("In this way we can use prettytable module to create tables in Python.")
print("========================================")