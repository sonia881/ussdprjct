from django.http.response import HttpResponse
from django.shortcuts import render
import africastalking
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def  welcome(request):
    return render(request, 'index.html')

#  python3 -m pip install africastalking
AfricasUsername='soniauwase@gmail.com'
api_key ='0788ac9244190cb1e9307dc01ec6c2fdedcdabd1ea1ee70253c639ee5ce0df5b'
africastalking.initialize(AfricasUsername,api_key)

@csrf_exempt
def ussdApp(request):

    if request.method == 'POST':

        session_id = request.POST.get("sessionId")
        service_code = request.POST.get("serviceCode")
        phone_number =request.POST.get("phoneNumber")
        text = request.POST['text']
        level = text.split('*')
        category = text[:3]
        response =""
        #  main menu for our application
        if text == '':
            response =  "CON Kugura no gutumiza imyenda n'inkweto by'abakobwa n'abagore \n"
            response += "1. BUYING \n"
            response += "2. ORDERING AND DELIVERY \n"
        elif text == '1':
            response = "CON Hitamo \n"
            response += "1. Closes \n"
            response += "2. Shoes \n"
        elif text == '1*1':
            products= Productsmodel.objects.all()
            response ="CON Hitamo umwenda"
            for product in products:
                response+= ""+str(product.id)+". "+str(product.title)+"\n"
            response = "CON Choose type of clothes' "+str(product)+"\n" 
            response = "1. Trousers\n" 
            response = "2. Shirts, T- shirts or Tops \n" 
            response = "3. Dresses \n"
        elif text == '1*2':
            response ="CON Choose type of shoes' "+str(product)+"\n"
            response =" 1. male shoes \n"
            response = " 2. female shoes\n" 
        elif text == '2*1':
            response = "CON Choose type of clothes' "+str(product)+"\n"
            response =" 1. Trousers\n"
            response = " 2. Shirts, T- shirts or Tops\n" 
            response = " 3. Dresses\n"
        elif text == '2*2':
            response = "CON Choose type of shoes' "+str(product)+"\n" 
            response += "1. Male shoes \n"
            response += "2. Female shoes  \n"
        elif text == '2*1':
            response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe rimwe mukwezi"
        elif text == '2*2':
            response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe kabiri mukwezi"
        elif text == '2*3':
            response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe Buri munsi"

        else:
            response = "END Ukanze ibitaribyo, ongera mukanya"
        return HttpResponse(response)
    else:
        return HttpResponse('we are on ussd app')