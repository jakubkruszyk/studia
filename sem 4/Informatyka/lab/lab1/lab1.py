text = input("Podaj liczby rozdzielone spacją:\n")
nums = [int(x) for x in text.split(" ")]
file = open('text.txt', 'w')
# for num in nums:
#     if num % 2:
#         num_str = str(num % 1000)
#     else:
#         num_str = str(num % 100)
#     print(num_str)
#     file.write(num_str + '\n')

nums = [str(num % 100) if num % 2 else str(num % 1000) for num in nums]
for num in nums:
    print(num)
    file.write(num + '\n')

file.close()
