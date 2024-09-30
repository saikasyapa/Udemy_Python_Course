# symmetric difference is a opposite of difference

# morning = {'java','c','ruby','lisp','c#'}
# evening = {'python','c#','ruby','c','java'}
#
# possible_courses = morning ^ evening
# print(possible_courses)

## using list
morning = ['java','c','ruby','lisp','c#']
evening = ['python','c#','ruby','c','java']

# possible_courses = set(morning) ^ set(evening)
possible_courses = set(morning).symmetric_difference(evening)
print(possible_courses)