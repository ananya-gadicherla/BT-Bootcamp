--51. Count per state with heart attack, slope=2, ≥1 X-ray & symptom

SELECT a.state, COUNT(DISTINCT m.member_id) AS count
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN xray x ON c.cardio_id = x.cardiodiagnosis_cardio_id
JOIN symptom s ON c.cardio_id = s.cardiodiagnosis_cardio_id
JOIN wearabledevicedata w ON c.cardio_id = w.cardiodiagnosis_cardio_id
WHERE c.cardioarrestdetected=1
AND w.slope = 2
GROUP BY a.state;



--SELECT a.state, COUNT(DISTINCT m.member_id) AS count
--FROM memberinfo m
--JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
--JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
--JOIN wearabledevicedata w ON c.cardio_id = w.cardiodiagnosis_cardio_id
--WHERE c.cardioarrestdetected = 1
--AND w.slope = 2
--AND EXISTS (
--   SELECT 1
--    FROM xray x
--    WHERE x.cardiodiagnosis_cardio_id = c.cardio_id
--)
--AND EXISTS (
--    SELECT 1
--    FROM symptom s
--    WHERE s.cardiodiagnosis_cardio_id = c.cardio_id
--)
--GROUP BY a.state;
