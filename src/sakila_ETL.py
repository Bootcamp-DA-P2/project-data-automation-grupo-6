from sqlalchemy import create_engine, text
from config import *
import pandas as pd
import os

# Create a database engine (El engine se crea una sola vez)
def get_engine():
    """Construir el motor de conexión"""
    url_db = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    return create_engine(url_db)

def test_connection():
    """Probar la conexión a la base de datos"""
    engine = get_engine()
    try:
        # Usamos el 'with' directamente con el engine para que cierre la conexión solo
        with engine.connect() as connection:
            print("✅ Conexión exitosa a la base de datos.")
            result = connection.execute(text("SELECT * FROM actor LIMIT 1;"))
            print(f"Primer registro de prueba: {result.fetchone()}")
    except Exception as e:
        print(f"❌ Error al conectar a la base de datos: {e}")

def get_data_list_from_join():
    """Obtener datos y exportar a CSV"""
    engine = get_engine()
    
    join_query_sql = """ 
    SELECT 
        LOWER(c.first_name) AS first_name,
        LOWER(c.last_name) AS last_name,
        LOWER(c.email) AS email,
        LOWER(ci.city) AS city,
        r.rental_id,
        r.rental_date,
        r.return_date,
        p.payment_id,
        p.amount,
        DATEDIFF(r.return_date, r.rental_date) AS rental_duration
    FROM rental r
    INNER JOIN payment p ON r.rental_id = p.rental_id
    INNER JOIN customer c ON r.customer_id = c.customer_id
    INNER JOIN address a ON c.address_id = a.address_id
    INNER JOIN city ci ON a.city_id = ci.city_id
    WHERE r.rental_id IS NOT NULL 
        AND p.payment_id IS NOT NULL
        AND p.amount > 0
        AND r.return_date IS NOT NULL
        AND r.rental_date < r.return_date;
    """
    
    try:
        with engine.connect() as connection:
            # Pandas puede leer directamente de la conexión usando read_sql
            df = pd.read_sql(text(join_query_sql), connection)
        
        # Crear carpeta output si no existe (para evitar errores)
        if not os.path.exists('output'):
            os.makedirs('output')

        # Exportar a CSV
        output_path = "output/actividad_clientes.csv"
        df.to_csv(output_path, index=False, encoding='utf-8')

        print(f"⭐ DataFrame creado y guardado en: {output_path}")
        print(df.head()) # Ver las primeras filas en consola
        return df

    except Exception as e:
        print(f"❌ Error durante el proceso ETL: {e}")

if __name__ == "__main__":
    test_connection()
    get_data_list_from_join()