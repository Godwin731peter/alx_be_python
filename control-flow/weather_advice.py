#!/bin/bash
# Weather conditions 
user_weather = input("What's the weather like today? (sunny/rainy/cold):")

# condition statement
if "sunny":
    print("Wear a t-shirt and sunglasses.")
elif "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
