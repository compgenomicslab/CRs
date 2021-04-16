# LBDs catalog

In our catalog, we have analysed 82,277 CR sequences from 11,806 representative microbial genomes covering the whole prokaryotic species phylogeny and have classified them according to their LBD types using a de novo LBD family annotation method. A total of 72,480 putative LBD sequences has been clustered in 5,149 families of homologous sequences. Here, LBDs hiden Markov models (HMMs) profiles from our novel families are avaiable for clasifying chemoreceptor protein sequences.

#####Plant-associated Chemoreceptors (CRs)

In order to identify LBD families specific for the plant associated lifestyle, we further analyzed each of our LBD clusters from an ecological and phylogenetic perspective. First, we computed the Degree of Plant Specificity (DPS) for each LBD family cluster using our manually curated database of 895 Plant-Associated Bacteria (PAB) species as a reference. We calculated DPS as the percentage of PAB species in each cluster over the total number of species within the same group, thus producing a score from 0% (LBD family never observed in a PAB species) to 100% (LBD observed only in PAB species). 


### Which LBD-family correspond to my chemoreceptor?

1. DOWNLOAD the database avaible in database folder. 
      

2. DECOMPRESS the files


3. Use HMMER (http://hmmer.org/)

      <pre><code>hmmscan ./database/LBDs-clusters my_chemoreceptor_protein.fasta</code></pre>
      
      INPUT:
      * ./database/LBDs-clusters are the HMMs profiles from our de novo clasification of LBD types, each family correspond to one cluster (cluster_1, cluster_2, cluster_3, ...)
      * my_chemoreceptor_protein.fasta is the fasta file with the protein sequence of the chemoreceptor of interest
       
      OUTPUT:
      * hmmscan output with the cluster of the LBD domain present, if any.
      
     

     
### Which is the Degree of Plant-Specificty according to my LBD-family?

Each cluster has an associated Degree of Plant-Specificty (DPS) calculated as the proportion of Plant-Associated Bacteria (PAB) over the total species detected with the corresponding LBD, as explained above. This value can be checked in the given table (DPS-clusters.tsv), consulting the DPS for the cluster number predicted in the previous step. 
