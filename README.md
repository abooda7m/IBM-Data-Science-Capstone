
# SpaceX Launch Success Prediction Project

This capstone project is part of the IBM Data Science Professional Certificate. The goal is to analyze SpaceX Falcon 9 launches and build a predictive model that estimates the likelihood of successful first stage landings. This enables us to simulate being a Data Scientist at a fictional company, SpaceY, aiming to compete with SpaceX by building cost-efficient reusable rockets.

---

##  Project Summary

- **Title:** SpaceX Launch Success Prediction
- **Submitted On:** May 5, 2025
- **Objective:** Predict if SpaceX's Falcon 9 first stage will land successfully based on public launch data
- **Tools Used:** Python, Pandas, SQL, BeautifulSoup, Scikit-Learn, Plotly Dash, Folium
- **Deliverables:**
  - Complete GitHub repository with all labs and dashboards
  - Presentation slides in PDF format
  - Machine learning model for classification
  - Dash interactive app for visual analytics

---

##  Repository Contents

```bash
.
├── SpaceX-Launch-Success-Prediction-Project.pdf       # Final presentation
├── PlotlyDash.py                                      # Interactive Dashboard
├── jupyter-labs-eda-dataviz-v2.ipynb                  # Data visualization lab
├── jupyter-labs-eda-sql-coursera_sqllite.ipynb        # SQL lab
├── jupyter-labs-webscraping.ipynb                     # Web scraping lab
├── lab-jupyter-launch-site-location-v2.ipynb          # Folium map lab
├── dataset_part_1.csv                                 # Collected data
├── spacex_launch_geo.csv                              # Geo data for map
├── my_data1.db                                        # SQL database
├── README.md                                          # Project summary (this file)
```

---

##  Methodologies

### 1. **Data Collection**

- **REST API**: Collected launch data from `https://api.spacexdata.com/v4/launches/past` and other endpoints like `/rockets`, `/payloads`, `/launchpads`, etc.
- **Web Scraping**: Used BeautifulSoup to extract HTML tables from Wikipedia to enhance our dataset.

### 2. **Data Wrangling**

- Merged multiple API responses using IDs
- Dropped Falcon 1 launches
- Handled NULL values (e.g., replaced null `PayloadMass` with mean)
- Created final dataframe with clean launch records

---

##  Exploratory Data Analysis

- Created various visualizations to understand launch success trends:
  - Flight Number vs. Launch Site (scatter)
  - Payload vs. Launch Site (scatter)
  - Success rate vs. Orbit Type (bar)
  - Payload vs. Orbit (scatter)
  - Yearly trends of success (line chart)

---

##  Machine Learning

### Classification Models:
- Logistic Regression
- Decision Tree
- K-Nearest Neighbors
- Support Vector Machine

### Metrics Used:
- Accuracy
- F1 Score
- Confusion Matrix
- Jaccard Index

**Best model:** Decision Tree — good tradeoff between interpretability and performance.

---

##  Dash & Interactive Visualizations

### 1. **Plotly Dash App**
- Pie chart: Success counts for all sites
- Pie chart: Most successful site
- Scatter: Payload vs. Launch outcome

### 2. **Folium Map**
- All launch sites with markers
- Distance to key infrastructures (coastline, highway, rail)

---

##  SQL Analysis

Performed SQL queries using `my_data1.db` to answer 10 business questions.

---

##  Creativity & Innovation

- Added interactive components beyond requirements
- Explored extra EDA correlations
- Included additional dashboard functionality
- Refined visual style of the final presentation

---

##  Project Outcomes

- **Landing prediction success**: High accuracy using classification models
- **Insight**: Payload mass, orbit type, and launch site are critical predictors
- **Business Value**: Estimating first stage landing enables cost prediction for each mission

---

## ▶ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/abooda7m/SpaceX-Launch-Success-Prediction
cd SpaceX-Launch-Success-Prediction
```

### 2. Create virtual environment & install dependencies

```bash
uv venv env
env\Scripts\activate      # Windows
uv pip install -r requirements.txt
```

### 3. Launch dashboard

```bash
streamlit run PlotlyDash.py
```

---

##  License

This project is for educational purposes only as part of the IBM Data Science Professional Certificate.

---

