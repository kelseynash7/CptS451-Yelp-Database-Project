-- Lyndsay Clarke 11066266
--1
SELECT DISTINCT course.courseno, course.credits
FROM course, student, enroll
WHERE student.trackcode = 'SYS' and student.major = 'CptS' and student.sID = enroll.sID and enroll.courseno = course.courseno
GROUP BY course.courseno, course.credits
ORDER BY course.courseno, course.credits;
--2
SELECT student.sName, student.sID, student.major, student.trackcode, SUM(credits)
FROM student, enroll, course
WHERE student.sID = enroll.sID and enroll.courseno = course.courseno
GROUP BY student.sID
HAVING SUM(credits) > 18
ORDER BY sname;
--3
SELECT a.courseno
FROM (SELECT DISTINCT courseno
	FROM enroll, student
	WHERE student.trackcode = 'SE' and student.sid = enroll.sid) a
		LEFT JOIN
			(SELECT DISTINCT courseno
			FROM enroll, student
			WHERE student.trackcode != 'SE' and student.sid = enroll.sid) b ON b.courseno = a.courseno
WHERE b.courseno is null;
--4
SELECT DISTINCT sname, sid, major, courseno, grade 
FROM (SELECT courseno, sid as sid1, grade
FROM ((SELECT courseno as COURSE, grade as GRADE1
	FROM enroll, student
	WHERE student.sname = 'Diane' and student.sid = enroll.sid) a INNER JOIN enroll on a.COURSE = enroll.courseno AND a.grade1 = enroll.grade)) b INNER JOIN student ON student.sid = b.sid1 AND sname != 'Diane'
--5
SELECT student.sname, student.sid
FROM enroll RIGHT OUTER JOIN student
ON student.sid = enroll.sid
WHERE student.major = 'CptS' and enroll.courseno is null;
--6
SELECT a.courseno, enroll_limit, enroll_num
FROM (SELECT course.courseno, enroll_limit
	FROM course
	WHERE classroom LIKE 'Sloan%'
	ORDER BY courseno) a RIGHT OUTER JOIN (SELECT DISTINCT courseno as course1, COUNT(enroll.sid) as enroll_num
	FROM enroll
	GROUP BY course1) as b ON b.course1 = a.courseno AND enroll_limit < enroll_num
WHERE courseno is not null
ORDER BY courseno
--7
--8
--9
--10
--This expression is returning the courseno and pcount 
--for course numbers that have more than 2 prerequisites