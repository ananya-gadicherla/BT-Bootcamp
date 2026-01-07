--14. Get symptom details for July 2019

SELECT *
FROM symptom
WHERE EXTRACT(MONTH FROM symptom.date) = 7
AND EXTRACT(YEAR FROM symptom.date) = 2019;