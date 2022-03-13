from django.views.generic import ListView
from products.models import Product

class PublicProductView(ListView):
    model = Product
    template_name = "publicProducts/public_store.html"    

# Create your views here.
