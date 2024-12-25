'''
Overly complicated prototype for movie/time selection menu
I know there are better ways to do this but it works for now while I'm figuring Python out again
It's definitely better than the switch/match statements used in the main file
This is meant to eventually replace those switch/match cases for menu selection
'''
# list of movies to add or remove from
movieList = ['Coraline', 'Pacific Rim', 'Breezed', 'The Crow', 
        'Fantastic Mr. Fox', 'Isle of Dogs', 
        'Who is your Daddy']
# list of view times to add or remove from
viewTime = ['12pm', '1:30pm', '3pm', '4:30pm', '6pm', '7:30pm', '9pm']
print(movieList, viewTime)  # print lists

# I know this is a terrible way of doing this but for now it's what works
movie = input('Type name of movie you want to add: ')  # user input adds to movieList
noMovie = input('Type name of movie you want to remove: ')  # user input removes from movieList
time = input('Type time slot you want to add: ')  # user input adds to viewTime
noTime = input('Type time slot you want to remove: ')  # user input removes from viewTime

# defining functions 
def addMovie(movieList):  # function that lets user add movies to movieList
    movieList = movieList.append(movie)
def removeMovie(movieList):  # function that lets user remove movies from movieList
    movieList = movieList.remove(noMovie)
def addTime(viewTime):  # function that adds time slots for movie viewing
    viewTime = viewTime.append(time)
def removeTime(viewTime):  # function that removes time slots for movie viewing
    viewTime = viewTime.remove(noTime)

# this block calls all the previous functions (mainly to test their functionality)
addMovie(movieList)
removeMovie(movieList)
addTime(viewTime)
removeTime(viewTime)

# prints movieList and viewTime (to prove changes)
print(movieList)
print(viewTime)

'''
The more I look at this file the more it reminds me of how I would code in
"Intro to scripting" in college and that makes me cringe
I apologize to anyone who views this repository
'''