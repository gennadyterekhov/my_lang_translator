from django.contrib import admin

# Register your models here.
from phonology.models import Consonant, Vowel, Manner, Place, Affricate, Feature, VowelHorizontalPosition, VowelVerticalPosition, Roundedness, Length
# from phonology.models import Voicedness, Aspiration
admin.site.register(Consonant)
admin.site.register(Vowel)

admin.site.register(Manner)
admin.site.register(Place)
# admin.site.register(Voicedness)
# admin.site.register(Aspiration)

admin.site.register(Affricate)
admin.site.register(Feature)

admin.site.register(VowelHorizontalPosition)
admin.site.register(VowelVerticalPosition)
admin.site.register(Roundedness)
admin.site.register(Length)
