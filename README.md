# Ferramax  

Plataforma de comercio electrónico para ferretería, con integración de APIs para gestión de inventario, **pagos y conversión de divisas**.  

## 🎯 Objetivo  
Automatizar ventas y gestionar integraciones con sistemas externos (WEBPAY, Banco Central) para mejorar la eficiencia operativa.  

## 🛠 Tecnologías  
- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python (Django)  
- **Base de datos**: Supabase (PostgreSQL)  
- **APIs**: Mercado Pago, Banco Central de Chile  
- **Herramientas**: VSCode, GitHub Desktop, Navegador  

## ⚡ Funcionalidades  
- API RESTful para consulta de productos  
- Pagos con MercadoPago  
- Conversión de divisas en tiempo real  

## 🚀 Configuración paso a paso  

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
