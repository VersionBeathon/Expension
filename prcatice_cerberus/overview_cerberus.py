import cerberus
# 创建查询字典
schema = {'name':{'type': 'string'}}
# 实例化(添加字典方式)
v = cerberus.Validator(schema)
# 样本字典
document = {'name': 'john doe'}
# 判断
print(v.validate(document))
# 实例化(不添加判断字典)
v = cerberus.Validator()
# 判断
print(v.validate(document, schema))

