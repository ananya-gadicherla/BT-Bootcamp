--27. Get the total number of blood tests done.

SELECT COUNT(*) AS total_bloodtests
FROM (
	SELECT *
	FROM bloodtest
)