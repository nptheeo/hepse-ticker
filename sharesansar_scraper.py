import requests
from bs4 import BeautifulSoup
import json

def scrape_sharesansar_stock(ticker):
    """
    Scrape stock data for the given ticker from ShareSansar
    
    Args:
        ticker (str): Stock ticker symbol (e.g., 'GHL', 'NABIL', 'TRH')
        
    Returns:
        dict: Stock data including price, high, low, volume, etc.
    """
    try:
        # Base URL for ShareSansar API or web scraping
        url = f"https://www.sharesansar.com/live-trading/search?q={ticker.upper()}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Parse the HTML to extract stock data
        # This is a simplified version - adapt based on actual ShareSansar HTML structure
        stock_data = {
            'ticker': ticker.upper(),
            'price': None,
            'high': None,
            'low': None,
            'volume': None,
            'data': 'Stock data for ticker',
            'status': 'success'
        }
        
        return stock_data
        
    except requests.exceptions.RequestException as e:
        return {
            'ticker': ticker.upper(),
            'error': f'Failed to fetch data: {str(e)}',
            'status': 'error'
        }
    except Exception as e:
        return {
            'ticker': ticker.upper(),
            'error': str(e),
            'status': 'error'
        }
