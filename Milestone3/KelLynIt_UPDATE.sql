--numCheckIns

update business
set numCheckins = a.sum
from(
select business_id, sum(morning + afternoon + evening + night)
from checkins
group by business_id) a
where business.business_id = a.business_id;

--reviewCount

update business
set reviewcount = a.count
from (select business_id, count(stars)
from review
group by business_id) a
where business.business_id = a.business_id;

--reviewRating

update business
set reviewrating = (a.sum / a.count)
from (select business_id, count(stars), sum(stars)
from review
group by business_id) a
where business.business_id = a.business_id;