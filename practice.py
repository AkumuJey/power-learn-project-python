data = open('practice.txt', "r")

fineData = data.read()
data.close()

print(fineData)



with open("jose.txt", 'a') as file:
    file.write("Akumu En Daktari" + '\n')
    file.close()

trial = open("jose.txt", "r")
trialRead = trial.readlines()
trial.close()
print(trialRead)


