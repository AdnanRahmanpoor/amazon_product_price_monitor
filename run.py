from app import create_app, db
from app.models import Product

app = create_app()

# Create database
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)