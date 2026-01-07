--49. People with X-rays every month from Special Province

SELECT COUNT(DISTINCT m.member_id)
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN xray x ON c.cardio_id = x.cardiodiagnosis_cardio_id
WHERE a.state = 'Special Province';