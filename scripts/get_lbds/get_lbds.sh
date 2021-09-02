#!/bin/bash
#FROM files:
#	1. TMHMM FILTERED (total.tmhmm.filtered)
#	2. HMM SEARCH OF DOMAINS (params.total_pfam_seq2dom_info.tsv)

cd ../../data/lbds/
python ../../src/tmhmm_output.py total.tmhmm.filtered ../mcps.proteins/total.mcps.faa
python ../../src/extract_fasta_hmm.py params.total_pfam_seq2dom_info.tsv ../mcps.proteins/total.mcps.faa
cat lbds_1tm_2tm.faa LBDs.faa > rebundant_lbds.faa
python ../../src/add_fasta_id.py rebundant_lbds.faa LBDs.faa > LBDs_total.faa

