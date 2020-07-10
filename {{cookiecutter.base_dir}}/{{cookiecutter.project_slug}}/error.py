from smsframework.exc import *


class {{ cookiecutter.provider_slug.capitalize()}}ProviderError(ProviderError):
    """ Custom {{ cookiecutter.provider }} errors """

    def __init__(self, message=''):
        Implement some custom errors or delete this stuff
        super({{ cookiecutter.provider_slug.capitalize()}}ProviderError, self).__init__(message)
