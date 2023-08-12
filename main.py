from pprint import pprint
from paddlenlp import Taskflow
from tqdm import tqdm
import pandas as pd
df=pd.read_excel('判决书内容2.xlsx')
schema = ['法院', {'原告': '委托代理人'}, {'被告':'委托代理人'},'侵权类型','抗辩理由','裁判结果'] 
ie = Taskflow('information_extraction', schema=schema)
ie.set_schema(schema)
for i in tqdm(df['内容'].tolist()):
    for t in i.replace('\n','。').split('。。'):
        print(t)
        print(ie(t))


from pprint import pprint
from paddlenlp import Taskflow
from tqdm import tqdm
import pandas as pd
schema = ['法院', {'原告':'委托代理人'}, {'被告':'委托代理人'}]
ie = Taskflow('information_extraction', schema=schema)
ie.set_schema(schema)
pprint(ie("北京市海淀区人民法院\n民事判决书\n(199x)建初字第xxx号\n原告：张三。\n委托代理人李四，北京市 A律师事务所律师。\n被告：B公司，法定代表人王五，开发公司总经理。\n委托代理人赵六，北京市 C律师事务所律师。"))