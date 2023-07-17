class DisplayTitleError(Exception):
    def __init__(self, length, exp_length):
        self.message = "Your title length is too large.\n\tCurrent length: {}\n\tAllowed length: {}".format(length,
                                                                                                         exp_length)
        super().__init__(self.message)


class DisplayBodyError(Exception):
    def __init__(self, height, exp_height):
        self.message = "The body is too tall.\n\tCurrent height: {}\n\tAllowed height: {}".\
            format(height, exp_height)

        super().__init__(self.message)


class DisplayActionsError(Exception):
    def __init__(self, width, exp_width):
        self.message = "There too many actions.\n\tCurrent width: {}\n\tAllowed width: {}".\
            format(width, exp_width)

        super().__init__(self.message)


def an_a_check(post_word):
    vowels = ["a", "e", "i", "o", "u"]

    if post_word.lower()[0] in vowels:
        return "n"
    else:
        return ""
