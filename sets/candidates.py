required_skills = ['python','github','linux']
candiates = {
    'anna' : {'java','linux','windows','github','python','full stack'},
    'bob' : {'github','linux','python'},
    'carol' : {'linux','javascript','html','python','github'},
    'dineal' : {'pascal','java','c++','github'}


}
interview = set()
# for candidate, skills in candiates.items():
#     if skills.issuperset(required_skills):
#         interview.add(candidate)
# print(interview)

## Proper superset: it contain means not all elemts contains only so elements

for candidate, skills in candiates.items():
    if skills > set(required_skills):
        interview.add(candidate)
print(interview)

