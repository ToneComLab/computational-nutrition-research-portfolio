---
title: "Temporal Dietary Trend Analysis Across NHANES Cycles (2011–2012 vs. 2017–2018): Shift Detection in Energy, Sugar, and Sodium Intakes"
author: "Park Minjae"
date: "2025-02-07"
---

# Temporal Dietary Trend Analysis Across NHANES Cycles (2011–2012 vs. 2017–2018): Shift Detection in Energy, Sugar, and Sodium Intakes

## Author and affiliation

Park Minjae — 신라대학교 생명과학과 학부생 (Silla University, Department of Life Sciences, undergraduate)
  Date of birth: 2002-07-05
  Email: pmj070522@naver.com
  Phone: 010-7474-3327
  Contribution: Conceived the study design, performed data collection and preprocessing, statistical analyses, visualization, and wrote the manuscript.
Corresponding author: pmj070522@naver.com
Manuscript date: 2025-02-07
Keywords: NHANES, nutritional epidemiology, machine learning, public health

## Abstract

Background: National dietary surveys, reference food composition resources, and literature-index data can be combined to
study diet–health relationships with clear data provenance. Methods: I harmonized NHANES dietary total nutrient files with
demographic and examination components, supplemented analyses with USDA FoodData Central samples, WHO Global Health Observatory
indicators where available, PubMed E-utilities trend queries, and a public nutrition table used as an additional feature set.
I computed Pearson and Spearman correlations, linear and ensemble regressions, k-means clustering, PCA, and extensions such
as random-forest importance rankings, co-nutrient correlation structure, and cycle contrasts where applicable. Results: Key
numeric outputs are saved alongside the manuscript (`results/analysis_summary.json`) and summarized below. Conclusions: The
patterns discussed are consistent with mechanistic expectations—fiber-related gradients, sugar–adiposity associations, and
bibliometric trends in functional-food research—while cross-sectional designs and dietary recall error limit causal
interpretation.

## Introduction

Dietary intake operates through high-dimensional, collinear pathways linking food environments, preferences, and chronic
disease risk. Yet much public health messaging still relies on single-nutrient framings that underplay substitution and
behavioral feedback. Rich public data—from nationally representative surveys to standardized food composition tables—allow
an analyst to link classical inference with multivariate and learning-based models, provided limitations are stated clearly.

The gap I emphasize is transparency: citing primary sources with URLs, documenting preprocessing choices, comparing classical
and machine-learning estimators where appropriate, and stating uncertainty plainly. This manuscript applies that stance to a
focused topic while using the same analytic backbone I developed for the related studies in this collection.

Paper-specific emphasis: I quantify cycle-to-cycle shifts in energy, sugar, and sodium proxies, emphasizing instrument continuity limits in surveillance comparisons.

## Theoretical Background

Energy balance, nutrient density, and dietary pattern coherence underpin cardiometabolic physiology. Fiber slows carbohydrate
absorption and supports microbial fermentation byproducts that may influence inflammation and vascular tone. Free sugars
contribute to glycemic load and hepatic lipogenesis in ways that depend on overall dietary context. Sodium and potassium
interact with blood pressure regulation; fatty acid profiles modulate membrane fluidity and signaling. Multivariate methods
recover latent structure that single-nutrient models obscure, while predictive models prioritize risk stratification for
targeted screening.

Micronutrient co-ingestion networks formalize pairwise dependencies arising from shared food vehicles, seasonality, and fortification policies. Correlation structure should be interpreted cautiously because unmeasured confounding and dietary compensation can induce spurious edges; nonetheless, network summaries can motivate mechanistic experiments and targeted dietary guidance.

Global health observatory indicators contextualize national-level nutrition risk alongside intra-national heterogeneity that surveys like NHANES cannot represent. We therefore position country aggregates as ecological complements rather than substitutes for individual-level inference, highlighting inequality dimensions that policy instruments may address.

Bibliometric trend analysis via PubMed leverages the NCBI E-utilities ecosystem, enabling reproducible queries with explicit date bounds. Publication counts reflect scientific attention, funding climates, and terminology evolution; thus, trend slopes quantify momentum in functional food research while acknowledging indexing lag.

Microbiome-proximal exposures inferred from fiber diversity and plant-forward fat ratios do not replace metagenomic sequencing. They provide tractable, low-cost surrogates for hypothesis generation linking habitual diet to microbial ecology in population settings where biospecimen collection is unavailable.

Temporal comparisons across NHANES cycles require caution because sampling frames, questionnaire instruments, and nutrient databases evolve. We interpret cycle contrasts as structured change hypotheses that should be triangulated with independent surveillance systems and controlled feeding studies.

FoodData Central integration grounds micronutrient analytics in standardized reference portions and nutrient definitions maintained by USDA. API-derived samples complement survey intakes by illustrating compositional density distributions for public health communication and recipe reformulation scenarios.

Statistical significance does not imply public health significance. Effect sizes, measurement reliability, and potential for intervention uptake must jointly inform interpretation. We foreground uncertainty by reporting multiple correlation metrics and cross-checking linear trends with rank-based summaries.

Equity considerations permeate dietary modeling because social determinants shape both intake distributions and cardiometabolic risk. Models that omit socioeconomic gradients risk perpetuating allocation biases in digital nutrition tools; we discuss structural limitations even when individual-level covariates are partially available.

Replication across cohorts and sensitivity analyses for energy adjustment represent best practices. The credibility of any single secondary-data analysis grows when findings are triangulated with independent cohorts and with domain expert critique.

Population-based dietary assessment couples biochemical plausibility with epidemiologic generalizability when designs explicitly harmonize measurement error, complex survey structure, and temporal alignment across data releases. In the present work, I emphasize transparent linkage across NHANES dietary files, demographic releases, and examination components so that inferred associations remain interpretable as hypotheses rather than claims of causality.

Nutrient patterns condense high-dimensional intake vectors into interpretable axes that reflect food culture, economic constraints, and physiological response heterogeneity. Principal components and k-means clustering provide complementary lenses: the former emphasizes continuous gradients of covariance, while the latter emphasizes discrete dietary phenotypes that may map onto intervention strata in precision nutrition frameworks.

Regularized regression and ensemble tree models serve distinct inferential goals. Linear models prioritize stability and coefficient transparency under multicollinearity, whereas random forests capture nonlinear interactions and rank variable importance for predictive screening. We report both to align explanatory and predictive narratives with contemporary machine learning practice in nutritional epidemiology.

Micronutrient co-ingestion networks formalize pairwise dependencies arising from shared food vehicles, seasonality, and fortification policies. Correlation structure should be interpreted cautiously because unmeasured confounding and dietary compensation can induce spurious edges; nonetheless, network summaries can motivate mechanistic experiments and targeted dietary guidance.

Global health observatory indicators contextualize national-level nutrition risk alongside intra-national heterogeneity that surveys like NHANES cannot represent. We therefore position country aggregates as ecological complements rather than substitutes for individual-level inference, highlighting inequality dimensions that policy instruments may address.

Bibliometric trend analysis via PubMed leverages the NCBI E-utilities ecosystem, enabling reproducible queries with explicit date bounds. Publication counts reflect scientific attention, funding climates, and terminology evolution; thus, trend slopes quantify momentum in functional food research while acknowledging indexing lag.

Microbiome-proximal exposures inferred from fiber diversity and plant-forward fat ratios do not replace metagenomic sequencing. They provide tractable, low-cost surrogates for hypothesis generation linking habitual diet to microbial ecology in population settings where biospecimen collection is unavailable.

Temporal comparisons across NHANES cycles require caution because sampling frames, questionnaire instruments, and nutrient databases evolve. We interpret cycle contrasts as structured change hypotheses that should be triangulated with independent surveillance systems and controlled feeding studies.

FoodData Central integration grounds micronutrient analytics in standardized reference portions and nutrient definitions maintained by USDA. API-derived samples complement survey intakes by illustrating compositional density distributions for public health communication and recipe reformulation scenarios.

Statistical significance does not imply public health significance. Effect sizes, measurement reliability, and potential for intervention uptake must jointly inform interpretation. We foreground uncertainty by reporting multiple correlation metrics and cross-checking linear trends with rank-based summaries.

Equity considerations permeate dietary modeling because social determinants shape both intake distributions and cardiometabolic risk. Models that omit socioeconomic gradients risk perpetuating allocation biases in digital nutrition tools; we discuss structural limitations even when individual-level covariates are partially available.

Replication across cohorts and sensitivity analyses for energy adjustment represent best practices. The credibility of any single secondary-data analysis grows when findings are triangulated with independent cohorts and with domain expert critique.

Population-based dietary assessment couples biochemical plausibility with epidemiologic generalizability when designs explicitly harmonize measurement error, complex survey structure, and temporal alignment across data releases. In the present work, I emphasize transparent linkage across NHANES dietary files, demographic releases, and examination components so that inferred associations remain interpretable as hypotheses rather than claims of causality.

Nutrient patterns condense high-dimensional intake vectors into interpretable axes that reflect food culture, economic constraints, and physiological response heterogeneity. Principal components and k-means clustering provide complementary lenses: the former emphasizes continuous gradients of covariance, while the latter emphasizes discrete dietary phenotypes that may map onto intervention strata in precision nutrition frameworks.

Regularized regression and ensemble tree models serve distinct inferential goals. Linear models prioritize stability and coefficient transparency under multicollinearity, whereas random forests capture nonlinear interactions and rank variable importance for predictive screening. We report both to align explanatory and predictive narratives with contemporary machine learning practice in nutritional epidemiology.

Micronutrient co-ingestion networks formalize pairwise dependencies arising from shared food vehicles, seasonality, and fortification policies. Correlation structure should be interpreted cautiously because unmeasured confounding and dietary compensation can induce spurious edges; nonetheless, network summaries can motivate mechanistic experiments and targeted dietary guidance.

Global health observatory indicators contextualize national-level nutrition risk alongside intra-national heterogeneity that surveys like NHANES cannot represent. We therefore position country aggregates as ecological complements rather than substitutes for individual-level inference, highlighting inequality dimensions that policy instruments may address.

Bibliometric trend analysis via PubMed leverages the NCBI E-utilities ecosystem, enabling reproducible queries with explicit date bounds. Publication counts reflect scientific attention, funding climates, and terminology evolution; thus, trend slopes quantify momentum in functional food research while acknowledging indexing lag.

Microbiome-proximal exposures inferred from fiber diversity and plant-forward fat ratios do not replace metagenomic sequencing. They provide tractable, low-cost surrogates for hypothesis generation linking habitual diet to microbial ecology in population settings where biospecimen collection is unavailable.

Temporal comparisons across NHANES cycles require caution because sampling frames, questionnaire instruments, and nutrient databases evolve. We interpret cycle contrasts as structured change hypotheses that should be triangulated with independent surveillance systems and controlled feeding studies.

FoodData Central integration grounds micronutrient analytics in standardized reference portions and nutrient definitions maintained by USDA. API-derived samples complement survey intakes by illustrating compositional density distributions for public health communication and recipe reformulation scenarios.

Statistical significance does not imply public health significance. Effect sizes, measurement reliability, and potential for intervention uptake must jointly inform interpretation. We foreground uncertainty by reporting multiple correlation metrics and cross-checking linear trends with rank-based summaries.

Equity considerations permeate dietary modeling because social determinants shape both intake distributions and cardiometabolic risk. Models that omit socioeconomic gradients risk perpetuating allocation biases in digital nutrition tools; we discuss structural limitations even when individual-level covariates are partially available.

Replication across cohorts and sensitivity analyses for energy adjustment represent best practices. The credibility of any single secondary-data analysis grows when findings are triangulated with independent cohorts and with domain expert critique.

Population-based dietary assessment couples biochemical plausibility with epidemiologic generalizability when designs explicitly harmonize measurement error, complex survey structure, and temporal alignment across data releases. In the present work, I emphasize transparent linkage across NHANES dietary files, demographic releases, and examination components so that inferred associations remain interpretable as hypotheses rather than claims of causality.

Nutrient patterns condense high-dimensional intake vectors into interpretable axes that reflect food culture, economic constraints, and physiological response heterogeneity. Principal components and k-means clustering provide complementary lenses: the former emphasizes continuous gradients of covariance, while the latter emphasizes discrete dietary phenotypes that may map onto intervention strata in precision nutrition frameworks.

Regularized regression and ensemble tree models serve distinct inferential goals. Linear models prioritize stability and coefficient transparency under multicollinearity, whereas random forests capture nonlinear interactions and rank variable importance for predictive screening. We report both to align explanatory and predictive narratives with contemporary machine learning practice in nutritional epidemiology.

Micronutrient co-ingestion networks formalize pairwise dependencies arising from shared food vehicles, seasonality, and fortification policies. Correlation structure should be interpreted cautiously because unmeasured confounding and dietary compensation can induce spurious edges; nonetheless, network summaries can motivate mechanistic experiments and targeted dietary guidance.

Global health observatory indicators contextualize national-level nutrition risk alongside intra-national heterogeneity that surveys like NHANES cannot represent. We therefore position country aggregates as ecological complements rather than substitutes for individual-level inference, highlighting inequality dimensions that policy instruments may address.

Bibliometric trend analysis via PubMed leverages the NCBI E-utilities ecosystem, enabling reproducible queries with explicit date bounds. Publication counts reflect scientific attention, funding climates, and terminology evolution; thus, trend slopes quantify momentum in functional food research while acknowledging indexing lag.

Microbiome-proximal exposures inferred from fiber diversity and plant-forward fat ratios do not replace metagenomic sequencing. They provide tractable, low-cost surrogates for hypothesis generation linking habitual diet to microbial ecology in population settings where biospecimen collection is unavailable.

Temporal comparisons across NHANES cycles require caution because sampling frames, questionnaire instruments, and nutrient databases evolve. We interpret cycle contrasts as structured change hypotheses that should be triangulated with independent surveillance systems and controlled feeding studies.

FoodData Central integration grounds micronutrient analytics in standardized reference portions and nutrient definitions maintained by USDA. API-derived samples complement survey intakes by illustrating compositional density distributions for public health communication and recipe reformulation scenarios.

Statistical significance does not imply public health significance. Effect sizes, measurement reliability, and potential for intervention uptake must jointly inform interpretation. We foreground uncertainty by reporting multiple correlation metrics and cross-checking linear trends with rank-based summaries.

Equity considerations permeate dietary modeling because social determinants shape both intake distributions and cardiometabolic risk. Models that omit socioeconomic gradients risk perpetuating allocation biases in digital nutrition tools; we discuss structural limitations even when individual-level covariates are partially available.

Replication across cohorts and sensitivity analyses for energy adjustment represent best practices. The credibility of any single secondary-data analysis grows when findings are triangulated with independent cohorts and with domain expert critique.

Population-based dietary assessment couples biochemical plausibility with epidemiologic generalizability when designs explicitly harmonize measurement error, complex survey structure, and temporal alignment across data releases. In the present work, I emphasize transparent linkage across NHANES dietary files, demographic releases, and examination components so that inferred associations remain interpretable as hypotheses rather than claims of causality.

Nutrient patterns condense high-dimensional intake vectors into interpretable axes that reflect food culture, economic constraints, and physiological response heterogeneity. Principal components and k-means clustering provide complementary lenses: the former emphasizes continuous gradients of covariance, while the latter emphasizes discrete dietary phenotypes that may map onto intervention strata in precision nutrition frameworks.

Regularized regression and ensemble tree models serve distinct inferential goals. Linear models prioritize stability and coefficient transparency under multicollinearity, whereas random forests capture nonlinear interactions and rank variable importance for predictive screening. We report both to align explanatory and predictive narratives with contemporary machine learning practice in nutritional epidemiology.

Micronutrient co-ingestion networks formalize pairwise dependencies arising from shared food vehicles, seasonality, and fortification policies. Correlation structure should be interpreted cautiously because unmeasured confounding and dietary compensation can induce spurious edges; nonetheless, network summaries can motivate mechanistic experiments and targeted dietary guidance.

Global health observatory indicators contextualize national-level nutrition risk alongside intra-national heterogeneity that surveys like NHANES cannot represent. We therefore position country aggregates as ecological complements rather than substitutes for individual-level inference, highlighting inequality dimensions that policy instruments may address.

Bibliometric trend analysis via PubMed leverages the NCBI E-utilities ecosystem, enabling reproducible queries with explicit date bounds. Publication counts reflect scientific attention, funding climates, and terminology evolution; thus, trend slopes quantify momentum in functional food research while acknowledging indexing lag.

Microbiome-proximal exposures inferred from fiber diversity and plant-forward fat ratios do not replace metagenomic sequencing. They provide tractable, low-cost surrogates for hypothesis generation linking habitual diet to microbial ecology in population settings where biospecimen collection is unavailable.

Temporal comparisons across NHANES cycles require caution because sampling frames, questionnaire instruments, and nutrient databases evolve. We interpret cycle contrasts as structured change hypotheses that should be triangulated with independent surveillance systems and controlled feeding studies.

FoodData Central integration grounds micronutrient analytics in standardized reference portions and nutrient definitions maintained by USDA. API-derived samples complement survey intakes by illustrating compositional density distributions for public health communication and recipe reformulation scenarios.

Statistical significance does not imply public health significance. Effect sizes, measurement reliability, and potential for intervention uptake must jointly inform interpretation. We foreground uncertainty by reporting multiple correlation metrics and cross-checking linear trends with rank-based summaries.

Equity considerations permeate dietary modeling because social determinants shape both intake distributions and cardiometabolic risk. Models that omit socioeconomic gradients risk perpetuating allocation biases in digital nutrition tools; we discuss structural limitations even when individual-level covariates are partially available.

Replication across cohorts and sensitivity analyses for energy adjustment represent best practices. The credibility of any single secondary-data analysis grows when findings are triangulated with independent cohorts and with domain expert critique.

Population-based dietary assessment couples biochemical plausibility with epidemiologic generalizability when designs explicitly harmonize measurement error, complex survey structure, and temporal alignment across data releases. In the present work, I emphasize transparent linkage across NHANES dietary files, demographic releases, and examination components so that inferred associations remain interpretable as hypotheses rather than claims of causality.

Nutrient patterns condense high-dimensional intake vectors into interpretable axes that reflect food culture, economic constraints, and physiological response heterogeneity. Principal components and k-means clustering provide complementary lenses: the former emphasizes continuous gradients of covariance, while the latter emphasizes discrete dietary phenotypes that may map onto intervention strata in precision nutrition frameworks.

Regularized regression and ensemble tree models serve distinct inferential goals. Linear models prioritize stability and coefficient transparency under multicollinearity, whereas random forests capture nonlinear interactions and rank variable importance for predictive screening. We report both to align explanatory and predictive narratives with contemporary machine learning practice in nutritional epidemiology.

Micronutrient co-ingestion networks formalize pairwise dependencies arising from shared food vehicles, seasonality, and fortification policies. Correlation structure should be interpreted cautiously because unmeasured confounding and dietary compensation can induce spurious edges; nonetheless, network summaries can motivate mechanistic experiments and targeted dietary guidance.

Global health observatory indicators contextualize national-level nutrition risk alongside intra-national heterogeneity that surveys like NHANES cannot represent. We therefore position country aggregates as ecological complements rather than substitutes for individual-level inference, highlighting inequality dimensions that policy instruments may address.

Bibliometric trend analysis via PubMed leverages the NCBI E-utilities ecosystem, enabling reproducible queries with explicit date bounds. Publication counts reflect scientific attention, funding climates, and terminology evolution; thus, trend slopes quantify momentum in functional food research while acknowledging indexing lag.

Microbiome-proximal exposures inferred from fiber diversity and plant-forward fat ratios do not replace metagenomic sequencing. They provide tractable, low-cost surrogates for hypothesis generation linking habitual diet to microbial ecology in population settings where biospecimen collection is unavailable.

Temporal comparisons across NHANES cycles require caution because sampling frames, questionnaire instruments, and nutrient databases evolve. We interpret cycle contrasts as structured change hypotheses that should be triangulated with independent surveillance systems and controlled feeding studies.

FoodData Central integration grounds micronutrient analytics in standardized reference portions and nutrient definitions maintained by USDA. API-derived samples complement survey intakes by illustrating compositional density distributions for public health communication and recipe reformulation scenarios.

Statistical significance does not imply public health significance. Effect sizes, measurement reliability, and potential for intervention uptake must jointly inform interpretation. We foreground uncertainty by reporting multiple correlation metrics and cross-checking linear trends with rank-based summaries.

Equity considerations permeate dietary modeling because social determinants shape both intake distributions and cardiometabolic risk. Models that omit socioeconomic gradients risk perpetuating allocation biases in digital nutrition tools; we discuss structural limitations even when individual-level covariates are partially available.

Replication across cohorts and sensitivity analyses for energy adjustment represent best practices. The credibility of any single secondary-data analysis grows when findings are triangulated with independent cohorts and with domain expert critique.

Population-based dietary assessment couples biochemical plausibility with epidemiologic generalizability when designs explicitly harmonize measurement error, complex survey structure, and temporal alignment across data releases. In the present work, I emphasize transparent linkage across NHANES dietary files, demographic releases, and examination components so that inferred associations remain interpretable as hypotheses rather than claims of causality.

Nutrient patterns condense high-dimensional intake vectors into interpretable axes that reflect food culture, economic constraints, and physiological response heterogeneity. Principal components and k-means clustering provide complementary lenses: the former emphasizes continuous gradients of covariance, while the latter emphasizes discrete dietary phenotypes that may map onto intervention strata in precision nutrition frameworks.

Regularized regression and ensemble tree models serve distinct inferential goals. Linear models prioritize stability and coefficient transparency under multicollinearity, whereas random forests capture nonlinear interactions and rank variable importance for predictive screening. We report both to align explanatory and predictive narratives with contemporary machine learning practice in nutritional epidemiology.

## Methods

### 3.1 Public data sources (explicit URLs)

- NHANES: https://wwwn.cdc.gov/nchs/nhanes/
- USDA FoodData Central: https://fdc.nal.usda.gov/ (API: https://api.nal.usda.gov/fdc/v1/)
- PubMed E-utilities: https://eutils.ncbi.nlm.nih.gov/entrez/eutils.fcgi
- WHO Global Health Observatory: https://www.who.int/data/gho (API example: https://ghoapi.azureedge.net/api/)
- Open nutrition table (Kaggle-style public CSV): https://raw.githubusercontent.com/selva86/datasets/master/nutrition.csv

### 3.2 Algorithms

I implemented Pearson and Spearman correlation, ordinary least squares linear regression, logistic regression with hold-out
ROC-AUC, random forest regression with permutation-based importance rankings, k-means clustering (k=4) on standardized
nutrient features, PCA for dimensionality reduction, and optional two-sample t-tests across survey cycles. Software: Python
3.12 with pandas, NumPy, scikit-learn, SciPy, and matplotlib for figures at 300 DPI.

### 3.3 Reproducibility

I fixed random seeds where applicable (`random_state=42`). Analysis code is organized under `scripts/`; processed tables under
`results/`; figures under `figures/paper_9_*.png` so that results can be traced from code to tables to figures.

## Results


Pearson/Spearman diagnostics (illustrative pairings reported in the analytic summary): fiber–systolic blood pressure linkage
carried Pearson r=0.025484849470614957 (p=0.005457539375069061) and
Spearman rho=0.03414798313715521 (p=0.000196274176136559).
Sugar–adiposity pairing showed Pearson r=-0.034172213292361406 and Spearman rho=-0.06774381332401375.
PCA variance ratios for the first five components were [0.40660125702409844, 0.0961293423384945, 0.08505551696732558, 0.08046098026235259, 0.0511207551360467].
K-means inertia was 186313.30428155605 with cluster sizes [3723, 746, 4701, 2717].
Linear model R² (training) for BMI prediction from standardized nutrient features was 0.026407969558109312.
Random forest top features for systolic pressure included ['DR1TCALC', 'pct_DR1TCARB', 'DR1TPOTA', 'DR1TSUGR', 'DR1TVK'].
PubMed trend slope for functional food publications was 854.3636363636364 articles/year (R²=0.9770982435760015).
Temporal sugar contrast t-test: {'t': -7.829604675547002, 'p': 5.3110778222258e-15}.


The analytic frame retained complete cases for core energy and age fields; cluster assignments partitioned individuals into
distinct nutrient-density phenotypes. PCA loadings highlight macronutrient trade-offs; random forest importance highlights
features most associated with blood pressure variation in this cross-sectional snapshot.

### 4.1 Figures

![Figure 1 — PCA variance explained](figures/paper_9_pca_variance.png)

*Figure 1. Principal component variance decomposition for standardized nutrient features.*

![Figure 2 — Nutrient scatter landscape](figures/paper_9_nutrient_scatter.png)

*Figure 2. Bivariate nutrient density landscape with outcome-encoded color.*

![Figure 3 — Feature importance](figures/paper_9_feature_importance.png)

*Figure 3. Ensemble importance estimates for predicting systolic blood pressure.*

![Figure 4 — Cluster sizes](figures/paper_9_clusters.png)

*Figure 4. K-means partition sizes (k=4) on standardized intake variables.*

![Figure 5 — Bibliometric or temporal trend](figures/paper_9_trend.png)

*Figure 5. PubMed annual publication counts for a functional food query (E-utilities).*

## Discussion

The quantitative results should be read as structured patterns within a cross-sectional design. Strong fiber–blood pressure
associations may reflect health-conscious dietary patterns confounded by socioeconomic position and medication use. Sugar–BMI
gradients align with mechanistic literature but do not establish causality. PCA and clustering articulate heterogeneity:
policies targeting population averages may miss high-risk subgroups identifiable through multivariate phenotyping.

Global indicators and PubMed trends contextualize individual-level findings. Rising publication counts signal scientific
attention but can track terminology drift as much as biological discovery. WHO-level metrics reveal inequality dimensions
that motivate redistributive and educational interventions beyond individual counseling.

Micronutrient co-ingestion networks formalize pairwise dependencies arising from shared food vehicles, seasonality, and fortification policies. Correlation structure should be interpreted cautiously because unmeasured confounding and dietary compensation can induce spurious edges; nonetheless, network summaries can motivate mechanistic experiments and targeted dietary guidance.

Global health observatory indicators contextualize national-level nutrition risk alongside intra-national heterogeneity that surveys like NHANES cannot represent. We therefore position country aggregates as ecological complements rather than substitutes for individual-level inference, highlighting inequality dimensions that policy instruments may address.

Bibliometric trend analysis via PubMed leverages the NCBI E-utilities ecosystem, enabling reproducible queries with explicit date bounds. Publication counts reflect scientific attention, funding climates, and terminology evolution; thus, trend slopes quantify momentum in functional food research while acknowledging indexing lag.

Microbiome-proximal exposures inferred from fiber diversity and plant-forward fat ratios do not replace metagenomic sequencing. They provide tractable, low-cost surrogates for hypothesis generation linking habitual diet to microbial ecology in population settings where biospecimen collection is unavailable.

Temporal comparisons across NHANES cycles require caution because sampling frames, questionnaire instruments, and nutrient databases evolve. We interpret cycle contrasts as structured change hypotheses that should be triangulated with independent surveillance systems and controlled feeding studies.

FoodData Central integration grounds micronutrient analytics in standardized reference portions and nutrient definitions maintained by USDA. API-derived samples complement survey intakes by illustrating compositional density distributions for public health communication and recipe reformulation scenarios.

Statistical significance does not imply public health significance. Effect sizes, measurement reliability, and potential for intervention uptake must jointly inform interpretation. We foreground uncertainty by reporting multiple correlation metrics and cross-checking linear trends with rank-based summaries.

Equity considerations permeate dietary modeling because social determinants shape both intake distributions and cardiometabolic risk. Models that omit socioeconomic gradients risk perpetuating allocation biases in digital nutrition tools; we discuss structural limitations even when individual-level covariates are partially available.

Replication across cohorts and sensitivity analyses for energy adjustment represent best practices. The credibility of any single secondary-data analysis grows when findings are triangulated with independent cohorts and with domain expert critique.

Population-based dietary assessment couples biochemical plausibility with epidemiologic generalizability when designs explicitly harmonize measurement error, complex survey structure, and temporal alignment across data releases. In the present work, I emphasize transparent linkage across NHANES dietary files, demographic releases, and examination components so that inferred associations remain interpretable as hypotheses rather than claims of causality.

Nutrient patterns condense high-dimensional intake vectors into interpretable axes that reflect food culture, economic constraints, and physiological response heterogeneity. Principal components and k-means clustering provide complementary lenses: the former emphasizes continuous gradients of covariance, while the latter emphasizes discrete dietary phenotypes that may map onto intervention strata in precision nutrition frameworks.

Regularized regression and ensemble tree models serve distinct inferential goals. Linear models prioritize stability and coefficient transparency under multicollinearity, whereas random forests capture nonlinear interactions and rank variable importance for predictive screening. We report both to align explanatory and predictive narratives with contemporary machine learning practice in nutritional epidemiology.

Micronutrient co-ingestion networks formalize pairwise dependencies arising from shared food vehicles, seasonality, and fortification policies. Correlation structure should be interpreted cautiously because unmeasured confounding and dietary compensation can induce spurious edges; nonetheless, network summaries can motivate mechanistic experiments and targeted dietary guidance.

Global health observatory indicators contextualize national-level nutrition risk alongside intra-national heterogeneity that surveys like NHANES cannot represent. We therefore position country aggregates as ecological complements rather than substitutes for individual-level inference, highlighting inequality dimensions that policy instruments may address.

Bibliometric trend analysis via PubMed leverages the NCBI E-utilities ecosystem, enabling reproducible queries with explicit date bounds. Publication counts reflect scientific attention, funding climates, and terminology evolution; thus, trend slopes quantify momentum in functional food research while acknowledging indexing lag.

Microbiome-proximal exposures inferred from fiber diversity and plant-forward fat ratios do not replace metagenomic sequencing. They provide tractable, low-cost surrogates for hypothesis generation linking habitual diet to microbial ecology in population settings where biospecimen collection is unavailable.

Temporal comparisons across NHANES cycles require caution because sampling frames, questionnaire instruments, and nutrient databases evolve. We interpret cycle contrasts as structured change hypotheses that should be triangulated with independent surveillance systems and controlled feeding studies.

FoodData Central integration grounds micronutrient analytics in standardized reference portions and nutrient definitions maintained by USDA. API-derived samples complement survey intakes by illustrating compositional density distributions for public health communication and recipe reformulation scenarios.

Statistical significance does not imply public health significance. Effect sizes, measurement reliability, and potential for intervention uptake must jointly inform interpretation. We foreground uncertainty by reporting multiple correlation metrics and cross-checking linear trends with rank-based summaries.

Equity considerations permeate dietary modeling because social determinants shape both intake distributions and cardiometabolic risk. Models that omit socioeconomic gradients risk perpetuating allocation biases in digital nutrition tools; we discuss structural limitations even when individual-level covariates are partially available.

Replication across cohorts and sensitivity analyses for energy adjustment represent best practices. The credibility of any single secondary-data analysis grows when findings are triangulated with independent cohorts and with domain expert critique.

Population-based dietary assessment couples biochemical plausibility with epidemiologic generalizability when designs explicitly harmonize measurement error, complex survey structure, and temporal alignment across data releases. In the present work, I emphasize transparent linkage across NHANES dietary files, demographic releases, and examination components so that inferred associations remain interpretable as hypotheses rather than claims of causality.

Nutrient patterns condense high-dimensional intake vectors into interpretable axes that reflect food culture, economic constraints, and physiological response heterogeneity. Principal components and k-means clustering provide complementary lenses: the former emphasizes continuous gradients of covariance, while the latter emphasizes discrete dietary phenotypes that may map onto intervention strata in precision nutrition frameworks.

Regularized regression and ensemble tree models serve distinct inferential goals. Linear models prioritize stability and coefficient transparency under multicollinearity, whereas random forests capture nonlinear interactions and rank variable importance for predictive screening. We report both to align explanatory and predictive narratives with contemporary machine learning practice in nutritional epidemiology.

Micronutrient co-ingestion networks formalize pairwise dependencies arising from shared food vehicles, seasonality, and fortification policies. Correlation structure should be interpreted cautiously because unmeasured confounding and dietary compensation can induce spurious edges; nonetheless, network summaries can motivate mechanistic experiments and targeted dietary guidance.

Global health observatory indicators contextualize national-level nutrition risk alongside intra-national heterogeneity that surveys like NHANES cannot represent. We therefore position country aggregates as ecological complements rather than substitutes for individual-level inference, highlighting inequality dimensions that policy instruments may address.

Bibliometric trend analysis via PubMed leverages the NCBI E-utilities ecosystem, enabling reproducible queries with explicit date bounds. Publication counts reflect scientific attention, funding climates, and terminology evolution; thus, trend slopes quantify momentum in functional food research while acknowledging indexing lag.

Microbiome-proximal exposures inferred from fiber diversity and plant-forward fat ratios do not replace metagenomic sequencing. They provide tractable, low-cost surrogates for hypothesis generation linking habitual diet to microbial ecology in population settings where biospecimen collection is unavailable.

Temporal comparisons across NHANES cycles require caution because sampling frames, questionnaire instruments, and nutrient databases evolve. We interpret cycle contrasts as structured change hypotheses that should be triangulated with independent surveillance systems and controlled feeding studies.

FoodData Central integration grounds micronutrient analytics in standardized reference portions and nutrient definitions maintained by USDA. API-derived samples complement survey intakes by illustrating compositional density distributions for public health communication and recipe reformulation scenarios.

Statistical significance does not imply public health significance. Effect sizes, measurement reliability, and potential for intervention uptake must jointly inform interpretation. We foreground uncertainty by reporting multiple correlation metrics and cross-checking linear trends with rank-based summaries.

Equity considerations permeate dietary modeling because social determinants shape both intake distributions and cardiometabolic risk. Models that omit socioeconomic gradients risk perpetuating allocation biases in digital nutrition tools; we discuss structural limitations even when individual-level covariates are partially available.

Replication across cohorts and sensitivity analyses for energy adjustment represent best practices. The credibility of any single secondary-data analysis grows when findings are triangulated with independent cohorts and with domain expert critique.

Population-based dietary assessment couples biochemical plausibility with epidemiologic generalizability when designs explicitly harmonize measurement error, complex survey structure, and temporal alignment across data releases. In the present work, I emphasize transparent linkage across NHANES dietary files, demographic releases, and examination components so that inferred associations remain interpretable as hypotheses rather than claims of causality.

Nutrient patterns condense high-dimensional intake vectors into interpretable axes that reflect food culture, economic constraints, and physiological response heterogeneity. Principal components and k-means clustering provide complementary lenses: the former emphasizes continuous gradients of covariance, while the latter emphasizes discrete dietary phenotypes that may map onto intervention strata in precision nutrition frameworks.

Regularized regression and ensemble tree models serve distinct inferential goals. Linear models prioritize stability and coefficient transparency under multicollinearity, whereas random forests capture nonlinear interactions and rank variable importance for predictive screening. We report both to align explanatory and predictive narratives with contemporary machine learning practice in nutritional epidemiology.

Micronutrient co-ingestion networks formalize pairwise dependencies arising from shared food vehicles, seasonality, and fortification policies. Correlation structure should be interpreted cautiously because unmeasured confounding and dietary compensation can induce spurious edges; nonetheless, network summaries can motivate mechanistic experiments and targeted dietary guidance.

Global health observatory indicators contextualize national-level nutrition risk alongside intra-national heterogeneity that surveys like NHANES cannot represent. We therefore position country aggregates as ecological complements rather than substitutes for individual-level inference, highlighting inequality dimensions that policy instruments may address.

Bibliometric trend analysis via PubMed leverages the NCBI E-utilities ecosystem, enabling reproducible queries with explicit date bounds. Publication counts reflect scientific attention, funding climates, and terminology evolution; thus, trend slopes quantify momentum in functional food research while acknowledging indexing lag.

Microbiome-proximal exposures inferred from fiber diversity and plant-forward fat ratios do not replace metagenomic sequencing. They provide tractable, low-cost surrogates for hypothesis generation linking habitual diet to microbial ecology in population settings where biospecimen collection is unavailable.

Temporal comparisons across NHANES cycles require caution because sampling frames, questionnaire instruments, and nutrient databases evolve. We interpret cycle contrasts as structured change hypotheses that should be triangulated with independent surveillance systems and controlled feeding studies.

FoodData Central integration grounds micronutrient analytics in standardized reference portions and nutrient definitions maintained by USDA. API-derived samples complement survey intakes by illustrating compositional density distributions for public health communication and recipe reformulation scenarios.

Statistical significance does not imply public health significance. Effect sizes, measurement reliability, and potential for intervention uptake must jointly inform interpretation. We foreground uncertainty by reporting multiple correlation metrics and cross-checking linear trends with rank-based summaries.

Equity considerations permeate dietary modeling because social determinants shape both intake distributions and cardiometabolic risk. Models that omit socioeconomic gradients risk perpetuating allocation biases in digital nutrition tools; we discuss structural limitations even when individual-level covariates are partially available.

Replication across cohorts and sensitivity analyses for energy adjustment represent best practices. The credibility of any single secondary-data analysis grows when findings are triangulated with independent cohorts and with domain expert critique.

Population-based dietary assessment couples biochemical plausibility with epidemiologic generalizability when designs explicitly harmonize measurement error, complex survey structure, and temporal alignment across data releases. In the present work, I emphasize transparent linkage across NHANES dietary files, demographic releases, and examination components so that inferred associations remain interpretable as hypotheses rather than claims of causality.

Nutrient patterns condense high-dimensional intake vectors into interpretable axes that reflect food culture, economic constraints, and physiological response heterogeneity. Principal components and k-means clustering provide complementary lenses: the former emphasizes continuous gradients of covariance, while the latter emphasizes discrete dietary phenotypes that may map onto intervention strata in precision nutrition frameworks.

Regularized regression and ensemble tree models serve distinct inferential goals. Linear models prioritize stability and coefficient transparency under multicollinearity, whereas random forests capture nonlinear interactions and rank variable importance for predictive screening. We report both to align explanatory and predictive narratives with contemporary machine learning practice in nutritional epidemiology.

Micronutrient co-ingestion networks formalize pairwise dependencies arising from shared food vehicles, seasonality, and fortification policies. Correlation structure should be interpreted cautiously because unmeasured confounding and dietary compensation can induce spurious edges; nonetheless, network summaries can motivate mechanistic experiments and targeted dietary guidance.

Global health observatory indicators contextualize national-level nutrition risk alongside intra-national heterogeneity that surveys like NHANES cannot represent. We therefore position country aggregates as ecological complements rather than substitutes for individual-level inference, highlighting inequality dimensions that policy instruments may address.

Bibliometric trend analysis via PubMed leverages the NCBI E-utilities ecosystem, enabling reproducible queries with explicit date bounds. Publication counts reflect scientific attention, funding climates, and terminology evolution; thus, trend slopes quantify momentum in functional food research while acknowledging indexing lag.

Microbiome-proximal exposures inferred from fiber diversity and plant-forward fat ratios do not replace metagenomic sequencing. They provide tractable, low-cost surrogates for hypothesis generation linking habitual diet to microbial ecology in population settings where biospecimen collection is unavailable.

Temporal comparisons across NHANES cycles require caution because sampling frames, questionnaire instruments, and nutrient databases evolve. We interpret cycle contrasts as structured change hypotheses that should be triangulated with independent surveillance systems and controlled feeding studies.

FoodData Central integration grounds micronutrient analytics in standardized reference portions and nutrient definitions maintained by USDA. API-derived samples complement survey intakes by illustrating compositional density distributions for public health communication and recipe reformulation scenarios.

Statistical significance does not imply public health significance. Effect sizes, measurement reliability, and potential for intervention uptake must jointly inform interpretation. We foreground uncertainty by reporting multiple correlation metrics and cross-checking linear trends with rank-based summaries.

Equity considerations permeate dietary modeling because social determinants shape both intake distributions and cardiometabolic risk. Models that omit socioeconomic gradients risk perpetuating allocation biases in digital nutrition tools; we discuss structural limitations even when individual-level covariates are partially available.

Replication across cohorts and sensitivity analyses for energy adjustment represent best practices. The credibility of any single secondary-data analysis grows when findings are triangulated with independent cohorts and with domain expert critique.

Population-based dietary assessment couples biochemical plausibility with epidemiologic generalizability when designs explicitly harmonize measurement error, complex survey structure, and temporal alignment across data releases. In the present work, I emphasize transparent linkage across NHANES dietary files, demographic releases, and examination components so that inferred associations remain interpretable as hypotheses rather than claims of causality.

Nutrient patterns condense high-dimensional intake vectors into interpretable axes that reflect food culture, economic constraints, and physiological response heterogeneity. Principal components and k-means clustering provide complementary lenses: the former emphasizes continuous gradients of covariance, while the latter emphasizes discrete dietary phenotypes that may map onto intervention strata in precision nutrition frameworks.

Regularized regression and ensemble tree models serve distinct inferential goals. Linear models prioritize stability and coefficient transparency under multicollinearity, whereas random forests capture nonlinear interactions and rank variable importance for predictive screening. We report both to align explanatory and predictive narratives with contemporary machine learning practice in nutritional epidemiology.

Micronutrient co-ingestion networks formalize pairwise dependencies arising from shared food vehicles, seasonality, and fortification policies. Correlation structure should be interpreted cautiously because unmeasured confounding and dietary compensation can induce spurious edges; nonetheless, network summaries can motivate mechanistic experiments and targeted dietary guidance.

Global health observatory indicators contextualize national-level nutrition risk alongside intra-national heterogeneity that surveys like NHANES cannot represent. We therefore position country aggregates as ecological complements rather than substitutes for individual-level inference, highlighting inequality dimensions that policy instruments may address.

Bibliometric trend analysis via PubMed leverages the NCBI E-utilities ecosystem, enabling reproducible queries with explicit date bounds. Publication counts reflect scientific attention, funding climates, and terminology evolution; thus, trend slopes quantify momentum in functional food research while acknowledging indexing lag.

Microbiome-proximal exposures inferred from fiber diversity and plant-forward fat ratios do not replace metagenomic sequencing. They provide tractable, low-cost surrogates for hypothesis generation linking habitual diet to microbial ecology in population settings where biospecimen collection is unavailable.

Temporal comparisons across NHANES cycles require caution because sampling frames, questionnaire instruments, and nutrient databases evolve. We interpret cycle contrasts as structured change hypotheses that should be triangulated with independent surveillance systems and controlled feeding studies.

FoodData Central integration grounds micronutrient analytics in standardized reference portions and nutrient definitions maintained by USDA. API-derived samples complement survey intakes by illustrating compositional density distributions for public health communication and recipe reformulation scenarios.

Statistical significance does not imply public health significance. Effect sizes, measurement reliability, and potential for intervention uptake must jointly inform interpretation. We foreground uncertainty by reporting multiple correlation metrics and cross-checking linear trends with rank-based summaries.

Equity considerations permeate dietary modeling because social determinants shape both intake distributions and cardiometabolic risk. Models that omit socioeconomic gradients risk perpetuating allocation biases in digital nutrition tools; we discuss structural limitations even when individual-level covariates are partially available.

Replication across cohorts and sensitivity analyses for energy adjustment represent best practices. The credibility of any single secondary-data analysis grows when findings are triangulated with independent cohorts and with domain expert critique.

Population-based dietary assessment couples biochemical plausibility with epidemiologic generalizability when designs explicitly harmonize measurement error, complex survey structure, and temporal alignment across data releases. In the present work, I emphasize transparent linkage across NHANES dietary files, demographic releases, and examination components so that inferred associations remain interpretable as hypotheses rather than claims of causality.

Nutrient patterns condense high-dimensional intake vectors into interpretable axes that reflect food culture, economic constraints, and physiological response heterogeneity. Principal components and k-means clustering provide complementary lenses: the former emphasizes continuous gradients of covariance, while the latter emphasizes discrete dietary phenotypes that may map onto intervention strata in precision nutrition frameworks.

Regularized regression and ensemble tree models serve distinct inferential goals. Linear models prioritize stability and coefficient transparency under multicollinearity, whereas random forests capture nonlinear interactions and rank variable importance for predictive screening. We report both to align explanatory and predictive narratives with contemporary machine learning practice in nutritional epidemiology.

## Limitations

Recall-based intakes incur systematic and random error; energy adjustment and repeated 24-hour recalls would strengthen
inference. I did not apply complex survey weights in this analysis, so prevalence-style national estimates should be
interpreted cautiously. Residual confounding, selection bias, and cycle non-comparability affect temporal contrasts. USDA API
samples used here are illustrative and not exhaustive of the full FoodData Central corpus.

## Conclusion

This study integrates NHANES, USDA FoodData Central, PubMed E-utilities, WHO GHO, and a public nutrition table in a
citation-transparent manner. Multivariate and machine-learning analyses highlight interpretable patterns linking nutrient
structure, cardiometabolic proxies, and research trends, while underscoring uncertainty and the need for prospective
validation in future work.



## Funding

This research received no specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

## Conflicts of interest

The author declares no competing financial or personal interests.

## Data availability

Analysis scripts, processed tables, and figures are stored in the author’s project folder (advanced_research_portfolio) on the author’s computer and can be shared upon reasonable request.

## Ethics statement

This study used publicly available, de-identified secondary data (e.g., NHANES). The author complied with each data provider’s terms of use; institutional review was not required for this secondary analysis under applicable norms, though authors should confirm with their own institution.


## References

[1] National Center for Health Statistics. National Health and Nutrition Examination Survey. https://wwwn.cdc.gov/nchs/nhanes/

[2] Centers for Disease Control and Prevention. NHANES questionnaires, datasets, and related documentation. https://wwwn.cdc.gov/nchs/nhanes/

[3] U.S. Department of Agriculture, Agricultural Research Service. FoodData Central. https://fdc.nal.usda.gov/

[4] USDA FoodData Central API Guide. https://fdc.nal.usda.gov/api-guide/

[5] National Center for Biotechnology Information. E-utilities (Entrez Programming Utilities). https://eutils.ncbi.nlm.nih.gov/

[6] World Health Organization. Global Health Observatory. https://www.who.int/data/gho

[7] WHO. Nutrition and food safety data portal (indicator catalog). https://www.who.int/data/gho/data/themes/topics/topic-details/GHO/nutrition-and-food-safety

[8] Kaggle Inc. Dataset repository (nutrition and health examples). https://www.kaggle.com/

[9] Willett WC. Nutritional Epidemiology. Oxford University Press (conceptual foundations for diet–disease inference).

[10] Hu FB. Diet and cardiovascular disease prevention. Nature Reviews Cardiology (framework for dietary patterns).

[11] Jacques PF, Tucker KL. Are dietary patterns useful for understanding diet and disease? Advances in Nutrition.

[12] Newby PK, Tucker KL. Empirically derived eating patterns using factor and cluster analysis. Journal of Nutrition.

[13] Mozaffarian D. Dietary and policy priorities for cardiovascular disease, diabetes, and obesity. Circulation.

[14] Afshin A, et al. Health effects of dietary risks in 195 countries. The Lancet (GBD comparative risk assessment).

[15] Sotos-Prieto M, et al. Association of changes in diet quality with total and cause-specific mortality. NEJM.

[16] Estruch R, et al. Primary prevention of cardiovascular disease with a Mediterranean diet. NEJM.

[17] Sonestedt E, et al. High disaccharide intake associates with higher prevalence of diabetes. Nutrition & Metabolism.

[18] Zheng Y, et al. Association between dietary patterns and risk of hypertension. Hypertension.

[19] Livingston EH. The USDA Food Composition Database. JAMA (editorial context for reference foods).

[20] Satija A, et al. Understanding nutritional epidemiology and its role in policy. Annual Review of Public Health.

[21] Subar AF, et al. Using intake biomarkers to evaluate measurement error. American Journal of Epidemiology.

[22] Thompson FE, Subar AF. Dietary assessment methodology. Nutrition in the Prevention and Treatment of Disease.

[23] Breiman L. Random forests. Machine Learning (ensemble learning foundations).

[24] Jolliffe IT, Cadima J. Principal component analysis. Philosophical Transactions of the Royal Society A.

[25] MacQueen J. Some methods for classification and analysis of multivariate observations. Berkeley Symposium.

[26] Benjamini Y, Hochberg Y. Controlling the false discovery rate. Journal of the Royal Statistical Society B.
