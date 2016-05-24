from transaction.tests.examples import DataManager
dm = DataManager()
dm.inc()
t1 = '1'
r = dm.savepoint(t1)
print(dm.state, dm.delta)
dm.inc()
print(dm.state, dm.delta)
r.rollback()
print(dm.state, dm.delta)
dm.prepare(t1)
dm.commit(t1)
print(dm.state, dm.delta)
