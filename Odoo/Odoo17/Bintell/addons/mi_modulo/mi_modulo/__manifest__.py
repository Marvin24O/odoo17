{
    'name': 'Mi Módulo',
    'version': '1.0',
    'summary': 'Mi primer módulo de prueba para Odoo 17',
    'description': 'Este módulo agrega nuevas funcionalidades.',
    'author': 'Roberto Valladares',
    'website': 'https://www.odoo.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/mi_modelo_view.xml',
        
    ],
    'installable': True,
    'application': True,
    'icon': 'static/odoo.jpg',  # Asegúrate de que la ruta sea correcta
}



