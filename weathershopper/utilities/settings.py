import configparser
import rootpath

class App:

    def settings(self):

        SettingsObject = {}
        ssettings = configparser.ConfigParser()
        path = rootpath.detect()
        print(path)
        readconfigs = ssettings.read(path + "/Documents/nivya/weathershopper/shopperProps.properties")
        print(readconfigs)

        SettingsObject['url'] = ssettings.get("defaults", "pythonanywhere.weathershopper.base.url")
        SettingsObject['tempcutoff'] = ssettings.get("defaults", "pythonanywhere.weathershopper.temperatureCutOff")
        SettingsObject['browsers'] = ssettings.get("defaults", "pythonanywhere.weathershopper.app.browser.run")
        SettingsObject['email'] = ssettings.get("defaults", "pythonanywhere.weathershopper.user.email")
        SettingsObject['expiry'] = ssettings.get("sandboxcarddetails", "pythonanywhere.weathershopper.sandboc.card.expiry")
        SettingsObject['card'] = ssettings.get("sandboxcarddetails", "pythonanywhere.weathershopper.sandbox.card.number")
        SettingsObject['cvv'] = ssettings.get("sandboxcarddetails", "pythonanywhere.weathershopper.sandboc.card.cvv")
        import random

        SettingsObject['email'] = "smailxcdvfserfsfs" + str(random.randint(10000,1000000)) + "@gmail.com"

        return SettingsObject
