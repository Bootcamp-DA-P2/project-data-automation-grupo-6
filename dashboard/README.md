# 📊 Dashboard - Visualización de Datos

Esta carpeta contiene el archivo Excel que sirve como **interfaz visual** del proyecto.

## 📄 Archivo Principal

**`Sakila_Dashboard.xlsx`** - Dashboard de Excel con gráficos y análisis

## 🎯 Propósito

El dashboard es la **capa de visualización** que presenta los datos procesados por Python de forma visual e interactiva.

```
┌─────────────────────────────────────┐
│  MySQL (Base de Datos)              │
│  └─ Datos crudos                    │
└─────────────────────────────────────┘
            ↓
┌─────────────────────────────────────┐
│  Python (Procesamiento)             │
│  └─ src/sakila_ETL.py               │
└─────────────────────────────────────┘
            ↓
┌─────────────────────────────────────┐
│  outputs/ (Datos procesados)         │
│  └─ CSVs con análisis               │
└─────────────────────────────────────┘
            ↓
┌─────────────────────────────────────┐
│  dashboard/ (Visualización)         │
│  └─ Sakila_Dashboard.xlsx           │
└─────────────────────────────────────┘
```

## 🔄 Cómo Funciona

1. **Python procesa** los datos de MySQL
2. **Genera CSVs** en la carpeta `outputs/`
3. **Excel lee** esos CSVs (conexiones de datos)
4. **Dashboard muestra** gráficos y análisis visual

## 📋 Estructura del Dashboard

### Hojas recomendadas:

1. **Dashboard** - Vista principal con todos los gráficos
2. **Actividad de los clientes** - Conectada a `outputs/actividad_clientes_clean.csv`
3. **Top Películas** - Conectada a `outputs/catalogo_peliculas_clean.csv`
4. **Por Actores y popularidad** - Conectada a `outputs/elenco_popularidad_clean.csv`

## 🔄 Actualizar Datos

Después de ejecutar `python main.py`:

```
1. Abrir dashboard/Sakila_Dashboard.xlsx
2. Presionar F5 (o Ctrl + Alt + F5)
3. Los datos se actualizan automáticamente
```

## 💡 Beneficios de esta Organización

- ✅ **Separación clara:** Visualización separada del código
- ✅ **Portable:** Puedes compartir solo el dashboard
- ✅ **Organizado:** Fácil de encontrar y mantener
- ✅ **Escalable:** Puedes agregar más dashboards

# Justificación de Selección de KPIs: Dashboard Sakila

Este apartado detalla la lógica de negocio y técnica detrás de la elección de las dos métricas principales desarrolladas para el análisis en el proyecto de automatización de datos.

---
## Respecto a la tabla Actividad de clientes

### 1. Optimización del Mercado Geográfico
*   **Análisis:** Identificación de ingresos totales y volumen de transacciones por ciudad (`city`).
*   **Decisión:** 
    *   Asignación de presupuestos de marketing en ciudades con mayor retorno.
    *   Evaluación de expansión o cierre de puntos de servicio según la densidad de clientes activos.

### 2. Segmentación y Fidelización de Clientes (RFM)
*   **Análisis:** Cruce entre la frecuencia de alquiler (`count rental_id`) y el gasto acumulado (`sum amount`).
*   **Decisión:** 
    *   **Clientes VIP:** Creación de programas de lealtad o descuentos exclusivos para usuarios de alto valor.
    *   **Clientes en Riesgo:** Identificación de usuarios con pocos alquileres para lanzar campañas de reactivación.

### 3. Gestión de Inventario y Logística
*   **Análisis:** Uso de la métrica derivada `rental_duration`.
*   **Decisión:** 
    *   Determinar el tiempo óptimo de rotación de las películas.
    *   Si los alquileres largos no generan ingresos proporcionales, se pueden ajustar las políticas de precios para incentivar devoluciones rápidas y aumentar la disponibilidad de stock.

### 4. Integridad Operativa y Financiera
*   **Análisis:** Limpieza de datos (exclusión de montos negativos y errores en fechas de retorno).
*   **Decisión:** 
    *   Garantizar que los informes financieros sean 100% precisos.
    *   Identificar posibles fallos en el sistema de registro de devoluciones si se detectan demasiadas fechas nulas o inconsistentes.

---
## Respecto a la tabla Catalogo de Peliculas

🛠️ Procesos de Limpieza Realizados
Para garantizar la calidad de los datos y facilitar el análisis en Excel, se aplicaron las siguientes reglas de limpieza directamente en las consultas SQL y el script de Python:

Normalización de Texto: Se aplicaron funciones **LOWER()** y **TRIM()** en campos de texto (títulos, descripciones, categorías) para eliminar espacios innecesarios y asegurar uniformidad.

Gestión de Nulos (Data Integrity): Se filtraron registros con rating o title nulos para evitar inconsistencias en las tablas dinámicas.

Depuración de Valores Atípicos: Eliminación de registros con duraciones (length) menores o iguales a 0.

Criterio de Tipo de Producción:

Cortometraje: Películas con una duración igual o inferior a 60 minutos.

Película: Producciones que superan los 60 minutos.
---
## Respecto a la tabla Elenco y Popularidad


## 1. Top 10 de Actores más "Productivos" 🌟

### ¿Por qué se eligió?
En una industria basada en el contenido (como el cine), el **"Star Power"** (poder de las estrellas) es un motor de ventas directo. Identificar a los actores con mayor volumen de películas en el catálogo permite al equipo de marketing:

* **Optimizar Recomendaciones:** Crear colecciones basadas en los actores más recurrentes.
* **Gestión de Inventario:** Asegurar que las películas de los actores más prolíficos estén siempre disponibles.
* **Análisis de Valor:** Determinar si la cantidad de películas de un actor se traduce directamente en mayor volumen de alquileres (cruce de datos).

### Implementación Técnica
* **Métrica:** `COUNT(film_id)` agrupado por `actor_full_name`.
* **Visualización:** Gráfico de barras horizontales ordenado de mayor a menor.
* **Filtro aplicado:** Filtro de valor *"Diez mejores"* (Top 10) para reducir el ruido visual y centrar la atención en los activos más valiosos.

---

## 2. Densidad de Elenco por Película 🎬

### ¿Por qué se eligió?
La **"Densidad de Elenco"** (cuántos actores participan en una sola cinta) es un indicador del tipo de producción y su potencial atractivo comercial.

* **Categorización Automática:** Permite clasificar las películas en "Producciones de Elenco Estelar" vs. "Producciones Independientes/Pequeñas".
* **Análisis de Diversidad:** Ayuda a entender si el catálogo de Sakila está balanceado o si tiende hacia superproducciones con muchos actores.
* **Correlación de Costos:** Generalmente, un elenco más grande implica mayores costos de adquisición o derechos; esta métrica ayuda a monitorizar la complejidad del catálogo.

### Implementación Técnica
* **Métrica:** Promedio y Máximo de `total_actores_en_pelicula`.
* **Segmentación:** Uso del campo `categoria_reparto` para filtrar por tipos de elenco (*Estelar, Gran Elenco, Estándar*).
* **Visualización:** Gráfico de columnas combinadas con líneas de tendencia.

---

## Conclusión del Valor Agregado 💎

La combinación de estas dos métricas ofrece una visión 360°:

1.  **Enfoque en el Talento (Actor):** Quiénes son nuestros pilares de contenido.
2.  **Enfoque en el Producto (Película):** Cómo están estructuradas nuestras películas.

Esta decisión estratégica permite que el Dashboard no solo sea una visualización de datos, sino una **herramienta de toma de decisiones** para la gestión del catálogo de Sakila.
