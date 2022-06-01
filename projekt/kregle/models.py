from django.db import models


class Zawodnik(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)
    plec = models.CharField(max_length=1, choices=[
        ('M', 'Mężczyzna'),
        ('K', 'Kobieta'),
        ('I', 'Coś innego'),
    ])
    pseudonim = models.CharField(max_length=20)
    nr_buta = models.IntegerField()
    nr_telefonu = models.IntegerField()
    # klub = models.ForeignKey(Klub, on_delete=models.CASCADE)

    def __str__(self):
        return self.imie + ' ' + self.nazwisko



class Klub(models.Model):
    nazwa = models.IntegerField(choices=[
        (1, 'Kręgle Club'),
        (2, 'Bilard Club'),
        (3, 'Dart Club'),
        (4, 'Brak')
    ])
    czlonkowie = models.ManyToManyField(Zawodnik, blank=True)

    def __str__(self):
        return str(self.get_nazwa_display())


class Tor(models.Model):
    dostepnosc = models.IntegerField(choices=[
        (1, 'Dostępny'),
        (2, 'Zajęty'),
    ])
    tor = models.IntegerField(choices=[
        (1, 'Krótki'),
        (2, 'Średni'),
        (3, 'Długi'),
    ])

    def __str__(self):
        return str(self.get_tor_display())
    

class Rezerwacja(models.Model):
    rezerwujacy = models.CharField(max_length=20, null=True)
    dzien = models.DateField(null=True) 
    godziny = models.IntegerField(choices=[
        (1, '15:00'),
        (2, '16:00'),
        (3, '17:00'),
        (4, '18:00'),
        (5, '19:00'),
        (6, '20:00'),
        (7, '21:00'),
        (8, '22:00'),
    ], null=True)
    tor = models.ForeignKey(Tor, null=True, on_delete=models.CASCADE)  
    osoby = models.IntegerField(choices=[
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),

    ], null=True)

    def __str__(self):
        return self.rezerwujacy + ' ' + str(self.dzien) + ' '  + str(self.get_godziny_display()) + ' ' + 'Tor ' + str(self.tor) + ' ' + str(self.osoby) + 'os.'
