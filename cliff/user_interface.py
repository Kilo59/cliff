"""
cliff.user_interface.py
~~~~~~~~~~~~~~~~~~~~~~~
"""
import readline


class Completer:  # Custom completer
    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches (entries that start with entered text)
                self.matches = [s for s in self.options if s and s.startswith(text)]
            else:  # no text entered, all matches possible
                self.matches = self.options[:]

        # return match indexed by state
        try:
            return self.matches[state]
        except IndexError:
            return None


if __name__ == "__main__":
    completer = Completer(["hello", "hi", "how are you", "goodbye", "great"])
    readline.set_completer(completer.complete)
    readline.parse_and_bind("tab: complete")

    my_input = input("Input: ")
    print("You entered", my_input)
