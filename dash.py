import streamlit as st, matplotlib.pyplot as plt, seaborn as sns, pandas as pd, numpy as np, joblib

def show_dash():
    
    st.title("Dashboard")
    clusert_model = joblib.load('cluster_model.pkl')
    df = pd.read_csv('finalx.csv')

    st.markdown("## Enter student details to predict final grade (G3)")
    # Define input fields for **ALL 28 features**
    age = st.number_input("Age", 10, 25, 16)
    Medu = st.slider("Mother's Education (0-4)", 0, 4, 2)
    Fedu = st.slider("Father's Education (0-4)", 0, 4, 2)

    # Features with _x suffix
    traveltime_x = st.slider("Travel Time (1-4)", 1, 4, 2)
    studytime_x = st.slider("Study Time (1-4)", 1, 4, 2)
    failures_x = st.slider("Past Failures (0-4)", 0, 4, 1)
    
    famrel_x = st.slider("Family Relationship Quality (1-5)", 1, 5, 3)
    freetime_x = st.slider("Free Time After School (1-5)", 1, 5, 3)
    goout_x = st.slider("Going Out with Friends (1-5)", 1, 5, 3)
    Dalc_x = st.slider("Workday Alcohol Consumption (1-5)", 1, 5, 1)
    Walc_x = st.slider("Weekend Alcohol Consumption (1-5)", 1, 5, 2)
    health_x = st.slider("Health Status (1-5)", 1, 5, 3)
    absences_x = st.number_input("Number of Absences", 0, 100, 5)
    G1_x = st.number_input("First Period Grade (0-20)", 0, 20, 10)
    G2_x = st.number_input("Second Period Grade (0-20)", 0, 20, 10)
    G3_x = st.number_input("Final Period Grade (0-20)", 0, 20, 10)

    # Features with _y suffix
    traveltime_y = st.slider("Travel Time (Duplicate) (1-4)", 1, 4, 2)
    studytime_y = st.slider("Study Time (Duplicate) (1-4)", 1, 4, 2)
    failures_y = st.slider("Past Failures (Duplicate) (0-4)", 0, 4, 1)
    famrel_y = st.slider("Family Relationship Quality (Duplicate) (1-5)", 1, 5, 3)
    freetime_y = st.slider("Free Time (Duplicate) (1-5)", 1, 5, 3)
    goout_y = st.slider("Going Out (Duplicate) (1-5)", 1, 5, 3)
    Dalc_y = st.slider("Workday Alcohol (Duplicate) (1-5)", 1, 5, 1)
    Walc_y = st.slider("Weekend Alcohol (Duplicate) (1-5)", 1, 5, 2)
    health_y = st.slider("Health Status (Duplicate) (1-5)", 1, 5, 3)
    absences_y = st.number_input("Number of Absences (Duplicate)", 0, 100, 5)
    G1_y = st.number_input("First Period Grade (Duplicate) (0-20)", 0, 20, 10)
    G2_y = st.number_input("Second Period Grade (Duplicate) (0-20)", 0, 20, 10)

    # Collect inputs in the same order as your training data (28 features)
    input_data = np.array([[age, Medu, Fedu,
                            traveltime_x, studytime_x, failures_x, famrel_x, freetime_x, goout_x, 
                            Dalc_x, Walc_x, health_x, absences_x, G1_x, G2_x, G3_x,
                            traveltime_y, studytime_y, failures_y, famrel_y, freetime_y, goout_y,
                            Dalc_y, Walc_y, health_y, absences_y, G1_y, G2_y]])
    opinion = st.button('Do you want to predict final marks?')
    if opinion:
        clusert_pred = clusert_model.predict(input_data)
        if clusert_pred == 0:
            group = "Average Students' group"
        elif clusert_pred == 1:
            group = "Excellent students' group"
        else:
            group = "Above Average students' group"

        st.success(f'Your child belongs to {group}')

   
   
#  Analysis of types of students   
    type_of_students = st.radio(label="Which type of students' performance you want to visualize?",
                                options=['Excellent', 'Above Average', 'Average'], )
    types = ['Average', 'Excellent', 'Above Average']
    ind = types.index(type_of_students)
    type_of_graph = st.radio(label='Which type of graph you want?', 
                             options=['histogram', 'cluster', 'simple line'])
    def graphs(type_of_graph):
        if type_of_graph == 'histogram':
            return sns.histplot(x=i, data=final_X,color='g', bins=10, fill=False, kde=True)
        elif type_of_graph == 'cluster':
            return sns.scatterplot(final_X.loc[final_X.Label==ind][i], color='g')
        else:
            return sns.lineplot(y='age', x=i, data=final_X, color='g')

    st.title(f"{type_of_students} type of students")
    final_X = pd.read_csv('finalx.csv')
    fig = plt.figure(figsize=(10,40), frameon=False)
    for wind, i in enumerate(final_X.loc[final_X.Label==ind], start=1):
        plt.subplot(10,3, wind, frameon=False)
        graphs(type_of_graph)
        plt.xticks(np.linspace(final_X[i].min(), final_X[i].max(), 6),rotation=45, color='y')
        plt.xlabel(i, color='w')
        plt.yticks(color='y')
        if type_of_graph == 'histogram':
            plt.ylabel('count', color='w')
        elif type_of_graph == 'cluster':
            plt.ylabel(i, color='w')
        else:
            plt.ylabel('Age', color='w')
    st.pyplot(fig)

    if st.button("🏠 Back to Home"):
        st.session_state.page = "home"
        st.rerun()