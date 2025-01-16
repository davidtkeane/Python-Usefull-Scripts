$subnet = "192.168.1"  # Replace with your subnet
$range = 1..254

foreach ($i in $range) {
    $ip = "$subnet.$i"
    $result = Test-Connection -ComputerName $ip -Count 1 -ErrorAction SilentlyContinue
    if ($result) {
        $dns = Resolve-DnsName -Name $ip -ErrorAction SilentlyContinue
        if ($dns) {
            $computerType = $dns.QueryType
            $computerName = $dns.NameHost
            Write-Host "Computer at $ip is online. Type: $computerType, Name: $computerName"
        } else {
            Write-Host "Computer at $ip is online."
        }
    }
}
