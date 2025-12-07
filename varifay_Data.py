def validate_name(name):
    return len(name) >=3 and name.replace(" ","").isalpha()
def validate_age(age):
    return age.isdigit() and 15<=int(age)<=50
def Course_valid(Course):
    return len(Course) >=2
def validate_Email(Email):
    return '@' in Email and '.' in Email
#print("all Done in validate ")
