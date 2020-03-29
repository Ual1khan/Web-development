from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse,JsonResponse
from django.http.request import HttpRequest
from api.models import Product,Category
# Create your views here.
def product_list(request):
    products = Product.objects.all()
    product_json = [product.to_json() for product in products]
    return JsonResponse(product_json,safe=False)
def product_details(request,p_id):

    try:
        product = Product.objects.get(id=p_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'Error':str(e)})
    return JsonResponse(product.to_json())

def category_list(request):
    categories = Category.objects.all()
    category_json = [category.to_json() for category in categories]
    return JsonResponse(category_json, safe=False)
def category_details(request,c_id):

    try:
        category = Category.objects.get(id=c_id)

    except Category.DoesNotExist as e:
        return JsonResponse({'Error':str(e)})

    return JsonResponse(category.to_json())

def category_products(request,c_id):
    # products= Product.objects.all()
    #
    # cat_products =[]
    #
    # try:
    #      for product in products:
    #         if(product.category_id_id==c_id):
    #             cat_products.append(product)
    # except Product.DoesNotExist as e:
    #     return JsonResponse({'Error': str(e)})

    try:
        pp = Product.objects.filter(category_id_id=c_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'Error':str(e)})
    # catP_json = [product.to_json() for product in cat_products]
    catP2_json = [product.to_json() for product in pp]

    return  JsonResponse(catP2_json, safe=False)