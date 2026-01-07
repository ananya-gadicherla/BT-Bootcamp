--36. Number of patients in each age group
SELECT
  CASE
    WHEN age BETWEEN 10 AND 20 THEN '10-20'
    WHEN age BETWEEN 20 AND 30 THEN '20-30'
    WHEN age BETWEEN 30 AND 40 THEN '30-40'
    WHEN age BETWEEN 40 AND 50 THEN '40-50'
    WHEN age BETWEEN 50 AND 60 THEN '50-60'
    WHEN age BETWEEN 60 AND 70 THEN '60-70'
  END AS age_group,
  COUNT(*) AS count
FROM memberinfo
GROUP BY age_group
ORDER BY age_group;
