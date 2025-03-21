# ========================================
# [Enter your name here]
# [Enter course number here]
# Lab: Movie Guide Part 1
# ========================================

# Step 1: Create an empty list to store movies
movies = []

# Step 2: Create the menu display function
def show_menu():
    """Display the menu options for the user."""
    # TODO: Add print statements to show:
    # - Movie Guide header
    # - Separator line using "=" * 12
    # - COMMAND MENU
    # - Four command options (lists, add, del, exit)


# Step 3: Create the function to list all movies
def list_movies():
    """Display all movies in the list with numbers."""
    # TODO: Add code to:
    # - Print "Movies:" header
    # - Loop through movies list and display each with a number
    # - Call show_menu() at the end


# Step 4: Create the function to add a movie
def add_movie():
    """Get movie name from user and add it to the list."""
    # TODO: Add code to:
    # - Get movie title from user using input()
    # - Add the title to movies list
    # - Print success message
    # - Call list_movies()


# Step 5: Create the function to delete a movie
def delete_movie():
    """Delete a movie from the list by number."""
    # TODO: Add code to:
    # - Show current list of movies
    # - Get movie number from user
    # - Check if number is valid
    # - Delete movie if valid, show error if invalid
    # - Show updated list or error message

    
# Step 6: Create the main function
def main():
    """Main program loop."""
    # TODO: Add code to:
    # - Show initial menu
    # - Start loop to get commands
    # - Check commands and call appropriate functions
    # - Exit when user chooses


# Step 7: Add the program start line
if __name__ == "__main__":
    main()