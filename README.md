# Ferramax  

Plataforma de comercio electrónico para ferretería, con integración de APIs para gestión de inventario, **pagos y conversión de divisas**.  

##  Objetivo  
Automatizar ventas y gestionar integraciones con sistemas externos (WEBPAY, Banco Central) para mejorar la eficiencia operativa.  

##  Tecnologías  
- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python (Django)  
- **Base de datos**: Supabase (PostgreSQL)  
- **APIs**: Mercado Pago, Banco Central de Chile  
- **Herramientas**: VSCode, GitHub Desktop, Navegador  

##  Funcionalidades  
- API RESTful para consulta de productos  
- Pagos con MercadoPago  
- Conversión de divisas en tiempo real  

##  Configuración paso a paso  

### 1. Clonar repositorio  
1.1 Usar GitHub Desktop para clonar  
1.2 Abrir VSCode  
1.3 Buscar y abrir el proyecto  
1.4 **Iniciar una terminal**  

### 2. Crear archivo .env  
2.1 Ruta requerida: `FERRAMAX_WEB_SERVICES/.env`  
2.2 Ejecutar en terminal para que se cree el file o hacerlo manual:  

```bash
New-Item -Path .env -ItemType File
```
### 3. En el archivo .env  pegar lo siguente
```
SUPABASE_URL=https://kqfhjpwxodvhbpkhotji.supabase.co/
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtxZmhqcHd4b2R2aGJwa2hvdGppIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgxNTM2MjcsImV4cCI6MjA2MzcyOTYyN30.1lSid-tkXuBxiB-XbYptofyXBElOwr4ZK1to_jhZ5zQ
DEBUG=true
SECRET_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtxZmhqcHd4b2R2aGJwa2hvdGppIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0ODE1MzYyNywiZXhwIjoyMDYzNzI5NjI3fQ.ZBNnpm9WbEnfbHj2bQ099_MkpexlGFbt_gDeeFOju6w
```
### 4. Instalar las dependencias
```
pip install Pillow
pip install mercadopago
pip install supabase
pip install djangorestframework
pip install psycopg2-binary
pip install django
pip install requests
pip install python-dotenv
pip install python-decouple
```
### 5. **En caso de error con el host o conexion con django**: 
Se debe a que tu conexion wifi utiliza ipv4 y no ipv6, Se debe a que supabase funciona con ipv6 no con ipv4 en ese saco conectate a una red que tenga ambos o solo ipv6.
https://www.whatismyip.com En esta pagina puedes verificar que ipv tienes. en caso que tu redes no funcionen con ipv6 puedes utilizar un pooler que supabase tiene que juntas ambas conexiones,
tienes que modificarlo en settings.py--> database en el host pegar esto:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres.kqfhjpwxodvhbpkhotji',
        'PASSWORD': 'renan12345', # <-- ¡IMPORTANTE! Reemplaza esto con tu contraseña
        'HOST': 'aws-0-sa-east-1.pooler.supabase.com', # <-- ¡ESTE ES EL NUEVO HOST DEL POOLER!
        'PORT': '6543', # <-- ¡Y ESTE ES EL NUEVO PUERTO DEL POOLER!
    }
}
```
