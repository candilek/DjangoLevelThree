from django.shortcuts import render
from . import forms #form u import ettik.

def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    form =forms.FormName() #FormName classını form nesnesine içerik olarak gönderdik.
    #Bu form  nesnesini form_page.html dosyasına akatarıcaz.


    if request.method == 'POST':
        form=forms.FormName(request.POST)#gelen veriyi form nesnesine attık

        if form.is_valid(): #eğer form isteği doğru gelmişse

            print("VALIDATION SUCCESS!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAİL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])

                #form.save()

    return render(request,'basicapp/form_page.html',{'form':form})   #context: içerik olarak aktarılıyor.
