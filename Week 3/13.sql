--13. Get symptom details for cardio IDs CID250 and CID300

SELECT *
FROM symptom s
WHERE s.cardiodiagnosis_cardio_id IN ('CID250', 'CID300');