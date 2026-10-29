<<<<<<< HEAD
# AI-Based Smart EV Battery Health Monitoring and Predictive Maintenance System

## Project Overview

This final-year group project aims to develop an AI/ML-based system for monitoring electric vehicle (EV) battery conditions and supporting predictive maintenance.

The system will analyze battery parameters, classify operating conditions as Normal, Warning, or Critical, and explore State of Health (SoH) estimation and Remaining Useful Life (RUL) prediction.

Future development will investigate ESP32 hardware, battery sensors, and an IoT dashboard.

## Objectives

- Analyze EV battery operating parameters.
- Classify battery conditions using machine learning.
- Investigate pack voltage, current, State of Charge (SoC), and individual cell voltages.
- Compare classification models using appropriate evaluation metrics.
- Explore SoH estimation and RUL prediction using suitable battery-aging datasets.
- Investigate hardware integration and IoT-based monitoring.

## Dataset

Current dataset: `ev_battery_synthetic_1000_dataset.csv`

- Samples: 1,000
- Columns: 19
- Input measurements include pack voltage, current, SoC, and 12 cell voltages.
- Target column: `label`
- Target classes: `normal`, `warning`, and `critical`

| Label | Samples | Percentage |
|---|---:|---:|
| Normal | 642 | 64.2% |
| Warning | 230 | 23.0% |
| Critical | 128 | 12.8% |

**Dataset limitation:** The current dataset is synthetic. Its results cannot establish real-world battery fault detection performance. Label consistency, feature relationships, class imbalance, and possible data leakage must be investigated.

## Technology Stack

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Joblib
- VS Code
- Git and GitHub
- ESP32 and IoT dashboard technologies (planned)

## Current Progress

### Completed

- [x] Created the Python virtual environment.
- [x] Installed the required Python libraries.
- [x] Inspected the dataset structure and data types.
- [x] Checked missing values and duplicate rows.
- [x] Examined target class distribution.
- [x] Generated initial exploratory data analysis (EDA) graphs.

### In progress

- [ ] Investigate label consistency and abnormality types.
- [ ] Analyze feature relationships and possible data leakage.
- [ ] Prepare training, validation, and test datasets.
- [ ] Train and compare classification models.
- [ ] Evaluate per-class precision, recall, F1-score, and confusion matrices.

### Planned

- [ ] Tune and validate the classification model.
- [ ] Save the trained model and preprocessing pipeline.
- [ ] Investigate real battery-aging datasets.
- [ ] Develop separate SoH and RUL models.
- [ ] Explore ESP32 sensor integration.
- [ ] Develop an IoT dashboard.
- [ ] Validate the prototype and document its limitations.

## Project Files

- `ev_battery_synthetic_1000_dataset.csv` — synthetic battery dataset.
- `step1_inspect.py` — dataset inspection.
- `step2_eda.py` — exploratory graphs.
- `step3_check_labels.py` — label and feature analysis.
- `eda_label_distribution.png` — class distribution graph.
- `eda_pack_voltage.png` — pack voltage graph.
- `eda_soc.png` — State of Charge graph.
- `eda_cell_voltages.png` — individual cell voltage graph.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/shrinivas-jooja/ev-battery-health-monitoring.git
cd ev-battery-health-monitoring
```

### 2. Create and activate a virtual environment

On Windows:

```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install pandas numpy matplotlib seaborn scikit-learn jupyter joblib
```

### 4. Inspect the dataset

```bash
python step1_inspect.py
```

### 5. Generate EDA graphs

```bash
python step2_eda.py
```

These commands require the corresponding dataset and scripts to be present in the repository.

## Team Collaboration

- Pull the latest changes before beginning work.
- Use descriptive commit messages.
- Discuss major changes with teammates.
- Keep `.venv/` out of version control.
- Never commit passwords, API keys, or confidential information.
- Document experiments and model evaluation results.

## Expected Outcome

The intended outcome is a prototype for EV battery condition classification, with future extensions for battery health estimation, predictive maintenance, hardware integration, and IoT monitoring.

## Project Status

**Under development — initial dataset analysis completed.**

Final model performance, SoH/RUL prediction, and hardware integration remain subject to implementation and validation.
=======
# ev-battery-health-monitoring
AI-based EV battery health monitoring and predictive maintenance using machine learning, with planned ESP32 and IoT integration.
>>>>>>> origin/main
