# Band Name App
#
# The app show band names options using pet and city name.

print("Welcome to the Band Name Generator.\nReady?\n")

response = input("Y / N: ").upper()

while response not in ["Y", "N"]:
  print("The input is not valid! Please input 'Y' for Yes or 'N' for No!\n")
  response = input("Y / N: ").upper()


if response == "N":
  print("See you next time")
  exit()

city = input("Okay\nWhat's your born city name? : ")
pet = input("Okay\nWhat's your pet name? : ")

# Options list name
options = [
  f"{city} {pet}",
  f"The {city} {pet}s",
  f"{pet} from {city}",
  f"{city} & The {pet}s",
  f"{city}-{pet} Project"
]

# One option at time
for name in options:
  print(f"What do you think about the name: {name}?")
  response = input("Y / N: ").upper()
  while response not in ["Y", "N"]:
      print("Invalid input. Please type Y or N.")
      response = input("Y / N: ").upper()
  if response == "Y":
      print("Great choice! Rock on!")
      break
else:
  print("No worries, maybe next time!")


""" Studant: Johnatas Dias dos Santos - Sao Paulo/Brazil, 07/mar/2026"""