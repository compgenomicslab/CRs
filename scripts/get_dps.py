import sys
#comand python get_dps.py mmseqs2_02/lbds.mmseqs.0.2.members.txt mmseqs2_02/lbds.mmseqs.0.2.count.sorted.txt f12.all_plant_associated.taxids progenomes/f12.rep.tax2lineage 2
members = sys.argv[1]
count = sys.argv[2]
PAB_file = sys.argv[3]
lineages = sys.argv[4]
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

taxid2lineage={}
for ln, line in enumerate(open(lineages)):
	line = line[:-1].split("\t")
	taxid2lineage[line[0]]=[]
	for i in line[1].split(","):
		taxid2lineage[line[0]].append(i)
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
	ra = 0
	for i in clust2mem[clust]:
		tot.append(i.split(".")[0])
		tot_name.append(taxid2name[i.split(".")[0]])
		if i.split(".")[0] in PAB:
			pr.append(i.split(".")[0])
			pr_name.append(taxid2name[i.split(".")[0]])
	dps = (len(set(pr))/len(set(tot)))*100
	ra = (len(pr)/len(PAB))*100
#	with open("./mmseqs2_0"+n+"/DPS_"+n, "a+") as f:
#		f.write(clust+"\t"+str("%.2f"%dps)+"\t"+str(len(set(pr)))+"\t"+str(len(set(tot)))+"\n")
#		f.close()
#	with open("./mmseqs2_0"+n+"/DPS_taxid_"+n, "a+") as f:
#		f.write(clust+"\t"+str("%.2f"%dps)+"\t"+str(set(pr))+"\t"+str(set(tot))+"\n")
#		f.close()
#	with open("./mmseqs2_0"+n+"/DPS_name_"+n, "a+") as f:
#		f.write(clust+"\t"+str("%.2f"%dps)+"\t"+str(set(pr_name))+"\t"+str(set(tot_name))+"\n")
#		f.close()

	print(clust+"\t"+str("%.2f"%dps)+"\t"+str(len(set(pr)))+"\t"+str(len(set(tot))))
#	print(clust+"\t"+str("%.2f"%dps)+"\t"+str(set(pr))+"\t"+str(set(tot)))
	#print(clust+"\t"+str("%.2f"%dps)+"\t"+str(set(pr_name))+"\t"+str(set(tot_name)))

