from . import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    availability = db.Column(db.String(20), nullable=False)
    link = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Product {self.name} - {self.price}>'
    
def save_product(name, price, availability, link):
    product = Product(name=name, price=price, availability=availability, link=link)
    db.session.add(product)
    db.session.commit()