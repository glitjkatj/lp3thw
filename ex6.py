kinds_of_people = 10
sentence_1 = f"There are {kinds_of_people} kinds of people."

language = "machine language"
knowledge = "don't"
sentence_2 = f"Those who know {language} and those who {knowledge}."

print(sentence_1)
print(sentence_2)

print(f"I said, {sentence_1}.")
print(f"Then I said, '{sentence_2}'.")

programmer_dad_joke = True
joke_evaluation = "Is that a programmer dad joke? {}"

print(joke_evaluation.format(programmer_dad_joke))

lhs = "I'm gonna add this left side of a string..."
rhs = "to this right side of a string."

print(lhs + rhs)