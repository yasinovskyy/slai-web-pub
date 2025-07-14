def read_txt(filename, state):
    with open(filename, "r") as input_file:
        data = input_file.readlines()
        for college in data:
            college_name = college.split("(")[0].strip()
            college_state = college.split(",")[1].strip()[:-1]
            if college_state == state:
                print(college_name)


read_txt("acm.txt", "Iowa")
