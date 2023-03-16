from source.utiles import all_utiles as u

class locator:

    locCarts = dict()

    locCarts['Cart_Place_Order_Button'] = (u.By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
    locCarts['Filed_Name'] = (u.By.XPATH, '//*[@id="name"]')
    locCarts["Filed_Country"] = (u.By.XPATH, '//*[@id="country"]')
    locCarts["Filed_City"] = (u.By.XPATH, '//*[@id="city"]')
    locCarts["Filed_Credit_Card"] = (u.By.XPATH, '//*[@id="card"]')
    locCarts["Filed_Month"] = (u.By.XPATH, '//*[@id="month"]')
    locCarts["Filed_Year"] = (u.By.XPATH, '//*[@id="year"]')
    locCarts["Close_Button"] = (u.By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[1]')
    locCarts["Purchase_Button"] = (u.By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]')
    locCarts["Ok_Button"] = (u.By.XPATH, '/html/body/div[10]/div[7]/div/button')


