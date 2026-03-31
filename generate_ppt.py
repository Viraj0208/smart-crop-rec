# -*- coding: utf-8 -*-
"""Generate the updated Smart Crop Advisory System PPT (Second Review)."""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
import os

# ── Colour palette (extracted from v3_final) ──────────────────────────
DARK_GREEN  = RGBColor(0x1B, 0x43, 0x32)   # #1B4332 – header bars, dark bg
MID_GREEN   = RGBColor(0x2D, 0x6A, 0x4F)   # #2D6A4F – accent shapes
LIGHT_GREEN = RGBColor(0x52, 0xB7, 0x88)   # #52B788 – decorative shapes
MINT        = RGBColor(0x95, 0xD5, 0xB2)   # #95D5B2 – subtitle, accents
WHITE       = RGBColor(0xFF, 0xFF, 0xFF)
OFF_WHITE   = RGBColor(0xF8, 0xF9, 0xF0)   # #F8F9F0 – slide bg
CARD_BG     = RGBColor(0xF3, 0xF4, 0xF6)   # #F3F4F6 – card backgrounds
DARK_TEXT   = RGBColor(0x1A, 0x1A, 0x2E)   # #1A1A2E – body text
RED_MUST    = RGBColor(0xDC, 0x26, 0x26)   # #DC2626 – must-have badge
ORANGE      = RGBColor(0xEA, 0x58, 0x0C)   # #EA580C – should-have badge
BLACK       = RGBColor(0x00, 0x00, 0x00)

# Slide dimensions (10" x 5.625")
SLIDE_W = Emu(9144000)
SLIDE_H = Emu(5143500)

prs = Presentation()
prs.slide_width = SLIDE_W
prs.slide_height = SLIDE_H

# Use blank layout
blank_layout = prs.slide_layouts[6]

# ── Utility functions ─────────────────────────────────────────────────
def set_bg(slide, color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_rect(slide, left, top, width, height, fill_color, line=False):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.fill.background()
    return shape

def add_circle(slide, left, top, size, fill_color):
    shape = slide.shapes.add_shape(MSO_SHAPE.OVAL, left, top, size, size)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.fill.background()
    return shape

def add_text_box(slide, left, top, width, height, text, font_size=14,
                 bold=False, color=DARK_TEXT, font_name="Calibri",
                 alignment=PP_ALIGN.LEFT, word_wrap=True):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = word_wrap
    p = tf.paragraphs[0]
    p.alignment = alignment
    run = p.add_run()
    run.text = text
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = font_name
    return txBox

def add_para(text_frame, text, font_size=12, bold=False, color=DARK_TEXT,
             font_name="Calibri", alignment=PP_ALIGN.LEFT, space_before=Pt(0)):
    p = text_frame.add_paragraph()
    p.alignment = alignment
    p.space_before = space_before
    run = p.add_run()
    run.text = text
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = font_name
    return p

def add_header_bar(slide, title_text):
    """Standard green header bar with white title text."""
    add_rect(slide, Emu(0), Emu(0), SLIDE_W, Emu(685800), DARK_GREEN)
    add_text_box(slide, Emu(365760), Emu(0), Emu(8229600), Emu(685800),
                 title_text, font_size=22, bold=True, color=WHITE,
                 font_name="Trebuchet MS", alignment=PP_ALIGN.LEFT)

def set_cell(cell, text, font_size=9, bold=False, color=DARK_TEXT,
             font_name="Calibri", alignment=PP_ALIGN.LEFT):
    cell.text = ""
    p = cell.text_frame.paragraphs[0]
    p.alignment = alignment
    run = p.add_run()
    run.text = text
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = font_name

def set_cell_fill(cell, color):
    tcPr = cell._tc.get_or_add_tcPr()
    solidFill = tcPr.makeelement(qn('a:solidFill'), {})
    srgbClr = solidFill.makeelement(qn('a:srgbClr'), {'val': '%02X%02X%02X' % (color[0], color[1], color[2])})
    solidFill.append(srgbClr)
    tcPr.append(solidFill)


# ═══════════════════════════════════════════════════════════════════════
# SLIDE 1 — Title
# ═══════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(blank_layout)
set_bg(slide, DARK_GREEN)

# Decorative elements
add_rect(slide, Emu(0), Emu(0), Emu(164592), SLIDE_H, LIGHT_GREEN)
add_circle(slide, Emu(6583680), Emu(-731520), Emu(3200400), MID_GREEN)
add_circle(slide, Emu(7315200), Emu(2926080), Emu(2011680), LIGHT_GREEN)

# Badge
add_rect(slide, Emu(457200), Emu(502920), Emu(3200000), Emu(347472), LIGHT_GREEN)
add_text_box(slide, Emu(457200), Emu(502920), Emu(3200000), Emu(347472),
             "SECOND REVIEW \u2014 MINOR PROJECT", font_size=8.5, bold=True,
             color=WHITE, alignment=PP_ALIGN.CENTER)

# Title
add_text_box(slide, Emu(457200), Emu(809244), Emu(7772400), Emu(777240),
             "CropIQ", font_size=48, bold=False, color=WHITE,
             font_name="Calibri")

# Subtitle
add_text_box(slide, Emu(457200), Emu(1691640), Emu(7772400), Emu(777240),
             "Smart Crop Advisory System", font_size=40, bold=False,
             color=WHITE, font_name="Calibri")

# Tagline
add_text_box(slide, Emu(457200), Emu(2578608), Emu(6858000), Emu(457200),
             "An ML-powered, region-aware agricultural advisory tool for Indian farmers \u2014 51 crops, 35 states, 96% F1",
             font_size=14, bold=False, color=MINT, font_name="Calibri")

# Divider
add_rect(slide, Emu(457200), Emu(3127248), Emu(4114800), Emu(36576), LIGHT_GREEN)

# Names
add_text_box(slide, Emu(457200), Emu(3310128), Emu(8229600), Emu(274320),
             "Viraj Balakrishnan  |  RA2311026010035", font_size=12, bold=False,
             color=WHITE, font_name="Calibri")
add_text_box(slide, Emu(457200), Emu(3630168), Emu(8229600), Emu(274320),
             "Devyansh Somvanshi  |  RA2311026010219", font_size=12, bold=False,
             color=WHITE, font_name="Calibri")

# Guide
txBox = slide.shapes.add_textbox(Emu(457200), Emu(3950208), Emu(8229600), Emu(274320))
tf = txBox.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
r1 = p.add_run()
r1.text = "Guide: "
r1.font.size = Pt(12)
r1.font.color.rgb = MINT
r1.font.name = "Calibri"
r2 = p.add_run()
r2.text = "Dr. P. Vaidehi Nayantara (Assistant Professor-CINTEL Department)"
r2.font.size = Pt(12)
r2.font.bold = True
r2.font.color.rgb = MINT
r2.font.name = "Calibri"
r3 = p.add_run()
r3.text = "  |  CSE (AI & ML), Sem VI  |  SRMIST"
r3.font.size = Pt(12)
r3.font.color.rgb = MINT
r3.font.name = "Calibri"


# ═══════════════════════════════════════════════════════════════════════
# SLIDE 2 — Abstract
# ═══════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(blank_layout)
set_bg(slide, OFF_WHITE)
add_header_bar(slide, "ABSTRACT")

# White card
add_rect(slide, Emu(274320), Emu(804672), Emu(8595360), Emu(4206240), WHITE)
add_rect(slide, Emu(274320), Emu(804672), Emu(109728), Emu(4206240), LIGHT_GREEN)

abstract_text = (
    "Agriculture forms the backbone of India\u2019s economy, sustaining over 60% of its rural population. "
    "Despite this, traditional crop selection remains rooted in generational intuition, leading to suboptimal "
    "yields, resource misallocation, and economic losses for smallholder farmers.\n\n"
    "This project presents CropIQ \u2014 a Smart Crop Advisory System powered by machine learning. The system "
    "accepts a farmer\u2019s State, District, and Land Size (in bigha) and automatically infers 7 soil and climate "
    "parameters (N, P, K, temperature, humidity, pH, rainfall) from a 7-zone agro-climatic mapping covering all "
    "35 Indian states and UTs. It then recommends the Top 5 most suitable crops, each accompanied by: ML suitability "
    "confidence (%), estimated production (kg), current market price (\u20b9/kg), composite risk score (0\u2013100), "
    "disease and pest warnings with prevention measures, and soil-specific growing tips.\n\n"
    "The ML pipeline compares 6 classifiers \u2014 SVM, Extra Trees, Random Forest, KNN, Logistic Regression, and "
    "Decision Tree \u2014 via GridSearchCV with 5-fold stratified CV (F1-macro scoring). The training dataset is expanded "
    "from 22 Kaggle crops to 51 crops (~5,310 rows) using agronomically validated synthetic data from ICAR/FAO parameters. "
    "SVM (RBF kernel) is selected as the best model with 95.98% test F1-macro. A disease knowledge base of 120+ entries "
    "(sourced from ICAR and NIPHM) powers the risk engine, while a 4-tier regional fallback (district \u2192 state \u2192 "
    "national \u2192 embedded defaults) ensures data availability for every location."
)

add_text_box(slide, Emu(502920), Emu(914400), Emu(8200000), Emu(3950208),
             abstract_text, font_size=10.5, bold=False, color=DARK_TEXT,
             font_name="Calibri")


# ═══════════════════════════════════════════════════════════════════════
# SLIDE 3 — Problem Statement
# ═══════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(blank_layout)
set_bg(slide, WHITE)
add_rect(slide, Emu(0), Emu(0), SLIDE_W, Emu(685800), MID_GREEN)
add_text_box(slide, Emu(365760), Emu(0), Emu(8229600), Emu(685800),
             "PROBLEM STATEMENT", font_size=22, bold=True, color=WHITE,
             font_name="Trebuchet MS")

problems = [
    ("Wrong Crop Selection",
     "Farmers choose crops based on tradition, not data \u2014 leading to low yields, soil degradation, and economic losses across 140M+ Indian farm households."),
    ("No Soil Testing Access",
     "Rural farmers cannot measure N, P, K, pH or climate values. Existing ML systems require exact lab inputs \u2014 unusable in the field."),
    ("Region Blindness",
     "Most ML systems use a single global model. Crop suitability in Kerala\u2019s coast is completely different from Rajasthan\u2019s arid plains \u2014 yet systems ignore this."),
    ("No Risk or Disease Info",
     "Farmers receive a crop label with no disease warnings, pest risks, or prevention measures \u2014 leaving them unprepared for the growing season."),
]

for idx, (title, desc) in enumerate(problems):
    col = idx % 2
    row = idx // 2
    left = Emu(274320 + col * 4480560)
    top = Emu(868680 + row * 1966080)

    # Card bg
    add_rect(slide, left, top, Emu(4206240), Emu(1737360), CARD_BG)
    # Card header
    add_rect(slide, left, top, Emu(4206240), Emu(384048), DARK_GREEN)
    # Title
    add_text_box(slide, Emu(left + 137160), top, Emu(3931920), Emu(384048),
                 title, font_size=12, bold=True, color=WHITE, font_name="Trebuchet MS")
    # Description
    add_text_box(slide, Emu(left + 137160), Emu(top + 457200), Emu(3931920), Emu(1188720),
                 desc, font_size=11, bold=False, color=DARK_TEXT, font_name="Calibri")

# Solution bar
add_rect(slide, Emu(0), Emu(4572000), SLIDE_W, Emu(571500), MINT)
add_text_box(slide, Emu(274320), Emu(4572000), Emu(8595360), Emu(571500),
             "Our Solution: State + District + Land Size (bigha) \u2192 Top 5 crops ranked by ML confidence with risk, disease info, profit estimates & explainability. No soil testing needed.",
             font_size=11, bold=True, color=DARK_GREEN, font_name="Calibri",
             alignment=PP_ALIGN.CENTER)


# ═══════════════════════════════════════════════════════════════════════
# SLIDE 4 — Research Objectives (Epics)
# ═══════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(blank_layout)
set_bg(slide, OFF_WHITE)
add_header_bar(slide, "RESEARCH OBJECTIVES (EPICS)")

epics = [
    ("E1", "Must Have", "Data Pipeline & Synthetic Expansion",
     "Load 2,200-row Kaggle CSV + generate synthetic data for 29 additional crops using ICAR/FAO agronomic ranges. Total: 51 crops, ~5,310 rows. EDA plots saved to reports/figures/."),
    ("E2", "Must Have", "ML Training & Selection (6 Models)",
     "Train SVM, Extra Trees, RF, KNN, LR, DT via GridSearchCV (5-fold, F1-macro). Auto-select best. SVM = 95.98% F1, Extra Trees = 95.96%, RF = 95.41%."),
    ("E3", "Must Have", "Region-Aware Advisory Engine",
     "7 agro-climatic zones mapped to all 35 states/UTs. 4-tier fallback (district\u2192state\u2192national\u2192defaults) for yield, price, cost. SHA-256 deterministic per-district offsets."),
    ("E4", "Must Have", "Risk & Disease Intelligence",
     "Disease knowledge base: 51 crops \u00d7 120+ entries from ICAR/NIPHM. Composite risk = 0.5 \u00d7 climate + 0.5 \u00d7 disease severity. Prevention tips per crop."),
    ("E5", "Should Have", "Explainability & Soil Health",
     "Permutation importance + optional SHAP per prediction. Threshold-based soil health warnings with crop-specific fertiliser suggestions."),
    ("E6", "Should Have", "Streamlit Web UI + Landing Page",
     "State/District/Bigha inputs \u2192 Top 5 crop cards with economics, risk, disease, soil tips, CSV download. Next.js 14 landing page with video hero."),
]

for idx, (eid, priority, title, desc) in enumerate(epics):
    col = idx % 2
    row = idx // 2
    left = Emu(274320 + col * 4389120)
    top = Emu(804672 + row * 1463040)

    # Card
    add_rect(slide, left, top, Emu(4206240), Emu(1371600), WHITE)
    # Number circle
    add_rect(slide, left, top, Emu(320040), Emu(320040), DARK_GREEN)
    add_text_box(slide, left, top, Emu(320040), Emu(320040),
                 eid, font_size=10, bold=True, color=WHITE,
                 alignment=PP_ALIGN.CENTER)
    # Priority badge
    badge_color = RED_MUST if priority == "Must Have" else ORANGE
    add_rect(slide, Emu(left + 350000), top, Emu(731520), Emu(274320), badge_color)
    add_text_box(slide, Emu(left + 350000), top, Emu(731520), Emu(274320),
                 priority, font_size=8, bold=True, color=WHITE,
                 alignment=PP_ALIGN.CENTER)
    # Title
    add_text_box(slide, Emu(left + 91440), Emu(top + 320040), Emu(4023360), Emu(274320),
                 title, font_size=11, bold=True, color=DARK_GREEN, font_name="Trebuchet MS")
    # Description
    add_text_box(slide, Emu(left + 91440), Emu(top + 594360), Emu(4023360), Emu(731520),
                 desc, font_size=9, bold=False, color=DARK_TEXT, font_name="Calibri")


# ═══════════════════════════════════════════════════════════════════════
# SLIDE 5 — Literature Survey (Papers 1-8)
# ═══════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(blank_layout)
set_bg(slide, WHITE)
add_header_bar(slide, "LITERATURE SURVEY \u2014 Papers 1 to 8")

papers_1 = [
    ["#", "Paper / Journal", "Methodology", "Gap / Limitation", "Result"],
    ["1", "Apat et al. \u2014 J. Sci. & Ind. Research", "SMOTE balancing + CatBoost, GNB on labeled agricultural dataset", "Limited to one dataset; no real-time IoT integration", "CatBoost ~99.5%, F-measure 0.9916"],
    ["2", "Aarthi et al. \u2014 Madras Agricultural Journal", "Multiple ML models (LR, DT, KNN, SVM, RF, XGBoost) + Flask web app", "Limited geographic validation; research prototype, not field-tested", "Random Forest highest at 98.2% accuracy"],
    ["3", "Sardeshmukh & Patil \u2014 Int. Research Journal", "Supervised ML + NLP for advisory; soil properties + crop price data", "No long-term field validation; market pricing integration is basic", "RF outperformed DT and KNN (context-aware)"],
    ["4", "Bouni et al. \u2014 Information, MDPI, 2024", "Extensive IoT data (soil + environment) to train ML for crop prediction", "Needs diverse environmental factors; adoption challenges in farms", "LightGBM ~98.90%, RF ~99.31% accuracy"],
    ["5", "Prity \u2014 Springer ML for Agriculture, 2024", "Compares LR, SVM, KNN, RF, boosting on historical climate & soil data", "Risk of overfitting; lacks IoT real-time data input methods", "RF and boosting show strong performance"],
    ["6", "Bakr \u2014 Information, MDPI, 2025", "Diverse ML and DL methods applied to crop datasets", "Deep learning requires extensive tuning and large datasets", "NB and XGBoost up to ~99.55% accuracy"],
    ["7", "Shastri et al. \u2014 Scientific Reports, 2025", "Gradient Boosting on nutrient and environmental features", "Lacks deployment or edge computing validation", "Accuracy ~99.27%, Precision ~99.32%"],
    ["8", "Chunduri, Raj & Narendra \u2014 ResearchGate", "DT, SVM, KNN, NB classifiers for farmer crop selection", "Basic ML; needs robust testing on broader regions", "Improvements in classification accuracy"],
]

rows_count = len(papers_1)
cols_count = len(papers_1[0])
table_shape = slide.shapes.add_table(rows_count, cols_count,
    Emu(182880), Emu(804672), Emu(8778240), Emu(4206240))
table = table_shape.table

# Set column widths
col_widths = [Emu(274320), Emu(2011680), Emu(2743200), Emu(2194560), Emu(1554480)]
for i, w in enumerate(col_widths):
    table.columns[i].width = w

for row_idx, row_data in enumerate(papers_1):
    for col_idx, cell_text in enumerate(row_data):
        cell = table.cell(row_idx, col_idx)
        is_header = row_idx == 0
        set_cell(cell, cell_text,
                 font_size=8 if not is_header else 9,
                 bold=is_header,
                 color=WHITE if is_header else DARK_TEXT)
        if is_header:
            set_cell_fill(cell, (0x1B, 0x43, 0x32))


# ═══════════════════════════════════════════════════════════════════════
# SLIDE 6 — Literature Survey (Papers 9-16)
# ═══════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(blank_layout)
set_bg(slide, WHITE)
add_header_bar(slide, "LITERATURE SURVEY \u2014 Papers 9 to 16")

papers_2 = [
    ["#", "Paper / Journal", "Methodology", "Gap / Limitation", "Result"],
    ["9", "Mohapatra & Kale \u2014 ITEGAM-JETIA, 2024", "Compares KNN, ANN, RF, SVM on Indian dataset", "Dataset scope limited; needs climate time series", "RF ~99.22%, SVM ~97.85% accuracy"],
    ["10", "Sharafat \u2014 ScienceDirect, 2025", "Integrated IoT + ML with sensor data for real-time edge recommendation", "Edge device resource limits; deployment preliminary", "Promising practical metrics (ML on sensor data)"],
    ["11", "Kaul, Hill & Walthall \u2014 Agricultural Systems, 2005", "ANN on historical weather and soil data for yield prediction", "Requires large historical datasets; limited spatial generalization", "RMSE/MSE; improved over linear regression"],
    ["12", "Jeong et al. \u2014 PLOS ONE, 2016", "Random Forest on global climate, soil, satellite datasets", "Limited interpretability; high computational cost", "R\u00b2 and RMSE for yield prediction"],
    ["13", "Chlingaryan et al. \u2014 Computers & Electronics in Agri., 2018", "SVM, RF, regression for yield prediction with remote sensing", "Focuses on yield/nitrogen prediction, not crop recommendation", "Survey of precision agriculture ML methods"],
    ["14", "McCown \u2014 Agricultural Systems, 2002", "Reviews DSS for crop selection and farm management", "Conceptual; no modern AI or real-time IoT integration", "Qualitative system evaluation; adoption metrics"],
    ["15", "Pantazi et al. \u2014 Biosystems Engineering, 2017", "Hyperspectral data + ML classification for intelligent agriculture", "High hardware/imaging cost; limited rural scalability", "Classification accuracy >85%"],
    ["16", "Khaki & Wang \u2014 Frontiers in Plant Science, 2019", "Deep learning on weather + genotype for crop yield forecasting", "Requires high computational resources and large datasets", "RMSE, R\u00b2; improved over traditional ML"],
]

table_shape = slide.shapes.add_table(len(papers_2), cols_count,
    Emu(182880), Emu(804672), Emu(8778240), Emu(4206240))
table = table_shape.table
for i, w in enumerate(col_widths):
    table.columns[i].width = w

for row_idx, row_data in enumerate(papers_2):
    for col_idx, cell_text in enumerate(row_data):
        cell = table.cell(row_idx, col_idx)
        is_header = row_idx == 0
        set_cell(cell, cell_text,
                 font_size=8 if not is_header else 9,
                 bold=is_header,
                 color=WHITE if is_header else DARK_TEXT)
        if is_header:
            set_cell_fill(cell, (0x1B, 0x43, 0x32))


# ═══════════════════════════════════════════════════════════════════════
# SLIDE 7 — Research Gaps & How We Address Them
# ═══════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(blank_layout)
set_bg(slide, OFF_WHITE)
add_header_bar(slide, "RESEARCH GAPS & HOW WE ADDRESS THEM")

gaps = [
    ("\u274c  All 16 surveyed systems require manual N, P, K, pH entry",
     "\u2705  Region-first flow: State \u2192 District \u2192 Zone defaults. No soil testing needed."),
    ("\u274c  Systems limited to specific regions \u2014 no pan-India geographic coverage",
     "\u2705  7 agro-climatic zones mapped to all 35 Indian states and UTs."),
    ("\u274c  No risk, disease, or pest information in any surveyed paper",
     "\u2705  Disease knowledge base (51 crops, 120+ entries, ICAR/NIPHM) with prevention measures."),
    ("\u274c  No market pricing or profit estimation for farmer decisions",
     "\u2705  4-tier regional fallback gives yield, price (\u20b9/kg), cost, profit & ROI per crop."),
    ("\u274c  Black-box predictions \u2014 farmers cannot understand recommendations",
     "\u2705  Permutation importance + SHAP values + human-readable explanation text."),
    ("\u274c  No real-world Indian unit system (bigha, \u20b9/kg) or land-size filtering",
     "\u2705  Production in kg, land in bigha (state-specific), price in \u20b9/kg. Land-size crop filtering."),
]

for idx, (gap, solution) in enumerate(gaps):
    top = Emu(804672 + idx * 685800)
    # Gap (left)
    add_text_box(slide, Emu(274320), top, Emu(4114800), Emu(548640),
                 gap, font_size=10, bold=False, color=DARK_TEXT, font_name="Calibri")
    # Arrow
    add_text_box(slide, Emu(4389120), top, Emu(365760), Emu(548640),
                 "\u2192", font_size=16, bold=True, color=LIGHT_GREEN,
                 font_name="Calibri", alignment=PP_ALIGN.CENTER)
    # Solution (right)
    add_text_box(slide, Emu(4754880), top, Emu(4206240), Emu(548640),
                 solution, font_size=10, bold=False, color=DARK_GREEN, font_name="Calibri")


# ═══════════════════════════════════════════════════════════════════════
# SLIDE 8 — Proposed Methodology
# ═══════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(blank_layout)
set_bg(slide, OFF_WHITE)
add_header_bar(slide, "PROPOSED METHODOLOGY")

steps = [
    ("1", "Data Collection & Expansion",
     "Kaggle CSV (2,200 rows, 22 crops) + synthetic generation for 29 additional crops using ICAR/FAO agronomic ranges. Total: ~5,310 rows, 51 crops."),
    ("2", "EDA",
     "Feature distributions, class balance, correlation matrix, IQR outlier analysis across expanded dataset. Saved to reports/figures/."),
    ("3", "Preprocessing",
     "LabelEncoder + StandardScaler (fit on train only) + Stratified 80/20 split preserving 51 crop class proportions."),
    ("4", "Model Training (6 Models)",
     "GridSearchCV on DT, RF, Extra Trees, KNN, SVM, LR \u2014 5-fold stratified CV, F1-macro scoring. SVM wins at 95.98% F1."),
    ("5", "Evaluation",
     "Accuracy, F1-macro, Precision, Recall, Confusion Matrix, Learning Curves. All 6 models above 89%. Top 3 above 95%."),
    ("6", "Profit Engine",
     "effective_yield = regional \u00d7 (0.60 + 0.40 \u00d7 confidence); Profit = revenue \u2212 cost. 4-tier regional fallback across 35 states."),
    ("7", "Risk Engine",
     "Composite risk = 0.5 \u00d7 climate + 0.5 \u00d7 disease. Disease KB: 51 crops, 120+ entries from ICAR/NIPHM."),
    ("8", "Streamlit UI + Landing Page",
     "State/District/Bigha \u2192 Top 5 cards with economics, risk, disease, soil tips, CSV. Next.js 14 landing page with video hero."),
]

for idx, (num, title, desc) in enumerate(steps):
    col = idx % 2
    row = idx // 2
    left = Emu(274320 + col * 4389120)
    top_pos = Emu(804672 + row * 1097280)

    # Number circle
    add_rect(slide, left, top_pos, Emu(320040), Emu(320040), DARK_GREEN)
    add_text_box(slide, left, top_pos, Emu(320040), Emu(320040),
                 num, font_size=12, bold=True, color=WHITE, alignment=PP_ALIGN.CENTER)
    # Title
    add_text_box(slide, Emu(left + 365760), top_pos, Emu(3840480), Emu(274320),
                 title, font_size=11, bold=True, color=DARK_GREEN, font_name="Trebuchet MS")
    # Description
    add_text_box(slide, Emu(left + 365760), Emu(top_pos + 320040), Emu(3840480), Emu(731520),
                 desc, font_size=9, bold=False, color=DARK_TEXT, font_name="Calibri")


# ═══════════════════════════════════════════════════════════════════════
# SLIDE 9 — ML Models & Evaluation Strategy
# ═══════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(blank_layout)
set_bg(slide, OFF_WHITE)
add_header_bar(slide, "ML MODELS & EVALUATION STRATEGY")

# Feature importance (left side)
add_text_box(slide, Emu(274320), Emu(804672), Emu(4114800), Emu(365760),
             "Feature Importance (Permutation)", font_size=14, bold=True,
             color=DARK_GREEN, font_name="Trebuchet MS")

features = [
    ("Nitrogen (N)", "44%", 0.88),
    ("Rainfall", "36%", 0.72),
    ("Potassium (K)", "35%", 0.70),
    ("Humidity", "35%", 0.70),
    ("Temperature", "31%", 0.62),
    ("Phosphorus (P)", "24%", 0.48),
    ("pH", "10%", 0.20),
]

for idx, (name, pct, bar_frac) in enumerate(features):
    y = Emu(1188720 + idx * 457200)
    # Label
    add_text_box(slide, Emu(274320), y, Emu(1371600), Emu(320040),
                 name, font_size=10, bold=False, color=DARK_TEXT)
    # Bar
    bar_w = int(2560320 * bar_frac)
    add_rect(slide, Emu(1645920), Emu(y + 45720), Emu(bar_w), Emu(228600), LIGHT_GREEN)
    # Percentage
    add_text_box(slide, Emu(1645920 + bar_w + 91440), y, Emu(548640), Emu(320040),
                 pct, font_size=10, bold=True, color=DARK_GREEN)

# Right side: evaluation metrics
add_text_box(slide, Emu(4754880), Emu(804672), Emu(4206240), Emu(365760),
             "Model Comparison (Test F1-macro)", font_size=14, bold=True,
             color=DARK_GREEN, font_name="Trebuchet MS")

models = [
    ("SVM (RBF)", "95.98%", True),
    ("Extra Trees", "95.96%", False),
    ("Random Forest", "95.41%", False),
    ("KNN", "95.12%", False),
    ("Logistic Regression", "94.09%", False),
    ("Decision Tree", "89.37%", False),
]

for idx, (name, f1, is_best) in enumerate(models):
    y = Emu(1188720 + idx * 457200)
    color = DARK_GREEN if is_best else DARK_TEXT
    add_text_box(slide, Emu(4754880), y, Emu(2194560), Emu(320040),
                 name, font_size=10, bold=is_best, color=color)
    add_text_box(slide, Emu(7040880), y, Emu(1097280), Emu(320040),
                 f1, font_size=10, bold=is_best, color=color)
    if is_best:
        add_text_box(slide, Emu(8138160), y, Emu(822960), Emu(320040),
                     "\u2190 BEST", font_size=9, bold=True, color=LIGHT_GREEN)

# Footer note
add_text_box(slide, Emu(4754880), Emu(4389120), Emu(4206240), Emu(548640),
             "Selection: Best model by test F1-macro. Ties broken by lower CV std (stability). SVM wins on F1-macro; Extra Trees wins on stability.",
             font_size=9, bold=False, color=DARK_TEXT, font_name="Calibri")


# ═══════════════════════════════════════════════════════════════════════
# SLIDE 10 — Algorithms Used
# ═══════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(blank_layout)
set_bg(slide, OFF_WHITE)
add_header_bar(slide, "ALGORITHMS USED")

algos = [
    ("SVM (RBF)", "95.98%", True,
     "SVM finds the optimal hyperplane maximising the margin between classes. RBF kernel maps 7 features into higher-dimensional space to separate all 51 crop classes. Best on this scaled, balanced dataset."),
    ("Extra Trees", "95.96%", False,
     "Extremely Randomized Trees builds multiple trees with random split points (not best splits). Reduces variance further than RF. Provides lowest CV std (0.37%) \u2014 most stable model."),
    ("Random Forest", "95.41%", False,
     "Ensemble of decision trees, each on bootstrap samples with random feature subsets. Majority vote for predictions. Robust to overfitting; provides intrinsic feature importance."),
    ("KNN", "95.12%", False,
     "Classifies by finding K most similar training samples (Euclidean distance in scaled space) and taking majority vote. Non-parametric; no assumption about data distribution."),
    ("Logistic Regression", "94.09%", False,
     "Multi-class via One-vs-Rest with L2 regularisation. Linear decision boundary. Strong interpretable baseline; softmax probabilities feed directly into suitability confidence."),
    ("Decision Tree", "89.37%", False,
     "Partitions feature space using Gini impurity. Human-readable rules. Least accurate but provides full transparency and serves as interpretability baseline."),
]

for idx, (name, f1, is_best, desc) in enumerate(algos):
    col = idx % 2
    row = idx // 2
    left = Emu(182880 + col * 4480560)
    top_pos = Emu(804672 + row * 1463040)

    # Card
    card_h = Emu(1371600)
    add_rect(slide, left, top_pos, Emu(4297680), card_h, WHITE)

    # Header
    header_text = f"Best Model \u2014 F1: {f1}" if is_best else f"F1: {f1}"
    header_color = LIGHT_GREEN if is_best else CARD_BG
    add_rect(slide, left, top_pos, Emu(4297680), Emu(320040), header_color)
    add_text_box(slide, Emu(left + 91440), top_pos, Emu(4114800), Emu(320040),
                 header_text, font_size=10, bold=True,
                 color=DARK_GREEN if is_best else DARK_TEXT)

    # Name
    add_text_box(slide, Emu(left + 91440), Emu(top_pos + 365760), Emu(4114800), Emu(274320),
                 name, font_size=12, bold=True, color=DARK_GREEN, font_name="Trebuchet MS")

    # Description
    add_text_box(slide, Emu(left + 91440), Emu(top_pos + 640080), Emu(4114800), Emu(685800),
                 desc, font_size=8.5, bold=False, color=DARK_TEXT, font_name="Calibri")


# ═══════════════════════════════════════════════════════════════════════
# SLIDE 11 — System Architecture: Monolithic Layered
# ═══════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(blank_layout)
set_bg(slide, OFF_WHITE)
add_header_bar(slide, "SYSTEM ARCHITECTURE: MONOLITHIC LAYERED")

layers = [
    ("\U0001f5a5\ufe0f  PRESENTATION LAYER",
     "app.py (568 lines) \u2014 Streamlit Web UI  |  my-product-site/ \u2014 Next.js 14 Landing Page",
     "State/District dropdowns | Land size (bigha) | Top 5 crop cards | Risk badges | Disease info | CSV download"),
    ("\u2699\ufe0f  APPLICATION LAYER",
     "predictor.py (339) | explainer.py (157) | soil_health.py (117) | market_price_fetcher.py (253)",
     "ML inference \u2192 Profit \u2192 Risk \u2192 Explainability \u2192 Soil health \u2192 Rank top 5"),
    ("\U0001f9e0  DOMAIN / BUSINESS LAYER",
     "profit_engine.py (104) | risk_engine.py (587) | region_data_loader.py (560) | train.py (186) | crop_params.py",
     "Profit formula | Disease KB (51 crops, 120+ entries) | 4-tier fallback | GridSearchCV 6 models | Synthetic data gen"),
    ("\U0001f4be  DATA LAYER",
     "data_loader.py | preprocess.py | config.py (247) | zone_soil.py | models/ | data/raw/",
     "5,310-row dataset | StandardScaler | LabelEncoder | 35-state bigha map | 7 agro-climatic zones | model.joblib"),
]

for idx, (title, modules, desc) in enumerate(layers):
    top_pos = Emu(804672 + idx * 1005840)

    # Layer card
    add_rect(slide, Emu(274320), top_pos, Emu(8595360), Emu(868680), WHITE)
    add_rect(slide, Emu(274320), top_pos, Emu(109728), Emu(868680), LIGHT_GREEN)

    # Title
    add_text_box(slide, Emu(457200), top_pos, Emu(8229600), Emu(274320),
                 title, font_size=12, bold=True, color=DARK_GREEN, font_name="Trebuchet MS")
    # Modules
    add_text_box(slide, Emu(457200), Emu(top_pos + 274320), Emu(8229600), Emu(274320),
                 modules, font_size=9, bold=False, color=DARK_TEXT, font_name="Calibri")
    # Description
    add_text_box(slide, Emu(457200), Emu(top_pos + 548640), Emu(8229600), Emu(274320),
                 desc, font_size=9, bold=False, color=MID_GREEN, font_name="Calibri")

    # Arrow between layers
    if idx < len(layers) - 1:
        add_text_box(slide, Emu(4297680), Emu(top_pos + 868680), Emu(548640), Emu(137160),
                     "\u25bc", font_size=14, bold=True, color=LIGHT_GREEN,
                     alignment=PP_ALIGN.CENTER)

# Footer
add_text_box(slide, Emu(274320), Emu(4846320), Emu(8595360), Emu(274320),
             "Why Monolithic: 2-person team \u2713  Single deployment (streamlit run app.py) \u2713  In-process < 3s \u2713  No network overhead \u2713  14+ modular src/ files",
             font_size=9, bold=False, color=MID_GREEN, font_name="Calibri",
             alignment=PP_ALIGN.CENTER)


# ═══════════════════════════════════════════════════════════════════════
# SLIDE 12 — Architecture Diagram (IMAGE)
# ═══════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(blank_layout)
set_bg(slide, WHITE)
add_header_bar(slide, "ARCHITECTURE DIAGRAM")

arch_img = "D:/PROJECTS/smart-crop-rec/ARCHITECTURE_DIAGRAM.png"
if os.path.exists(arch_img):
    slide.shapes.add_picture(arch_img,
        Emu(274320), Emu(804672), Emu(8595360), Emu(3840480))

# Caption
add_text_box(slide, Emu(274320), Emu(4700000), Emu(8595360), Emu(400000),
             "The architecture shows the end-to-end flow: Farmer inputs (State, District, Land) \u2192 Streamlit App \u2192 Predictor Hub \u2192 "
             "Profit Engine + Risk Engine + Region Data (4-tier fallback) \u2192 Top 5 crops. Below: ML Training Pipeline "
             "(Ingest \u2192 Preprocess \u2192 Train 6 models \u2192 Evaluate \u2192 Save). Storage: CSVs, model artifacts, EDA figures.",
             font_size=9, bold=False, color=DARK_TEXT, font_name="Calibri",
             alignment=PP_ALIGN.CENTER)


# ═══════════════════════════════════════════════════════════════════════
# SLIDE 13 — Key Technical Innovations
# ═══════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(blank_layout)
set_bg(slide, OFF_WHITE)
add_header_bar(slide, "KEY TECHNICAL INNOVATIONS")

innovations = [
    ("Synthetic Data Expansion",
     "29 additional crops beyond Kaggle\u2019s 22, using truncated normal distributions within ICAR/FAO agronomic [min, max, mean, std] ranges. "
     "Total: 51 crops, ~5,310 balanced training rows. Each crop has validated parameter ranges from crop_params.py."),
    ("7 Agro-Climatic Zone Mapping",
     "All 35 Indian states/UTs mapped to 7 zones (arid_nw, eastern_humid, southern, west_coast, central, himalayan, western_dry). "
     "SHA-256 deterministic per-district offsets ensure unique but reproducible soil/climate defaults."),
    ("4-Tier Regional Fallback",
     "Data priority: district CSV \u2192 state CSV \u2192 national CSV \u2192 embedded CACP/NHB defaults. Confidence level reported "
     "alongside each recommendation. Ensures 100% data availability for every Indian location."),
    ("Composite Risk Scoring",
     "Risk = 0.5 \u00d7 climate vulnerability + 0.5 \u00d7 disease severity. Knowledge base: 51 crops \u00d7 120+ disease entries "
     "(Rice Blast at 45%, Fall Armyworm at 55%, etc.). Each with specific prevention measures from ICAR/NIPHM."),
    ("Land-Size Crop Filtering",
     "Crops requiring more space than available are excluded (e.g., sugarcane needs 2+ acres, pulses work on 0.1). "
     "State-specific bigha-to-acres conversions for all 35 states (Bihar = 0.20, Rajasthan = 0.62)."),
    ("Next.js 14 Landing Page",
     "Dark-themed marketing site with Framer Motion animations, full-screen video hero, 6-stat grid, "
     "feature cards, and a smart \u201cLaunch App\u201d button that checks Streamlit availability."),
]

for idx, (title, desc) in enumerate(innovations):
    col = idx % 2
    row = idx // 2
    left = Emu(274320 + col * 4389120)
    top_pos = Emu(804672 + row * 1463040)

    add_rect(slide, left, top_pos, Emu(4206240), Emu(1371600), WHITE)
    add_rect(slide, left, top_pos, Emu(4206240), Emu(45720), LIGHT_GREEN)
    add_text_box(slide, Emu(left + 91440), Emu(top_pos + 91440), Emu(4023360), Emu(274320),
                 title, font_size=11, bold=True, color=DARK_GREEN, font_name="Trebuchet MS")
    add_text_box(slide, Emu(left + 91440), Emu(top_pos + 411480), Emu(4023360), Emu(868680),
                 desc, font_size=8.5, bold=False, color=DARK_TEXT, font_name="Calibri")


# ═══════════════════════════════════════════════════════════════════════
# SLIDE 14 — Agile Approach: Sprints & Backlog
# ═══════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(blank_layout)
set_bg(slide, OFF_WHITE)
add_header_bar(slide, "AGILE APPROACH: SPRINTS & BACKLOG")

sprints = [
    ("Sprint 1", "Weeks 1\u20133", "DONE", LIGHT_GREEN,
     "Goal: Data Foundation & ML",
     [
         "Literature survey (16 papers)",
         "Dataset load, EDA, preprocessing",
         "Train 6 classifiers \u2014 SVM wins at 95.98%",
         "Synthetic data expansion: 22 \u2192 51 crops",
     ]),
    ("Sprint 2", "Weeks 4\u20136", "DONE", LIGHT_GREEN,
     "Goal: Region Engine & Risk",
     [
         "7 agro-climatic zone mapping (35 states/UTs)",
         "4-tier regional fallback + SHA-256 district offsets",
         "Disease KB (51 crops, 120+ entries, ICAR/NIPHM)",
         "Composite risk + profit engine + balanced ranking",
     ]),
    ("Sprint 3", "Weeks 7\u201310", "DONE", LIGHT_GREEN,
     "Goal: UI, Landing Page & Delivery",
     [
         "Streamlit UI: state/district dropdowns, crop cards",
         "Next.js 14 landing page with video hero",
         "Bug fixes (Chandigarh, district reset, theming)",
         "REPORT.md + ARCHITECTURE.md + README + GitHub",
     ]),
]

for idx, (name, weeks, status, status_color, goal, items) in enumerate(sprints):
    left = Emu(274320 + idx * 2926080)
    top_base = Emu(868680)
    card_w = Emu(2743200)

    # Card
    add_rect(slide, left, top_base, card_w, Emu(3931920), WHITE)

    # Sprint name
    add_text_box(slide, Emu(left + 91440), top_base, Emu(card_w - 182880), Emu(365760),
                 name, font_size=16, bold=True, color=DARK_GREEN, font_name="Trebuchet MS")
    # Weeks
    add_text_box(slide, Emu(left + 91440), Emu(top_base + 320040), Emu(card_w - 182880), Emu(274320),
                 weeks, font_size=10, bold=False, color=DARK_TEXT)
    # Goal
    add_text_box(slide, Emu(left + 91440), Emu(top_base + 594360), Emu(card_w - 182880), Emu(274320),
                 goal, font_size=10, bold=True, color=MID_GREEN)

    # Items
    for j, item in enumerate(items):
        add_text_box(slide, Emu(left + 91440), Emu(top_base + 914400 + j * 548640),
                     Emu(card_w - 182880), Emu(502920),
                     "\u2192  " + item, font_size=9, bold=False, color=DARK_TEXT)

    # Status badge
    add_rect(slide, Emu(left + 91440), Emu(top_base + 3474720), Emu(914400), Emu(320040), status_color)
    add_text_box(slide, Emu(left + 91440), Emu(top_base + 3474720), Emu(914400), Emu(320040),
                 status, font_size=10, bold=True, color=WHITE, alignment=PP_ALIGN.CENTER)


# ═══════════════════════════════════════════════════════════════════════
# SLIDE 15 — SDG Alignment & SRMIST Theme
# ═══════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(blank_layout)
set_bg(slide, OFF_WHITE)
add_header_bar(slide, "SDG ALIGNMENT & SRMIST THEME")

# SDG 2
add_rect(slide, Emu(274320), Emu(868680), Emu(4114800), Emu(3749040), WHITE)
add_rect(slide, Emu(274320), Emu(868680), Emu(4114800), Emu(365760), DARK_GREEN)
add_text_box(slide, Emu(411480), Emu(868680), Emu(3840480), Emu(365760),
             "\U0001f33e  SDG 2: ZERO HUNGER", font_size=14, bold=True, color=WHITE,
             font_name="Trebuchet MS")

sdg2_items = [
    "Recommends top 5 crops based on ML + regional intelligence across 51 crops",
    "Covers all 35 Indian states/UTs with 7 agro-climatic zone defaults",
    "Smallholder farmers get data-driven advice without soil testing",
    "Production estimates (kg) help plan harvest and food supply",
    "Reduces crop failure risk through 120+ disease/pest warnings",
    "Suitability ranking prioritises farmer success \u2192 food security",
]
for j, item in enumerate(sdg2_items):
    add_text_box(slide, Emu(411480), Emu(1325880 + j * 502920), Emu(3840480), Emu(457200),
                 "\u2192  " + item, font_size=9.5, bold=False, color=DARK_TEXT)

# SDG 12
add_rect(slide, Emu(4663440), Emu(868680), Emu(4206240), Emu(3749040), WHITE)
add_rect(slide, Emu(4663440), Emu(868680), Emu(4206240), Emu(365760), DARK_GREEN)
add_text_box(slide, Emu(4800600), Emu(868680), Emu(3931920), Emu(365760),
             "\u267b\ufe0f  SDG 12: RESPONSIBLE CONSUMPTION", font_size=14, bold=True, color=WHITE,
             font_name="Trebuchet MS")

sdg12_items = [
    "Disease info + risk scores prevent unnecessary pesticide use",
    "Soil health advisor targets fertiliser only where needed",
    "Matching crops to regional climate reduces water waste",
    "4-tier fallback avoids over-reliance on imported/assumed data",
    "Permutation importance ensures transparent, responsible AI",
    "CSV reports support informed, sustainable farm planning",
]
for j, item in enumerate(sdg12_items):
    add_text_box(slide, Emu(4800600), Emu(1325880 + j * 502920), Emu(3931920), Emu(457200),
                 "\u2192  " + item, font_size=9.5, bold=False, color=DARK_TEXT)


# ═══════════════════════════════════════════════════════════════════════
# SLIDE 16 — Project Timeline
# ═══════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(blank_layout)
set_bg(slide, OFF_WHITE)
add_header_bar(slide, "PROJECT TIMELINE")

timeline = [
    ("Week 1\u20132", "Literature review (16 papers), problem definition, dataset collection & validation", "Done"),
    ("Week 3", "EDA, preprocessing pipeline. Synthetic data expansion (22 \u2192 51 crops using ICAR/FAO ranges)", "Done"),
    ("Week 4", "Model training \u2014 6 classifiers via GridSearchCV. SVM selected at 95.98% F1-macro", "Done"),
    ("Week 5", "Model evaluation, learning curves. Region data loader (4-tier fallback, 35 states/UTs)", "Done"),
    ("Week 6", "Profit engine \u2014 effective_yield formula, state-specific bigha conversions, profit ranking", "Done"),
    ("Week 7", "Risk engine \u2014 disease KB (51 crops, 120+ entries), composite risk scoring", "Done"),
    ("Week 8", "Explainability (permutation importance + SHAP), soil health advisor, market price fetcher", "Done"),
    ("Week 9", "Streamlit UI \u2014 state/district/bigha inputs, 5 crop cards, CSV download. Bug fixes.", "Done"),
    ("Week 10", "Next.js 14 landing page, Streamlit re-theme, Chandigarh fix, README rewrite, final review", "Done"),
]

for idx, (week, desc, status) in enumerate(timeline):
    top_pos = Emu(804672 + idx * 457200)

    # Week label
    add_text_box(slide, Emu(274320), top_pos, Emu(1005840), Emu(411480),
                 week, font_size=10, bold=True, color=DARK_GREEN)
    # Description
    add_text_box(slide, Emu(1371600), top_pos, Emu(6583680), Emu(411480),
                 desc, font_size=9, bold=False, color=DARK_TEXT)
    # Status badge
    add_rect(slide, Emu(8046720), top_pos, Emu(822960), Emu(320040), LIGHT_GREEN)
    add_text_box(slide, Emu(8046720), top_pos, Emu(822960), Emu(320040),
                 status, font_size=9, bold=True, color=WHITE, alignment=PP_ALIGN.CENTER)


# ═══════════════════════════════════════════════════════════════════════
# SLIDE 17 — Future Directions & Conclusion
# ═══════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(blank_layout)
set_bg(slide, OFF_WHITE)
add_header_bar(slide, "FUTURE DIRECTIONS & CONCLUSION")

futures = [
    ("01", "\U0001f4ca", "District-Level Dataset Enrichment",
     "Source, clean, and integrate district-specific yield histories, micro-climate variability, soil type distributions, "
     "and seasonal crop patterns. This will improve the precision of regional predictions and enable truly hyperlocal "
     "recommendations beyond the current zone-based approach."),
    ("02", "\U0001f5a5\ufe0f", "Dual-Mode User Interface",
     "Simple Farmer View: minimal interface with top recommendation, production (kg), and key risk warnings for "
     "low-literacy users. Full Analytics Dashboard: all model outputs, profit comparisons, SHAP explainability, "
     "disease probability tables, and downloadable reports for agronomists and researchers."),
    ("03", "\U0001f9ea", "Algorithm Expansion & Deep Learning",
     "Systematically evaluate XGBoost, LightGBM, CatBoost, and ensemble stacking against the current SVM baseline "
     "using the same GridSearchCV and stratified k-fold protocol. Explore deep learning (ANN/CNN) on expanded datasets. "
     "The focus remains academic \u2014 rigorous algorithm comparison for the research contribution."),
]

for idx, (num, icon, title, desc) in enumerate(futures):
    top_pos = Emu(804672 + idx * 1371600)

    # Number
    add_text_box(slide, Emu(274320), top_pos, Emu(457200), Emu(365760),
                 num, font_size=24, bold=True, color=LIGHT_GREEN,
                 font_name="Trebuchet MS")
    # Icon
    add_text_box(slide, Emu(731520), top_pos, Emu(457200), Emu(365760),
                 icon, font_size=20, bold=False, color=DARK_GREEN)
    # Title
    add_text_box(slide, Emu(1188720), top_pos, Emu(7680960), Emu(365760),
                 title, font_size=14, bold=True, color=DARK_GREEN, font_name="Trebuchet MS")
    # Description
    add_text_box(slide, Emu(1188720), Emu(top_pos + 365760), Emu(7680960), Emu(960120),
                 desc, font_size=9.5, bold=False, color=DARK_TEXT, font_name="Calibri")

# Conclusion
add_rect(slide, Emu(274320), Emu(4480560), Emu(8595360), Emu(548640), DARK_GREEN)
add_text_box(slide, Emu(411480), Emu(4480560), Emu(8321040), Emu(548640),
             "Conclusion: CropIQ establishes a rigorous, research-grade ML pipeline for Indian agricultural advisory \u2014 "
             "51 crops, 35 states, 96% F1, 120+ disease entries, and a 4-tier regional fallback. "
             "Future work centres on data depth, UI accessibility, and algorithmic expansion.",
             font_size=10, bold=False, color=WHITE, font_name="Calibri")


# ═══════════════════════════════════════════════════════════════════════
# SLIDE 18 — Thank You
# ═══════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(blank_layout)
set_bg(slide, DARK_GREEN)

add_rect(slide, Emu(0), Emu(0), Emu(164592), SLIDE_H, LIGHT_GREEN)
add_circle(slide, Emu(6583680), Emu(-731520), Emu(3200400), MID_GREEN)
add_circle(slide, Emu(7315200), Emu(2926080), Emu(2011680), LIGHT_GREEN)

add_text_box(slide, Emu(457200), Emu(1280160), Emu(7772400), Emu(777240),
             "Thank You", font_size=48, bold=False, color=WHITE, font_name="Calibri",
             alignment=PP_ALIGN.LEFT)

add_text_box(slide, Emu(457200), Emu(2194560), Emu(7772400), Emu(548640),
             "CropIQ \u2014 Smart Crop Advisory System", font_size=20, bold=False,
             color=MINT, font_name="Calibri")

add_rect(slide, Emu(457200), Emu(2834640), Emu(4114800), Emu(36576), LIGHT_GREEN)

add_text_box(slide, Emu(457200), Emu(2971800), Emu(7772400), Emu(274320),
             "Viraj Balakrishnan  |  Devyansh Somvanshi", font_size=14, bold=False,
             color=WHITE, font_name="Calibri")
add_text_box(slide, Emu(457200), Emu(3291840), Emu(7772400), Emu(274320),
             "Guide: Dr. P. Vaidehi Nayantara  |  CSE (AI & ML), Sem VI  |  SRMIST",
             font_size=12, bold=False, color=MINT, font_name="Calibri")


# ── Save ──────────────────────────────────────────────────────────────
output_path = "D:/ALL DATA/Downloads/Smart_Crop_Review_v4_Second_Review.pptx"
prs.save(output_path)
print(f"Saved to: {output_path}")
print(f"Total slides: {len(prs.slides)}")
