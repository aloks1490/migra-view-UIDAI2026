import plotly.express as px
from prophet import Prophet

def create_district_bar_chart(filtered_df, update_type):
    """Generates the Top 20 Districts horizontal bar chart."""
    map_data = (
        filtered_df.groupby('district')['total_updates']
        .sum()
        .reset_index()
        .sort_values('total_updates', ascending=False)
        .head(20)
    )

    fig = px.bar(
        map_data,
        x='total_updates',
        y='district',
        orientation='h',
        color='total_updates',
        color_continuous_scale='Viridis',
        title=f"Top 20 Districts by {update_type} Volume",
        labels={'total_updates': 'Total Updates', 'district': 'District'}
    )

    fig.update_layout(
        height=600,
        showlegend=False,
        yaxis={'categoryorder': 'total ascending'}
    )
    return fig

def run_forecast(filtered_df):
    """Prepares data, runs Prophet, and returns the forecast figure."""
    prophet_df = (
        filtered_df.groupby('date')['total_updates']
        .sum()
        .reset_index()
        .dropna()
    )
    prophet_df.columns = ['ds', 'y']

    if len(prophet_df) > 2:
        m = Prophet(yearly_seasonality=True)
        m.fit(prophet_df)

        future = m.make_future_dataframe(periods=90)
        forecast = m.predict(future)

        fig = px.line(
            forecast, x='ds', y='yhat', 
            title="90-Day Aadhaar Update Demand Forecast"
        )
        
        fig.add_scatter(
            x=prophet_df['ds'], y=prophet_df['y'], 
            name="Actual Historical Updates",
            mode='markers', marker=dict(size=6, color='red')
        )
        
        fig.update_layout(xaxis_title="Timeline", yaxis_title="Number of Updates")
        return fig
    return None