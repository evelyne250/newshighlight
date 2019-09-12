class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,description,url,category,country):
        '''
        Function that initiates the sources class
        '''
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
