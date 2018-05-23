function GetIP {
	$IP = Get-NetIPAddress | Where-Object {$_.IPv4Address -like '10*'}
	return $IP.IPv4Address
}
