birthday = '1635/02/07'

import datetime
import calendar as c

d = datetime.date(1635, 2, 7)
print(c.day_name[d.weekday()])