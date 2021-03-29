from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Utilisateur(AbstractUser):
      class Meta:
          permissions = [
              ("perm_administrerRef", "peut acceder a la vue administration referentiel"),
              ("perm_publicite", "peut acceder a la vue publicite"),
              ("perm_commandes", "peut acceder a la vue commandes"),
          ]