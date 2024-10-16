import matplotlib.pyplot as plt
from flask import Blueprint, flash, render_template, request, redirect, url_for
from app.models import Product
from app.scraper import scrape_product_data

app = Blueprint('dashboard', __name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product_link = request.form.get('product-url')
        if product_link:
            try:
                scrape_product_data(product_link)
                flash('Product data scraped successfully!', 'success')
            except Exception as e:
                flash(f'Error scraping product data: {e}', 'danger')
            return redirect(url_for('dashboard.index'))


    products = Product.query.all()
    prices = [p.price for p in products]  # Convert prices to float
    product_names = [p.name for p in products]

    if prices:  # Check if prices list is not empty
        plt.figure(figsize=(10, 5))
        plt.plot(product_names, prices, marker='o', label='Price',)
        plt.xlabel('Products')
        plt.ylabel('Price ($)', )
        plt.title('Product Prices Over Time')
        plt.xticks(rotation=45)
        plt.ylim(min(prices), max(prices))
        plt.legend()
        plt.tight_layout()
        plt.savefig('app/static/price_chart.png')
        plt.close()  # Close the plot to prevent display issues

    return render_template('index.html', products=products)
