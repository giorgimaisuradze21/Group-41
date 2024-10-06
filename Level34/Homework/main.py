# ფუნქცია find_short პოულობს უმოკლესი სიტყვის სიგრძეს ს სტრიქონში. ის ყოფს სტრიქონს სიტყვებად, ახდენს word_len-ის ინიციალიზაციას პირველი სიტყვის სიგრძით და შემდეგ იმეორებს სიტყვებს, რათა იპოვოს და განაახლოს უმოკლესი სიტყვის სიგრძე. საბოლოო შედეგი არის სტრიქონში ყველაზე მოკლე სიტყვის სიგრძე. ფუნქცია დააბრუნებს 3-ს z

# def find_short(s):
#     list1 = s.split(" ")
#     word_len = len(list1[0])
#     for i in list1:
#         if len(i) < word_len:
#             word_len = len(i)
    
#     # word_len = 3
#     return word_len

# print(find_short("bitcoin take over the world maybe who knows perhaps"))
# number1
# def split_by_space(text):
#     return text.split()

# result = split_by_space("hello world")
# print(result) 
# number2
# def split_by_comma(text):
#     return text.split(',')

# result = split_by_comma("apple,banana,cherry")
# print(result) 
# number3
# def split_by_newline(text):
#     return text.split('\n')

# result = split_by_newline("line1\nline2\nline3")
# print(result)
# number4
# def split_by_dash(text):
#     return text.split('-')

# result = split_by_dash("2024-08-18")
# print(result)
# number 5
# def split_by_multiple_delimiters(text):
#     return text.replace(';', ',').split(',')

# result = split_by_multiple_delimiters("one;two;three,four")
# print(result)
# number 6
# def split_with_limit(text, delimiter, limit):
#     return text.split(delimiter, limit)

# result = split_with_limit("one,two,three,four", ',', 2)
# print(result) 
# number 7
# def split_and_strip(text):
#     return [part.strip() for part in text.split(',')]

# result = split_and_strip(" apple , banana , cherry ")
# print(result)
# number 8
# def split_and_strips1(text, delimiter):
#     parts = text.split(delimiter)
#     return parts[:2]  # Return the first two parts

# result = split_and_strips1("a-b-c-d", "-")
# print(result)
# number 9
# def split_and_count(text, delimiter):
#     return len(text.split(delimiter))

# result = split_and_count("one,two,three,four", ',')
# print(result) 
# number10
# def split_and_join(text, split_delimiter, join_delimiter):
#     parts = text.split(split_delimiter)
#     return join_delimiter.join(parts)

# result = split_and_join("apple;banana;cherry", ';', ', ')
# print(result) 