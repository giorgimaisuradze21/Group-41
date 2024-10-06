# 2) შექმენით ფუნქცია რომელიც გამოიტანს 2 რიცხვის ჯამს
def sum(num1,num2):
    print(num1 + num2)
sum(10,20)
# 3) შექმენით ფუნქცია რომელიც გამოიტანს 3 რიცხვის ნამრავლს
def multiply(num1,num2,num3):
    print(num1 * num2 * num3)
multiply(num1=21,num2=90,num3=23)
# 4) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს სახელს და გვარს და გამოიტანს მისალმებას
def info(name,surname):
    print(f"Hello {name} {surname}")
info("Giorgi","Maisuradze")    
# 5) შექმენით ფუნქცია რომელიც დააბრუნებს 2 რიცხვის ჯამს, შემდეგ კი დაბრუნებული მნიშვნელობა მიანიჭეთ ცვლადს
def sum(num1,num2):
    return num1 + num2
sum_numbers=sum(21,900)    
print(sum_numbers)
# 6) შექმენით ფუნქცია რომელიც დააბრუნებს 3 რიცხვის ნამრავლს, შემდეგ კი დაბრუნებული მნიშვნელობა მიანიჭეთ ცვლადს
def multiply(num1,num2,num3):
    return num1 * num2 * num3
multiply_numbers=multiply(90,20,200)
print(multiply_numbers)
# 7) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს საჭმელების list'ს და გამოიტანს ყველას ცალ-ცალკე
foods=["Burger","potatoes","lobiani","pizza"]
def food(food_list):
    for i in food_list:
        print(i)
food(foods)        
# 8) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს რიცხვების list'ს და გამოიტანს ყველას ცალ-ცალკე
numbers=[1,2,3,4,5]
def number(numbers_list):
    for i in numbers_list:
        print(i)
number(numbers)       