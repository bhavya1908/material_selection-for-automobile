# import pandas as pd
# import streamlit as st
#
# # Load the dataset with error handling
# try:
#     data = pd.read_csv('automobile data.csv')
#     data.columns = data.columns.str.strip()  # Clean column names
# except FileNotFoundError:
#     st.error("The specified file was not found.")
#     st.stop()
#
# # Display column names and preview the dataset
# st.write("Columns in the dataset:", data.columns.tolist())
# st.write("Dataset Preview:")
# st.dataframe(data.head())
#
# # User Input Section
# st.title("Material Selection Tool for Automotive Applications")
#
# st.sidebar.header("User Preferences")
# max_weight = st.sidebar.slider("Max Density (g/cm³)", 0.0, 10.0, 5.0)
# max_cost = st.sidebar.slider("Max Cost ($/kg)", 0.0, 50.0, 10.0)
# min_tensile_strength = st.sidebar.slider("Min Tensile Strength (MPa)", 0, 1000, 100)
# min_yield_strength = st.sidebar.slider("Min Yield Strength (MPa)", 0, 1000, 50)
# corrosion_resistance = st.sidebar.selectbox("Corrosion Resistance", ["Low", "Medium", "High"])
# sustainability_index = st.sidebar.slider("Sustainability Index (1-5)", 1, 5, 3)
#
# # Check for sustainability index column
# if 'Sustainability Index (1-5)' in data.columns:
#     # Filter the dataset based on user input
#     filtered_data = data[
#         (data['Density (g/cm³)'] <= max_weight) &
#         (data['Cost ($/kg)'] <= max_cost) &
#         (data['Tensile Strength (MPa)'] >= min_tensile_strength) &
#         (data['Yield Strength (MPa)'] >= min_yield_strength) &
#         (data['Corrosion Resistance'].str.lower() == corrosion_resistance.lower()) &
#         (data['Sustainability Index (1-5)'] >= sustainability_index)
#     ]
# else:
#     st.error("Column 'Sustainability Index (1-5)' not found in the dataset.")
#     st.stop()
#
# # Display the filtered results
# st.write("Recommended Materials:")
# if filtered_data.empty:
#     st.write("No materials found that match the criteria.")
# else:
#     st.dataframe(filtered_data)
#
#     # Download button for filtered results
#     csv = filtered_data.to_csv(index=False)
#     st.download_button(
#         label="Download Filtered Data",
#         data=csv,
#         file_name='filtered_materials.csv',
#         mime='text/csv'
#     )
import pandas as pd
import streamlit as st

# Load the dataset with error handling
try:
    data = pd.read_csv('automobile data.csv')
    data.columns = data.columns.str.strip()  # Clean column names
except FileNotFoundError:
    st.error("The specified file was not found.")
    st.stop()

# User Input Section
st.title("Material Selection Tool for Automotive Applications")

st.sidebar.header("User Preferences")
max_weight = st.sidebar.slider("Max Density (g/cm³)", 0.0, 10.0, 5.0)
max_cost = st.sidebar.slider("Max Cost ($/kg)", 0.0, 50.0, 10.0)
min_tensile_strength = st.sidebar.slider("Min Tensile Strength (MPa)", 0, 1000, 100)
min_yield_strength = st.sidebar.slider("Min Yield Strength (MPa)", 0, 1000, 50)
corrosion_resistance = st.sidebar.selectbox("Corrosion Resistance", ["Low", "Medium", "High"])
sustainability_index = st.sidebar.slider("Sustainability Index (1-5)", 1, 5, 3)

# Check for sustainability index column
if 'Sustainability Index (1-5)' in data.columns:
    # Filter the dataset based on user input
    filtered_data = data[
        (data['Density (g/cm³)'] <= max_weight) &
        (data['Cost ($/kg)'] <= max_cost) &
        (data['Tensile Strength (MPa)'] >= min_tensile_strength) &
        (data['Yield Strength (MPa)'] >= min_yield_strength) &
        (data['Corrosion Resistance'].str.lower() == corrosion_resistance.lower()) &
        (data['Sustainability Index (1-5)'] >= sustainability_index)
    ]
else:
    st.error("Column 'Sustainability Index (1-5)' not found in the dataset.")
    st.stop()

# Display the filtered results
st.write("Recommended Materials:")
if filtered_data.empty:
    st.write("No materials found that match the criteria.")
else:
    st.dataframe(filtered_data)

    # Download button for filtered results
    csv = filtered_data.to_csv(index=False)
    st.download_button(
        label="Download Filtered Data",
        data=csv,
        file_name='filtered_materials.csv',
        mime='text/csv'
    )
