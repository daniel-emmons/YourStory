# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")
define nar = Character('', color="#c8ffc8")


# The game starts here.
label start:

    nar "If you want to catch someone who can teleport, you do it when they're asleep."

    nar "Of course, they obviously know that, so outwitting them is very important."

    nar "*CRASH*"

    $ say('Gruff Voice', "Damnit, keep your voice down!")

    nar "And these guys apparently did not get the memo."

    #Change scene to MC sidled up against door looking out

    nar "Two men. Well armed. Clearly idiots."

    

    return
