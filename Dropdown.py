import dash
import dash_core_components as dcc
import dash_html_components as html

# Sample options for the dropdowns
vehicle_options = ['Sedan', 'SUV', 'Truck']
year_options = [2018, 2019, 2020, 2021]

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    [
        html.H1("Dash Application"),
        
        # Dropdown for Vehicle Type
        html.Label('Select Vehicle Type:'),
        dcc.Dropdown(
            id='vehicle-dropdown',
            options=[{'label': v, 'value': v} for v in vehicle_options],
            value=vehicle_options[0]  # Default selected value
        ),
        
        # Dropdown for Year
        html.Label('Select Year:'),
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': str(y), 'value': y} for y in year_options],
            value=year_options[0]  # Default selected value
        ),

        # Add more components as needed
    ]
)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
