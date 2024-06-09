import streamlit as st
from streamlit_option_menu import option_menu
import home
import analysis
import blog

# Load CSS function
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

# About Us page function
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

# MultiApp class to manage multiple pages
class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        with st.sidebar:
            st.image("Screenshot_2024-05-27_102248-removebg-preview.png", width=200)
            st.write("# Dataexplore")
            option = option_menu(
                menu_title='Menu',
                options=['Home', 'Analysis', 'Blogs', 'About Us'],
                icons=['fa-magic', 'fa-magic', 'fa-magic', 'fa-magic'],
                default_index=0,
                styles={
                    "menu_title": {"color": "#125", "font-size": "22px", "font-weight": "600", "padding": "10px"},
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if option == "Home":
            home.home()
        elif option == "Analysis":
            analysis.analysis()
        elif option == "Blogs":
            blog.blog()
        elif option == "About Us":
            abouts()

# Initialize and run the app
if __name__ == "__main__":
    app = MultiApp()
    app.run()

