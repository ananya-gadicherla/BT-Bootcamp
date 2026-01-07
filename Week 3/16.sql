--16. Get wearable device data for cardio IDs between CID100 and CID200

SELECT *
FROM wearabledevicedata
WHERE wearabledevicedata.cardiodiagnosis_cardio_id BETWEEN 'CID100' AND 'CID200';