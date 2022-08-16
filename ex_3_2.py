from builtins import input


def usr_func(u_name, u_fam, u_year, u_city, u_email, u_tel):
    print(f"Данные юзера: имя-{u_name}, фамилия-{u_fam}, год рождения-{u_year}, город проживания-{u_city}, email-{u_email}, телефон-{u_tel}")


user_name = input("Введите имя пользователя:")
user_fam = input("Фамилия:")
user_year = input("Год рождения:")
user_city = input("Город проживание:")
user_email = input("Эл.почту:")
user_tel = input("Телефон:")

usr_func(
    u_tel = user_tel,
    u_email = user_email, 
    u_city= user_city,
    u_fam= user_fam,
    u_name= user_name,
    u_year= user_year)


