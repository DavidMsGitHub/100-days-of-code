# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# # Don't change code above 👆
#
# # Write your code below:
#
# sentence_in_words = sentence.split()
#
#
# result = {letter:len(letter) for letter in sentence_in_words}
# print(result)
'''AVUIE N1'''


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {day:(temp * 1.8) + 32 for [day, temp] in weather_c.items()}
weather_f = weather_f


print(weather_f)


