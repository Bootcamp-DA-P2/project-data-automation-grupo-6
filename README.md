# 📊 Proyecto Sakila - Automatización MySQL → Python → Excel

Este proyecto automatiza la extracción y análisis de datos de la base de datos SQL usando Python, generando varios archivos CSV que se conectan automáticamente a un libro de Excel.

**✨ Sin macros - Solo Python + Excel con F5**

---

### Gestión del Proyecto
Puedes seguir nuestro progreso en nuestro [Tablero de Trello](https://trello.com/b/qzzHfqya/proyecto-4-grupo-6).

---

## 🚀 INICIO RÁPIDO (3 pasos)

```powershell
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Configurar MySQL
# Edita el archivo .env con tus credenciales

# 3. Ejecutar
python main.py
```

---

## 📁 Estructura del Proyecto

```
project-data-automation-grupo-6/
│
├── main.py                    ⭐ EJECUTAR ESTE (punto de entrada)
│
├── src/                       📦 Código fuente (procesamiento)
│   ├── __init__.py
│   ├── sakila_ETL.py          (extracción y transformación de datos)
│   └── config.py              (configuración desde .env)
│
├── outputs/                    📂 Datos procesados (CSVs)
│   ├── actividad_clientes_clean.csv
│   ├── catalogo_peliculas_clean.csv
│   └── elenco_popularidad_clean.csv
│
├── dashboard/                 📊 Visualización (Excel)
│   ├── Sakila_Dashboard.xlsx  (tu dashboard de Excel)
│   └── README.md              (guía del dashboard)
├── notebooks
│   ├──Flujo_de_datos_SQL_Python_Grupo_6.ipynb
├── queries/                   🗄️  Consultas SQL
│   ├── actividad_clientes.sql
│   ├── catalogo.sql
│   ├── elenco_popularidad.sql
│   
│
├── requirements.txt           (dependencias Python)
├── .env                       🔒 Credenciales (configurado ✓)
├── .env.example               (plantilla)
├── .gitignore                 (protección Git)
└── README.md(esta guía)
```

**Organización tipo aplicación:**
- **src/** = Procesamiento (Python)
- **outputs/** = Datos intermedios (CSVs)
- **dashboard/** = Visualización (Excel)
- **queries/** = Consultas SQL
- **notebooks/** = Limpieza dataframes (Python)

**🔒 IMPORTANTE:** El archivo `.env` contiene tus credenciales y NO se sube a Git (está en `.gitignore`)

---

## ⚙️ CONFIGURACIÓN

### 1. Instalar Python y MySQL
- Python 3.8 o superior
- MySQL con base de datos Sakila instalada

### 2. Instalar dependencias
```powershell
pip install -r requirements.txt
```

Esto instala:
```powershell
pip install pandas mysql-connector-python sqlalchemy openpyxl python-dotenv
```

### 3. Configurar MySQL (IMPORTANTE)

Edita el archivo **`.env`** con tus credenciales:

```env
DB_USER=root
DB_PASSWORD=tu_contraseña_mysql
DB_HOST=localhost
DB_NAME=sakila
```

**¿Dónde encontrar estos datos?**
- `DB_USER`: Usuario de MySQL (generalmente `root`)
- `DB_PASSWORD`: La contraseña que pusiste al instalar MySQL
- `DB_HOST`: `localhost` (si MySQL está en tu PC)
- `DB_NAME`: `sakila` (nombre de la base de datos)

**🔒 SEGURIDAD:** El archivo `.env` NO se sube a Git (protegido por `.gitignore`)

### 4. Fichero con limpieza realizada en Collab o Jypiter

Ves ejecutando cada parte del fichero para realizar la limpieza de los 3 datasets.

### 5. Crear Dashboard Excel (manualmente)

Crea tu archivo Excel en la carpeta `dashboard/`:

**Ubicación:** `dashboard/Sakila_Dashboard.xlsx`

**💡 Estructura recomendada:** 4 hojas
- `Dashboard` - Aquí pondrás tus gráficos y análisis visual
- `Datos Diarios` - Para conectar `../output/resumen_diario.csv`
- `Top Peliculas` - Para conectar `../output/top_peliculas.csv`
- `Por Categoria` - Para conectar `../output/por_categoria.csv`