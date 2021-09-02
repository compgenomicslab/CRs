#!/bin/bash
#FROM files:
#	1. TMHMM FILTERED (total.tmhmm.filtered)
#	2. HMM SEARCH OF DOMAINS (params.total_pfam_seq2dom_info.tsv)

python tmhmm_output.py total.tmhmm.filtered {fasta of CRs}
python extract_fasta_hmm.py params.total_pfam_seq2dom_info.tsv {fasta of CRs}
cat lbds_1tm_2tm.faa LBDs.faa > rebundant_lbds.faa
python add_fasta_id.py rebundant_lbds.faa LBDs.faa > LBDs_total.faa

