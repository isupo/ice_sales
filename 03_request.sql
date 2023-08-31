select eventdate,
       count(*) AS count
from sales
GROUP BY eventdate;

WITH tbl AS (select eventdate,
                    count(*) AS count
             from sales
             GROUP BY eventdate)

SELECT tbl.eventdate, count, temp
from tbl
left join weather
on tbl.eventdate = weather.eventdate;
