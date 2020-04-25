# COVID19

Commands and codes used for the RNASeq and Proteomics data analysis SARS-Cov2 infected samples

## About

The project aims to identify host cellular response against SARS-CoV2 infection in Huh7 cell lines. A time-series integrative proteo-transcriptomics analysis design was employed in the project. The Huh7 cells were collected at 24, 48, 72 hours post infection and RNASeq & Proteomics data were generated. Also an uninfected sample was included which used as a control. There were three replicates in the design.
Proteomics and transcriptomics data were analysed using R package LIMMA, both for pairwise and time series analysis. 

## Data input and output
Inputs :

- Proteomics : Proteomics raw data with uniprot accession as rows and samples as columns. Annotation file with as columns 1)            Uniprot Accession 2) Gene name.

- Transcriptomics : Transcriptomics count data with Ensembl ID as rows and samples as columns.

Outputs :  
- PCA, Distribution after normalization
- Up or down regulated proteins & transcripts (time series analysis)
- Up or down regulated proteins & transcripts (pair-wise analysis)

## Outline 
### Pre-processing (Proteomics)
1) Count missing values / PCA
2) Normalization
3) Plotting Distribution / Dimension reduction : PCA 2

### Pre-processing (Transcriptomics)
1) Calculation of Normalization factors
2) Filtering of low abundant genes
3) Voom transformation

### Expression analysis
1) LIMMA : 6 pair-wise comparisons (UNINF/T24 / T48 / T72)
2) LIMMA : time series analysis (T24, T48, T72)

### Figure generation
1) Pathway enrichment heatmap (All analysis)
2) Sankey plot (top 4 pathways)
3) Scatter plots (top 4 pathways)


## Installation

## Clone repository
```
git clone https://github.com/neogilab/COVID19.git
cd COVID19/
```

## Requirements
All the analysis were performed in Linux-ubuntu environment.
1. Python3.5+ (Please check https://github.com/zqfang/gseapy for GSEAPY requirements.)
2. R packages (Analysis and figure generation) :

```
Rscript source/requierements.R
# This command will install the following packages:
# NormalyzerDE==1.4.0
# ggfortify==0.4.9
# xlsx==0.6.3
# gplots==3.0.3 
# edgeR==3.28.1
# limma==3.42.2
# matrixStats==0.56.0
# reshape2==1.4.3
# ggalluvial==0.11.1
# ggplot2==3.3.0
# dplyr==0.8.5
```

## Execution

All data should be placed in a folder called data (transcriptomics data must be in a file named Transcriptomics and proteomics data in a file named Proteomics).

### Proteomics 
```
Rscript -e "rmarkdown::render('covid-19_proteomics_preprocessing.Rmd')"
Rscript -e "rmarkdown::render('cov-19_time_series_proteomics_antiviral.Rmd')"
Rscript -e "rmarkdown::render('covid-19_transcriptomics_pairwise_comp.Rmd')"
```

### Transcriptomics
```
Rscript -e "rmarkdown::render('cov-19_time_series_transcriptomics_antiviral.Rmd')"
Rscript -e "rmarkdown::render('covid-19_transcriptomics_pairwise_comp.Rmd')"
```

### Gene set enrichment analysis
```
python3 GSEA.py
```

### make figures
```
Rscript -e "rmarkdown::render('covid-19_figures_heatmap.Rmd')"
Rscript -e "rmarkdown::render('covid-19_figures_top_4_pathways.Rmd')"
```
