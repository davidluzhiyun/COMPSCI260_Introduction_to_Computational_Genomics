import fm_index
from fm_index import *

ref = "GATTACATTCATTTTTTTTTCAT"
data = fm_index.make_all(ref)
print(fm_index.find("CAT",data))