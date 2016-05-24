
from transaction.tests.examples import DataManager

dm2 = DataManager()
dm2.inc()
t1 = '1'
dm2.prepare(t1)
dm2.commit(t1)
print(dm2.state)
dm2.inc()
t2 = '2'
dm2.prepare(t2)
dm2.abort(t2)
print(dm2.state)