import streamlit as st
import yfinance as yf
from datetime import datetime
import plotly.graph_objects as go

# Function to fetch stock data


def get_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Main function for the Streamlit app


def main():
    st.title('Interactive Financial Market Analysis')

    # Sidebar for user inputs
    st.sidebar.header('User Input Options')
    # Default to Apple Inc.
    selected_stock = st.sidebar.text_input(
        'Enter Stock Ticker', 'AAPL').upper()

    # Date input for start and end date
    start_date = st.sidebar.date_input("Start Date", datetime(2023, 1, 1))
    end_date = st.sidebar.date_input("End Date", datetime(2023, 12, 31))

    # Validate the date range
    if start_date < end_date:
        stock_data = get_stock_data(selected_stock, start_date, end_date)
        st.write(f"Displaying data for: {selected_stock}")
        st.write(stock_data)

        # Plotting with Plotly
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=stock_data.index,
            y=stock_data['Close'],
            mode='lines',
            name='Close'
        ))

        fig.update_layout(
            title=f'{selected_stock} Closing Prices',
            xaxis_title='Date',
            yaxis_title='Closing Price',
            xaxis_rangeslider_visible=True
        )

        st.plotly_chart(fig)
    else:
        st.error('Error: End date must fall after start date.')


if __name__ == '__main__':
    main()

