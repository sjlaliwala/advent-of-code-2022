ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

WIN = 6
DRAW = 3
LOSS = 0

OPPONENT_CHOICES = {
  'A': ROCK,
  'B': PAPER,
  'C': SCISSORS
}

ROUND_DECISIONS = {
  'X': LOSS,
  'Y': DRAW,
  'Z': WIN
}

CHOICE_POINTS = {
  ROCK: 1,
  PAPER: 2,
  SCISSORS: 3,
}

LOSES = {
  ROCK: SCISSORS,
  SCISSORS: PAPER,
  PAPER: ROCK
}

WINS = {
  ROCK: PAPER,
  PAPER: SCISSORS,
  SCISSORS: ROCK,
}

def decode_opponent_choice(opponent_choice):
  return OPPONENT_CHOICES[opponent_choice]

def decode_round_decision(round_decision):
  return ROUND_DECISIONS[round_decision]

def get_winning_play(choice):
  return WINS[choice]

def get_losing_play(choice):
  return LOSES[choice]

def get_choice_points(round_points, opp):
  my = opp
  if round_points == WIN:
    my = get_winning_play(opp)
  elif round_points == LOSS:
    my = get_losing_play(opp)
  return CHOICE_POINTS[my]


total_points = 0
with open('strategyguide.txt') as strategy_guide:
  for rps_round in strategy_guide:
    opponent_choice, round_decision = rps_round.strip().split(' ')
    round_points = decode_round_decision(round_decision)
    opp = decode_opponent_choice(opponent_choice)
    choice_points = get_choice_points(round_points, opp)
    print(round_points, choice_points)
    total_points += round_points + choice_points

print(total_points)




