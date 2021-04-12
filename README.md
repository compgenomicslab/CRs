# LBD catalog

In our catalog, we have analysed 82,277 CR sequences from 11,806 representative microbial genomes covering the whole prokaryotic species phylogeny and have classified them according to their LBD types using a de novo LBD family annotation method. Here, LBDs hiden Markov models (HMMs) profiles from our novel families are avaiable for clasifying chemoreceptor protein sequences.


## Wich LBD-family correspond to my chemoreceptor?

1. DOWNLOAD the database avaible in database folder. 
      

2. DECOMPRESS the files


3. Use HMMER (http://hmmer.org/)

      <pre><code>hmmscan my_chemoreceptor_protein.faa ./database/LBDs-clusters</code></pre>

     
## Wich is the Degree of Plant-Specificty according to my LBD cluster family?

Each cluster has an associated Degree of Plant-Specificty (DPS) (DPS-clusters.tsv file) - corresponding to the proportion of Plant-Associated Bacteria (PAB) over the total species.  
