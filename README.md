# Gym Members Exercise Tracking Dashboard

This is a Dash application that visualizes **Total Calories Burned by Workout Type and Gender** based on gym members' exercise tracking data. The app provides interactive controls to filter the data by workout type(s) and gender, displaying the results as a stacked bar chart.

---

## Features

- **Interactive Dropdown**: Select one or more workout types to filter the data.
- **Gender Checklist**: Filter results by gender with a simple checklist.
- **Dynamic Visualization**: View filtered results in a clear, interactive bar chart.
- **Responsive Design**: Suitable for both desktop and mobile devices.

---

## Requirements

Before running the application, ensure you have the following installed:

- **Python** (3.7 or higher)
- Required Python Libraries:
  - `dash`
  - `dash-core-components`
  - `dash-html-components`
  - `dash-bootstrap-components`
  - `plotly`
  - `pandas`

---

## Dataset

The application uses the dataset `gym_members_exercise_tracking.csv`. The dataset must have the following columns:

- **Workout_Type**: The type of workout (e.g., Cardio, Strength Training).
- **Gender**: The gender of the gym member (e.g., Male, Female).
- **Calories_Burned**: The total calories burned during the workout.

