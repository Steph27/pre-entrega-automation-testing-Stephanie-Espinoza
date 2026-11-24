from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger

def test_inventory(driver):
    try:
        logger.info("Inicializando pruebas de inventario")
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver) 

        logger.info("Ingresando a la pagina web de pruebas")
        driver.get("https://www.saucedemo.com/")
        logger.info("Ingreso de credenciales para iniciar sesion")
        login_page.login("standard_user","secret_sauce")
        logger.info("Sesion iniciada correctamente")

        productos = inventory_page.obtener_productos()
        logger.info("Productos de la pagina web capturados")

        logger.info("Inciando verificacion de existencia de al menos un producto")
        assert len(productos) > 0 # Verificar que hay productos
        logger.info("Prueba exitosa")
        logger.info("Iniciando prueba de comparacion nombre de primer producto")
        assert inventory_page.obtener_nombre_primer_producto() == "Sauce Labs Backpack" #Verificar que el nombre del primer producto esta bien
        logger.info("Prueba exitosa")
        logger.info("Inciando prueba de comparacion precio del primer producto")
        assert inventory_page.obtener_precio_primer_producto() == "$29.99" #Verificar que el precio del primer prodcuto esta bien
        logger.info("Prueba exitosa")
        logger.info("Inciando prueba de visibilidad del menu en la pagina")
        assert inventory_page.menu_visible() #Devuelve true si es visible y pasa el test
        logger.info("Prueba exitosa")
        logger.info("Iniciando prueba de visibilidad del filtro en la pagina")
        assert inventory_page.filtro_visible() #Devuelve true si es visible y pasa el test 
        logger.info("prueba exitosa")
    except Exception:
        logger.exception("Error durante la prueba de inventario")
        raise