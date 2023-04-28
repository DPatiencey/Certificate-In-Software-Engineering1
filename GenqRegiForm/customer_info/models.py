from django.db import models

# Create your models here.
class Category (models.Model):
    name = models.CharField (max_length= 50, null= True, blank= True)
    def __str__(self):
        return self.name
    
class Bio_Data(models.Model):
    # Here we are connecting products model to category model
    # A foreign key is in one table that is being used by another table
    # In this case the foreign key is given to us by django and it is here to reference to the category table
    category_name = models. ForeignKey (Category, on_delete = models.CASCADE, null = True, )  

    customer_Fname = models.CharField (max_length= 50, null= True, blank = True)
    custome_Lname = models.CharField (max_length= 50, null= True, blank = True)
    date_of_birth = models.DateField (auto_now_add= True)
    gender = models.CharField (max_length= 50, null= True, blank = True)
    
    def __str__(self):
        return self.Bio_data
    
class Location (models.Model):
    country = models.CharField (max_length= 50, null= True, blank= True)
    state = models.CharField (max_length= 50, null= True, blank= True)
    town = models.CharField (max_length= 50, null= True, blank= True)
    zip_code = models.IntegerField (default= 0, null= True, blank= True)
    # date = models.DateField (auto_now_add = True,)
    def __str__(self):
        return self.Location

class Contacts_and_Address (models.Model):
    phone_number1 = models.IntegerField (default= 0, null= True, blank= True)
    phone_number2 = models.IntegerField (default= 0, null= True, blank= True)
    email = models.CharField (max_length= 50, null= True, blank= True)

    def __str__(self):
        return self.Contacts

