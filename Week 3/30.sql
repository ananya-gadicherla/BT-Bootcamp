--30. Get the list of tests done between January 1, 2015, and January 31, 2019

SELECT *
FROM cardiodiagnosis
WHERE cardiodiagnosis.date BETWEEN '2015-01-01' AND '2019-01-31';