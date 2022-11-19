from django.db import models
from django.urls import reverse
import datetime
# Create your models here.
class Faculty(models.Model):
    name=models.CharField(max_length=256)
    age=models.PositiveIntegerField()
    designation=models.CharField(max_length=50)
    faculty_id=models.CharField(max_length=5,blank=True)

    photo = models.ImageField(upload_to='photos',default='default_pic.jpg')

    MALE="male"
    FEMALE="female"

    GENDER_CHOICE=[
    (MALE,"male"),
    (FEMALE,"female")
    ]

    gender=models.CharField(
        max_length=10,
        choices=GENDER_CHOICE,
        default=MALE
    )

    dob=models.DateField(default=datetime.date.today)

    groups=[
    ("A+ve","A+ve"),
    ("B+ve","B+ve"),
    ("A-ve","A-ve"),
    ("B-ve","B-ve"),
    ("O+ve","O+ve"),
    ("AB-ve","AB-ve")
    ]

    blood_group=models.CharField(
        max_length=5,
        choices=groups,
        blank=True
    )


    aadhar_no=models.CharField(max_length=12)
    pan_no=models.CharField(max_length=10,blank=True)
    mobile=models.CharField(max_length=10,blank=True)
    email=models.EmailField(blank=True)


    state_choices = [
        ("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),
        ("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),
        ("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),
        ("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),
        ("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),
        ("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),
        ("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),
        ("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry")
        ]
    state=models.CharField(
    max_length=35,
    choices=state_choices,
    blank=True
    )
    district=models.CharField(max_length=256,blank=True)
    house_no=models.PositiveIntegerField(default=0)
    locality=models.CharField(default="unspecified",max_length=100)
    pin=models.CharField(max_length=6,blank=True)
    permanent_address_is_same_as_current_address=models.BooleanField(default=True)


    qualification_choices=[
    ("SSC","SSC"),
    ("Inter","Inter"),
    ("UG","UG"),
    ("PG","PG"),
    ("Phd","Phd"),
    ("Others","Others")
    ]
    qualification=models.CharField(
    max_length=25,
    choices=qualification_choices,
    blank=True
    )
    college=models.CharField(max_length=100,blank=True)
    graduation_year=models.CharField(max_length=4,blank=True)
    university=models.CharField(max_length=60,blank=True)
    percentage=models.DecimalField(decimal_places=2,max_digits=5,default=0.00)

    award=models.CharField(max_length=100,blank=True)
    year_of_award=models.CharField(max_length=4,blank=True)
    organisation_of_award=models.CharField(max_length=50,blank=True)

    #journals
    publication_journal_name=models.CharField(max_length=100,blank=True)
    publication_journal_vol=models.PositiveIntegerField(default=1)
    issn_no=models.PositiveIntegerField(default=0)
    publisher=models.CharField(max_length=100,blank=True)
    year_of_publication=models.CharField(max_length=4,blank=True)
    article_title=models.CharField(max_length=50,blank=True)




    #r&d
    project_title=models.CharField(max_length=100,blank=True)
    duration=models.PositiveIntegerField(default=1)
    cost_of_project=models.DecimalField(decimal_places=5,max_digits=10,default=0.00)
    funding_agency=models.CharField(max_length=100,blank=True)
    start_date=models.DateField(default=datetime.date.today)
    end_date=models.DateField(default=datetime.date.today)



    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk' :self.pk})

    def __str__(self):
        return self.name
