from django.db import models


class Feature(models.Model):
    name = models.CharField(max_length=40)


    def __str__(self):
        return self.name
    
    
    def __unicode__(self):
        return self.name


# class Voicedness(models.Model):
#     name = models.CharField(max_length=5)
#     def __str__(self):
#         return self.ipa
    
    
#     def __unicode__(self):
#         return self.ipa

# class Aspiration(models.Model):
#     name = models.CharField(max_length=5)
#     def __str__(self):
#         return self.ipa
    
    
#     def __unicode__(self):
#         return self.ipa


class Place(models.Model):
    name = models.CharField(max_length=40)


    def __str__(self):
        return self.name
    
    
    def __unicode__(self):
        return self.name


class Manner(models.Model):
    name = models.CharField(max_length=40)


    def __str__(self):
        return self.name
    
    
    def __unicode__(self):
        return self.name


class VowelHorizontalPosition(models.Model):
    name = models.CharField(max_length=40)


    def __str__(self):
        return self.name
    
    
    def __unicode__(self):
        return self.name


class VowelVerticalPosition(models.Model):
    name = models.CharField(max_length=40)


    def __str__(self):
        return self.name
    
    
    def __unicode__(self):
        return self.name


class Roundedness(models.Model):
    name = models.CharField(max_length=40)


    def __str__(self):
        return self.name
    
    
    def __unicode__(self):
        return self.name



class Length(models.Model):
    name = models.CharField(max_length=40)


    def __str__(self):
        return self.name
    
    
    def __unicode__(self):
        return self.name



class Consonant(models.Model):
    ipa = models.CharField(max_length=5)
    features = models.ManyToManyField(Feature)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    manner = models.ForeignKey(Manner, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ipa
    
    
    def __unicode__(self):
        return self.ipa


class Vowel(models.Model):
    ipa = models.CharField(max_length=5)
    horizontal = models.ForeignKey(VowelHorizontalPosition, on_delete=models.CASCADE)
    vertical = models.ForeignKey(VowelVerticalPosition, on_delete=models.CASCADE)
    roundedness = models.ForeignKey(Roundedness, on_delete=models.CASCADE)
    length = models.ForeignKey(Length, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ipa
    
    
    def __unicode__(self):
        return self.ipa





class Affricate(models.Model):
    ipa = models.CharField(max_length=5)
    # features = models.ManyToManyField(Feature)
    first = models.ForeignKey(Consonant, on_delete=models.CASCADE, related_name='affricate_first_element')
    second = models.ForeignKey(Consonant, on_delete=models.CASCADE, related_name='affricate_second_element')
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    manner = models.ForeignKey(Manner, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ipa
    
    
    def __unicode__(self):
        return self.ipa





