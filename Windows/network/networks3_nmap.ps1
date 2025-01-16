# Sure, here is the PowerShell script that you can use to scan a subnet for devices:

$subnet = "192.168.1"
$range = 1..254

foreach ($i in $range) {
    $ip = "$subnet.$i"

    # Ping the device using nmap and capture ping response time
    $pingResult = & nmap.exe $ip

    if ($pingResult -match "Host is up") {
        $pingStatus = "Online"
        # Extract ping response time from the ping result
        $pingResponseTime = $pingResult | Select-String -Pattern "Host is up \((\d+\.\d+)s latency\)" | ForEach-Object { $_.Matches.Groups[1].Value }

        # Device is online, proceed with port scanning
        $nmapOutput = & nmap.exe $ip

        $macMatch = $nmapOutput | Select-String -Pattern "MAC Address: ([0-9A-Fa-f:]+) \(.+?\)"
        if ($macMatch) {
            $macAddress = $macMatch.Matches.Groups[1].Value
        } else {
            $macAddress = "Unknown"
        }

        $dns = Resolve-DnsName -Name $ip -ErrorAction SilentlyContinue
        if ($dns) {
            $computerType = $dns.QueryType
            $computerName = $dns.NameHost.Split()[0]  # Use only the first name
            Write-Host "Device at $ip is $pingStatus. Ping: $pingResponseTime ms. Type: $computerType, Name: $computerName, MAC Address: $macAddress"
        } else {
            Write-Host "Device at $ip is $pingStatus. Ping: $pingResponseTime ms. Type: Unknown, MAC Address: $macAddress"
        }
    } else {
        $pingStatus = "Offline"
        Write-Host "Device at $ip is $pingStatus."
    }
}


<# This script will first ping each device in the subnet. If the device is up, the script will then run an nmap scan to determine the open ports and the MAC address of the device. If the device is registered in DNS, the script will also display the computer name and type.

To run this script, you will need to have the following installed on your system:

PowerShell
Nmap
DNS
Once you have all of the necessary software installed, you can run the script by typing the following command at the PowerShell prompt:

PowerShell
.\scan-subnet.ps1
Use code with caution. Learn more
The script will then scan the subnet and display the results. #>

