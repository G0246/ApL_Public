table_size = int(input("Input Addition Table Size smaller 10: "))
print("Addition Table")
print("------------------------")
for i in (1, table_size, 1):
    for v in (1, table_size, 1):
        print(v, "+", i, "=", i + v)

print("------------------------")