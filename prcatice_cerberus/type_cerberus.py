import cerberus
v = cerberus.Validator({'quotes':{'type':['string', 'list']}})
print(v.validate({'quotes':'Hello world!'}))

print(v.validate({'quotes':['Do not distrub my circles!', 'Heureka!']}))
v = cerberus.Validator({'quotes':{'type':['string', 'list'], 'schema':{'type': 'string'}}})
print(v.validate({'quotes':[1, 'Heureka!']}))
print(v.errors)

# 如果shema中所需的数据段是强制的,当该数据段不存在的时候会失败,加入 update=True可成功通过
shcema = {'name':{'required': True, 'type': 'string'}, 'age':{'type': 'integer'}}
v = cerberus.Validator(shcema)
document = {'age': 10}
print(v.validate(document))
print(v.errors)
print(v.validate(document, update=True))

# 如果字段可以不存在 可在 shcema中添加 nullable
shcema = {'a_nullable_inter':{'nullable': True, 'type': 'integer'}, 'an_integer':{'type': 'integer'}}
v = cerberus.Validator(shcema)
print(v.validate({'a_nullable_inter':None}))
print(v.validate({'an_integer':None}))

# 选择指定字段内容 allowed
shema = {'role':{'type': 'list', 'allowed':['agent', 'client', 'supplier']}}
v = cerberus.Validator(shema)
print(v.validate({'role':['agent', 'supplier']}))
print(v.validate({'role':['test']}))
print(v.errors)

# 设定字段可否为空
schema = {'name':{'type':'string', 'empty':False}}
document = {'name': ''}
v = cerberus.Validator()
print(v.validate(document, shcema))
print(v.errors)

# list中可以设置多个数据类型 通过items
schema = {'list_of_values': {'type': 'list', 'items': [{'type': 'string'}, {'type': 'integer'}]}}
document = {'list_of_values': ['hello', 100]}
print(v.validate(document, schema))
document = {'list_of_values': [100, 'hello']}
print(v.validate(document, shcema))
print(v.errors)

# dict中设置数据类型 schema
shcema = {'a_dict': {'type': 'dict', 'schema':{'address': {'type': 'string'}, 'city': {'type': 'string', 'required': True}}}}
document = {'a_dict': {'address': 'my address', 'city': 'my town'}}
print(v.validate(document, shcema))

# 也可以使用schema来设置判断列表
schema = {'a_list':{'type': 'list', 'schema':{'type': 'integer'}}}
document = {'a_list':[3, 4, 5]}
print(v.validate(document, schema))

# valueschema 设定字典中所有的value数据类型
schema = {'numbers': {'type': 'dict', 'valueschema': {'type': 'integer', 'min': 10}}}
document = {'numbers': {'an integer': 10, 'another integer': 100}}
print(v.validate(document, schema))
document = {'numbers': {'first':9}}
print(v.validate(document, schema))
print(v.errors)

# propertyschema 设定列表中所有的key的数据类型
schema = {'a_dict': {'type': 'dict', 'propertyschema': {'type': 'string', 'regex': '[a-z]+'}}}
document = {'a_dict':{'key': 'value'}}
print(v.validate(document, schema))
document = {'a_dict':{'KEY': 'value'}}
print(v.validate(document, schema))

# regex 正则匹配
schema = {'email': {'type': 'string', 'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'}}
document = {'email': 'john@example.com'}
print(v.validate(document, schema))

# dependencies 指定需要
schema = {'field1': {'required': False}, 'field2': {'required': False, 'dependencies': ['field1']}}
document = {'field1': 7}
print(v.validate(document, schema))
document = {'field2': 7}
print(v.validate(document, schema))
document = {'field1': 7, 'field2': 8}
print(v.validate(document, schema))

schema = {'field1': {'required': False}, 'field2': {'required': True, 'dependencies': {'field1': ['one', 'two']}}}
document = {'field1': 'one', 'field2': 7}
print(v.validate(document, schema))
document = {'field1': 'three', 'field2': 7}
print(v.validate(document, schema))
print(v.errors)

# anyof 指定数据范围(或运算)
schema = {'prop1':
              {'type': 'number', 'anyof':[{'min': 0, 'max': 10}, {'min': 100, 'max': 110}]}}
doc = {'prop1': 5}
print(v.validate(doc, schema))
doc = {'prop1': 55}
print(v.validate(doc, schema))
print(v.errors)

# allfof 与anyof类似不过是 与运算
schema = {'prop1':
              {'type': 'number', 'allof':[{'min':0, 'max': 10}, {'type': 'integer'}]}
}
doc = {'prop1': 5}
print(v.validate(doc, schema))
doc = {'prop1': 5.5}
print(v.validate(doc, schema))
print(v.errors)

# noneof 与anyof类似不过是 非运算
schema = {'prop1':
              {'type': 'number', 'noneof':[{'min': 0, 'max': 10}, {'min': 50, 'max': 100}]}
}
doc = {'prop1': 11}
print(v.validate(doc, schema))

# oneof 只允许一个规则
schema = {'prop1':
              {'type': 'number', 'oneof':[{'min': 0, 'max': 10}, {'min': 50, 'max': 100}]}

}
doc = {'prop1': 51}
print(v.validate(doc, schema))

# allow_unknown允许没有设置规则的字段通过
schema = {'name': {'type': 'string', 'maxlength': 10}}
print(v.validate({'name': 'john', 'sex': 'M'}, schema))
print(v.errors)
v = cerberus.Validator(schema={})
v.allow_unknown = True
print(v.validate({'name': 'john', 'sex': 'M'}, schema))

# allow_unknown指定可以通过的没有设置规则字段的数据类型
v = cerberus.Validator(schema={})
v.allow_unknown = {'type': 'string'}
print(v.validate({'an_unknown_field': 'john'}))
print(v.validate({'an_unknown_field': 20}))
print(v.errors)

# allow_unknown 在初始化中设置
v = cerberus.Validator(schema=schema, allow_unknown=True)
print(v.validate({'name': 'john', 'sex': 'M'}))

# allow_unknow 在设置字典
v = cerberus.Validator()
print(v.allow_unknown)
schema = {
    'name': {'type': 'string'},
    'a_dict': {
        'type': 'dict',
        'allow_unknown': True,
        'schema': {
            'address': {'type': 'string'}
        }
    }
}
print(v.validate({'name': 'john', 'a_dict':{'an_unknown_field': 'is allowed'}}, schema))

# coerce胁迫数据类型
v = cerberus.Validator({'amount': {'type': 'integer'}})
print(v.validate({'amount': '1'}))
v = cerberus.Validator({'amount': {'type': 'integer', 'coerce': int}})
print(v.validate({'amount': '1'}))
to_bool = lambda v: v.lower() in ['true', '1']
v = cerberus.Validator({'flag': {'type': 'boolean', 'coerce': to_bool}})
print(v.validate({'flag': 'true'}))
