def main():

   # Step 2: Create a complex data structure
    about_me = {
        'full_name': 'HAMZA SHAIKH',
        'student_id': 1023456  ,
        'pizza_toppings': ['MUSHROOMS', 'OLIVES', 'ANCHOVIES'],
        'movies': [
            {'title': 'Inception', 'genre': 'thriller'},
            {'title': 'The Matrix', 'genre': 'sci-fi'}
        ]
    }

    # Step 3: Add another movie to the data structure
    new_movie = {'title': 'The Godfather', 'genre': 'crime'}
    about_me['movies'].append(new_movie)
    print(new_movie)
    
# Step 4: Function that prints student name and ID
    def  print_student_name_and_id(about_me):
        full_name = about_me['fulll name']
        first_name = (full_name.split(' '))[0]
        student_id = about_me['student_id']

        print(f"My name is {full_name}, but you can call me Mr.{first_name}" )
    
# Step 5: Function that adds pizza toppings to the data structure
    first_toppings = ['PEPPERS', 'ONIONS', 'CHICKEN']
    add_pizza_toppings=(about_me, first_toppings)

# Step 6: Function that prints two types of sentences for pizza toppings
def print_pizza_toppings(about_me['pizza_toppings'])

# Step 7: Function that prints comma-separated list of movie genres
    def print_movie_genres(about_me):
        if 'movies' in about_me:
            movies=about_me['movies']
            if movies:
                genres = [movie['genre'] for movie in movies]
                genre_li = ','.join(genres[:-1]+)+("&" if len(genres))+ genres[-1]

            print(f"I would like to watch {genre_list} movies")
        return
# Step 8: Function that prints comma-separated list of movie titles
    def print_movie_titles (about_me['movies'])
      if movie_list:
          titles = [['title' for movie in movie_list ]]
          print (f"Some of my favourite movies a re {edited_titles}")
      if __name__ == '__main__':
       main()