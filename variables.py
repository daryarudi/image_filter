class variables:

    @staticmethod
    def change_dir(dir):
        IMAGES_DIR = dir
    IMAGE_SIZE = 400

    class FILTER:
        def __init__(self, code, name):
            self.code = code
            self.name = name

    FILTERS = []
    FILTERS.append(FILTER("IDL", "Идеальный режекторный фильтр"))
#    FILTERS.append(FILTER("FUR", "Фурье"))
    FILTERS.append(FILTER("BW","Черно-белый"))
    FILTERS.append(FILTER("NEG","Негатив"))
