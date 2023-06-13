from django.shortcuts import render
from rest_framework import generics
from .models import Customer
from .serializer import CustomerSerializer
from rest_framework.renderers import TemplateHTMLRenderer ,JSONRenderer
from django.shortcuts import redirect

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'eapp/profile_create.html'

    def get(self, request):
        print(self.__dict__)
        if '/customer/' in request.GET:
            print("checck")
            return render({'template_name': 'profile_create.html'})
        else:
            customers = self.queryset.all()
            serializer = self.serializer_class(customers, many=True)
            context = {'customers': serializer.data}
            return render(request, "eapp/profile_list.html", context)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            return redirect('eapp:customer-list')
        else:
            context = {'form': serializer}
            return render(request, 'eapp/profile_create.html', context)  

    
class CustomerRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    