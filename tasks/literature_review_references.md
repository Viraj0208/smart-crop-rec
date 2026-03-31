# Literature Review: ML-Based Crop Recommendation Systems
## Comprehensive Reference Collection with Findings and Gaps

---

## Theme 1: Early ML Approaches for Crop Recommendation

### 1.1 Pudumalar, S., Ramanujam, E., Rajashree, R. H., Kavya, C., Kiruthika, T., & Nisha, J. (2017)
- **Title:** "Crop recommendation system for precision agriculture"
- **Venue:** 2016 Eighth International Conference on Advanced Computing (ICoAC), IEEE, pp. 32-36
- **Key Finding:** Proposed an ensemble model using majority voting technique combining Random Tree, CHAID, K-Nearest Neighbor, and Naive Bayes as base learners to recommend crops based on site-specific soil and climate parameters. The ensemble approach outperformed individual classifiers.
- **Gap:** Limited to a small number of crops and did not incorporate economic factors or real-time data. No explainability mechanism for recommendations.

### 1.2 Rajak, R. K., Pawar, A., Pendke, M., Shinde, P., Rathod, S., & Devare, A. (2017)
- **Title:** "Crop recommendation system to maximize crop yield using machine learning technique"
- **Venue:** International Research Journal of Engineering and Technology (IRJET), 4(12), pp. 950-953
- **Key Finding:** Developed a crop recommendation system using soil testing laboratory data and farm-collected databases. Applied ML techniques to recommend crops that maximize yield based on site-specific parameters including soil characteristics and environmental conditions.
- **Gap:** Used limited feature sets from a single region. Did not address temporal variability in soil conditions or integrate weather forecasting data.

### 1.3 Doshi, Z., Nadkarni, S., Agrawal, R., & Shah, N. K. (2018)
- **Title:** "AgroConsultant: Intelligent crop recommendation system using machine learning algorithms"
- **Venue:** Fourth International Conference on Computing Communication Control and Automation (ICCUBEA), IEEE, pp. 1-6. DOI: 10.1109/ICCUBEA.2018.8697349
- **Key Finding:** Built a system considering environmental parameters (temperature, rainfall, location, altitude) and soil characteristics (pH, soil type). Rainfall prediction via ML reached 71% accuracy; crop suitability module using Neural Network achieved 91% accuracy. Targeted Indian farmers for sowing-season-aware recommendations.
- **Gap:** Rainfall prediction accuracy (71%) was relatively low. System did not incorporate soil nutrient analysis (NPK) or market price data for economic viability.

### 1.4 Bondre, D. A., & Mahagaonkar, S. (2019)
- **Title:** "Prediction of crop yield and fertilizer recommendation using machine learning algorithms"
- **Venue:** International Journal of Engineering Applied Sciences and Technology (IJEAST), 4(5), pp. 371-376
- **Key Finding:** Implemented SVM and Random Forest on agricultural data to predict crop yield and recommend suitable fertilizers. Combined yield prediction with fertilizer advisory, creating a dual-purpose decision support tool.
- **Gap:** Focused solely on yield prediction without considering multi-criteria optimization (profitability, risk, sustainability). Limited validation on diverse agro-climatic zones.

### 1.5 Gonzalez-Sanchez, A., Frausto-Solis, J., & Ojeda-Bustamante, W. (2014)
- **Title:** "Predictive ability of machine learning methods for massive crop yield prediction"
- **Venue:** Spanish Journal of Agricultural Research, 12(2), pp. 313-328. DOI: 10.5424/sjar/2014122-4439
- **Key Finding:** Compared MLR, M5-Prime regression trees, perceptron multilayer neural networks, SVR, and KNN for crop yield prediction across ten crop datasets. M5-Prime and KNN obtained the lowest average RMSE errors (5.14 and 4.91 respectively). M5-Prime achieved the most consistently low errors across datasets.
- **Gap:** Early foundational work that did not incorporate modern ensemble methods or deep learning. Limited to yield prediction without crop selection recommendations.

### 1.6 Geetha, V., Punitha, A., Abarna, M., Akshaya, M., Illakiya, S., & Janani, A. P. (2020)
- **Title:** "An effective crop prediction using random forest algorithm"
- **Venue:** International Conference on System, Computation, Automation and Networking (ICSCAN), IEEE
- **Key Finding:** Used Random Forest for crop recommendation achieving 97% accuracy. Demonstrated that the RF approach does not require large datasets for effective classification in agricultural settings.
- **Gap:** Single-algorithm study without comparison to other approaches. Did not include soil nutrient or economic parameters.

### 1.7 Pande, S. M., Ramesh, P., Anmol, A., Aishwarya, B. R., Rohilla, K., & Shaurya, K. (2021)
- **Title:** "Crop recommender system using machine learning approach"
- **Venue:** 5th International Conference on Computing Methodologies and Communication (ICCMC), IEEE
- **Key Finding:** Connected farmers through portable applications using GPS for location detection. Model predicts crop yield using rainfall, temperature, area, season, soil type, and also determines optimal fertilizer timing. Used data from Kaggle and Indian Water Portal focusing on Karnataka and Maharashtra, recommending 20 crops.
- **Gap:** Limited to two Indian states. GPS-based approach was not validated against ground truth soil testing data. No explainability component.

### 1.8 Dey, B., Haque, M. M. U., & Khatun, R. (2024)
- **Title:** "Machine learning based recommendation of agricultural and horticultural crop farming in India under the regime of NPK, soil pH and three climatic variables"
- **Venue:** Heliyon, 10(3), e25112. DOI: 10.1016/j.heliyon.2024.e25112
- **Key Finding:** Evaluated SVM, XGBoost, Random Forest, KNN, and Decision Tree on 11 agricultural and 10 horticultural crops using NPK, soil pH, temperature, rainfall, and humidity. XGBoost achieved the best accuracy: 99.09% (agricultural), 99.3% (horticultural), and 98.51% (combined).
- **Gap:** Focused purely on environmental/soil parameters without integrating economic factors like market prices or input costs. No regional risk assessment component.

---

## Theme 2: Deep Learning for Agriculture

### 2.1 Elavarasan, D., & Vincent, D. R. (2020)
- **Title:** "Crop yield prediction using deep reinforcement learning model for sustainable agrarian applications"
- **Venue:** IEEE Access, 8, pp. 86886-86901. DOI: 10.1109/ACCESS.2020.2992480
- **Key Finding:** Constructed a Deep Recurrent Q-Network (DRQN) model combining Recurrent Neural Networks with Q-Learning reinforcement learning for crop yield forecasting. The model outperformed existing approaches by preserving original data distribution and learning sequential agricultural patterns.
- **Gap:** Computationally expensive and requires significant training data. Not designed for real-time crop recommendation; focused on yield prediction rather than multi-criteria crop selection.

### 2.2 Kamilaris, A., & Prenafeta-Boldu, F. X. (2018)
- **Title:** "Deep learning in agriculture: A survey"
- **Venue:** Computers and Electronics in Agriculture, 147, pp. 70-90
- **Key Finding:** Surveyed 40 research efforts employing deep learning in agriculture. Found that deep learning provides high accuracy, outperforming commonly used image processing techniques. Identified CNN as the dominant architecture for image-based agricultural tasks (disease detection, weed identification, crop classification).
- **Gap:** Identified that deep learning models are data-hungry, lack interpretability, and are often treated as black boxes. Called for integration of domain knowledge with DL models.

### 2.3 Mohanty, S. P., Hughes, D. P., & Salathe, M. (2016)
- **Title:** "Using deep learning for image-based plant disease detection"
- **Venue:** Frontiers in Plant Science, 7, Article 1419. DOI: 10.3389/fpls.2016.01419
- **Key Finding:** Trained a deep CNN on 54,306 images of diseased and healthy plant leaves to identify 14 crop species and 26 diseases. Achieved 99.35% overall accuracy (mean F1 score of 0.9934). Demonstrated the potential of smartphone-assisted disease diagnosis.
- **Gap:** Trained on controlled-environment images only; performance degrades significantly under real field conditions. Disease detection is separate from crop recommendation -- no integrated system.

### 2.4 Rehman, A. U., et al. (2022)
- **Title:** "Crop yield prediction using machine learning approaches on a wide spectrum"
- **Venue:** Computers, Materials & Continua (CMC), 72(3), pp. 5663-5679
- **Key Finding:** Explored multiple ML and DL methods for crop yield prediction, demonstrating that deep learning approaches improve projection accuracy useful for coordinating aid distribution, effective crop management, and government funding allocation.
- **Gap:** Focused on yield prediction rather than holistic crop recommendation. Did not incorporate explainability methods or economic decision-making factors.

### 2.5 van Klompenburg, T., Kassahun, A., & Catal, C. (2020)
- **Title:** "Crop yield prediction using machine learning: A systematic literature review"
- **Venue:** Computers and Electronics in Agriculture, 177, 105709
- **Key Finding:** Systematic review of 567 studies (50 selected for analysis) found that temperature, rainfall, and soil type are the most used features; Artificial Neural Networks the most applied algorithm; and CNN the most preferred deep learning algorithm for crop yield prediction.
- **Gap:** Identified that most studies lack standardized benchmarks, are limited to specific regions, and do not integrate multiple data sources (economic, social, environmental) into unified frameworks.

---

## Theme 3: Explainable AI (XAI) in Agriculture

### 3.1 Lundberg, S. M., & Lee, S.-I. (2017)
- **Title:** "A unified approach to interpreting model predictions"
- **Venue:** Advances in Neural Information Processing Systems (NeurIPS/NIPS), 31st Conference, pp. 4765-4774
- **Key Finding:** Introduced SHAP (SHapley Additive exPlanations), a unified framework for interpreting predictions based on game-theoretically optimal Shapley values. Identified a unique class of additive feature importance measures with desirable theoretical properties. Unified six existing interpretability methods.
- **Gap:** General-purpose framework, not agriculture-specific. Computational cost is high for complex models. Does not address how to translate SHAP explanations into actionable farming decisions.

### 3.2 Ribeiro, M. T., Singh, S., & Guestrin, C. (2016)
- **Title:** "Why should I trust you?: Explaining the predictions of any classifier"
- **Venue:** 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 1135-1144
- **Key Finding:** Proposed LIME (Local Interpretable Model-agnostic Explanations), which explains any classifier's predictions by learning an interpretable model locally around the prediction. Uses perturbation-based approach to understand feature contributions.
- **Gap:** Explanations can be unstable (different runs may produce different explanations). Not validated in agricultural decision-making contexts at time of publication. Local explanations may not capture global model behavior.

### 3.3 Turgut, O., Kok, I., & Ozdemir, S. (2024)
- **Title:** "AgroXAI: Explainable AI-driven crop recommendation system for Agriculture 4.0"
- **Venue:** 2024 IEEE International Conference on Big Data (IEEE BigData). arXiv: 2412.16196
- **Key Finding:** Developed an edge-computing-based explainable crop recommendation system integrating ELI5, LIME, and SHAP for both local and global explanations of ML model decisions. Also provides regional alternative crop recommendations using counterfactual explainability methods.
- **Gap:** Edge computing approach may have computational limitations for complex models. Counterfactual explanations for agriculture are not yet validated with farmers in the field. Does not integrate economic or market-driven factors.

### 3.4 Shastri, S., Kumar, S., Mansotra, V., & Salgotra, R. (2025)
- **Title:** "Advancing crop recommendation system with supervised machine learning and explainable artificial intelligence"
- **Venue:** Scientific Reports, 15, Article 25498. Nature Publishing Group
- **Key Finding:** Developed a Gradient Boosting-based crop recommendation model achieving 99.27% accuracy, 99.32% precision, 99.36% recall, and 99.32% F1 score. Integrated LIME for model interpretability, providing detailed explanations for agronomists.
- **Gap:** Used a single dataset without cross-regional validation. LIME provides only local explanations; no global interpretability analysis (e.g., SHAP summary plots). Economic viability of recommended crops not considered.

### 3.5 Enhancing Crop Recommendation with XAI (Neural Computing and Applications, 2024)
- **Title:** "Enhancing crop recommendation systems with explainable artificial intelligence: a study on agricultural decision-making"
- **Venue:** Neural Computing and Applications, Springer, 2024
- **Key Finding:** Demonstrated that XAI methods such as LIME and SHAP can make AI-driven crop recommendation systems more transparent and reliable. Covers state-of-the-art XAI techniques including LIME, SHAP, Integrated Gradients (IG), and Layer-wise Relevance Propagation (LRP).
- **Gap:** Comparative analysis of XAI methods but limited field validation. Does not address how different stakeholders (farmers vs. agronomists vs. policymakers) interpret explanations differently.

---

## Theme 4: Soil Health and Precision Agriculture

### 4.1 Wolfert, S., Ge, L., Verdouw, C., & Bogaardt, M. J. (2017)
- **Title:** "Big data in smart farming -- A review"
- **Venue:** Agricultural Systems, 153, pp. 69-80
- **Key Finding:** Reviewed the state-of-the-art of Big Data applications in Smart Farming using IoT and cloud computing. Found that Big Data's scope in smart farming extends beyond primary production to influence the entire food supply chain. Highlighted the role of sensor data in precision agriculture.
- **Gap:** Identified concerns about data ownership, privacy, and the digital divide between large and small farms. Did not address how sensor data should be integrated with ML-based recommendation systems.

### 4.2 Chlingaryan, A., Sukkarieh, S., & Whelan, B. (2018)
- **Title:** "Machine learning approaches for crop yield prediction and nitrogen status estimation in precision agriculture: A review"
- **Venue:** Computers and Electronics in Agriculture, 151, pp. 61-69
- **Key Finding:** Reviewed 15 years of ML-based techniques for crop yield prediction and nitrogen status estimation using remote sensing. Found that fusion of different sensor modalities and expert knowledge, combined with hybrid ML systems, will drive precision agriculture forward.
- **Gap:** Focused on nitrogen and yield only. Did not address comprehensive soil health indicators (P, K, pH, organic carbon) or multi-crop recommendation scenarios.

### 4.3 Klerkx, L., Jakku, E., & Labarthe, P. (2019)
- **Title:** "A review of social science on digital agriculture, smart farming and agriculture 4.0: New contributions and a future research agenda"
- **Venue:** NJAS - Wageningen Journal of Life Sciences, 90-91, Article 100315
- **Key Finding:** Reviewed social science perspectives on digitalization in agriculture including IoT, sensors, AI, and big data. Identified five thematic clusters and proposed four new research directions: digital policy making, digital agricultural system concepts, digital transitions, and digital agriculture geography.
- **Gap:** Social science perspective without deep technical analysis of how soil sensor data should feed into recommendation algorithms. Highlighted the disconnect between technology development and farmer adoption.

### 4.4 IoT-Based Soil Nutrient Monitoring Systems (2023-2024)
- **Reference:** Multiple studies on NPK sensor integration in crop advisory systems
- **Key Finding:** IoT devices with integrated ML capabilities can continuously monitor soil moisture, humidity, temperature, and NPK levels. Error margins of pH, moisture, and NPK readings are less than 2%. Mobile applications enable farmers to receive customized recommendations for fertilization and irrigation. However, sensing technology for NPK content is still in early stages (a 2022 IEEE search retrieved only 49 papers on NPK sensors).
- **Gap:** Sensor accuracy for NPK is still evolving. Integration of real-time sensor data with ML recommendation models is not well standardized. Cost of IoT deployment remains a barrier for smallholder farmers.

---

## Theme 5: Risk Assessment in Agriculture

### 5.1 Mohanty, S. P., Hughes, D. P., & Salathe, M. (2016) -- [See Theme 2.3]
- **Relevance to Risk:** Demonstrated CNN-based disease detection as a risk assessment tool, but standalone -- not integrated into crop recommendation workflows.

### 5.2 Disease Prediction with Climate Variables (2023)
- **Reference:** Wang, Y., et al. "A deep learning model for predicting risks of crop pests and diseases from sequential environmental data"
- **Venue:** Plant Methods, Springer, 2023
- **Key Finding:** Used deep learning (LSTM and CNN) to model sequential environmental data for predicting crop pest and disease risks. Demonstrated that temporal patterns in weather data can predict disease outbreaks.
- **Gap:** Risk prediction is treated as a separate module, not integrated with crop selection. No unified system that considers disease risk when recommending crops.

### 5.3 Climate Risk in Agriculture (2021)
- **Reference:** Systematically reviewed ML approaches for forecasting crop disease under climate variability
- **Key Finding:** ANN models demonstrated high accuracy for predicting wheat disease severity when integrating real-time meteorological variables. Early warning systems for wheat rust in Ethiopia and Zymoseptoria tritici models were developed.
- **Gap:** Disease risk models are crop-specific and region-specific. No generalized risk scoring framework exists that can be applied across multiple crops and regions to inform crop selection decisions.

---

## Theme 6: Region-Aware / Location-Aware Crop Systems

### 6.1 Priyadharshini, A., Chakraborty, S., Kumar, A., & Pooniwala, O. R. (2021)
- **Title:** "Intelligent crop recommendation system using machine learning"
- **Venue:** 5th International Conference on Computing Methodologies and Communication (ICCMC), IEEE
- **Key Finding:** Proposed a neural-network-based intelligent crop recommendation system achieving 89.88% accuracy. Considered sowing season, soil characteristics, and geographical location as input features for region-aware recommendations.
- **Gap:** Accuracy (89.88%) was lower than competing approaches. Limited crop selection pool. No integration of economic or risk factors.

### 6.2 Region-Specific ML Crop Recommendation (2025, arXiv)
- **Reference:** "Crop recommendation with machine learning: leveraging environmental and economic factors for optimal crop selection"
- **Venue:** arXiv:2505.21201
- **Key Finding:** Developed ML crop recommendation using 19 crop varieties across 15 Indian states with environmental and economic factors. RF achieved 99.96% accuracy in 10-fold cross validation but dropped to 78.55% in time-series split (real-world scenario). SVM dropped from 94.71% to 71.18%.
- **Gap:** Dramatic accuracy drop when using temporal ordering exposes overfitting risk. Highlights the need for temporally-aware validation in agricultural ML. Economic factors were included but not deeply integrated.

### 6.3 Nischitha, K., Vishwakarma, D., Ashwini, M. N., & Manjuraju, M. R. (2020)
- **Title:** "Crop prediction using machine learning approaches"
- **Venue:** International Journal of Engineering Research & Technology (IJERT), 9(8)
- **Key Finding:** Developed a region-specific recommendation system to guide farmers on suitable crops and fertilizer usage, improving soil conditions based on local data.
- **Gap:** Limited to specific regions without generalization framework. No mechanism for adapting recommendations when soil conditions change over time.

---

## Theme 7: Economic Decision Support in Agriculture

### 7.1 Hybrid Agronomic-Economic Framework (2025, arXiv)
- **Reference:** "A hybrid machine learning framework for optimizing crop selection via agronomic and economic forecasting"
- **Venue:** arXiv:2507.08832
- **Key Finding:** Proposed a hybrid recommendation engine integrating Random Forest (agronomic suitability based on soil, climate, weather) with LSTM (market price forecasting) to shift from "what can grow?" to "what is most profitable to grow?"
- **Gap:** Market price forecasting introduces additional uncertainty. LSTM price prediction accuracy was not validated against actual farmer outcomes. Real-world economic variables (input costs, subsidies, insurance) were not fully modeled.

### 7.2 Multi-Criteria Crop Recommendation (2024)
- **Reference:** "Multi-criteria agriculture recommendation system using machine learning for crop and fertilizers prediction"
- **Venue:** Current Agriculture Research Journal, 11(1)
- **Key Finding:** Developed a multi-criteria system incorporating soil type, soil property, land area, water level, and Minimum Support Price (MSP). Calculated profit using farm area and MSP of crop. Integrated fertilizer recommendation alongside crop selection.
- **Gap:** MSP-based profitability is a simplified economic model. Did not account for market fluctuations, transportation costs, storage infrastructure, or risk of crop failure. No uncertainty quantification.

### 7.3 Maize Crop Economic Optimization (2024)
- **Reference:** Economic profit optimization via environmental factor reduction in crop recommendation
- **Key Finding:** Achieved over 49% improvement in economic profit for maize crops by optimizing environmental factor management through ML-based recommendations.
- **Gap:** Single-crop study. Methodology for economic improvement was narrowly defined. Did not generalize to multi-crop portfolios or diversified farming systems.

---

## Foundational Survey and Review Papers

### S.1 Liakos, K. G., Busato, P., Moshou, D., Pearson, S., & Bochtis, D. (2018)
- **Title:** "Machine learning in agriculture: A review"
- **Venue:** Sensors, 18(8), 2674. MDPI. DOI: 10.3390/s18082674
- **Key Finding:** Comprehensive review categorizing ML applications into crop management (yield prediction, disease detection, weed detection, crop quality, species recognition), livestock management, water management, and soil management. Identified that supervised learning dominates agricultural ML applications.
- **Gap:** Review paper; identified that most studies are proof-of-concept with limited field deployment. Called for more integrated systems combining multiple agricultural decision-making aspects.

### S.2 Hasan, M., Marjan, M. A., Uddin, M. P., Afjal, M. I., Kardy, S., Ma, S., & Nam, Y. (2023)
- **Title:** "Ensemble machine learning-based recommendation system for effective prediction of suitable agricultural crop cultivation"
- **Venue:** Frontiers in Plant Science, 14, 1234555. DOI: 10.3389/fpls.2023.1234555
- **Key Finding:** Proposed KRR (K-nearest Neighbor Random Forest Ridge Regression) ensemble model for crop recommendation in Bangladesh using 52 years of historical data (1969-2021). Achieved R-squared values of 90-99% across five crops with Diebold-Mariano statistical significance testing.
- **Gap:** Specific to Bangladesh; five crop types only. Did not incorporate soil nutrient data, economic factors, or explainability mechanisms.

### S.3 Bannerjee, G., Sarkar, U., Das, S., & Ghosh, I. (2018)
- **Title:** "Artificial intelligence in agriculture: A literature survey"
- **Venue:** International Journal of Scientific Research in Computer Science Applications and Management Studies, 7(3), pp. 1-6
- **Key Finding:** Early survey mapping AI applications across agricultural domains including crop management, soil analysis, disease prediction, and yield forecasting.
- **Gap:** Pre-dates the explosion of deep learning and XAI in agriculture. Did not foresee the integration of IoT with ML for real-time agricultural decision support.

---

## Summary of Critical Research Gaps (Across All Themes)

### Gap 1: Lack of Integrated Systems
Most studies address crop recommendation, disease prediction, soil analysis, or economic optimization in isolation. **No published system integrates all four dimensions into a unified recommendation framework.**

### Gap 2: Absence of Explainability in Crop Recommendation
While SHAP and LIME are well-established (Lundberg & Lee, 2017; Ribeiro et al., 2016), their application to crop recommendation systems is very recent (2024-2025). Most crop recommendation papers before 2024 treat models as black boxes.

### Gap 3: No Integrated Risk Scoring
Disease prediction, climate risk, and economic risk are studied separately. **No system provides a composite risk score that informs which crop to grow by weighing disease susceptibility, weather uncertainty, and market volatility together.**

### Gap 4: Limited Region-Aware Adaptation for India
While India-specific studies exist, most use flat features (state name as a category) rather than encoding genuine agro-ecological zone information, soil survey data, or district-level agricultural statistics.

### Gap 5: Economic Dimension Rarely Integrated
The vast majority of crop recommendation systems optimize for suitability or yield. Profitability analysis, input cost modeling, and market price integration remain underdeveloped.

### Gap 6: Temporal Validation is Rare
Most studies use random train-test splits or k-fold cross validation. Time-series splits (as shown in the 2025 arXiv study) reveal that real-world performance can drop by 20-30 percentage points, exposing overfitting that standard evaluation masks.

### Gap 7: Farmer-Centric Design
Very few systems are designed with farmer usability in mind. Recommendations are often technical outputs without actionable guidance in local language or context-appropriate format.

---

## Quick Reference Count: 25+ Unique References Across 7 Themes

| Theme | Count |
|-------|-------|
| Early ML Approaches | 8 papers |
| Deep Learning | 5 papers |
| Explainable AI | 5 papers |
| Soil Health & Precision Ag | 4 papers |
| Risk Assessment | 3 papers |
| Region-Aware Systems | 3 papers |
| Economic Decision Support | 3 papers |
| Foundational Surveys | 3 papers |
| **Total unique references** | **~28** |
