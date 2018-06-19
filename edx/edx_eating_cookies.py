# giving cookiemonster cookies to eat

cookies_eaten = 0

while True:
    number_of_cookies = float(input("Give me a big number of cookies: "))
    cookies_eaten = cookies_eaten + number_of_cookies
    int_cookies_eaten = int(cookies_eaten)
    half_cookies = cookies_eaten - int_cookies_eaten
    text_half_cookies = ""
    if half_cookies > 0:
        text_half_cookies = "with the crumbs,"
    while number_of_cookies > 0:
        number_of_cookies = number_of_cookies - 1
        print("Nom")
    print("I ate all", int_cookies_eaten, "cookies,", text_half_cookies, "give me more!!!")
