DataExplore-AnalysisBot

DataExplore-AnalysisBot is a Streamlit-based application that allows users to perform Exploratory Data Analysis (EDA) and apply various machine learning models on their datasets. Users can upload CSV files, explore the data, visualize it, encode categorical variables, and train and evaluate machine learning models.

 Features

- Data Upload: Upload a CSV file for analysis.
- Data Overview: View the first few rows of the dataset, column types, missing values, and basic statistical summaries.
- Data Visualization: Visualize data with histograms, pair plots, heatmaps, count plots, distribution plots, box plots, violin plots, and scatter plots.
- Feature Encoding: Encode categorical variables using One Hot, Binary, Label, or Frequency encoding methods.
- Machine Learning: Train and evaluate machine learning models such as Logistic Regression, Naive Bayes, XGBoost, Decision Tree, and Random Forest.
- Model Saving and Loading: Save trained models and load pre-trained models for later use.

 Installation

To run the application locally, follow these steps:

1. Clone the repository:
    bash
    git clone https://github.com/yourusername/DataExplore-AnalysisBot.git
    cd DataExplore-AnalysisBot
    

2. Install the required dependencies:
    bash
    pip install -r requirements.txt
    

3. Run the Streamlit app:
    bash
    streamlit run app.py
    

 Usage

1. Upload a CSV file using the sidebar.
2. Explore the data using the various options available in the sidebar.
3. Encode categorical variables if necessary.
4. Train and evaluate machine learning models on your data.
5. Save or load models using the options provided.

 Code Overview

 Main Functions

- load_css(): Loads custom CSS for styling the sidebar.
- analysis(): Main function that handles data upload, visualization, feature encoding, and machine learning.

 Data Visualization Options

- Histogram: Displays histograms for numerical variables.
- Pair Plot: Displays pair plots to show relationships between variables.
- Heat Map: Displays a heatmap of the correlation matrix.
- Count Plot: Displays a count plot for categorical variables.
- Dist Plot: Displays distribution plots for numerical variables.
- Box Plot: Displays box plots for selected columns.
- Violin Plot: Displays violin plots for selected columns.
- Scatter Plot: Displays scatter plots for selected pairs of variables.

 Feature Encoding

- One Hot Encoding: Converts categorical variables into a series of binary columns.
- Binary Encoding: Converts categories into binary digits.
- Label Encoding: Converts categories into numeric labels.
- Frequency Encoding: Maps each category to its frequency in the data.

 Machine Learning Models

- Logistic Regression
- Naive Bayes
- XGBoost
- Decision Tree
- Random Forest

 Model Saving and Loading

- Save trained models as `.pkl` files.
- Load pre-trained models for predictions.

 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


