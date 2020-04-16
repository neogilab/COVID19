#!/usr/bin/env python

import gseapy

### GSEA with python

# TRANSCRIPTOMICS

## Time series

import gseapy

gseapy.enrichr(gene_list="results/covid-19_transcriptomics/Time_series/12F_up_regulated_2_txn.txt",description='12F_up_txn',gene_sets="data/KEGG_advanced/KEGG.gmt",outdir='results/GSEA',cutoff=0.5,verbose=True, background  = 19997)

gseapy.enrichr(gene_list="results/covid-19_transcriptomics/Time_series/12F_down_regulated_2_txn.txt",description='12F_down_txn',gene_sets="data/KEGG_advanced/KEGG.gmt",outdir='results/GSEA',cutoff=0.5,verbose=True, background  = 19997)


## Pairwise comp

gseapy.enrichr(gene_list="results/covid-19_transcriptomics/Pathways_heatmap/txn_up_regulated_H24PI-UNINF_2.txt",description='txn_up_0_24',gene_sets="data/KEGG_advanced/KEGG.gmt",outdir='results/GSEA_time_series',cutoff=0.5,verbose=True, background  = 19997)

gseapy.enrichr(gene_list="results/covid-19_transcriptomics/Pathways_heatmap/txn_down_regulated_H24PI-UNINF_2.txt",description='txn_down_0_24',gene_sets="data/KEGG_advanced/KEGG.gmt",outdir='results/GSEA_time_series',cutoff=0.5,verbose=True, background  = 19997)

gseapy.enrichr(gene_list="results/covid-19_transcriptomics/Pathways_heatmap/txn_up_regulated_H48PI-H24PI_2.txt",description='txn_up_24_48',gene_sets="data/KEGG_advanced/KEGG.gmt",outdir='results/GSEA_time_series',cutoff=0.5,verbose=True, background  = 19997)

gseapy.enrichr(gene_list="results/covid-19_transcriptomics/Pathways_heatmap/txn_down_regulated_H48PI-H24PI_2.txt",description='txn_down_24_48',gene_sets="data/KEGG_advanced/KEGG.gmt",outdir='results/GSEA_time_series',cutoff=0.5,verbose=True, background  = 19997)

gseapy.enrichr(gene_list="results/covid-19_transcriptomics/Pathways_heatmap/txn_up_regulated_H72PI-H48PI_2.txt",description='txn_up_48_72',gene_sets="data/KEGG_advanced/KEGG.gmt",outdir='results/GSEA_time_series',cutoff=0.5,verbose=True, background  = 19997)

gseapy.enrichr(gene_list="results/covid-19_transcriptomics/Pathways_heatmap/txn_down_regulated_H72PI-H48PI_2.txt",description='txn_down_48_72',gene_sets="data/KEGG_advanced/KEGG.gmt",outdir='results/GSEA_time_series',cutoff=0.5,verbose=True, background  = 19997)

# PROTEOMICS

## Time series

gseapy.enrichr(gene_list="results/covid-19_proteomics/Time_series/12F_up_regulated_2.txt",description='12F_up',gene_sets="data/KEGG_advanced/KEGG.gmt",outdir='results/GSEA',cutoff=0.5,verbose=True, background  = 7757)

gseapy.enrichr(gene_list="results/covid-19_proteomics/Time_series/12F_down_regulated_2.txt",description='12F_down',gene_sets="data/KEGG_advanced/KEGG.gmt",outdir='results/GSEA',cutoff=0.5,verbose=True, background  = 7757)

## Pairwise comp

gseapy.enrichr(gene_list="results/covid-19_proteomics/Pathways_heatmap/prot_down_regulated_H48PI-H24PI_2.txt",description='prot_down_24_48',gene_sets="data/KEGG_advanced/KEGG.gmt",outdir='results/GSEA_time_series',cutoff=0.5,verbose=True, background  = 7757)

gseapy.enrichr(gene_list="results/covid-19_proteomics/Pathways_heatmap/prot_up_regulated_H48PI-H24PI_2.txt",description='prot_up_24_48',gene_sets="data/KEGG_advanced/KEGG.gmt",outdir='results/GSEA_time_series',cutoff=0.5,verbose=True, background  = 7757)


gseapy.enrichr(gene_list="results/covid-19_proteomics/Pathways_heatmap/prot_down_regulated_H72PI-H48PI_2.txt",description='prot_down_48_72',gene_sets="data/KEGG_advanced/KEGG.gmt",outdir='results/GSEA_time_series',cutoff=0.5,verbose=True, background  = 7757)

gseapy.enrichr(gene_list="results/covid-19_proteomics/Pathways_heatmap/prot_up_regulated_H72PI-H48PI_2.txt",description='prot_up_48_72',gene_sets="data/KEGG_advanced/KEGG.gmt",outdir='results/GSEA_time_series',cutoff=0.5,verbose=True, background  = 7757)




