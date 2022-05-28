from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

db_datas = [{
    "id": 1,
    "title": "The Shawshank Redemption",
    "year": 1994,
}]