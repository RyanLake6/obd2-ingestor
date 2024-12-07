import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import time
import random

class DashClient:
    def __init__(self):
        self.app = None
        self.x_data = []
        self.y_data = []
    
    def create_app(self):
        self.app = dash.Dash(__name__)

        # Define the layout of the app
        self.app.layout = html.Div(
            children=[
                html.H1("Real-Time Plotly Update Example"),
                dcc.Graph(id="live-update-graph"),
                dcc.Store(id="x_data_store", data=[]),  # Store for x_data
                dcc.Store(id="y_data_store", data=[]),  # Store for y_data
                dcc.Interval(
                    id="interval-component",
                    interval=1000,  # Update every 1000 ms (1 second)
                    n_intervals=0
                ),
            ]
        )

        # Define callback to update the plot and store data
        @self.app.callback(
            Output("live-update-graph", "figure"),
            Output("x_data_store", "data"),  # Output updated x_data
            Output("y_data_store", "data"),  # Output updated y_data
            Input("interval-component", "n_intervals"),
            State("x_data_store", "data"),  # Get the current stored x_data
            State("y_data_store", "data"),  # Get the current stored y_data
        )

        def update_plot(n, x_data, y_data):
            # Simulate new data (e.g., from a sensor or real-time data source)
            # new_x = time.time()
            # new_y = random.randint(0, 100)

            # Append new data
            if self.x_data and self.y_data:
                x_data = self.x_data
                y_data = self.y_data

            # Only keep the last 50 data points to avoid overcrowding the plot
            x_data = x_data[-50:]
            y_data = y_data[-50:]

            # Create the plot
            figure = {
                "data": [go.Scatter(x=x_data, y=y_data, mode="lines+markers")],
                "layout": go.Layout(
                    title="Live Data Update",
                    xaxis={"title": "Time", "rangeslider": {"visible": True}},
                    yaxis={"title": "Value"},
                    plot_bgcolor='#121212',  # Set the plot background to dark
                    paper_bgcolor='#121212',
                ),
            }

            return figure, x_data, y_data  # Return updated figure and data


    def update_data(self, new_x, new_y):
        """Method to update the plot data from outside the class"""
        self.x_data.append(new_x)
        self.y_data.append(new_y)

    def run_dash(self):
        self.app.run_server(debug=True)


# # Create a Dash app
# app = dash.Dash(__name__)

# # Define the layout of the app
# app.layout = html.Div(
#     children=[
#         html.H1("Real-Time Plotly Update Example"),
#         dcc.Graph(id="live-update-graph"),
#         dcc.Store(id="x_data_store", data=[]),  # Store for x_data
#         dcc.Store(id="y_data_store", data=[]),  # Store for y_data
#         dcc.Interval(
#             id="interval-component",
#             interval=1000,  # Update every 1000 ms (1 second)
#             n_intervals=0
#         ),
#     ]
# )



