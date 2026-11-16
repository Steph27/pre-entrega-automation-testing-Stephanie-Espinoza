from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver) 

    driver.get("https://www.saucedemo.com/")

    login_page.login("standard_user","secret_sauce")

    productos = inventory_page.obtener_productos()

    assert len(productos) > 0 # Verificar que hay productos

    assert inventory_page.obtener_nombre_primer_producto() == "Sauce Labs Backpack" #Verificar que el nombre del primer producto esta bien
    assert inventory_page.obtener_precio_primer_producto() == "$29.99" #Verificar que el precio del primer prodcuto esta bien

    assert inventory_page.menu_visible() #Devuelve true si es visible y pasa el test
    assert inventory_page.filtro_visible() #Devuelve true si es visible y pasa el test 
