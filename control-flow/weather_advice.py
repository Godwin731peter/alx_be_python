#!/bin/bash
# Weather conditions variable
weather = ['sunny', 'rainy', 'cold']
user_weather = input("What's the weather like today? (sunny/rainy/cold):")

# condition statement
if user_weather == weather[0]:
    print("Wear a t-shirt and sunglasses.")
elif user_weather == weather[1]:
    print("Don't forget your umbrella and a raincoat.")
elif user_weather == weather[2]:
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
