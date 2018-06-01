#Simple Random Sampling
import random
import csv
def load_data(filename):
	csvDataFile = open(filename)
	dataset = csv.reader(csvDataFile)
	dataset = list(dataset)
	csvDataFile.close()
	label = dataset[0]
	dataset.remove(label)
	return dataset, label


def SRS(dataset, no_sample):
	sample = []
	for i in range (no_sample):
		instance = random.choice(dataset)
		sample.append(instance)
		dataset.remove(instance)
	return sample


#Stratified Sampling
def getTargetIndex(targetAttr, label):
	return label.index(targetAttr)

def getTargetValue(dataset, TarIn):
	targetVal = []
	for i in range (len(dataset)):
		val = dataset[i][TarIn]
		if val not in targetVal:
			targetVal.append(val)
		else:
			continue
	return targetVal

def dictPopulation(filename, targetAttr):
	data, label = load_data(filename)
	tarIn = getTargetIndex(targetAttr, label)
	tarVal = getTargetValue(data, tarIn)
	data_dict = {}
	for item in tarVal:
		data_dict[item] = []
		for instance in data:
			if instance[tarIn] == item:
				data_dict[item].append(instance)
	return data_dict

def StratSampling(filename, targetAttr, no_sample):
	data_dict = dictPopulation(filename, targetAttr)
	sample = []
	for k, v in data_dict.items():
		if len(v) <= no_sample:
			sample = sample + v
		else:
			sample = sample + SRS(v, no_sample)
	return sample
print(StratSampling("iris.csv", "class", 10))
# data, label = load_data("iris.csv")
# print(SRS(data, 5))
# tarIn = getTargetIndex('class', label)
# print(getTargetValue(data,tarIn)) 