# EvilDoS - Herramienta Avanzada de Denegación de Servicio

<p align="center">
  <img src="https://i.imgur.com/Example.png" alt="EvilDoS Logo" width="300"/>
</p>

## ⚠️ Advertencia Legal

**ESTA HERRAMIENTA ES SOLO PARA FINES EDUCATIVOS Y DE PRUEBAS ÉTICAS**

El uso de EvilDoS para atacar objetivos sin consentimiento previo expreso es ilegal y está prohibido. Los desarrolladores no asumen ninguna responsabilidad por el uso indebido de este software. Al utilizar esta herramienta, aceptas utilizarla únicamente para:

- Pruebas en tus propios servidores
- Auditorías de seguridad autorizadas
- Investigación y educación en entornos controlados

## 🔍 Descripción

EvilDoS es una herramienta avanzada de denegación de servicio desarrollada con fines educativos que permite simular diversos tipos de ataques DoS. Cuenta con módulos específicos para diferentes protocolos y servicios, interfaz visual mejorada y sistema de autenticación para prevenir el uso no autorizado.

## ✨ Características

- **Múltiples métodos de ataque:**
  - Ataque específico para servidores Minecraft
  - Inundación TCP (SYN/ACK/FIN)
  - Inundación UDP amplificada

- **Sistema de autenticación KeyAuth**
  - Protección contra uso no autorizado
  - Credenciales encriptadas para mayor seguridad

- **Interfaz visual mejorada**
  - Diseño en colores para mejor visualización
  - Efectos visuales tipo hacker
  - Estadísticas en tiempo real

- **Optimización de rendimiento**
  - Envío de paquetes en lotes para mayor eficiencia
  - Control de conexiones y reconexiones automáticas
  - Manejo de errores y recuperación automática

## 🔧 Requisitos

- Python 3.7+
- Bibliotecas:
  - colorama
  - keyauth
  - socket
  - hashlib
  - base64

## 📥 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/Ades12121212121/MCatt.git

# Acceder al directorio
cd MCatt

# Instalar dependencias
pip install -r requirements.txt
```

## 💻 Uso

```bash
# Ejecutar la herramienta
python EvilDoS.py
```

1. Introduce tu clave de licencia cuando se solicite
2. Selecciona el método de ataque (1-3)
3. Introduce la IP objetivo
4. Introduce el puerto objetivo
5. Configura los paquetes por segundo (opcional)
6. Observa las estadísticas en tiempo real
7. Para detener el ataque, presiona CTRL+C

## 🔑 Sistema de Licencias

La herramienta utiliza un sistema de licencias KeyAuth. Para obtener una licencia válida, contacta a los desarrolladores. Las claves de licencia deben comenzar con el prefijo "KEYAUTH-" seguido de un código único.

## 🛡️ Protección

Para proteger tus servidores contra ataques DoS como los simulados por esta herramienta, recomendamos:

- Implementar limitación de tasa (rate limiting)
- Utilizar servicios de mitigación DDoS como Cloudflare
- Configurar firewalls correctamente
- Mantener actualizados los sistemas

## 📝 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

<p align="center">
  Desarrollado con ❤️ para la comunidad de seguridad informática
</p>

<p align="center">
  <strong>Recuerda: Con un gran poder viene una gran responsabilidad</strong>
</p>
