--38. Get members and their cardio history

SELECT m.*, c.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id;