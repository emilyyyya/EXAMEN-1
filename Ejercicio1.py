def format_recipe_info(corrupt_string):
    # Reverse the string
    reversed_string = corrupt_string[::-1]

    # Extract the recipe name and calories
    recipe_name = reversed_string[9:][::-1]
    calories = reversed_string[:9][::-1]

    # Format the string
    formatted_string = f"La receta de {recipe_name} contiene {calories} calorías."
    
    return formatted_string

def main():
    # Given string
    corrupt_string = input("Ingrese la cadena de texto corrupta: ")

    # Format the recipe information
    formatted_string = format_recipe_info(corrupt_string)

    print(formatted_string)

if __name__ == "__main__":
    main()





