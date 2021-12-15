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
            response =  "CON WELCOME ON HAHA \n"
            response += "1. BUYING \n"
            response += "2. ORDERING AND DELIVERY \n"
        elif text == '1':
            response = "CON Hitamo \n"
            response += "1. Clothes \n"
            response += "2. Shoes \n"
        elif text == '1*1':
            response = "CON Choose type of clothes \n " 
            response += "1. Trousers\n"     
            response += "2. Dresses \n" 
            response += "3. Shirts \n"
            response += "4. T-shirts \n"
            response += "5. Tops \n"
        elif text == '1*1*1':
            response ="CON Which type\n"
            response += "1. jeans \n"
            response += "2. mampa \n "
            response += "3. suitelike pants \n"
        elif text =='1*1*1*1':
            response ="CON Enter size and mode of payment"
            response = "Enter phone number"
        elif text =='1*1*1*2':
            response ="CON Enter size and mode of payment"
            response = "Enter phone number"
        elif text =='1*1*1*3':
            response ="CON Enter size and mode of payment"
            response = "Enter phone number"
        elif text =='1*1*2':
            response ="CON Which type \n"
            response += "1. jeans \n"
            response += "2. mampa \n "
            response += "3. suitelike shirts \n"
        elif text =='1*1*2*1':
            response ="CON Enter size and mode of payment"
            response = "Enter phone number"
        elif text =='1*1*2*2':
            response ="CON Enter size and mode of payment"
            response = "Enter phone number"
        elif text =='1*1*2*3':
            response ="CON Enter size and mode of payment"
            response = "Enter phone number"
        elif text =='1*1*3':
            response =""
        elif text == '1*2':
            response ="CON Choose type of shoes \n"
            response += " 1. boots \n"
        elif text == '1*2*1':
            response =" "
            response += " 2. high heels \n"
        elif text =='1*2*2':
            response =""
            response += " 3. wedge \n"
        elif text =='1*2*3':
            response =""
            response += " 4. sandals \n"
        elif text =='1*2*4':
            response =""
        elif text =='2':
            response = "CON Hitamo \n"
            response += "1. Clothes \n"
            response += "2. Shoes \n" 
        elif text == '2*1':
            response = "CON Choose type of clothes \n"
            response +=" 1. Trousers\n"
            response += " 2. Shirts, T- shirts or Tops\n" 
            response += " 3. Dresses\n"
        elif text == '2*2':
            response = "CON Choose type of shoes \n" 
            response += "1. Male shoes \n"
            response += "2. Female shoes  \n"
        else:
            response = "END Ukanze ibitaribyo, ongera mukanya"
        return HttpResponse(response)
    else:
        return HttpResponse('we are on ussd app')