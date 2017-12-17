from IoTCloud import app

# config
app.config.update(
    DEBUG = True, # Comment this por production Server
    SQLALCHEMY_DATABASE_URI = 'postgres://tmlavqsg:RKTImPhtspZ5X2kuZK-5NTAQij3Xp82C@horton.elephantsql.com:5432/tmlavqsg',
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
)

app.secret_key = '46d18aa6-9eef-4dd1-acda-df2048eaf5e0'
