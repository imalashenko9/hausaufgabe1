import nltk
nltk.download()

nltk.download('names')
nltk.download('wordnet')

from nltk.corpus import names
import random
#1
def generate_names(char, num):

    female_names = [(name, 'female') for name in names.words('female.txt') if name.startswith(char)]
    male_names = [(name, 'male') for name in names.words('male.txt') if name.startswith(char)]

    random.shuffle(female_names)
    random.shuffle(male_names)
    female_names = female_names[0:num]
    male_names = male_names[0:num]
    print(female_names)
    print(male_names)
#2
    with open("female_names.txt", "w") as writer:
        for item in female_names:
            writer.write(item[0] + "\n")

    with open("male_names.txt", "w") as writer_male:
        for item in male_names:
            writer_male.write(item[0] + "\n")

generate_names("kuk",20)

