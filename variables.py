class variables:

    @staticmethod
    def change_dir(dir):
        IMAGES_DIR = dir
    IMAGE_SIZE = 400

    class FILTER:
        def __init__(self, code, name):
            self.code = code
            self.name = name
        def name_is(self, name):
            return name == self.name


    FILTERS = []
    FILTERS.append(FILTER("INF", "Идеальный низкочастотный"))
    FILTERS.append(FILTER("IVF", "Идеальный высокочастотный"))
    FILTERS.append(FILTER("BNF", "Баттерворта низкочастотный"))
    FILTERS.append(FILTER("BVF", "Баттерворта высокочастотный"))
    FILTERS.append(FILTER("GNF", "Гаусса низкочастотный"))
    FILTERS.append(FILTER("GVF", "Гаусса высокочастотный"))
#    FILTERS.append(FILTER("BW","Черно-белый"))
#    FILTERS.append(FILTER("NEG","Негатив"))

    def get_filter_code(self, name):
        for i in range(0, len(self.FILTERS)):
            if (self.FILTERS[i].name_is(name)):
                return self.FILTERS[i].code