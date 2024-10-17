# E-commerce Price Monitoring Tool

This project is a web-based tool that allows users to scrape product data (name, price, and availability) from e-commerce websites and store the information in a database. The tool also provides a simple API for accessing the scraped data and a dashboard to visualize product prices over time.

## Features

- **Product Data Scraping**: Scrapes product names, prices, and availability from e-commerce websites such as Amazon.
- **Database Storage**: Stores the scraped data in a relational database (SQLite).
- **API**: Provides a RESTful API to access the scraped product data.
- **Dashboard**: A basic dashboard that displays product data and generates a chart visualizing product prices.

## Tech Stack

- **Backend**: Flask
- **Web Scraping**: BeautifulSoup and Selenium
- **Database**: SQLite
- **Data Visualization**: Matplotlib
- **Frontend**: HTML templates (using Jinja2)
- **API Testing**: Postman (optional)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/ecommerce-price-monitoring-tool.git
    cd ecommerce-price-monitoring-tool
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    Run the Flask app to automatically create the SQLite database.
    ```bash
    python run.py
    ```

5. **Access the app**:
    The app should now be running at `http://127.0.0.1:5000/`.

## Usage

1. **Scrape Product Data**:
    - On the homepage, paste the URL of the product page you want to scrape.
    - Click "Scrape Data" to scrape the product name, price, and availability.
    - The scraped data will be stored in the database and displayed on the home page.

2. **Access the API**:
    - The product data is available via the API at `/api/products`.
    - Example usage:
      ```bash
      curl http://127.0.0.1:5000/api/products
      ```

3. **Dashboard**:
    - A basic dashboard is available at `/dashboard` which shows a table of products and a plot of prices.

## Project Structure

```
ecommerce_price_monitoring_tool/
│
├── app/
│   ├── __init__.py          # Initialize Flask App
│   ├── models.py            # Database Models
│   ├── scraper.py           # Web Scraping Logic (BeautifulSoup/Selenium)
│   ├── api.py               # Flask API for managing requests
│   ├── dashboard.py         # Visualization (using Flask, Matplotlib)
│   ├──static/               # Static files (CSS, JS) for the dashboard
│   └──templates/            # HTML templates for the dashboard
│      └── index.html        # Dashboard HTML
│
├── config.py                # Configuration for Database and Scraping Interval
│
├── requirements.txt         # List of dependencies
├── README.md                # Documentation
└── run.py                   # Script to run the Flask app
```

## Incomplete Features

Currently, the data visualization chart is not fully functional. The chart displays the prices of all products on the same plot, rather than visualizing individual product price changes over time. This feature is under development and will be addressed in future updates.

## Future Improvements

- **Improved Price Visualization**: Display price changes over time for each individual product rather than all products on one plot.
- **Advanced Scraping**: Support for more e-commerce sites and more robust scraping (e.g., handling captchas).
- **Authentication**: Add user authentication to personalize product tracking.
- **Email Notifications**: Implement email notifications when product prices drop.

## License

This project is open-source under the MIT License.

