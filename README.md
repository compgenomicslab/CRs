# LBDs catalog

In our catalog, we have analysed 82,277 CR sequences from 11,806 representative microbial genomes covering the whole prokaryotic species phylogeny and have classified them according to their LBD types using a de novo LBD family annotation method. Here, LBDs hiden Markov models (HMMs) profiles from our novel families are avaiable for clasifying chemoreceptor protein sequences.


### Which LBD-family correspond to my chemoreceptor?

1. DOWNLOAD the database avaible in database folder. 
      

2. DECOMPRESS the files


3. Use HMMER (http://hmmer.org/)

      <pre><code>hmmscan ./database/LBDs-clusters my_chemoreceptor_protein.fasta</code></pre>
      
      INPUT: 
            ./database/LBDs-clusters are the HMMs profiles from our de novo clasification of LBD types, each family correspond to one cluster (cluster_1, cluster_2, cluster_3, ...)
            my_chemoreceptor_protein.fasta is the fasta file with the protein sequence of our chemoreceptor of interest
       
      OUTPUT:
            hmmscan output with the cluster of the LBD domain present, if any.
      
     

     
### Which is the Degree of Plant-Specificty according to my LBD cluster family?

Each cluster has an associated Degree of Plant-Specificty (DPS) (DPS-clusters.tsv file) calculated as the proportion of Plant-Associated Bacteria (PAB) over the total species detected with the corresponding LBD.  
