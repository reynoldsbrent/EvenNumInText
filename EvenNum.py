'''
The file numbers.txt contains numbers. (Actually, the same numbers from the last exercise.) There is exactly one number per line.
Read the numbers from the file and write only the even numbers into a new file named even_numbers.txt. Again, there should be one number per line. The order of the numbers shall be unchanged. 
To indicate that the program is finished, print the following output: “List of even numbers created!”
'''
number_list = []
with open('numbers.txt', 'r') as file:
    for line in file:
        line.strip()
        number_list.append(int(line))

with open("even_numbers.txt", 'w') as evenfile:
    for number in number_list:
        if number % 2 == 0:
            evenfile.write(str(number) + '\n')

print("List of even numbers created!")