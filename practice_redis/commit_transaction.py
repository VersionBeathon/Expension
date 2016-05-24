from transaction.tests.examples import DataManager
dm = DataManager()
print(dm.state)
dm.inc()
t1 = '1'
dm.prepare(t1)
dm.commit(t1)
print(dm.state)