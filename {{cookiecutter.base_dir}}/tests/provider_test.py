# -*- coding: utf-8 -*-

import unittest
from datetime import datetime

from flask import Flask
from freezegun import freeze_time

from smsframework import Gateway, OutgoingMessage
from smsframework.providers import NullProvider
from {{cookiecutter.project_slug}} import {{ cookiecutter.provider_slug.capitalize()}}Provider


class {{ cookiecutter.provider_slug.capitalize()}}ProviderTest(unittest.TestCase):
    def setUp(self):
        # Gateway
        gw = self.gw = Gateway()
        gw.add_provider('null', NullProvider)  # provocation
        gw.add_provider('main', {{ cookiecutter.provider_slug.capitalize()}}Provider, user='kolypto', password='1234')

        # Flask
        app = self.app = Flask(__name__)

        # Register receivers
        gw.receiver_blueprints_register(app, prefix='/a/b/')

    def test_send(self):
        """ Test message send """
        gw = self.gw
        self.assertTrue(Fasle, 'Implement the test!')

    @freeze_time('2014-07-01 12:00:00')
    def test_receive_message(self):
        """ Test message receipt """
        self.assertTrue(Fasle, 'Implement the test!')
