name = "Krishna Chaitanya Reddy Kothakapu"
age = 22
city = "Mahabubnagar"
university = "University of Pittsburgh"
cgpa = 7.15


def check_eligibility(cgpa):
    if cgpa > 7.0:
        print(f"Eligible: CGPA {cgpa} is above 7.0")
    else:
        print(f"Not Eligible: CGPA {cgpa} is below 7.0")


def print_profile():
    print("=" * 30)
    print("       STUDENT PROFILE")
    print("=" * 30)
    print(f"Name       : {name}")
    print(f"Age        : {age}")
    print(f"City       : {city}")
    print(f"University : {university}")
    print(f"CGPA       : {cgpa}")
    print("=" * 30)


print_profile()
check_eligibility(cgpa)
