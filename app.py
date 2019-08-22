movies = []


def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, 'q' to quit the "
                       "program: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print("Unknown command-Please input from the options only")

        user_input = input(
            "Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, 'q' to quit the program: ")


def add_movie():
    name = input("Enter the movie name: ")
    genre = input("Enter the movie genre: ")

    movies.append({
        'name': name,
        'genre': genre
    })


def show_movies(movies_list):
    for movie in movies_list:
        print(f"Name: {movie['name']}")
        print(f"Genre: {movie['genre']}")


def find_movie():
    find_by = input("What property of the movie are you looking for? ")
    looking_for = input("What are you searching for? ")

    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    show_movies(found_movies)


def find_by_attribute(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)

    return found


menu()
