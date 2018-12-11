from random import randint

BEST_ROUND_NUMBER_OF_GUESSES = 0

class Game:
  MIN = 0
  MAX = 100
  number_of_guesses = 0

  SYSTEM_GUESS = 0

  def start_game(self):
    print "starting game"
    self.init_game()
    self.roll()

  def init_game(self):
    self.MIN = 0
    self.MAX = 100
    self.number_of_guesses = 0
    self.SYSTEM_GUESS = randint(self.MIN, self.MAX)

  # this function asks for and processes the user's input
  def roll(self):
    guess = raw_input(self.get_statement())
    guess = self.parse_input(guess)
    if int(guess) == self.SYSTEM_GUESS:
      self.process_correct_guess()
    else:
      self.process_incorrect_guess(guess)

  def process_correct_guess(self):
    print "You guessed it right!"
    print 'It only took you {0} guesses'.format(self.number_of_guesses)
    # update the ccounter of the user's best round
    self.update_best_round(self.number_of_guesses)
    self.ask_again()

  def process_incorrect_guess(self, guess):
    if (int(guess) > self.SYSTEM_GUESS):
      print 'Too high'
      self.MAX = int(guess) - 1
    else:
      print 'Too low'
      self.MIN = int(guess) + 1
    self.roll()

  def get_statement(self):
    return 'Enter a number between {0} and {1} - '.format(self.MIN, self.MAX)

  # parse the user's input and return return only a valid input
  def parse_input(self, input):
    if (not input.isdigit()):
      print('Your guess should be a number.')
      self.roll()
    if (int(input) < self.MIN or int(input) > self.MAX):
      print 'Your guess should be between {0} and {1}'.format(self.MIN, self.MAX)
      self.roll()
    # since this was a valid input, we increment the number of guesses
    self.number_of_guesses = self.number_of_guesses + 1
    return input

  def ask_again(self):
    input = raw_input('Would you like to play agian? y/n ')
    if input.lower() == 'y':
      self.start_game()
    if input.lower() == 'n':
      self.print_best_attempt_and_exit()
    # it seems the user has not answered y or n. Ask again
    self.ask_again()

  def update_best_round(self, attempts):
    global BEST_ROUND_NUMBER_OF_GUESSES
    if BEST_ROUND_NUMBER_OF_GUESSES == 0 or attempts < BEST_ROUND_NUMBER_OF_GUESSES:
      BEST_ROUND_NUMBER_OF_GUESSES = attempts

  def print_best_attempt_and_exit(self):
    global BEST_ROUND_NUMBER_OF_GUESSES
    print ' '
    print 'Thanks for playing!'
    print 'Your best round was {0} guesses.'.format(BEST_ROUND_NUMBER_OF_GUESSES)
    exit()

if __name__ == '__main__':
  g = Game()
  g.start_game()