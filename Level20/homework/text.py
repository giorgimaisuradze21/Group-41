# # 2) შექმენით 2 int ტიპის ცვლადი და გამოიტანეთ მათი ჯამი.
# num1=5
# num2=21
# print(num1+num2)
# # 3) შექმენით 2 str ტიპის ცვლადი და გამოიტანეთ მათი შეერთებული ვერსია (ასევე კომენტარის სახით აღწერეთ რა არის კონკატენაცია).
# str1="Gio"
# str2="Maisuradze"
# print(str1+str2)
# # კონკატენაცია არის სტრინგების მიმატების დროს მომხდარი მოქმედება როდესაც სიტყვები შეერთდა.
# # 4) შექმენით 2 int ტიპის ცვლადი და გამოიტანეთ მათი განაყოფი, შემდეგ კი ახსენით რატომ გამოიტანა floatი და რა ქვია ამ convert'ს (implicit or explicit)
# num1=9
# num2=3
# print(num1 / num2)#implicit
# # 5) გაიხსენეთ ყველა შედარების ოპერატორი და ჩამოწერეთ ყველაზე 1 მაგალითი
# number=5
# number2=10
# print(number > number2) #boolean #the majority
# print(number < number2) #boolean #lack
# print(number == number2) #boolean #equals
# print(number != number2) #boolean #not equal
# print(number >= number2) #boolean #greater or equal
# print(number <= number2) #boolean #less or equal to
# # 6) შეურიეთ შედარების ოპერატორები და მათემატიკური ოპერაციები (მაგ: 5 + 5 == 8  + 2)
# print(9+10==16+3)
# print(9+10!=15+4)
# print(9+10<=14+5)
# print(9+10>=13+6)
# # 7) გაიხსენეთ ლოგიკური ოპერატორი და ჩამოწერეთ ყველა კომბინაცია რაც საჭიროა (სულ უნდა იყოს რვა, გაიხსენეთ ნასწავლიდან)
# # and operator
# x=False
# y=False
# print(x and y) #Output:False
# x=False
# y=True
# print(x and y) #Output:False
# x=True
# y=False
# print(x and y) #Output:False
# x=True
# y=True
# print(x and y) #Output:True
# # or operator
# x=False
# y=False
# print(x or y) #Output:False
# x=False
# y=True
# print(x or y) #Output:True
# x=True
# y=False
# print(x or y) #Output:True
# x=True
# y=True
# print(x or y) #Output:True
# # 8) შეურიეთ ერთმანეთს ლოგიკური და შედარების ოპერატორები და მოიყვანეთ 5 მაგალითი


# x = 75

# if x > 0 and x < 100:
#     print(f"{x} is a positive number less than 100.")
# else:
#     print(f"{x} does not satisfy the conditions.")


# y = -1

# if y < 0 or y % 5 == 0:
#     print(f"{y} is either negative or divisible by 5.")
# else:
#     print(f"{y} does not satisfy the conditions.")




# username = "Giorgi221"

# if "Giorgi" in username and username != "":
#     print(f"Username '{username}' is valid.")
# else:
#     print(f"Invalid username.")









# numbers = [1, 2, 3]

# if not len(numbers) == 0:
#     print("The list contains elements.")
# else:
#     print("The list is empty.")






# z = -10

# if z != 0 and z > 0:
#     print(f"{z} is non-zero and either positive.")
# else:
#     print(f"{z} number is negative.")



# 9) შექმენით for loop'ი 1-დან 10-მდე რიცხვების დასაბეჭდად.
# for i in range(1 , 10):
#     print(i)

# # 10) შექმენით რიცხვების list'ი, შექმენით for loop'ი list'ის რიცხვების ჯამის გამოსათვლელად.
# List=[12,23,31,43,55,69]
# sum=0
# for i in List:
#     sum+=i
# print("The sum of the List is:",sum)


# # 11) შექმენით for loop'ი თითოეული სიმბოლოს დასაბეჭდად სტრინგში -> "Hello, World!".
# string = "Hello, World!"
# for i in string:
#     print(i)

# # 12) შექმენით while loop'ი 1-დან 10-მდე რიცხვების დასაბეჭდად.
# i=1
# while i < 10:
#     print(i)
#     i+=1
# # 13) შექმენით while loop'ი რომელიც დათვლის რიცხვებს 1დან 100მდე თუმცა გამოტოვებს რიცხვებს 50დან 60მდე.
# a=1
# while a < 100:
#     a +=1
#     if a in range(50, 60):
#         pass
#     else:
#         print(a)
# # 14) შექმენით while loop'ი, რომელიც დაიწყებს რიცხვების შეკრებას 1-დან, სანამ ჯამი არ გაუტოლდება 50-ს.
# sum_numbers=0
# num=1
# while sum_numbers < 50:
#     sum_numbers+=num 
#     num+=1
# print("The sum of numbers is:", sum_numbers)
# print("The last number added is:", num - 1)

# # 15) შექმენით ფუნქცია რომელიც მომხმარებელს შემოატანინებს რიცხვს და დაპრინტავს ეს რიცხვი თუ იყოფა 3ზე ან 5ზე ან ორივეზე
# num = int(input("Enter a number: "))
# def print_if_divisible(num):
#     if num % 3 == 0 or num % 5 == 0 or num % 3 ==0 and num % 5 ==0:
#         print(f"The number {num} is divisible by 3 or 5 or both.")
#     else:
#         print(f"The number {num} is not divisible by 3 or 5.")
# print_if_divisible(num)        
# # 16) შექმენით ფუნქცია რომელსაც გადაეცემა რიცხვების სია,თქვენი მოვალეობააა გამოითვალე ამ სიის საშუალო არითმეტიკული. test case: [1,3,4,5,2] | output: 3
# Listt=[1,2,3,22,24,90]
# def average(List_numbers):
#     sum=0
#     for i in List_numbers:
#       sum+=i
#     print(sum / len(Listt))  

# average(Listt)


# 17) შექმენით ფუნქცია რომელსაც გადაეცემა რაიმე string,თქვენი მოვალეობაა ყოველ მეორე ინდექსე მყოფი ასო გახადოს დიდი (upper). test case: hello | output: HeLlO
# def every_second_letter(input_string):
#     result = ""
#     for i in range(len(input_string)):
       
#         if i % 2 == 0:  
#             result += input_string[i].upper()
#         else:
#             result += input_string[i] 
#     return result
# input_str = "hello"
# output_str = every_second_letter(input_str)
# print(f"Input: {input_str} | Output: {output_str}")




# 18) შექმენით ფუნქცია რომელსაც გადაეცემა  რიცხვების სია,თქვენი მოვალეობააა შექმნათ ახალი სია და ამ ახალ სიაში გამოიტანოთ ყოველი რიცხვის კვადრატი (append) და შემდეგ დააბრუნეთ ახალი სია.

# def square_numbers(numbers):
#     squared_list = []
#     for num in numbers:
#         squared_list.append(num ** 2)
#     return squared_list


# numbers = [1, 2, 3, 4, 5]
# squared_numbers = square_numbers(numbers)
# print(f"Original list: {numbers}")
# print(f"Squared list: {squared_numbers}")
