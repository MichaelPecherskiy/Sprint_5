from faker import Faker

fake = Faker()


class Constants:
    EMAIL = 'test@qa.qa'
    PASSWORD = 123321
    NAME = fake.name()
    URL_MAIN_PAGE = "https://stellarburgers.nomoreparties.site/"
    URL_LOGIN = 'https://stellarburgers.nomoreparties.site/login'
    URL_PROFILE = 'https://stellarburgers.nomoreparties.site/account/profile'
