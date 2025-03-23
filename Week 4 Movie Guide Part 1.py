# ========================================
# Hebrert Doucet    
# CIS261
# Lab: Movie Guide Part 1
# ========================================
movies = []
def show_menu():
    print("The Movie List Program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()
 
def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        i = 1
        for movie in movie_list:
            row = movie
            print(str(i) + "." + row[0] + " (" + str(row[1]) + ")")
            i += 1
        print()
            
def add(movie_list):
    name = input("Name: ")
    movie = []
    movie.append(name)
    movie_list.append(movie)
    print(movie[0] + " was added.\n")

def delete(movie_list):
    number = int(input("Number: "))
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number-1)
        print(movie[0] + " was deleted.\n")
        
def main():
    movie_list = [["Monty Python and the Holy Grail", 1975],["On the Waterfront", 1954],
                  ["Cat pn a Hot Tin Roof" , 1958]]
    
    show_menu()
    while True:
        command = input("Command: ")
        if command == "list":
            list(movie_list)
        elif command == "add":
            add(movie_list)
        elif command == "del":
            delete(movie_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")
            

if __name__ == "__main__":
    main()