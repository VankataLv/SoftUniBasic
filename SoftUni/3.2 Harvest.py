import math
V = int(input())
grapes_sqm = float(input())
wine_needed = int(input())
workers = int(input())
grapes_for_wine = (V * grapes_sqm) * 0.4
wine_made = grapes_for_wine / 2.5
if wine_made < wine_needed:
    wine_shortage = wine_needed - wine_made
    print(f'It will be a tough winter! More {math.floor(int(wine_shortage))} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(int(wine_made))} liters.')
    extra_wine = wine_made - wine_needed
    print(f'{math.ceil(int(extra_wine))} liters left -> {math.ceil(int(extra_wine/workers))} liters per person.')
