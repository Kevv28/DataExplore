def analysis():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    import category_encoders as ce
    from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
    from sklearn.linear_model import LogisticRegression
    from sklearn.naive_bayes import GaussianNB
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.tree import DecisionTreeClassifier
    from xgboost import XGBClassifier
    from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
    from sklearn.metrics import classification_report, confusion_matrix
    import joblib

    def load_css():
        css = """
        <style>
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

        .sidebar nav ul li a.btn {
            background-color: #e0e0e0;
            color: black;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 5px;
            transition: background-color 0.3s ease;
        }

        .sidebar nav ul li a.btn:hover {
            background-color: #c0c0c0;
        }
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)

    load_css()
    
    st.sidebar.title("DataExplore-AnalysisBot")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file for which you want to perform analysis", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.write("### DataFrame Overview")
        st.write(df.head())

        if st.sidebar.checkbox("Show Column Types"):
            st.write(df.dtypes)

        if st.sidebar.checkbox("Show Columns"):
            st.write(df.columns.tolist())

        if st.sidebar.checkbox("Show Missing Values"):
            st.write(df.isnull().sum())

        if st.sidebar.checkbox("Show Dataframe Tabulation"):
            st.write(df.describe())
        
        if st.sidebar.checkbox("Show Numerical Variables"):
            st.write(df.select_dtypes(include=[np.number]).columns.tolist())

        if st.sidebar.checkbox("Show Categorical Variables"):
            st.write(df.select_dtypes(include=[object]).columns.tolist())

        # Data visualization
        if st.sidebar.checkbox("Show Histogram"):
            df.hist(figsize=(20, 20))
            plt.show()

        if st.sidebar.checkbox("Show Pair Plot"):
            st.pyplot(sns.pairplot(df))

        if st.sidebar.checkbox("Show Heat Map"):
            plt.figure(figsize=(20, 20))
            sns.heatmap(df.corr(), annot=True)
            st.pyplot()

        if st.sidebar.checkbox("Show Count Plot"):
            plt.figure(figsize=(20, 20))
            sns.countplot(data=df)
            st.pyplot()

        if st.sidebar.checkbox("Show Dist Plot"):
            plt.figure(figsize=(20, 20))
            sns.distplot(df)
            st.pyplot()

        if st.sidebar.checkbox("Show Box Plot"):
            column = st.sidebar.selectbox("Select column for Box Plot", df.columns)
            sns.boxplot(x=df[column])
            st.pyplot()

        if st.sidebar.checkbox("Show Violin Plot"):
            column = st.sidebar.selectbox("Select column for Violin Plot", df.columns)
            sns.violinplot(x=df[column])
            st.pyplot()

        if st.sidebar.checkbox("Show Scatter Plot"):
            x_column = st.sidebar.selectbox("Select X column for Scatter Plot", df.columns)
            y_column = st.sidebar.selectbox("Select Y column for Scatter Plot", df.columns)
            sns.scatterplot(x=df[x_column], y=df[y_column])
            st.pyplot()

        st.sidebar.subheader("Feature Encoding")
        encoding_option = st.sidebar.selectbox("Choose encoding method", ["One Hot", "Binary", "Label", "Frequency"])
        if encoding_option:
            columns_to_encode = st.sidebar.multiselect("Select columns to encode", df.columns)
            if columns_to_encode:
                if encoding_option == "One Hot":
                    df = pd.get_dummies(df, columns=columns_to_encode)
                elif encoding_option == "Binary":
                    encoder = ce.BinaryEncoder(cols=columns_to_encode)
                    df = encoder.fit_transform(df)
                elif encoding_option == "Label":
                    le = LabelEncoder()
                    for col in columns_to_encode:
                        df[col] = le.fit_transform(df[col])
                elif encoding_option == "Frequency":
                    for col in columns_to_encode:
                        freq = df[col].value_counts()
                        df[col] = df[col].map(freq)
                st.write("### Encoded DataFrame")
                st.write(df.head())

        st.sidebar.subheader("Machine Learning")
        target = st.sidebar.selectbox("Select Target Column", df.columns)
        if target:
            X = df.drop(columns=[target])
            y = df[target]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            model_option = st.sidebar.selectbox("Choose Model", ["Logistic Regression", "Naive Bayes", "XGBoost", "Decision Tree", "Random Forest"])
            if model_option:
                if model_option == "Logistic Regression":
                    model = LogisticRegression()
                elif model_option == "Naive Bayes":
                    model = GaussianNB()
                elif model_option == "XGBoost":
                    model = XGBClassifier()
                elif model_option == "Decision Tree":
                    model = DecisionTreeClassifier()
                elif model_option == "Random Forest":
                    model = RandomForestClassifier()

                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)
                report = classification_report(y_test, y_pred)
                conf_matrix = confusion_matrix(y_test, y_pred)

                st.write("### Classification Report")
                st.text(report)
                st.write("### Confusion Matrix")
                st.write(conf_matrix)

                save_option = st.sidebar.checkbox("Save Model")
                if save_option:
                    model_name = st.sidebar.text_input("Enter Model Name", "model.pkl")
                    joblib.dump(model, model_name)
                    st.sidebar.write(f"Model saved as {model_name}")

                load_option = st.sidebar.checkbox("Load Model")
                if load_option:
                    loaded_model_name = st.sidebar.text_input("Enter Model Filename", "model.pkl")
                    loaded_model = joblib.load(loaded_model_name)
                    st.sidebar.write(f"Model {loaded_model_name} loaded")
    else:
        st.write("## Welcome to DataExplore-AnalysisBot!")
        st.write("""
            This application allows you to perform Exploratory Data Analysis (EDA) and apply various machine learning models on your dataset.
            Please follow the steps below to get started:
            1. Upload a CSV file using the sidebar.
            2. Explore the data using the various options available.
            3. Encode categorical variables if necessary.
            4. Train and evaluate machine learning models on your data.
        """)
        st.write("### Sample DataFrame")
        sample_data = {
            "A": [1, 2, 3, 4, 5],
            "B": [10, 20, 30, 40, 50],
            "C": ["a", "b", "c", "d", "e"]
        }
        df_sample = pd.DataFrame(sample_data)
        st.write(df_sample)

    st.set_option('deprecation.showPyplotGlobalUse', False)


if __name__ == "__main__":
    analysis()
