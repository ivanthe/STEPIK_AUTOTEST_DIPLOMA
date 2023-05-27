from faker import Faker

fake = Faker()
class Data():
    # EMAIL_FOR_REGISTRATION = fake.email()  -  Сайт не позволяет удалять акуунты,
                                            #   поэтому использование константы для этого параметра нет смысла
    PASSWORD_FOR_REGISTRATION = "just_password"     #пароль для регистрации и подтверждения

class Constants():
    BASKET_EMPTY = "Your basket is empty"    # строка в содержится в сообщение с пустой корзиной
