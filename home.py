import streamlit as st

styles = """
<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
}

.container {
    display: flex;
    width: 100%;
}

.sidebar {
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
    background-color: #d3d3d3;
    padding: 20px;
    width: 250px;
    flex-shrink: 0;
}

.sidebar h2 {
    margin-bottom: 20px;
}

.sidebar nav ul {
    list-style: none;
    padding-left: 0;
}

.sidebar nav ul li {
    margin: 10px 0;
}

.sidebar nav ul li a {
    text-decoration: none;
    color: black;
    display: flex;
    align-items: center;
    padding: 10px;
    border-radius: 10px;
    cursor: pointer;
}

.sidebar nav ul li a i {
    margin-right: 10px;
}

.sidebar nav ul li.active a {
    background-color: lightgray;
}

.main-content {
    margin-left: 270px;  /* Ensure it doesn't overlap with the sidebar */
    padding: 20px;
    flex-grow: 1;
}

header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.welcome-text h1 {
    font-size: 2em;
}

.welcome-text p {
    font-size: 1.2em;
    color: gray;
}

.profile-image img {
    border-radius: 50%;
    width: 50px;
    height: 50px;
}

.logo {
    width: 20px;
    margin-bottom: 20px;
}
</style>
"""

def home():
        st.markdown(styles, unsafe_allow_html=True)

      
        st.title("Exploratory Data Analysis (EDA)")

        
        st.header("What is Exploratory Data Analysis?")
        st.markdown("""
        Exploratory Data Analysis (EDA) is a crucial initial step in data science projects. It involves analyzing and visualizing data to understand its key characteristics, uncover patterns, and identify relationships between variables. This method of studying and exploring data sets helps comprehend their main traits, discover patterns, locate outliers, and establish relationships between variables.
        """)
        st.image("D:\EDA\Timespent.png", caption="Time Spent on Different EDA Activities")
       
        st.header("Key Aspects of EDA")
        st.markdown("""
        - **Distribution of Data:** Understanding the range, central tendencies (mean, median), and dispersion (variance, standard deviation).
        - **Graphical Representations:** Using histograms, box plots, scatter plots, and bar charts to visualize relationships and distributions.
        - **Outlier Detection:** Identifying data points that deviate from others which might indicate errors or unique cases.
        - **Correlation Analysis:** Assessing how variables affect each other by computing correlation coefficients and creating matrices.
        - **Handling Missing Values:** Addressing missing data points through imputation or removal.
        - **Summary Statistics:** Calculating key statistics to provide insights into data trends.
        - **Testing Assumptions:** Ensuring the data meet the conditions assumed by statistical tests and models.
        """)

        st.header("Why Exploratory Data Analysis is Important?")
        st.markdown("""
        - **Understanding Data Structures:** Familiarizing with the dataset, its features, and data types.
        - **Identifying Patterns and Relationships:** Revealing hidden patterns and intrinsic relationships through visualizations.
        - **Detecting Anomalies and Outliers:** Identifying errors or unusual data points early in the analysis process.
        - **Testing Assumptions:** Checking assumptions underlying statistical models.
        - **Informing Feature Selection and Engineering:** Using insights from EDA to decide on feature relevance and transformations.
        - **Optimizing Model Design:** Selecting appropriate modeling techniques based on data characteristics.
        - **Facilitating Data Cleaning:** Improving data quality by addressing missing values and errors.
        - **Enhancing Communication:** Making it easier to communicate findings to stakeholders.
        """)
        
        
        st.header("Types of Exploratory Data Analysis")
        st.markdown("""
        Depending on the dimensionality of the analysis, EDA can be divided into:
        - **Univariate Analysis:** Focusing on one variable.
        - **Bivariate Analysis:** Exploring relationships between two variables.
        - **Multivariate Analysis:** Examining relationships among multiple variables simultaneously.
        """)

        
        st.markdown("---")
        st.markdown("Last Updated: 16 May, 2024")