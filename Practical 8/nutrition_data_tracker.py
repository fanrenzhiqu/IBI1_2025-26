"""
Practical 8: Nutrition Data Tracker.

Pseudocode
1. Define a class called food_item.
2. Each food_item stores:
   - name
   - calories
   - protein in grams
   - carbohydrates in grams
   - fat in grams
3. Define a function that receives a list of food_item objects eaten in 24 hours.
4. Start totals for calories, protein, carbohydrates and fat at zero.
5. Loop through the list and add each food item's values to the totals.
6. Check whether total calories are more than 2500 or total fat is more than 90 g.
7. Report the totals and any warnings.
8. Return the totals and warnings so the result can also be tested by other code.
9. Include an example class use and function call at the bottom of the script.
"""


class food_item:
    """
    Store nutrition information for one item of food.
    """

    def __init__(self, name, calories, protein, carbohydrates, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat


def calculate_daily_nutrition(food_items):
    """
    Calculate nutrition totals for food eaten over a 24 hour period.

    Returns a dictionary containing the totals and any warning messages.
    """
    total_calories = 0
    total_protein = 0
    total_carbohydrates = 0
    total_fat = 0

    for item in food_items:
        total_calories += item.calories
        total_protein += item.protein
        total_carbohydrates += item.carbohydrates
        total_fat += item.fat

    warnings = []

    if total_calories > 2500:
        warnings.append("Warning: more than 2,500 calories consumed.")

    if total_fat > 90:
        warnings.append("Warning: more than 90 g fat consumed.")

    results = {
        "total_calories": round(total_calories, 2),
        "total_protein": round(total_protein, 2),
        "total_carbohydrates": round(total_carbohydrates, 2),
        "total_fat": round(total_fat, 2),
        "warnings": warnings,
    }

    print("Total calories:", results["total_calories"])
    print("Total protein:", results["total_protein"], "g")
    print("Total carbohydrates:", results["total_carbohydrates"], "g")
    print("Total fat:", results["total_fat"], "g")

    for warning in warnings:
        print(warning)

    return results


def nutrition_data_tracker(food_items):
    """
    Wrapper function with a name matching the practical task.
    """
    return calculate_daily_nutrition(food_items)


if __name__ == "__main__":
    apple = food_item("apple", 60, 0.3, 15, 0.5)
    chicken_sandwich = food_item("chicken sandwich", 430, 28, 42, 14)
    pasta = food_item("pasta", 650, 22, 95, 18)
    large_meal = food_item("large meal", 2600, 50, 200, 95)

    food_eaten_today = [apple, chicken_sandwich, pasta, large_meal]
    calculate_daily_nutrition(food_eaten_today)
