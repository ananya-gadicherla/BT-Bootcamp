--47. Avg BP for age groups 40–50 and 50–60
SELECT
  CASE
    WHEN m.age BETWEEN 40 AND 49 THEN '40-49'
    WHEN m.age BETWEEN 50 AND 60 THEN '50-60'
  END AS age_group,
  AVG(b.bloodpressure) AS avg_bp
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b ON c.cardio_id = b.cardiodiagnosis_cardio_id
WHERE m.age BETWEEN 40 AND 60
GROUP BY age_group;
