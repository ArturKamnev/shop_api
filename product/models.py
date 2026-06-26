from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    @property
    def products_count(self):
        products = self.products.all() # pyright: ignore[reportAttributeAccessIssue]
        return len(products)

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self) -> str:
        return self.title
    
    @property
    def rating(self):
        reviews = self.reviews.all() # pyright: ignore[reportAttributeAccessIssue]

        if not reviews.exists():
            return 0

        total = sum(review.stars for review in reviews)
        count = reviews.count()
        return total / count
    

class Review(models.Model):
    text = models.TextField(max_length=300)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    # vscode почему то ругаеться на строку stars поэтому я добавил игноры
    stars = models.IntegerField(choices=((i, i) for i in range(1, 6)), null=True) # pyright: ignore[reportCallIssue, reportArgumentType]

    def __str__(self) -> str:
        return self.product.title
    