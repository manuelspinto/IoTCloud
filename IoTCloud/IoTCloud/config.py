from IoTCloud import app

# config
app.config.update(
    DEBUG = True, # Comment this por production Server
    SQLALCHEMY_DATABASE_URI = 'postgres://tmlavqsg:wGTiOq8ydTXod6hoiYySWFC82ZAxnLhI@horton.elephantsql.com:5432/tmlavqsg',
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)
