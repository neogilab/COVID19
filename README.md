# COVID19

Commands and codes used for the RNASeq and Proteomics data analysis SARS-Cov2 infected samples

## About

Analyse proteomics and transcriptomics data from cov-19 infected samples using LIMMA pairwise and time series design. COVID19 aims to find biomarkers and terms associated with covid-19 infection in human cells. Pipeline is adapted for low number of samples.

## Data specificity
- paired samples
- time course experiments
- 4 conditions(6 comparisons)

## Data input and output
Inputs :

- Proteomics : Proteomics raw data is submitted with uniprot accession as row and samples as columns. Annotation file with as columns 1) Uniprot Accession 2) Gene name.

- Transcriptomics : Transcriptomics count data is submitted with Ensembl ID as row and samples as columns.

Ouputs :  
- PCA, Distribution after norm
- Proteins / transcripts up or down regulated according to time in infected samples
- Proteins / transcripts up or down regulated in each pairwise comparison

## Outline 
### Pre-processing Proteomics
1) Count missing values / PCA
2) Normalization ( NormalizerDE, selection based on report)
3) Plotting Distribution / Dimension reduction : PCA 2

### Pre-processing Transcriptomics
1) Calculation of Normalization factors
2) Filtering of low abundannce reads
3) Voom transformation

### Multiple comparisons
4) LIMMA : 6 comparisons (UNINF/T24 / T48 / T72) paired samples
5) LIMMA : time serie analysis in infected samples

### Figures generation
6) Pvalue heatmap (summary all methods)
7) Sankey plot (top 4 pathways)
8) Scatter plots (top 4 pathways)


## Installation

## Clone repository
```
git clone https://github.com/neogilab/COVID19.git
cd COVID19/
```

## Requirements
python
1. A linux distribution.
2. Install the few required **R packages** :

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

## Running code

All data should be placed in a folder called data (transcriptomics data must be in a file called Transcriptomics and proteomics data in a file called Proteomics).

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