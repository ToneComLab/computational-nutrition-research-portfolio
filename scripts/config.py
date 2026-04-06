"""Paths and constants for reproducible research portfolio."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
PAPERS = ROOT / "papers"
LOGS = ROOT / "logs"

for p in (DATA, RESULTS, FIGURES, PAPERS, LOGS):
    p.mkdir(parents=True, exist_ok=True)

# Public data URLs (explicitly cited in papers)
NHANES_BASE = "https://wwwn.cdc.gov/nchs/nhanes/"
# Current CDC public file layout (DataFiles under Nchs/Data/Nhanes/Public/<year>/)
NHANES_2017 = {
    "DR1TOT": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/DR1TOT_J.xpt",
    "DEMO": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/DEMO_J.xpt",
    "BMX": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/BMX_J.xpt",
    "BPX": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/BPX_J.xpt",
}
NHANES_2011 = {
    "DR1TOT": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2011/DataFiles/DR1TOT_G.xpt",
    "DEMO": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2011/DataFiles/DEMO_G.xpt",
    "BMX": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2011/DataFiles/BMX_G.xpt",
    "BPX": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2011/DataFiles/BPX_G.xpt",
}

USDA_FDC_HOME = "https://fdc.nal.usda.gov/"
USDA_FDC_API = "https://api.nal.usda.gov/fdc/v1/"
# Public demo key pattern (USDA allows limited demo usage; fallback to cached CSV if rate-limited)
USDA_API_KEY = "DEMO_KEY"

PUBMED_EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

WHO_GHO = "https://www.who.int/data/gho"
WHO_GHO_API = "https://ghoapi.azureedge.net/api/"

# Open nutrition table (Kaggle-style public alternative; mirrors common nutrition ML tasks)
KAGGLE_PROXY_NUTRITION = (
    "https://raw.githubusercontent.com/selva86/datasets/master/nutrition.csv"
)

FIG_DPI = 300

PAPERS_META = [
    {
        "id": 1,
        "slug": "nutrient_pattern_metabolic_risk",
        "title": "Integrative Nutrient Pattern Clustering and Multivariate Metabolic Risk Stratification in U.S. Adults: Evidence from NHANES 2017–2018",
    },
    {
        "id": 2,
        "slug": "ai_dietary_personalization",
        "title": "Convex Surrogate Modeling for AI-Driven Dietary Personalization: Energy–Macronutrient Response Surfaces Calibrated with National Survey and Composition Data",
    },
    {
        "id": 3,
        "slug": "functional_compounds_disease",
        "title": "Linking USDA FoodData Central Micronutrient Density to Cardiometabolic Proxies: A Cross-Sectional Compound–Outcome Correlation Framework",
    },
    {
        "id": 4,
        "slug": "global_nutrition_inequality",
        "title": "Global Nutrition Inequality and Socioeconomic Gradients in Diet Adequacy: A WHO Global Health Observatory Harmonization Study",
    },
    {
        "id": 5,
        "slug": "microbiome_proxy_diet",
        "title": "Dietary Fiber Diversity and Plant-Forward Indices as Microbiome-Proximal Exposures: Inferential Modeling from 24-Hour Recall Data",
    },
    {
        "id": 6,
        "slug": "nutrient_interaction_network",
        "title": "Nutrient Co-Ingestion Topology and Interaction Networks: From Pairwise Correlations to Community Structure in Population Diets",
    },
    {
        "id": 7,
        "slug": "chronic_disease_diet_prediction",
        "title": "Predictive Modeling of Elevated Blood Pressure and Adiposity from Dietary Composition: Regularized Regression on NHANES-Linked Phenotypes",
    },
    {
        "id": 8,
        "slug": "dimensionality_reduction_nutrition",
        "title": "Principal Nutrition Manifolds: PCA-Based Dimensionality Reduction of 24-Hour Nutrient Intakes with Interpretable Loading Structures",
    },
    {
        "id": 9,
        "slug": "temporal_dietary_trends",
        "title": "Temporal Dietary Trend Analysis Across NHANES Cycles (2011–2012 vs. 2017–2018): Shift Detection in Energy, Sugar, and Sodium Intakes",
    },
    {
        "id": 10,
        "slug": "functional_food_pubmed_meta",
        "title": "Bibliometric Meta-Analysis of Functional Food and Bioactive Compound Research Trends: PubMed Corpus Mining with Structured Time-Series Inference",
    },
]
