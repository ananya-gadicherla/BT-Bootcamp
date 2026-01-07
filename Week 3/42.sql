--42. Males with BP > 140 and no heart attack

SELECT DISTINCT m.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b ON c.cardio_id = b.cardiodiagnosis_cardio_id
WHERE m.gender = '0'
AND b.bloodpressure > 140
AND c.cardioarrestdetected=0;