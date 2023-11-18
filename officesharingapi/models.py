from django.db import models


#First created Registration database table 
class RegTable(models.Model):
    # Define your fields here
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    #Automate to name the data in table db using name in RegTable 
    def __str__(self):
        return self.name

#Created for UploadedFile Database Table 
class File(models.Model):
    file = models.FileField(upload_to='name/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    #Automate to name the data in table db using name in File 
    def __str__ (self):
        return self.file