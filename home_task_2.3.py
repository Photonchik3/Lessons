seasons = ["зима", "весна", "лето", "осень"]
month_seasons = {1: 1, 2: 1, 3: 2, 4: 2, 5: 2, 6: 3, 7: 3, 8: 3, 9: 4, 10: 4, 11: 4, 12: 1}
month = int(input("введіть місяць: "))
print(seasons[month_seasons[month]-1])