import re

sentence = "I'm here! Have you 22323 heard he said 33332 he was an imposter."
regex = r"\d+"

result = re.finditer(regex, sentence)
for r in result:
    print(r.group())

correct_sentence =  re.subn(regex,"", sentence)

print(correct_sentence[0])

# more training when I'm gonna do a fun project in python
