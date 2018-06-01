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

#Cluster Sampling
def ClusterSampling(filename, targetAttr, no_sample_set):
	data_dict = dictPopulation(filename, targetAttr)
	set_feature = []
	selected = []
	sample = []
	for item in data_dict.keys():
		set_feature.append(item)
	if no_sample_set >= len(set_feature):
		for k,  v in data_dict.items():
			sample = sample + v
	else:
		for i in range (no_sample_set):
			selected.append(random.choice(set_feature))
		for k,v in data_dict.items():
			if k in selected:
				sample = sample + v
	return sample

data1 = ClusterSampling("monks1.csv", "jacket_color", 2 )
with open("output.csv", "w", newline="") as f:
	writer = csv.writer(f)
	writer.writerows(data1)
