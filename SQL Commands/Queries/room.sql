SELECT DISTINCT
    R.RoomNumber,
    R.NumberOfBed,
    R.PricePerNight,
    CASE 
        WHEN SR.RoomNumber IS NOT NULL THEN 'Single'
        WHEN TR.RoomNumber IS NOT NULL THEN 'Twin'
        WHEN KR.RoomNumber IS NOT NULL THEN 'King'
        ELSE 'Unknown'
    END AS RoomType
FROM
    Room R
    LEFT JOIN SingleRoom SR ON R.RoomNumber = SR.RoomNumber
    LEFT JOIN TwinRoom TR ON R.RoomNumber = TR.RoomNumber
    LEFT JOIN KingRoom KR ON R.RoomNumber = KR.RoomNumber
ORDER BY
    RoomType,
    R.RoomNumber;