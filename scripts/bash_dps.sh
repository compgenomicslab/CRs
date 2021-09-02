mkdir ../../results/clustering/DPS_02
for n in 2
do
	python ../get_dps.py ../../results/clustering/mmseqs2_0${n}_cov/lbds.mmseqs.0.${n}.members.txt ../../results/clustering/mmseqs2_0${n}_cov/lbds.mmseqs.0.${n}.count.sorted.txt ../../data/PAB/f12.all_plant_associated.taxids.v5 ../../data/mcps.proteins/total.tax2lineage ${n} > ../../results/clustering/DPS_0${n}/DPS_2.tsv

	python ../get_dps_taxid.py ../../results/clustering/mmseqs2_0${n}_cov/lbds.mmseqs.0.${n}.members.txt ../../results/clustering/mmseqs2_0${n}_cov/lbds.mmseqs.0.${n}.count.sorted.txt ../../data/PAB/f12.all_plant_associated.taxids.v5 ../../data/mcps.proteins/total.tax2lineage ${n} > ../../results/clustering/DPS_0${n}/DPS_taxid.tsv


	python ../get_dps_name.py ../../results/clustering/mmseqs2_0${n}_cov/lbds.mmseqs.0.${n}.members.txt ../../results/clustering/mmseqs2_0${n}_cov/lbds.mmseqs.0.${n}.count.sorted.txt ../../data/PAB/f12.all_plant_associated.taxids.v5 ../../data/mcps.proteins/total.tax2lineage ${n} > ../../results/clustering/DPS_0${n}/DPS_name.tsv

done

