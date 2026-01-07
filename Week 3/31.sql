--31. Get number of males and females aged 50–60

SELECT gender, COUNT(*) AS count
FROM memberinfo
WHERE age BETWEEN 50 AND 60
GROUP BY gender;