# Integración de Consul Service Discovery

## Resumen de cambios realizados

Se ha integrado **Consul Service Discovery** en los tres microservicios usando `flask-consulate`:

### 1. **microProducts** (Puerto 5003)
   - Agregado endpoint `/healthcheck`
   - Registrado en Consul como servicio `microproducts`
   - Health check cada 10 segundos

### 2. **microUsers** (Puerto 5002)
   - Agregado endpoint `/healthcheck`
   - Registrado en Consul como servicio `microusers`
   - Health check cada 10 segundos

### 3. **frontend** (Puerto 5001)
   - Agregado endpoint `/healthcheck`
   - Registrado en Consul como servicio `frontend`
   - Health check cada 10 segundos

---

## Instrucciones de ejecución

### Prerequisitos
- Consul debe estar ejecutándose y accesible en `http://localhost:8500`
- Python 3.7+
- Base de datos MySQL inicializada con `init.sql`

### Paso 1: Instalar dependencias en cada microservicio

```bash
# En microUsers
cd microUsers
pip3 install -r requirements.txt

# En microProducts
cd ../microProducts
pip3 install -r requirements.txt

# En frontend
cd ../frontend
pip3 install -r requirements.txt
```

### Paso 2: Ejecutar los microservicios en terminales separadas

```bash
# Terminal 1 - microUsers (Puerto 5002)
cd microUsers
python3 run.py

# Terminal 2 - microProducts (Puerto 5003)
cd microProducts
python3 run.py

# Terminal 3 - frontend (Puerto 5001)
cd frontend
python3 run.py
```

### Paso 3: Verificar registro en Consul

Accede a la interfaz de Consul en:
```
http://localhost:8500/ui
```

Deberías ver tres servicios registrados:
- **microusers** - Health check: http://localhost:5002/healthcheck
- **microproducts** - Health check: http://localhost:5003/healthcheck
- **frontend** - Health check: http://localhost:5001/healthcheck

### Paso 4: Verificar salud de los servicios

```bash
# Ver todos los servicios
curl http://localhost:8500/v1/catalog/services

# Ver detalles de un servicio específico
curl http://localhost:8500/v1/catalog/service/microusers

# Verificar health check manualmente
curl http://localhost:5002/healthcheck
curl http://localhost:5003/healthcheck
curl http://localhost:5001/healthcheck
```

---

## Estructura de archivos actualizados

```
microweb/
├── microUsers/
│   ├── users/
│   │   └── views.py (✅ Consul integration)
│   └── requirements.txt (✅ Nuevo archivo con flask-consulate)
│
├── microProducts/
│   ├── products/
│   │   └── views.py (✅ Consul integration)
│   └── requirements.txt (✅ Actualizado)
│
└── frontend/
    ├── web/
    │   └── views.py (✅ Consul integration)
    └── requirements.txt (✅ Nuevo archivo con flask-consulate)
```

---

## Notas importantes

- Cada servicio registra un healthcheck que se ejecuta cada 10 segundos
- Si Consul no está disponible, los servicios igualmente se ejecutarán pero no se registrarán
- Los servicios están etiquetados con tags para facilitar búsquedas:
  - `microusers`: tags `['users', 'api']`
  - `microproducts`: tags `['products', 'api']`
  - `frontend`: tags `['web', 'frontend']`
