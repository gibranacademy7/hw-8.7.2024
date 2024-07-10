volume = int(input("Please enter the volume level (0-10): "));
#or
def get_volume_feedback(volume):

    match volume:
        case 0:
            feedback = "mute"
        case 1:
            feedback = "very quiet"
        case 2:
            feedback = "very quiet"
        case 3:
            feedback = "quiet"
        case 4:
            feedback = "moderately quiet"
        case 5:
            feedback = "medium"
        case 6:
            feedback = "moderately loud"
        case 7:
            feedback = "loud"
        case 8:
            feedback = "very loud"
        case 9:
            feedback = "extremely loud"
        case 10:
            feedback = "extremely loud"
        case _:
            feedback = "Invalid volume level"

    return feedback

