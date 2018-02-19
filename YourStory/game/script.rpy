# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:


    # Leaving this stuff here for reference.


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    # e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.


    scene black

    # $ renpy.pause(1.0, hard='True')
    $ renpy.pause(1.0)

    $ test_bool = True

    "Yes yes, I'm coming."

    "You wanted a story, yes?"

    "Well, what kind of story do you want tonight?"

    menu:
        "Adventure":
            "Tragedy"


        "Tragedy":
            "Romance"

        "Romance." if test_bool:
            "Nice"
            





    return
