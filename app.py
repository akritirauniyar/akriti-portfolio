import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="Akriti | Data Science Lab",
    page_icon="🧠",
    layout="wide"
)


# --------------------------------
# CUSTOM CSS
# --------------------------------

st.markdown("""
<style>

body {
    background-color: #05070a;
}

.main {
    background-color: #05070a;
}

h1, h2, h3 {
    color: white;
}

.green {
    color: #00ff9d;
}

.card {
    padding: 25px;
    border: 1px solid #222;
    border-radius: 15px;
    background: #0b0e12;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------
# HEADER
# --------------------------------

st.title("🧠 Data Science Lab")

st.markdown(
    """
    ### Welcome to Akriti's Interactive Data Science Portfolio

    Explore machine learning experiments, data analysis,
    visualizations and prediction models.
    """
)


st.divider()


# --------------------------------
# SIDEBAR
# --------------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Explore",
    [
        "Home",
        "Student Performance Predictor",
        "EDA Playground",
        "About"
    ]
)


# --------------------------------
# HOME
# --------------------------------

if page == "Home":

    st.header("🚀 Data Science Playground")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Projects",
            "4+"
        )

    with col2:
        st.metric(
            "Primary Language",
            "Python"
        )

    with col3:
        st.metric(
            "Focus",
            "Machine Learning"
        )


    st.markdown("---")

    st.subheader("What you can explore")

    c1, c2 = st.columns(2)

    with c1:

        st.markdown("""
        ### 🎓 Student Performance

        Predict student marks based on:

        - Study Hours
        - Attendance
        - Previous Score
        """)

    with c2:

        st.markdown("""
        ### 📊 Interactive EDA

        Upload your own dataset and explore:

        - Statistics
        - Distributions
        - Correlations
        - Visualizations
        """)


# --------------------------------
# STUDENT PREDICTOR
# --------------------------------

elif page == "Student Performance Predictor":

    st.header("🎓 Student Performance Predictor")

    st.write(
        "Predict expected marks using study hours and attendance."
    )


    np.random.seed(42)

    data = pd.DataFrame({

        "study_hours":
            np.random.uniform(1, 10, 100),

        "attendance":
            np.random.uniform(50, 100, 100)

    })


    data["marks"] = (
        data["study_hours"] * 5
        + data["attendance"] * .4
        + np.random.normal(0, 3, 100)
    )


    X = data[
        ["study_hours", "attendance"]
    ]

    y = data["marks"]


    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=.2,
        random_state=42
    )


    model = LinearRegression()

    model.fit(
        X_train,
        y_train
    )


    score = r2_score(
        y_test,
        model.predict(X_test)
    )


    col1, col2, col3 = st.columns(3)

    with col1:

        study = st.slider(
            "Study Hours",
            1.0,
            12.0,
            5.0
        )

    with col2:

        attendance = st.slider(
            "Attendance %",
            40,
            100,
            80
        )

    with col3:

        st.metric(
            "Model R²",
            f"{score:.2f}"
        )


    prediction = model.predict(
        [[study, attendance]]
    )[0]


    st.markdown("---")


    st.subheader("Prediction")

    st.success(
        f"Predicted Marks: {prediction:.2f}"
    )


    fig = px.scatter(
        data,
        x="study_hours",
        y="marks",
        size="attendance",
        title="Study Hours vs Marks"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# --------------------------------
# EDA PLAYGROUND
# --------------------------------

elif page == "EDA Playground":

    st.header("📊 EDA Playground")

    uploaded_file = st.file_uploader(
        "Upload CSV Dataset",
        type=["csv"]
    )


    if uploaded_file:

        df = pd.read_csv(
            uploaded_file
        )

        st.success(
            "Dataset loaded successfully!"
        )


        st.subheader("Dataset Preview")

        st.dataframe(
            df.head(20),
            use_container_width=True
        )


        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Rows",
                df.shape[0]
            )

        with col2:
            st.metric(
                "Columns",
                df.shape[1]
            )

        with col3:
            st.metric(
                "Missing Values",
                int(df.isnull().sum().sum())
            )


        numeric_columns = df.select_dtypes(
            include=np.number
        ).columns


        if len(numeric_columns) >= 2:

            x_axis = st.selectbox(
                "X Axis",
                numeric_columns
            )

            y_axis = st.selectbox(
                "Y Axis",
                numeric_columns,
                index=1
            )


            fig = px.scatter(
                df,
                x=x_axis,
                y=y_axis,
                title=f"{x_axis} vs {y_axis}"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )

    else:

        st.info(
            "Upload a CSV file to start exploring."
        )


# --------------------------------
# ABOUT
# --------------------------------

else:

    st.header("👩‍💻 About Akriti")

    st.write("""
    I am a Computer Science graduate interested in
    Data Science, Machine Learning and Data Analytics.

    My focus is on building practical, data-driven
    solutions using Python and modern analytics tools.
    """)

    st.markdown("""
    ### Core Technologies

    - Python
    - Pandas
    - NumPy
    - Scikit-learn
    - SQL
    - Power BI
    - Plotly
    - Machine Learning
    """)


st.divider()

st.caption(
    "Built with Python • Streamlit • Plotly • Machine Learning"
)