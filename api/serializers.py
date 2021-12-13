)
 from rest.framework import serializers
 from ussd.models import *
 from .models import *

 class FarmersSerializer(serializers.models):
     class Meta :
         moodel = Farmers
         depth = l
         fields =(' __all__')