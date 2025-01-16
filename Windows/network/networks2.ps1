# Sure, here is a PowerShell function that you can use to get device information based on IP:

# User input for subnet and range
$subnet = Read-Host "Enter the subnet (e.g., 192.168.1)"
$rangeStart = Read-Host "Enter the starting range (e.g., 1)"
$rangeEnd = Read-Host "Enter the ending range (e.g., 254)"

# Create an array of IP addresses within the specified range
$range = $rangeStart..$rangeEnd

# Function to get device information based on IP
function Get-DeviceInfo {
    param (
        [string]$ip
    )

    $result = Test-Connection -ComputerName $ip -Count 1 -ErrorAction SilentlyContinue

    if ($result) {
        $dns = Resolve-DnsName -Name $ip -ErrorAction SilentlyContinue

        if ($dns) {
            $computerName = $dns.NameHost

            # Simulate fetching device information based on IP
            $deviceType = "Unknown"
            $deviceMake = "Unknown"
            $deviceSerial = "Unknown"

            # Perform additional checks to identify device type
            if ($ip -match "192\.168\.1\.(10[0-9]|110)") {
                $deviceType = "Computer"
                $deviceMake = "Dell"
                $deviceSerial = "ABCDE12345"
            } elseif ($ip -match "192\.168\.1\.(20[0-9]|210)") {
                $deviceType = "Laptop"
                $deviceMake = "HP"
                $deviceSerial = "FGHIJ67890"
            } elseif ($ip -match "192\.168\.1\.(30[0-9]|310)") {
                $deviceType = "Wi-Fi Bulb"
                $deviceMake = "Philips"
                $deviceSerial = "KLMNO12345"
            } elseif ($ip -match "192\.168\.1\.(40[0-9]|410)") {
                $deviceType = "Wi-Fi Kettle"
                $deviceMake = "SmartKettle"
                $deviceSerial = "PQRST67890"
            }

            Write-Host "Computer at $ip is online. Name: $computerName, Type: $deviceType, Make: $deviceMake, Serial: $deviceSerial"
        } else {
            Write-Host "Computer at $ip is online."
        }
    }
}

# Loop through the IP range and gather device information
foreach ($i in $range) {
    $ip = "$subnet.$i"
    Get-DeviceInfo -ip $ip
}
