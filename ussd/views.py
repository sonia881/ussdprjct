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
            response += "1. Kugura \n"
            response += "2. Gutumiza \n"
        elif text == '1':
            response = "CON Hitamo \n"
            response += "1. Imyenda \n"
            response += "2. Inkweto \n"
        elif text == '1*1':
            products= Productsmodel.objects.all()
            response ="CON Hitamo umwenda"
            for product in products:
                response+= ""+str(product.id)+". "+str(product.title)+"\n"
            response = "CON Hitamo ubwoko bw'umwenda' "+str(product)+"\n" 
            response = "1. Ipantaro \n" 
            response = "2. Umupira cyangwa ishati \n" 
            response = "3. Ikanzu \n"


        elif text == '1*2':
            product ="Inkweto"
            response ="CON ' "+str(product)+"\n"
        elif 
            response = "CON  \n"
        elif 
            response = "CON  \n"
        elif 

        
            response = "END Murakoze kwiyandikisha kuri Ida farm \n"
         
        #  ======================== INGENGABIHE==================
        elif text == '2':
            response = "CON Hitamo igihe \n "
            response += "1. Rimwe mukwezi \n"
            response += "2. Kabiri Mukwezi \n"
            response += "3. Buri gihe"
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