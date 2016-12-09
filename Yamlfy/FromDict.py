from .Yamlfyer import Yamlfyer


class FromDict(Yamlfyer):

    _dictData = None

    def __init__(self, dict_data):

        self._dictData = dict_data
        self._yaml = self.convert_to_yaml(dict_data)

    def convert_to_yaml(self, dict_data):

        yaml = ""
        for key, item in dict_data.items():
            if not isinstance(item, dict):
                yaml += "%s: %s\n" % (key, item)
            else:
                yaml += "%s:\n %s" % (key, self.dict_items(item))

        return yaml

    def dict_items(self, dict_item, tabs=1):

        yaml = ""
        for key, item in dict_item.items():
            str_tab = ""
            for i in range(tabs):
                str_tab += "\t"

            if not isinstance(item, dict):
                yaml += "%s%s: %s\n" % (str_tab, key, item)
            else:
                tabs += 1
                yaml += "%s%s:\n %s" % (str_tab, key, self.dict_items(item, tabs))

        return yaml
