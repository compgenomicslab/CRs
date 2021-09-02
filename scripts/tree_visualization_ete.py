import sys, random, re, pickle
from ete3 import TreeStyle, ImgFace, RectFace, TextFace, Tree,NodeStyle, CircleFace, faces, PhyloTree, SeqGroup, SeqMotifFace, NCBITaxa
from ete3.treeview.faces import add_face_to_node
from ete3.treeview import random_color
from lbds_colors import palette #internal package with colors assigned to each LBD type

n = sys.argv[1] #n is the number of the cluster to be represented
ncbi = NCBITaxa()

#GET THE COLOR ASSIGNED TO EACH DOMAIN
dom2color = palette()

#CARGAR FORMULA ESTRUCTURAL
seq2domor={}
with open('../../results/formula_estructural_v6.pickle', 'rb') as f:
    seq2domor = pickle.load(f)

#GET THE DOMAINS COORDENATES FOR VISUALIZATION 
#load the coordenates from a dictionary
seq2domor={}
with open('formula_estructural_v6.pickle', 'rb') as f: 
    seq2domor = pickle.load(f)
#visualization of the domains for each sequence in the tree (source ETE 3.0)
def get_motifs(seq_name):
    box_motifs=[]
    seq_name = ".".join(seq_name.split(".")[0:3])
    for dom in seq2domor[seq_name]:
        dom_s = dom.split(".")[0]
        try:
            box_motifs.append([int(seq2domor[seq_name][dom][0]),int(seq2domor[seq_name][dom][1]), "[]", None, 10, "black", "rgradient:"+str(dom2color[dom_s]), "arial|8|black|"+str(dom_s)])
        except KeyError:
            box_motifs.append([int(seq2domor[seq_name][dom][0]),int(seq2domor[seq_name][dom][1]), "[]", None, 10, "black", "rgradient:"+str(dom2color[dom_s]), "arial|8|black|"+str(dom_s)])
    return box_motifs

#LOAD THE INFORMATION ASSOCIATED TO EACH SEQUENCE: DPS, NUMBER OF PLANT SPECIES, TOTAL NUMBER OF SPECIES
seq2info={}
for ln, line in enumerate(open("metadata_sequences.tsv")):
    line = line[:-1].split("\t")
    if not line[0] in seq2info.keys():
        seq2info[line[0]]={}
    seq2info[line[0]]["DPS"]=line[1]
    seq2info[line[0]]["plant"]=line[2]
    seq2info[line[0]]["tot"]=line[3]

#LOAD THE PLANT-ASSOCIATED TAXIDS FOR VISUALIZATION
plant_taxids = "plant_associated.taxids"
doms = "../../data/lbds/params.total_pfam_seq2dom.tsv"
plant_associated=[]
for ln, line in enumerate(open(plant_taxids)):
    line = line[:-1]
    plant_associated.append(line)

#LOAD THE TREEFILE AND ALIGNMENT
t = PhyloTree("cluster_"+n+"_cov.alg.treefile", sp_naming_function=lambda name: name.split('.')[0])
t.set_outgroup(t.get_midpoint_outgroup())
alg = SeqGroup("cluster_"+n+"_cov.alg")
tax2names, tax2lineages, tax2rank = t.annotate_ncbi_taxa()

#VISUALIZATION LAYOUT        
def mylayout(node):
    if node.is_leaf():
        #LBD NAME
        dom = TextFace(node.name.split(".")[3], fsize=10, fgcolor='black', penwidth=20, fstyle='normal', tight_text=False, bold=False)
        dom.background.color = dom2color[node.name.split(".")[3]]
        add_face_to_node(dom, node, column = -1, position = "aligned")

        #IN CASE SOME LBDs ARE MORE THAN 1 TIME IN THE SAME MCP SEQUENCE, ADD AN INDEX FOR DIFERENCIATION
        if node.name in seq2domor.keys():
            repes=[]
            for i in seq2domor[node.name]:
                if not i.split(".")[0] in repes:
                    repes.append(i.split(".")[0])
                else:
                    i = i.split(".")[0]+"."+str((int(i.split(".")[1])-1))
                tm = 'TM'
                r = re.search(i, tm)
                #print(r)
                if not (i.split(".")[0] == "MCPsignal" or i.split(".")[0] == "HAMP" or i.split(".")[0]== "HAMP_N3" or re.search(tm, 
                                                                                      i)):
                    name = node.name+"."+i
                    print(name)

        #NAME OF THE PROTEIN AND THE SPECIES. PLANT ASSOCIATED NAMES IN GREEN
        names = TextFace(node.name.split(".")[2])
        sci = TextFace(node.sci_name)
        if str(node.taxid) in plant_associated:
            names.background.color = "DarkSeaGreen"
            sci.background.color = "DarkSeaGreen"
        add_face_to_node(names, node, column=-2, position="aligned")
        add_face_to_node(sci, node, column=-3, position="aligned")

        #ALIGMENT AND DOMAINS STRUCTURE
        seqF = SeqMotifFace(alg.get_seq(node.name), seq_format='compactseq', scale_factor=1)
        seqFace = SeqMotifFace(seq=None, motifs=get_motifs(node.name), gap_format="line")
        (t & node.name).add_face(seqFace, 0, "aligned")
        seqF.margin_left = 1
        add_face_to_node(seqF, node, column=1, position="aligned")


#applying the layout of visualization                               
ts = TreeStyle()
ts.layout_fn = mylayout
ts.show_leaf_name = False

#FORMATTING OUTPUT
ts.aligned_header.add_face(TextFace("| Sci name |",  fsize=12, bold=True), column=-3)
ts.aligned_header.add_face(TextFace("| Protein acc. |",  fsize=12, bold=True), column=-2)
ts.aligned_header.add_face(TextFace("LBD-domain |",  bold=True,  fsize=12), column=-1)
ts.aligned_header.add_face(TextFace("Domain architecture ", bold=True,  fsize=14), column=-0)
ts.aligned_header.add_face(TextFace("| MCP alignment ",  bold=True,  fsize=14), column=1)

#PLOTTING THE ANCESTORS NAME
for ln, node in enumerate(t.traverse()):
        if ln < 0.2*len(t):
            node.add_face(TextFace(node.sci_name), column= 0, position ="branch-right")

#GET THE PDF OF THE VISUALIZATION TREE
t.render("tree_cluster_"+n+".pdf", tree_style=ts)
 