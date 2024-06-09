import streamlit as st

def abouts():
    load_css()  # Ensure the CSS is loaded before rendering content

    st.title("About Us")
    st.write("""
    ## Welcome to DataExplore-AnalysisBot!
    
    DataExplore-AnalysisBot is a powerful tool designed to help you perform comprehensive exploratory data analysis (EDA) and apply various machine learning models to your datasets. Our goal is to simplify the process of data analysis and model training, making it accessible to everyone, from beginners to experienced data scientists.
    """)

    st.subheader("Vision")
    st.write("""
    To democratize data analysis and machine learning, making advanced data science tools accessible to everyone.
    """)

    st.subheader("Mission")
    st.write("""
    To provide a user-friendly platform that enables users to gain valuable insights from their data and build predictive models with ease.
    """)

    st.subheader("Aim")
    st.write("""
    - **Simplify Data Analysis:** Offer an intuitive interface for performing exploratory data analysis.
    - **Enhance Accessibility:** Make machine learning techniques easy to understand and use.
    - **Support Users:** Provide comprehensive resources and support to help users succeed in their data projects.
    """)

    st.subheader("Meet the Team")
    st.write("""
    - **Kevil Rana:** Data Scientist and Developer
    
    """)

    st.subheader("Contact Us")
    st.write("""
    If you have any questions, feedback, or suggestions, feel free to reach out to us at support@dataexplore.com.
    """)

def load_css():
    css = """
    <style>
    .sidebar .sidebar-content {
        background-color: #d3d3d3;
        padding: 20px;
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

    .content {
        padding: 20px;
        margin-left: 250px; /* Adjust margin for sidebar */
    }

    .content h2, .content h3 {
        color: #333;
    }

    .content p {
        font-size: 16px;
        line-height: 1.6;
        color: #555;
    }

    .content ul {
        list-style-type: disc;
        margin-left: 20px;
    }

    .content ul li {
        margin-bottom: 10px;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

if __name__ == "__main__":
    abouts()
