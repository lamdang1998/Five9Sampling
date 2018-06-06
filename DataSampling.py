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


def SRS(data, no_sample):
	sample = []
	for i in range (no_sample):
		instance = random.choice(data)
		sample.append(instance)
		data.remove(instance)
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

def dictPopulation(data, label, targetAttr):
	tarIn = getTargetIndex(targetAttr, label)
	tarVal = getTargetValue(data, tarIn)
	data_dict = {}
	for item in tarVal:
		data_dict[item] = []
		for instance in data:
			if instance[tarIn] == item:
				data_dict[item].append(instance)
	return data_dict

def StratSampling(data, label, targetAttr, no_sample):
	data_dict = dictPopulation(data, label, targetAttr)
	sample = []
	for k, v in data_dict.items():
		if len(v) <= no_sample:
			sample = sample + v
		else:
			sample = sample + SRS(v, no_sample)
	return sample

#Cluster Sampling
def ClusterSampling(data, label, targetAttr, no_sample_set):
	data_dict = dictPopulation(data, label, targetAttr)
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

#Systematic Sampling
def SystemSampling(data, label , no_sample):
	nth_selected = round(len(data) / no_sample)
	sample = []
	i = 0
	while len(sample) < no_sample:
		if i == len(data):
			i = len(data) - i
			data = [x for x in data if x not in sample]
		sample.append(data[i])
		i = i + nth_selected
	return sample 
		
#Multistage Sampling
def MultiStageSampling_util(data, label):
	current = data
	print("Select Sampling Method(a, b, c or d): ")
	print("a/ Simple Random Sampling")
	print("b/ Stratified Sampling")
	print("c/ Cluster Sampling")
	print("d/ Systematic Sampling")
	sampling_type = input("Your way of sampling: ")
	if sampling_type == "b" or sampling_type == "c":
		print("Available label: " + str(label))
		attr = input("Your target attribute: ")
	if sampling_type == "c":
		sample_set = input("Number of sample set: ")
	else:
		sample_size = input("Number of sample: ")
	if sampling_type == "a":
		current = SRS(current, int(sample_size))
	elif sampling_type == "b":
		current = StratSampling(current, label, attr, int(sample_size))
	elif sampling_type == "c":
		current = ClusterSampling(current, label, attr, int(sample_set))
	elif sampling_type == "d":
		current = StratSampling(current, label, int(sample_size))
	print("Your current sample size after previous sampling is " + str(len(current)))
	answer = input("Would you wish to minimize your sample size(Y/n): ")
	if answer == "Y":
		current = MultiStageSampling_util(current, label)
	else:
		return current

def MultiStageSampling(filename):
	data, label = load_data(filename)
	result = MultiStageSampling_util(data, label)
	return result



# data,label = load_data("iris.csv")
# data1 = SRS(data, 2)
# print(data1)


data1 = MultiStageSampling("iris.csv")
print(data1)
# with open("output.csv", "w", encoding="utf8" , newline="") as f:
# 	writer = csv.writer(f)
# 	writer.writerows(data1)
