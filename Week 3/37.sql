--37. Get members and their addresses
SELECT m.*, a.*
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id;