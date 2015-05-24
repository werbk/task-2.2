# -*- coding: utf-8 -*-
import pytest

from fixture.variables import UserLogin
from group_lib import Group, GroupBase


@pytest.fixture
def app(request):
    fixture = GroupBase()
    request.addfinalizer(fixture.restore_group)
    return fixture


def test_create_group(app):
    """Validation of correct create test group"""
    app.session.login(UserLogin.name, UserLogin.password)
    app.create_group(Group(group_name='test', group_header='test', group_footer='test'))
    app.click_group_page()
