import sys
import random

# My Modules.
from quiz_data import data

# Check for arguments parsed.
script_name, *args = sys.argv

# Chose random Quiz.
RANDOM_QUIZ = random.choice([data[quiz]['COUNTRY_CODE'] for quiz in data.keys()])

# Check for user parsed arguments.
USER_PICK = args[0].lower() if args else RANDOM_QUIZ

# Get particular quiz.
GET_QUIZ = {
    data[quiz_name]['COUNTRY_CODE']: quiz_name for quiz_name in data.keys() if data[quiz_name]['COUNTRY_CODE'] in USER_PICK
}

# Quiz Settings.
DATA = data.get(GET_QUIZ[USER_PICK])
QUIZ_CONTENT = DATA.get('STATES', DATA.get('DISTRICTS'))
QUIZ_TOPIC = DATA['QUIZ_TOPIC']
QUIZ_QUESTION = DATA['QUIZ_QUESTION']
FILE_NAME = DATA['FILE_NAME']
PLURAL = DATA.get('VERBOSE_NAME_SUFFIX', '')
