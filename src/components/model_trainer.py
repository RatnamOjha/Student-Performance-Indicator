class User:
    pass     ## this lines does nothing
user2 = User()
user2.first_name = "Frank"
user2.last_name = "Smith"

print(user2.first_name, user2.last_name)

user2.age = 37
user2.is_active = True

print(user2.first_name, user2.last_name, user2.age, user2.is_active)
