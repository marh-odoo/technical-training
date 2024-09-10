{
    "name": "Estate",  # The name that will appear in the App list
    "version": "16.0.0",  # Version
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base"],  # dependencies
    "data": [
        'security/ir.model.access.csv',
        'views/test_model.xml',
        'data/res.country.state.csv'
    ],
    "installable": True,
    'license': 'LGPL-3',
}
