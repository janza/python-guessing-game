from random import randint

MIN_ATTEMPTS = 0

class Game:
  MIN = 0
  MAX = 100
  count = 0

  SYSTEM_GUESS = 0

  def start_game(self):
    print "starting game"
    self.init()
    self.SYSTEM_GUESS = randint(self.MIN, self.MAX)
    print self.SYSTEM_GUESS
    self.roll()

  def init(self):
    self.MIN = 0
    self.MAX = 100
    self.count = 0

  def roll(self):
    guess = raw_input(self.get_statement())
    guess = self.parse_input(guess)
    if int(guess) == self.SYSTEM_GUESS:
      self.process_correct_guess()
    else:
      self.process_incorrect_guess(guess)

  def process_correct_guess(self):
    print "You guessed it right!"
    print 'It only took you {0} guesses'.format(self.count)
    self.update_best_round(self.count)
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

  def parse_input(self, input):
    if (not input.isdigit()):
      print('Your guess should be a number.')
      self.roll()
    if (int(input) < self.MIN or int(input) > self.MAX):
      print 'Your guess should be between {0} and {1}'.format(self.MIN, self.MAX)
      self.roll()
    self.count = self.count + 1
    return input

  def ask_again(self):
    input = raw_input('Would you like to play agian? y/n ')
    if input.lower() == 'y':
      self.start_game()
    if input.lower() == 'n':
      self.print_best_attempt_and_exit()
    self.ask_again()

  def update_best_round(self, attempts):
    global MIN_ATTEMPTS
    if MIN_ATTEMPTS == 0 or attempts < MIN_ATTEMPTS:
      MIN_ATTEMPTS = attempts

  def print_best_attempt_and_exit(self):
    global MIN_ATTEMPTS
    print ' '
    print 'Thanks for playing!'
    print 'Your best round was {0} guesses.'.format(MIN_ATTEMPTS)
    exit()

if __name__ == '__main__':
  g = Game()
  g.start_game()