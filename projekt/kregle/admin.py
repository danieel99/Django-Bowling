from django.contrib import admin

# Register your models here.
from .models import Zawodnik
from .models import Klub
from .models import Tor
from .models import Rezerwacja

admin.site.register(Zawodnik)
admin.site.register(Klub)
admin.site.register(Tor)
admin.site.register(Rezerwacja)

