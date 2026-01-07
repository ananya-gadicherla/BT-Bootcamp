--46. Count of males and females with BP >140 and heart attack

SELECT m.gender, COUNT(DISTINCT m.member_id) AS count
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b ON c.cardio_id = b.cardiodiagnosis_cardio_id
WHERE b.bloodpressure > 140
AND c.cardioarrestdetected=1
GROUP BY m.gender;