SELECT
    P.Customer_Id,
    P.Phone,
    P.Email,
    PI.FirstN,
    PI.MiddleN,
    PI.LastN,
    PI.city,
    PI.postalCode,
    PI.street,
    PI.province
FROM
    Passenger_ID P
INNER JOIN
    Passenger_INFO PI
ON
    P.Phone = PI.Phone AND P.Email = PI.Email;
ORDER BY
    P.Customer_Id,
    PI.LastN