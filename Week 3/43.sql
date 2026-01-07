--43. Members with heart attack from Mountain Province

SELECT DISTINCT m.*
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
WHERE a.state = 'Mountain Province'
AND c.cardioarrestdetected=1;
