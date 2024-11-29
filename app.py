import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('gym_members_exercise_tracking.csv')

# Summarize total calories burned by workout type and gender
calories_by_workout_gender = df.groupby(['Workout_Type', 'Gender'])['Calories_Burned'].sum().reset_index()

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server
# Layout for the app
app.layout = html.Div([
    html.H1("Total Calories Burned by Workout Type and Gender"),
    
    # Dropdown for selecting workout type(s)
    dcc.Dropdown(
        id='workout-type-dropdown',
        options=[{'label': workout, 'value': workout} for workout in calories_by_workout_gender['Workout_Type'].unique()],
        multi=True,
        placeholder="Select Workout Type(s)",
        value=calories_by_workout_gender['Workout_Type'].unique().tolist()  # Default to all workout types
    ),
    
    # Checklist for selecting gender
    dcc.Checklist(
        id='gender-checklist',
        options=[{'label': gender, 'value': gender} for gender in calories_by_workout_gender['Gender'].unique()],
        value=calories_by_workout_gender['Gender'].unique().tolist(),  # Default to both genders
        inline=True
    ),

    # Graph to display the calories burned data
    dcc.Graph(id='calories-bar-chart')
])

# Callback to update the chart based on selected workout types and gender
@app.callback(
    Output('calories-bar-chart', 'figure'),
    [
        Input('workout-type-dropdown', 'value'),
        Input('gender-checklist', 'value')
    ]
)
def update_chart(selected_workouts, selected_genders):
    # Filter data based on the selected workout types and genders
    filtered_df = calories_by_workout_gender[
        (calories_by_workout_gender['Workout_Type'].isin(selected_workouts)) & 
        (calories_by_workout_gender['Gender'].isin(selected_genders))
    ]
    
    # Create the stacked bar chart using Plotly Express
    fig = px.bar(
        filtered_df,
        x='Workout_Type',
        y='Calories_Burned',
        color='Gender',
        title="Total Calories Burned by Workout Type and Gender",
        labels={'Calories_Burned': 'Total Calories Burned', 'Workout_Type': 'Workout Type'},
        text='Calories_Burned'
    )
    
    # Customize layout
    fig.update_layout(barmode='stack', xaxis_title="Workout Type", yaxis_title="Total Calories Burned")
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
