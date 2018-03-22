--Update business review count on insert into 
CREATE OR REPLACE FUNCTION updateReviewCount() 
RETURNS TRIGGER AS
$$
BEGIN
	UPDATE Business
    Set reviewcount = Business.reviewcount + 1
    Where Business.business_id = NEW.business_id;
    
    RETURN NEW;
END;


$$
LANGUAGE 'plpgsql'
    
CREATE TRIGGER updateRCount
	AFTER INSERT
    ON review
    FOR EACH ROW
    EXECUTE PROCEDURE updateReviewCount();


--Update business review rating on insert into review

CREATE OR REPLACE FUNCTION updateReviewRating()
RETURNS TRIGGER AS
$$
BEGIN
	UPDATE business
    Set reviewrating = (SELECT averageRev
                        FROM (Select review.business_id, (SUM(review.stars)/ COUNT(review.stars)) as averageRev
                              from review
                              where review.business_id = NEW.business_id
                              group by review.business_id) as average)
    WHERE Business.business_id = NEW.business_id;
    RETURN NEW;
END;
$$
language 'plpgsql'

CREATE TRIGGER updateRating
AFTER INSERT
ON review
FOR EACH ROW
EXECUTE PROCEDURE updateReviewRating()

	
-- Update business number of checkins on insert into checkins
CREATE OR REPLACE FUNCTION updateCheckin()
RETURNS TRIGGER AS
$$
BEGIN
	UPDATE Business
    SET Business.numcheckins = Business.numcheckins + 1
    WHERE Business.business_id = NEW.business_id;

END;
$$
LANGUAGE 'plpgsql'

CREATE TRIGGER updateBusCheckins
	AFTER INSERT
    ON checkins
    FOR EACH ROW
    EXECUTE PROCEDURE updateCheckin();
WHERE checkins.business_id = NEW.business_id;


--customers can only write reviews for open businesses (1)
CREATE OR REPLACE FUNCTION stopReview()
RETURNS trigger AS
$$
BEGIN
	IF (EXISTS (SELECT business.business_id
                         FROM business
                         WHERE business.is_open = 0 AND NEW.business_id = business.business_id))
	THEN
		RETURN NULL;
	END IF;
	RETURN NEW;
END;
$$
LANGUAGE 'plpgsql'


CREATE TRIGGER stopReview
BEFORE INSERT ON review
FOR EACH ROW
EXECUTE PROCEDURE stopReview()

--TESTS
-- Update reviewcount and review rating when a review is added
INSERT INTO review
VALUES ('j2810sk384hsk18260jsgu', 'g3V76Ja0XgWS1rqx0gxL_A', '2eJEUJIP54tex7T9YOcLSw', '2018-03-21', 'Cool stuff man.', 4,0, 0, 0);

-- Checkin increments business's num_checkin 
Insert into checkins
values ('Wednesday', 'morning', 1, 'VT5Eh1ksIng56j2YwYbHVg')

--Try to review a business that is not open 
INSERT INTO review
VALUES ('j2810sk384hsk18260js53', 'g3V76Ja0XgWS1rqx0gxL_A', 'SnlaPHqW3ksKfpH12pDGeg', '2018-03-21', 'Cool stuff man.', 2,0, 0, 0);