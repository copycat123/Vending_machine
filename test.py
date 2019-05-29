# course = {"title": "python collections", "teacher": {
#     "First_name": "pushpinder", "Last_name": "singh"}, "videos": 22}
# print(course)

# dic = {(1, 2, 3): "abc", 3.1415: "abc"}
# print(dic)

# PACKING DICTIONARIES


# def pack(name=None,  **kwargs):
#     print(kwargs)


# # UNPACKING DICTIONARIES
# def unpack(First_name=None, Last_name=None):
#     if First_name and Last_name:
#         print("hi {} {}".format(First_name, Last_name))
#     else:
#         print("Hi there!")


# pack(name='pushpinder', age=22, work=None)
# unpack(**{"Last_name": "singh", "First_name": "pushpinder"})


# player = {"name": "Douglas", "remaining_lives": 3,
#           "levels": [1, 2, 3, 4], "items": {"pork": 5}}


# def favorite_food(dict):
#     return "Hi, I'm {name} and I love to eat {food}!".format(**dict)


# dict Iteration

# course_minutes = {"python course": 232, "django course": 433, "basics": 43}

# for course in course_minutes:
#     print(course_minutes[course])

# for course in course_minutes:
#     print(course)

# for keys in course_minutes.keys():
#     print(keys)

# for values in course_minutes.values():
#     print(values)

# for items in course_minutes.items():
#     print(items)

# New Terms

#     .keys() - this method returns an iterable of all of the keys in a dictionary.
#     .values() - this method returns an iterable of all of the values in the dictionary.
#     .items() - this method is basically a combo of the above two. It returns an iterable of key/value pairs inside of tuples (more on them in the next stage!).

#  .pop(<key>) - like lists, dicts have .pop(). It'll return the key's value to you and then delete the key.
# .popitem() - similar to .pop() but instead of returning just the value, returns you a tuple (more in the next stage!) with the key and the value. Also, this doesn't take any arguments, you get a random key/value pair!
# .clear() - need to quickly empty out a dictionary? This method is your tool of choice, then


# def word_count(string):
#     words = string.lower().split()
#     dictionary = {}
#     for word in words:
#         dictionary[word] = 0
#     for word in words:
#         dictionary[word] += 1
#     print(dictionary)
#     return dictionary

# word_count("I do not like it Sam I Am")
