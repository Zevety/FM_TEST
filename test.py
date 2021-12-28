import pytest
import shutil
import os
import sys
import manager as fm

@pytest.fixture()
def ls_fixture():
    fm.ls()
    return True
def test_ls(ls_fixture):
    assert ls_fixture == True


@pytest.fixture()
def create_fixture():
    fm.create('ind.txt')
    return True
def test_create(create_fixture):
    assert create_fixture == True


@pytest.fixture()
def rewrite_fixture():
    fm.rewrite('new.txt', 'privet')
    return True
def test_rewrite(rewrite_fixture):
    assert rewrite_fixture == True

@pytest.fixture()
def add_fixture():
    fm.add('new.txt', ', privet snova')
    return True
def test_add(add_fixture):
    assert add_fixture == True

@pytest.fixture()
def remove_fixture():
    try:
        fm.rmv('')
        return True
    except:
        return False
def test_remove(remove_fixture):
    assert remove_fixture == False

@pytest.fixture()
def rename_fixture():
    fm.rename('ind.txt', 'new_ind.txt')
    return True
def test_rename(rename_fixture):
    assert rename_fixture == True

@pytest.fixture()
def copy_fixture():
    fm.copy('CODEGEASS_NEW.txt', 'CODEGEASS2.txt')
    return True
def test_copy(copy_fixture):
    assert copy_fixture == True

@pytest.fixture()
def move_fixture():
    fm.move('CODEGEASS2.txt', 'CODEGEASS3.txt')
    return True
def test_move(move_fixture):
    assert move_fixture == True

@pytest.fixture()
def mkfold_fixture():
    fm.mkfold('newfold')
    return True
def test_mkfold(mkfold_fixture):
    assert mkfold_fixture == True

@pytest.fixture()
def cf_fixture():
    fm.cf('./newfold')
    return True
def test_cf(cf_fixture):
    assert cf_fixture == True

@pytest.fixture()
def rmfold_fixture():
    fm.rmfold('newfold')
    return True
def test_rmfold(rmfold_fixture):
    assert rmfold_fixture == True

@pytest.fixture()
def cet_fixture():
    fm.cet('new.txt')
    return True
def test_cet(cet_fixture):
    assert cet_fixture == True

@pytest.fixture()
def pwd_fixture():
    fm.pwd()
    return True
def test_pwd(pwd_fixture):
    assert pwd_fixture == True

@pytest.fixture()
def beginerLength_fixture():
    fm.beginerLength()
    return True
def test_beginerLength(beginerLength_fixture):
    assert beginerLength_fixture == True

@pytest.fixture()
def  help_fixture():
    fm.help()
    return True
def test_help(help_fixture):
    assert help_fixture == True