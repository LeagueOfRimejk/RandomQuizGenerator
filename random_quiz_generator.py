import random
from pathlib import Path

# My Modules.
import settings as s


def create_quiz(quiz_number: int = 20, question_quantity: int = 10):
    """
    Main program loop. Accepts quiz quantity and answers though.

    :param quiz_number: Number of quiz's.
    :param question_quantity: Number of questions.
    """
    for quiz_num in range(quiz_number):
        # Check Directories, if does not exist, create them.
        questions, answers = _check_dirs()

        # Create quiz files and answers to them.
        quiz_file = _create_question_file(questions, quiz_num)
        answer_key_file = _create_answer_key_file(answers, quiz_num)

        # Save Quiz Header.
        _safe_quiz_header_in_file(quiz_file, quiz_num)

        # Set a random order of states.
        states = list(s.QUIZ_CONTENT)
        random.shuffle(states)

        # Iterate through All States and set question for them.
        _set_questions(question_quantity, states, quiz_file, answer_key_file)

        # When finished, closed files.
        quiz_file.close()
        answer_key_file.close()


def _make_dirs():
    """Make Directories for files."""
    cwd = Path.cwd()
    question_dir = Path(cwd / 'Quiz_questions')
    answer_dir = Path(cwd / 'Quiz_answers')
    return question_dir, answer_dir


def _check_dirs():
    """Check if directories exists, otherwise create them."""
    dirs = []
    for directory in _make_dirs():
        if not directory.exists():
            directory.mkdir()
        dirs.append(directory)
    return dirs


def _create_question_file(question_file_dir, quantity):
    """
    Creates and opens file mentioned by "question_file_dir".

    :param question_file_dir: Path object
    :param quantity: For loop iterator
    :return: File object
    """
    quiz_file = open(
        question_file_dir / f'{s.FILE_NAME}{quantity + 1}.txt',
        'w',
        encoding='UTF-8'
    )
    return quiz_file


def _create_answer_key_file(answer_file_dir, quantity):
    """
    Creates and opens file mentioned by "answer_file_dir".

    :param answer_file_dir: Path object
    :param quantity: For loop iterator
    :return: File object
    """
    answer_key_file = open(
        answer_file_dir / f'{s.FILE_NAME}_answers{quantity + 1}.txt',
        'w',
        encoding='UTF-8'
    )
    return answer_key_file


def _safe_quiz_header_in_file(quiz_file, quantity: int):
    """
    Safe Header for quiz_file.

    :param quiz_file: File Object
    :param quantity: For loop iterator
    """
    quiz_file.write('Imię i nazwisko:\n\nData:\n\nKlasa:\n\n')
    quiz_file.write(
        (' ' * 20) + f'{s.QUIZ_TOPIC} (Quiz {quantity + 1})'
    )
    quiz_file.write('\n\n')


def _set_questions(question_quantity: int,
                   states: list,
                   quiz_file,
                   answer_key_file):
    """
    Populate quiz with answer provided by params.

    :param question_quantity: Accepts Int, Set the number of questions
        (default 10).

    :param states: List of all states.
    :param quiz_file: File object to save.
    :param answer_key_file: File object to save.
    """
    for question_num in range(question_quantity):

        # Set Correct and Incorrect Answers.
        correct_answer = s.QUIZ_CONTENT[states[question_num]]
        incorrect_answer = list(s.QUIZ_CONTENT.values())
        del incorrect_answer[incorrect_answer.index(correct_answer)]
        incorrect_answer = random.sample(incorrect_answer, 3)
        answer_options = incorrect_answer + [correct_answer]
        random.shuffle(answer_options)

        # Save Question and Answer to the file.
        quiz_file.write(
            f'{question_num + 1}. {s.QUIZ_QUESTION} {states[question_num]}{s.PLURAL}?\n')

        # Set Answer options with one correct within.
        for num_questions in range(len(answer_options)):
            quiz_file.write(
                f"\t{'ABCD'[num_questions]}. {answer_options[num_questions]}\n")
        quiz_file.write('\n')

        # Save questions to file.
        answer_key_file.write(
            f"{question_num + 1}. {'ABCD'[answer_options.index(correct_answer)]}\n")


# Check if run from main script.
if __name__ == '__main__':
    # Create quiz's.
    create_quiz(question_quantity=5, quiz_number=5)
