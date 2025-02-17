# Usa la imagen base de Odoo 17.0 que mencionas
FROM odoo:17.0-20241029

# Copia tus módulos personalizados de Odoo al contenedor
COPY ./addons /mnt/extra-addons

# Define las variables de entorno para la configuración
ENV HOST=db-odoo17-Bintell-prueba
ENV USER=odoo
ENV PASSWORD=odoo

# Aquí puedes agregar cualquier otra configuración que necesites
