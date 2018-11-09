from django import forms
from django.core import validators #validators=doğrulayıcı (Hata kontrol işlemi) import ettik

class FormName (forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    verify_email=forms.EmailField(label='Enter your email again:') #kullanıcının email'i bir daha girmesini isteyerek yanlış girmeye karşı önlem aldık.
    text=forms.CharField(widget=forms.Textarea)

   #oluşturduğumuz formun tamamını  bir kerede temizlemek için clean metodunu oluşturalım.
    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['email'] #ilk girilen email
        vmail=all_clean_data['verify_email']#doğğrulanmış email


        # ilk girilen email ile ikinci girilen email eşit değilse hata mesajı versin.
        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")


    #def clean_botcatcher(self): #hata yakalama
                      #Eğer formdaki değer bot tarafından değiştirilmişse, o zaman bu işlev botu yakalayacak ve doğrulama hatasını verecektir.
        #botcatcher = self.cleaned_data['botcatcher']
        #if len(botcatcher) > 0:
            #raise forms.ValidationError("Gotcha BOT")
            #return botcatcher
