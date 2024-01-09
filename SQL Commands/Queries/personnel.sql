SELECT DISTINCT
    PID.NIN,
    PID.FirstN,
    PID.MiddleN,
    PID.LastN,
    PINFO.Salary,
    TO_DATE(TO_CHAR(PINFO.Date_of_Birth, 'YYYY-MM-DD'), 'YYYY-MM-DD') AS Date_of_Birth,
    PINFO.Street,
    PINFO.home_number,
    PINFO.City,
    PINFO.province,
    PINFO.postalcode
FROM
    Personnel_ID PID
INNER JOIN
    Personnel_INFO PINFO
ON
    PID.NIN = PINFO.NIN;
ORDER BY
    PID.NIN,
    PID.LastN
