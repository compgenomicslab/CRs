import sys

members = sys.argv[1]
count = sys.argv[2] # count of number of sequences in each cluster
PAB_file = sys.argv[3]
n = sys.argv[5]

clust2mem={}
for ln, line in enumerate(open(members)):
	line = line[:-1].split("\t")
	clust2mem[line[0]]=[]
	try:
		for i in line[1].split(","):
			clust2mem[line[0]].append(i)
	except IndexError:
		print(line)

order=[]

for ln, line in enumerate(open(count)):
	line = line[:-1].split("\t")
	order.append(line[0])

PAB=[]
for ln, line in enumerate(open(PAB_file)):
	PAB.append(line[:-1])

taxid2name={}
for ln, line in enumerate(open("../../data/mcps.proteins/total.taxinfo")):
	line = line[:-1].split("\t")
	taxid2name[line[0]]=line[1]

for clust in order:
	pr = []
	pr_name=[]
	dps = 0
	tot = []
	tot_name=[]
	for i in clust2mem[clust]:
		tot.append(i.split(".")[0])
		tot_name.append(taxid2name[i.split(".")[0]])
		if i.split(".")[0] in PAB:
			pr.append(i.split(".")[0])
			pr_name.append(taxid2name[i.split(".")[0]])
	dps = (len(set(pr))/len(set(tot)))*100


	print(clust+"\t"+str("%.2f"%dps)+"\t"+str(len(set(pr)))+"\t"+str(len(set(tot))))

