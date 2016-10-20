import factory as f
import factory.fuzzy as fuzzy
from factory.mongoengine import MongoEngineFactory
from faker import Factory as FakerFactory

from .models import Category, Site


faker = FakerFactory.create()


def get_random_coordinates():
    coord_generator = fuzzy.FuzzyDecimal(-180, 180, 6)
    return [str(coord_generator.fuzz()), str(coord_generator.fuzz())]


class CategoryFactory(MongoEngineFactory):
    name = f.Sequence(lambda n: 'category %s' % n)
    description = f.LazyAttribute(lambda x: faker.text())

    class Meta:
        model = Category
        inline_args = ('name', )


class SiteFactory(MongoEngineFactory):
    name = f.Sequence(lambda n: 'location %s' % n)
    description = f.LazyAttribute(lambda x: faker.text())
    coordinates = f.LazyAttribute(lambda x: get_random_coordinates())

    class Meta:
        model = Site
        inline_args = ('name', )
