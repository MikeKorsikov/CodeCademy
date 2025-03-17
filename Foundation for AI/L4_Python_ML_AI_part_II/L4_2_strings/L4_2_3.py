# strip

featuring = "           rob thomas                 "
print(featuring.strip())
# => 'rob thomas'

# problem
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

# solution
love_maybe_lines_stripped = [phrase.strip() for phrase in love_maybe_lines]
print(love_maybe_lines_stripped)
love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)

# problem
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

# solution
toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")
print(toomer_bio_fixed)

# problem
god_wills_it_line_one = "The very earth will disown you"

# solution
disown_placement = god_wills_it_line_one.find('disown')
print(disown_placement)

#
def favorite_song_statement(song, artist):
  return "My favorite song is {} by {}.".format(song, artist)

print(favorite_song_statement("Smooth", "Santana"))
# => "My favorite song is Smooth by Santana."

# 
def poem_title_card(title, poet):
  return  'The poem "{}" is written by {}.'.format(title, poet)

example = poem_title_card("I Hear America Singing", "Walt Whitman")
print(example)

#
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

my_beard_description = poem_description(author = "Shel Silverstein", title = "My Beard", original_work = "Where the Sidewalk Ends", publishing_date = "1974")
print(my_beard_description)
