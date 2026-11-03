$env:AWS_PROFILE = "signin"
$token = $(aws cognito-idp initiate-auth --auth-flow USER_PASSWORD_AUTH --client-id "4mm560mu7hh9p3bhjlnk9f9sl1" --auth-parameters USERNAME="amalsaadon@hotmail.com",PASSWORD="Saadon123321@" --query "AuthenticationResult.IdToken" --output text)
$employees = Invoke-RestMethod -Uri "https://txzumolyx7.execute-api.us-east-1.amazonaws.com/prod/employees" -Headers @{Authorization=$token}
$userId = $employees.employees[0].employeeId
Write-Host "USER_ID: $userId"
$body = '{"user_id": "' + $userId + '", "start_date": "2026-07-01", "end_date": "2026-07-05"}'
$result = Invoke-RestMethod -Uri "https://txzumolyx7.execute-api.us-east-1.amazonaws.com/prod/hr-requests/time-off" -Method POST -Headers @{Authorization=$token; "Content-Type"="application/json"} -Body $body
$result | ConvertTo-Json
