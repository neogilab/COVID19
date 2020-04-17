# Omics covid-19

Analyse proteomics and transcriptomics data from cov-19 infected samples using LIMMA pairwise and time series design.

## About

Omics covid-19 aims to find biomarkers and terms associated with covid-19 infection in human cells. Pipeline is adapted for low number of samples.

## Data specificity
- paired samples
- time course experiments
- 4 conditions(6 comparisons)

## Data input and output
Inputs :

Proteomics :
Proteomics raw data is submitted with uniprot accession as row and samples as columns.
Annotation file with as columns 1) Uniprot Accession 2) Gene name

Transcriptomics :
Transcriptomics count data is submitted with Ensembl ID as row and samples as columns.

Ouputs :  
1)  PCA, Distribution after norm
2)  Proteins / transcripts up or down regulated according to time in infected samples
3)  Proteins / transcripts up or down regulated in each pairwise comparison

## Outline 
### Pre-processing Proteomics
Count missing values / PCA
Normalization ( NormalizerDE, selection based on report)
Plotting Distribution / Dimension reduction : PCA 2

### Pre-processing Transcriptomics
Calculation of Normalization factors
Filtering of low abundannce reads
Voom transformation

### Multiple comparisons
LIMMA : 6 comparisons (UNINF/T24 / T48 / T72) paired samples
LIMMA : time serie analysis in infected samples


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
# sva==3.26.0
```

## Running code

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
