<#
    Clifton Wolfe
    Usage: run this script to load the function into memory, then execute the function with "Invoke-SubnetDNSResolve"
    The function requires three parameters, the first three octets of the subnet you wish to enumerate
#>
function Invoke-SubnetDNSResolve{
    [cmdletbinding()]
    Param(
        [Parameter(Mandatory=$true,position=0)]
        $1,
        [Parameter(Mandatory=$true,position=1)]
        $2,
        [Parameter(Mandatory=$true,position=2)]
        $3
    )

    $addresses = for($i = 1; $i -lt 255;$i++){
        Write-Verbose -Message "Starting async-resolve for: $1`.$2`.$3`.$i" 
        [system.net.dns]::GetHostEntryAsync("$1`.$2`.$3`.$i")
    }
    Write-Verbose -Message "Waiting on Async-resolves..."
    return ($addresses|where{$_.status -ne "Faulted"}).result | where{$_ -ne $null}
}

#Invoke-SubnetDNSResolve 192 168 1
