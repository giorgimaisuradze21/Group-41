# 2) for loopის გამოყენებით გამოიტანეთ რიცხვები 1დან 100ის ჩათვლით 2ის გამოტოვებით.
for i in range(1,101,2):
    print(i)


# 3) while loopის გამოყენებით გამოიტანეთ რიცხვები 1დან 1000მდე.

number = 1
while number < 1001:
    print(number)
    number += 1

# 4) while loopის გამოყენებით გამოიტანეთ 1დან 10მდე რიცხვების ჯამი.

number = 0
sum = 0
while number < 10:
    sum += number
    number += 1
print(sum)



# 5) ითამაშეთ ამ ორი loopით, გააკეთეთ 5 for loop მაგალითი და 5 while loop მაგალითი (ისეთი რაც აქამდე არ გაგიკეთებიათ).

for i in range(101):
    print(i)

for i in range(1,101,2):
    print(i)

for i in range(11):
    print(str(i) + "." + "hello world")

for i in range(11):
    print("hello world")