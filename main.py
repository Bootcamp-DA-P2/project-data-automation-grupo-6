from src.sakila_ETL import generar_reporte_csv

# Definimos las 3 consultas
SQL_CLIENTES = """SELECT 
    -- Estandarización a minúsculas
    LOWER(c.first_name) AS first_name,
    LOWER(c.last_name) AS last_name,
    LOWER(c.email) AS email,
    LOWER(ci.city) AS city,
    
    -- Datos del alquiler y pago
    r.rental_id,
    r.rental_date,
    r.return_date,
    p.payment_id,
    p.amount,
    
    -- Columna derivada: Duración en días
    DATEDIFF(r.return_date, r.rental_date) AS rental_duration
-- Tabla principal: rental, que contiene la información de los alquileres
FROM rental r

-- Joins definidos por llaves primarias/foráneas
-- Se unen las tablas rental, payment, customer, address y city para obtener toda la información relevante
INNER JOIN payment p ON r.rental_id = p.rental_id
INNER JOIN customer c ON r.customer_id = c.customer_id
INNER JOIN address a ON c.address_id = a.address_id
INNER JOIN city ci ON a.city_id = ci.city_id

-- Filtros de limpieza y consistencia lógica
WHERE 
    -- Filtros de limpieza solicitados
    r.rental_id IS NOT NULL 
    AND p.payment_id IS NOT NULL
    -- Asegurar que el monto del pago sea positivo
    AND p.amount > 0
    AND r.return_date IS NOT NULL
    -- Consistencia lógica de fechas
    AND r.rental_date < r.return_date"""
SQL_CATALOGO = """
SELECT 
        f.film_id,
        LOWER(TRIM(f.title)) AS title,
        LOWER(TRIM(f.description)) AS description,
        f.release_year,
        LOWER(l.name) AS language,
        LOWER(cat.name) AS category,
        f.length,
        f.rating,
        -- Columna derivada: Película larga
        CASE WHEN f.length >= 120 THEN 1 ELSE 0 END AS is_long_film,
        -- Conteo de copias en inventario (Agrupación útil)
        (SELECT COUNT(*) FROM inventory i WHERE i.film_id = f.film_id) AS inventory_count
    FROM film f
    INNER JOIN language l ON f.language_id = l.language_id
    LEFT JOIN film_category fc ON f.film_id = fc.film_id
    LEFT JOIN category cat ON fc.category_id = cat.category_id
    WHERE 
        f.length > 0              -- Eliminar duraciones <= 0
        AND f.rating IS NOT NULL   -- Eliminar ratings nulos
        AND f.title IS NOT NULL   -- Integridad básica"""
SQL_ACTORES = "SELECT ... FROM actor ..." # Tu tercera query

def run():
    print("Iniciando extracción de reportes...")
    
    # Ejecutamos la función 3 veces para obtener los 3 CSVs independientes
    generar_reporte_csv(SQL_CLIENTES,"actividad_clientes")
    generar_reporte_csv(SQL_CATALOGO,"catalogo_peliculas")
    # generar_reporte_csv(SQL_ACTORES, "elenco_popularidad")
    
    print("¡Todos los archivos han sido generados en la carpeta /output!")

if __name__ == "__main__":
    run()