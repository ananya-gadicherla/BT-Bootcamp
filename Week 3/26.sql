--26. Get the total number of members in the database.

SELECT COUNT(*) AS total_members
FROM (
	SELECT *
	FROM memberinfo
)