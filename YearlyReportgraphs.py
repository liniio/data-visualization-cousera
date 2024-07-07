import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Sample options for the dropdowns
vehicle_options = ['Sedan', 'SUV', 'Truck']
year_options = [2018, 2019, 2020, 2021]

# Sample data for demonstration
data = {'Year': [2018, 2018, 2018, 2019, 2019, 2019, 2020, 2020, 2020, 2021, 2021, 2021],
        'Sales': [12000, 14000, 10000, 11000, 9500, 7500, 16000, 18000, 12000, 20000, 22000, 25000],
        'AveragePrice': [25000, 24000, 26000, 27000, 28000, 26000, 30000, 28000, 32000, 35000, 33000, 31000],
        'VehicleType': ['Sedan', 'SUV', 'Truck', 'Sedan', 'SUV', 'Truck', 'Sedan', 'SUV', 'Truck', 'Sedan', 'SUV', 'Truck'],
        'Recession': [0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0]}
df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    [
        html.H1("Yearly Report Statistics"),
        
        # Dropdown for Vehicle Type
        html.Label('Select Vehicle Type:'),
        dcc.Dropdown(
            id='vehicle-dropdown',
            options=[{'label': v, 'value': v} for v in vehicle_options],
            value=vehicle_options[0]  # Default selected value
        ),
        
        # Graph for Sales
        dcc.Graph(id='sales-graph'),

        # Graph for Average Price
        dcc.Graph(id='average-price-graph'),

        # Add more components as needed
    ]
)

# Callback to update graphs based on dropdown values
@app.callback(
    [Output('sales-graph', 'figure'),
    Output('average-price-graph', 'figure')],
    [Input('vehicle-dropdown', 'value')]
)
def update_graphs(vehicle_type):
    # Filter data based on selected values
    filtered_data = df[df['VehicleType'] == vehicle_type]

    # Create Sales graph
    sales_fig = px.bar(filtered_data, x='Year', y='Sales', title=f'Sales for {vehicle_type} by Year')

    # Create Average Price graph
    avg_price_fig = px.line(filtered_data, x='Year', y='AveragePrice', title=f'Average Price for {vehicle_type} by Year')

    return sales_fig, avg_price_fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
