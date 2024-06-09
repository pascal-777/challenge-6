class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if len(value) == 0:
            raise ValueError("Name must be greater than zero characters.")
        self._name = value

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        if hasattr(self, '_hometown'):
            raise AttributeError("Hometown is immutable.")
        if not isinstance(value, str):
            raise TypeError("Hometown must be a string.")
        if len(value) == 0:
            raise ValueError("Hometown must be greater than zero characters.")
        self._hometown = value

    def concerts(self):
        return [concert for concert in Concert.all if concert.band == self]

    def venues(self):
        return list({concert.venue for concert in Concert.all if concert.band == self})

    def play_in_venue(self, venue, date):
        return Concert(date, self, venue)

    def all_introductions(self):
        return [f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}" 
                for concert in Concert.all if concert.band == self]


class Concert:
    all = []

    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError("Date must be a string.")
        if len(value) == 0:
            raise ValueError("Date must be greater than zero characters.")
        self._date = value

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if not isinstance(value, Band):
            raise TypeError("Band must be of type Band.")
        self._band = value

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if not isinstance(value, Venue):
            raise TypeError("Venue must be of type Venue.")
        self._venue = value

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if len(value) == 0:
            raise ValueError("Name must be greater than zero characters.")
        self._name = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if not isinstance(value, str):
            raise TypeError("City must be a string.")
        if len(value) == 0:
            raise ValueError("City must be greater than zero characters.")
        self._city = value

    def concerts(self):
        return [concert for concert in Concert.all if concert.venue == self]

    def bands(self):
        return list({concert.band for concert in Concert.all if concert.venue == self})

    def concert_on(self, date):
        return next((concert for concert in Concert.all if concert.venue == self and concert.date == date), None)
