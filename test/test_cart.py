from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from utils.reader import read_productos_json
from utils.logger import logger

def test_cart(driver):
    try:
        logger.info("Inicializacion prueba de carrito")
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver) 
        cart_page = CartPage(driver)

        logger.info("Ingresando a la pagina web de prueba")
        driver.get("https://www.saucedemo.com/")
        logger.info("Ingreso de credenciales para iniciar sesion")
        login_page.login("standard_user","secret_sauce")
        logger.info("Sesion iniciada correctamente")

        logger.info("Lectura del primer producto desde archivo formato json")
        producto = read_productos_json()[0] #Lee el primer producto del archivo productos.json

        logger.info("Agregando producto al carrito")
        inventory_page.agregar_producto(producto["nombre"])

        logger.info("Inciando verificacion de producto agregado al carrito")
        #Validar que agrego el producto al carrito
        assert inventory_page.obtener_contador_carrito() == "1"
        logger.info("Prueba exitosa")

        logger.info("Ir a la pagina del carrrito")
        #Ir al carrito
        inventory_page.ir_al_carrito()

        logger.info("Iniciando prueba de comparacion de nombre producto")
        #Validar nombre contra el JSON
        assert cart_page.obtener_nombre_producto() == producto["nombre"]
        logger.info("Prueba exitosa")

        logger.info("Iniciando prueba de comparacoin de precio producto")
        #Validar precio contra el JSON
        assert cart_page.obtener_precio_producto() == producto["precio"]
        logger.info("Prueba exitosa")
    except Exception:
        logger.exception("Error durante la prueba del carrito")
        raise