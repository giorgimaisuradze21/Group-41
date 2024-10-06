# 5) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს 3 რიცხვს და დააბრუნებს მათ ნამრავლს, შემდეგ კი ფუნქციის გამოძახებისას მიღებული შედეგი მიანიჭეთ რაიმე ცვლადს
# def function(num1,num2, num3):
#     return num1 * num2 * num3
# g=function(21,34,56)
# print(g)

# 6) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს ასაკს, თუ ასაკი მეტია ან ტოლი 18ზე დააბრუნოს რომ ვერ მიიღო ფასდაკლება, სხვა შემთხვევაში კი დაბრუნოს რომ მიიღო ფასდაკლება
# def info(num):
#     if num >= 18:
#         print("Return it if you can't get a discount")
#     else:
#         print("he should return it if he received a discount")
#         print(info(27))
#         print(info(19))

    # 7) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს სიას და გამოიტანს მის ყველა ელემენტს ( გადაატარეთ for loop'ი )
def lstn(list):
    for i in list:
        print(i)
        lstn=[21,34,56,78,90,76]
        lstn(list)