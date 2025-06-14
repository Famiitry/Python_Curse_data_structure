# Definimos una clase llamada Solution
class Solution(object):

    # Definimos una función llamada maxProfit que recibe una lista de precios (uno por cada día)
    def maxProfit(self, prices):
        """
        :type prices: List[int]   # La lista 'prices' contiene los precios de una acción por día
        :rtype: int               # La función devuelve un número entero: la ganancia máxima posible
        """

        # Si la lista está vacía, no se puede hacer ninguna transacción, entonces la ganancia es 0
        if not prices:
            return 0

        # Inicializamos la variable min_price con infinito.
        # Esto nos servirá para encontrar el precio mínimo al que podríamos haber comprado la acción
        min_price = float('inf')

        # Inicializamos la ganancia máxima en 0.
        # Esta variable almacenará la mayor ganancia encontrada hasta el momento
        max_profit = 0

        # Recorremos todos los precios en la lista uno por uno
        for price in prices:

            # Si el precio actual es menor que el mínimo que hemos visto hasta ahora,
            # lo actualizamos. Esto significa que encontramos una mejor oportunidad para comprar.
            if price < min_price:
                min_price = price

            # Si no es un nuevo precio mínimo, entonces calculamos la ganancia que se obtendría
            # si compramos al precio mínimo y vendemos al precio actual
            elif price - min_price > max_profit:
                # Si esa ganancia es mayor que la ganancia máxima registrada hasta ahora,
                # actualizamos la ganancia máxima
                max_profit = price - min_price

        # Al final del ciclo, devolvemos la mayor ganancia posible que encontramos
        return max_profit


# -------------------------------
# Aquí ejecutamos la función con un ejemplo
# -------------------------------

# Creamos una instancia de la clase Solution
s = Solution()

# Definimos una lista de precios de ejemplo
precios = [7, 1, 5, 3, 6, 4]

# Llamamos al metodo maxProfit con la lista de precios y mostramos el resultado
print(s.maxProfit(precios))  # La salida esperada es 5 (comprar a 1 y vender a 6)
