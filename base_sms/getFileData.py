import sys, os

sys.path.append(os.getcwd())


import yaml, os


class GetFileData:
    def __init__(self):
        pass

    def get_yml_data(self, yamlName):
        with open("./data" + os.sep + yamlName, "r") as f:
            return yaml.safe_load(f)

# def get_data():
#     data_list = []
#     with open(r"C:\Users\86176\Desktop\sms\data_sms\data_yaml.yaml","r",encoding="utf-8") as f:
#         data = yaml.safe_load(f).get("TestSmsData").values()
#         for i in data:
#             i.get("send")
#             i.get("expect")
#             data_list.append((i.get("send"),i.get("expect")))
#     return data_list
#
# a = get_data()
# print(a)
