# Note: Missing imports 

class Event(models.Model):
    title = models.CharField(max_length=200)
    date_published = models.DateTimeField('published date',default=datetime.now, blank=True)
    date_start = models.DateTimeField('start date')
    date_end = models.DateTimeField('end date')
    description = models.TextField()
    price = models.IntegerField(null=True, blank=True)
    venue = models.ForeignKey(Venue)


class Venue(models.Model):
    title = models.CharField(max_length=200)
    date_published = models.DateTimeField('published date',default=datetime.now, blank=True)
    venue_address = models.CharField(max_length=200)
    venue_city = models.CharField(max_length=200)
    venue_state = models.CharField(max_length=200)
    venue_country = models.CharField(max_length=200)
    description = models.TextField()


# List all the fields for a given model
Event._meta.get_fields()
event = Event.objects.last()
event._meta.get_fields()

############################ Foreign key reverse look up ############################
# Assume the two different models

# Pay attention to ralated_name if getting errors.
venue = Venue.objects.last()
venue.event_set.all()

# You can also use the following if want to go the other way around.
Event.objects.filter(venue__id=venue.id)
