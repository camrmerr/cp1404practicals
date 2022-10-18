"""
CP1404/CP5632 Practical
Hex Colours
Dictionary lookup to convert Colour to hex codes
"""

COLOUR_TO_CODES = {"babypink": "#f4c2c2", "beige": "#f5f5dc", "black": "#000000", "bronze": "#cd7f32",
                   "bubblegum": "#ffc1cc", "byzantine": "#bd33a4", "carmine": "#960018", "coffee": "#6f4e37",
                   "coral": "#ff7f50", "darkgreen": "#006400"}

print("Please enter colour to display hex code for, or blank to end")
colour_to_display = input("Colour:").lower()
while colour_to_display != "":
    try:
        print(COLOUR_TO_CODES[colour_to_display])
    except KeyError:
        print("Please enter colour in dictionary")
    print("Please enter colour to display hex code for, or blank to end")
    colour_to_display = input("Colour:").lower()
print("Thanks for using my Colour to Hex Code program")