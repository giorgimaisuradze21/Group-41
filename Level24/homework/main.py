# 1) შექმენით ფუნქცია რომელიც გამოიტანს რიცხვების საშუალო არითმეტიკულს 
# Listt=[1,2,3,35,51,95]
# def average(List_numbers):
#     sum=0
#     for i in List_numbers:
#       sum+=i
#     print(sum / len(Listt))  
# average(Listt)



# შექმენით manual_abs() ფუნქცია. (ვისაც არ გახსოვთ abs რა არის დაგუგლეთ)

# def manual_abs(num):
#     if num == 0:
#         return 0
#     elif num < 0:
#         return -(num)
#     else:
#         return(num)


# შექმენით ფუნქცია რომელიც გამოიტანს მიცემულ ლისტს დუპლიკატების გარეშე
# e.g: input: [1, 2, 3, 1]; output: [1, 2, 3]

def remove_same_element(listnnn1):
    new_listnn = []
    for i in listnnn1:
        if i not in new_listnn:
            new_listnn.append(i)
    return new_listnn
print(remove_same_element([96, 21, 23, 26, 29, 30]))
