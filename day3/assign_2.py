# Scenario:
# You are organizing a movie marathon. You start with a playlist:
# ["Inception", "The Matrix", "Interstellar"]
# Prompt the user to enter the name of a movie they want to add.
# If the movie is already in the list, print "Already added!" and do not insert it.
# If it is not in the list, append it to the end of the list.
# Finally, sort the movie list alphabetically and print the updated playlist.

# Sample Input:
# "Interstellar"
# Sample Output:

# Already added!
# Alphabetical Playlist: ['Inception', 'Interstellar', 'The Matrix']

# Sample Input:
# "Avatar"

# Assignment.md
# 2026-08-28
# 1 / 5

# Sample Output:

# Added Avatar!
# Alphabetical Playlist: ['Avatar', 'Inception', 'Interstellar', 'The Matrix']

playlist=["Inception", "The Matrix", "Interstellar"]
new_movie=input("Enter the new movie name: ")
if new_movie in playlist:
    print("Already added!")
else:
    playlist.append(new_movie)
    print("Added",new_movie)
playlist.sort()
print(playlist)
    