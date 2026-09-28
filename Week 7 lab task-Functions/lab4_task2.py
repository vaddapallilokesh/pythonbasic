grade = lambda marks: "Pass" if marks >= 40 else "Fail"

marks_list = [35, 60, 75, 20, 50, 39]
for m in marks_list:
    print(m, ":", grade(m))

'''output-
35 : Fail
60 : Pass
75 : Pass
20 : Fail
50 : Pass
39 : Fail
'''
