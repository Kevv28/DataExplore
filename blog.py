import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-image: linear-gradient(#2e7bcf, #2e7bcf);
        color: white;
    }
    .blog-container {
        margin: 20px 0;
        padding: 20px;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .blog-title {
        font-size: 26px;
        font-weight: bold;
        color: #2e7bcf;
        margin-bottom: 10px;
    }
    .blog-content {
        font-size: 18px;
        line-height: 1.6;
        color: #333;
    }
    .blog-author {
        font-size: 14px;
        color: #777;
        text-align: right;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

def blog():
    st.sidebar.title("EDA Blog Selector")
    option = st.sidebar.selectbox("Choose a blog", ("Blog 1: Understanding Data Distributions", 
                                                    "Blog 2: Correlation and Causation in Data", 
                                                    "Blog 3: Missing Data Handling", 
                                                    "Blog 4: Feature Engineering for EDA"))
    
    if option == "Blog 1: Understanding Data Distributions":
        st.markdown("""
            <div class="blog-container">
                <div class="blog-title">Understanding Data Distributions</div>
                <div class="blog-content">
                    Exploratory Data Analysis (EDA) often starts with understanding the distribution of data. 
                    This includes visualizing data distributions using histograms, box plots, and density plots. 
                    It helps in identifying outliers, skewness, and the central tendency of data.
                    <br><br>
                    <b>Histograms:</b> These plots provide a visual representation of the distribution of a single numerical variable by splitting the data into bins. They help in identifying the shape of the distribution, whether it is normal, skewed, bimodal, etc.
                    <br><br>
                    <b>Box Plots:</b> Box plots are useful for understanding the spread and skewness of data. They highlight the median, quartiles, and potential outliers.
                    <br><br>
                    <b>Density Plots:</b> Similar to histograms, density plots smooth the data using a kernel density estimate. They provide a continuous estimation of the distribution.
                    <br><br>
                    By analyzing these plots, we can make informed decisions about data transformations, identify potential issues, and plan further analyses accordingly.
                </div>
                <div class="blog-author">Author: Data Enthusiast</div>
            </div>
        """, unsafe_allow_html=True)
    
    elif option == "Blog 2: Correlation and Causation in Data":
        st.markdown("""
            <div class="blog-container">
                <div class="blog-title">Correlation and Causation in Data</div>
                <div class="blog-content">
                    In EDA, examining the relationships between variables is crucial. Scatter plots and correlation matrices 
                    are common tools to assess how variables interact with each other. Understanding correlation can lead 
                    to insights about potential causal relationships that can be further explored.
                    <br><br>
                    <b>Scatter Plots:</b> These plots visualize the relationship between two continuous variables. By observing the pattern, we can infer the strength and direction of their relationship. For instance, a positive linear pattern suggests a positive correlation.
                    <br><br>
                    <b>Correlation Matrices:</b> Correlation matrices display the correlation coefficients between multiple variables. The coefficients range from -1 to 1, where values close to 1 or -1 indicate strong relationships, and values close to 0 indicate weak relationships.
                    <br><br>
                    <b>Heatmaps:</b> When used in conjunction with correlation matrices, heatmaps provide a visual summary of correlations. Color gradients help in quickly identifying strong and weak relationships.
                    <br><br>
                    While correlation does not imply causation, understanding these relationships is a key step in forming hypotheses for further investigation. Advanced techniques such as regression analysis and causal inference methods can then be employed to explore causal relationships.
                </div>
                <div class="blog-author">Author: Data Analyst</div>
            </div>
        """, unsafe_allow_html=True)
    
    elif option == "Blog 3: Missing Data Handling":
        st.markdown("""
            <div class="blog-container">
                <div class="blog-title">Missing Data Handling</div>
                <div class="blog-content">
                    Missing data is a common issue in datasets. EDA includes identifying missing values and understanding 
                    their patterns. Techniques like imputation, deletion, or using algorithms that handle missing data 
                    are critical to ensure the integrity of analysis.
                    <br><br>
                    <b>Identifying Missing Data:</b> The first step in handling missing data is to identify where and how much data is missing. Visualizations such as missing data heatmaps can be helpful in this regard.
                    <br><br>
                    <b>Imputation:</b> One common approach is to fill in the missing values with substituted ones. Techniques include mean/median imputation, where missing values are replaced with the mean or median of the column, and more advanced methods like K-Nearest Neighbors (KNN) imputation.
                    <br><br>
                    <b>Deletion:</b> In some cases, it may be appropriate to delete rows or columns with missing data, especially if the amount of missing data is small and its removal does not bias the analysis.
                    <br><br>
                    <b>Advanced Methods:</b> Algorithms such as Multiple Imputation by Chained Equations (MICE) or using models like Random Forests can predict and fill in missing data based on other available data points.
                    <br><br>
                    Addressing missing data properly ensures that the subsequent analysis is accurate and reliable, avoiding potential biases and misleading results.
                </div>
                <div class="blog-author">Author: Data Scientist</div>
            </div>
        """, unsafe_allow_html=True)
    
    elif option == "Blog 4: Feature Engineering for EDA":
        st.markdown("""
            <div class="blog-container">
                <div class="blog-title">Feature Engineering for EDA</div>
                <div class="blog-content">
                    Feature engineering involves creating new features from existing data to improve model performance. 
                    During EDA, this process can reveal hidden patterns and relationships. Techniques like binning, 
                    polynomial features, and interaction terms are often used.
                    <br><br>
                    <b>Binning:</b> This technique involves converting continuous variables into categorical ones by grouping data into bins. For instance, ages can be binned into categories such as 'child', 'teen', 'adult', and 'senior'.
                    <br><br>
                    <b>Polynomial Features:</b> Creating polynomial features involves generating new features by taking powers of existing features. This can help in capturing non-linear relationships.
                    <br><br>
                    <b>Interaction Terms:</b> These are features created by multiplying or combining two or more existing features. Interaction terms can capture the combined effect of multiple variables on the target variable.
                    <br><br>
                    <b>Date and Time Features:</b> Extracting features such as day of the week, month, or hour from date-time variables can provide additional insights and improve model performance.
                    <br><br>
                    Feature engineering is a creative process that often requires domain knowledge and experimentation. The goal is to enhance the predictive power of the models by providing them with more informative input features.
                </div>
                <div class="blog-author">Author: ML Engineer</div>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    blog()
