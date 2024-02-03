class PropertyUtil:
    @staticmethod
    def getPropertyString():
        properties = {}
        with open('db.properties', 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                properties[key] = value
        return properties
