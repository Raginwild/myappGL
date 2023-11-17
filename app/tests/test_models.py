# tests/test_models.py
from  import User

def test_creation_utilisateur():
    user = User(id_user='1',username='testuser', email='test@user.fr', id_fonction='1')
    assert user.username == 'testuser'
    assert user.id_user == '1'
    assert user.email == 'test@user.fr'
    assert user.id_fonction == '1'

