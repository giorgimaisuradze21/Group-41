# შემქნით ფუნცქცია რომელიც არგუმენტად მიიღებს ინტეჯერს, ამ ფუნქციის დავალებაა რომ აიღოს ეს ინტეჯერი და დაგვიბრუნოს გაორმაგებული
# def numbers(num):
#     print(num * 2)

# numbers(21)
# 2)დაწერე ფუნქცია greet(name), რომელიც იღებს ადამიანის სახელს და აბრუნებს მისალმების ტექსტს
# def greet(name):
#     print(f" Hello {name} ")

# greet("Giorgi")

# )შექმენით ფუნქცია is_even(num), რომელიც ამოწმებს, არის თუ არა რიცხვი ლუწი, თუ ლუწია, აბრუნებს True, სხვა შემთხვევაში False.
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# შექმენით მარტივი ფუნქცია თქვენი სურვილით რომელსაც მისცემთ default valueს
# def manual_min(listn):
#     min_value = listn[0]
#     for i in listn:
#         if i < min_value:
#             min_value = i
            
#     return min_value
# print(manual_min([25,50,40,30,29]))
# 5)შექმენით ფუნქცია nickname(name), რომელიც არგუმენტად იღებს სახელს და აბრუნებს პირველი სამი ასო(გამოიყენეთ slicingი)
def nickname(name):
    return name[:3]

print(nickname("daviti"))
print(nickname("Giorgi"))