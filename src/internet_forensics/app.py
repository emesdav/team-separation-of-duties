from src.internet_forensics.user.user_manager import UserManager

try:
    u = UserManager(firstname="human", lastname="being", address="earth", email="Tony.bond@gmail.com",
                    mobile="123456789", password="secret", privacy=True, gdpr_marketing=True, gdpr_necessary=True)

    result = u.user_creation()
    print(result)
except Exception as e:
    print("Erorr: " + str(e))
