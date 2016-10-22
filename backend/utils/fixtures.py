import pytest
import mongoengine as me


@pytest.fixture
def mongomock(request):
    db = me.connect('testdb', host='mongomock://localhost')
    yield db
    db.drop_database('testdb')
    db.close()


@pytest.fixture
def mongo(request):
    db = me.connect('testdb', host='mongodb://localhost')
    yield db
    db.drop_database('testdb')
    db.close()
