$IP = (Get-NetIPAddress | Where-Object {$_.IPv4Address -like '10*'}).IPv4Address
$Body = "Hostname: $env:COMPUTERNAME`n`rIP Address: $IP"
Send-MailMessage -Body $Body -Subject IT3030 -From wolfeco@mail.uc.edu -To wolfeco@mail.uc.edu -SmtpServer smtp.uc.edu
