def many_data():
    for n in range(50):
        yield print(n)

print(many_data())

# for x in many_data():
#     x


print(next(many_data()))