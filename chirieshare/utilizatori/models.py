from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    #Necesar pentru a scoate username de la required

    def create_user(self, email, password, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=email, is_staff=True, is_superuser=True, **kwargs)
        user.set_password(password)
        user.save()
        return user


class Utilizator(AbstractUser):
    """ Tabel info utilizator 
        nume            - extras automat din email ([nume]@gmail.com)
        email           - se va loga cu emailul
        parola          - *** 
        descriere       - informatiile despre utilizator scrise de acesta pentru celilati potential colegi de apartament
        ocupatie        - tipul jobului
        sex             - mf
        varsta          - 
        buget           - 
        imagine_profil  - imagine profil
        cont_admin      - are access la backend, administratorul poate gestiona utilizatorii si anunturile
        cont_premium: regular: cont gratis poate avea activ doar un anunt, 
                      premium: cont platit poate avea activ unul sau mai multe anunturi, 
                               poate vedea statistici cu privire la anunturile postate
                               primeste prin email atunci cand un anunt a fost postat
        Un utilizator poate avea unul sau mai multe anunturi postate si/sau unul sau mai multe anunturi salvate la favorite
    """
    email      = models.EmailField(unique=True)
    descriere  = models.CharField(max_length=255, blank=True)
    ocupatie   = models.CharField(max_length=50, blank=True, default="nespecificat")
    nume       = models.CharField(max_length=50, blank=True)
    sex        = models.CharField(max_length=1, blank=True, default="N")
    varsta     = models.PositiveIntegerField(blank=True, null=True)
    buget      = models.PositiveIntegerField(blank=False, null=True)
    telefon    = models.CharField(max_length=20, blank=True, default="nespecificat")
    imagine_profil  = models.ImageField(blank=True, upload_to="utilizatori/", default="utilizatori/imagine_profil.svg")
    cont_premium    = models.BooleanField(default=False)
    
    token = models.CharField(max_length=1, blank=True)
    
    #Scoatem field/coloanele 
    first_name = None
    last_name  = None

    #Necesare pentru a inlocui username cu email
    username  = None
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []
    objects   = UserManager()
    
    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name_plural = "Utilizatori"

    