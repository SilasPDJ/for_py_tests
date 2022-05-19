# https://github.com/matheusfelipeog/fordev
from fordev.generators import people
import pandas as pd

df = pd.DataFrame(people(20, age=18))
pd.read_html()
df.to_excel("datas/test.xlsx")
