# Get a list of all network adapters
$adapters = Get-NetAdapter

# Check if any adapters are found
if ($adapters.Count -gt 0) {
    Write-Host "Network Adapters:"
    
    # Display details for each network adapter
    $adapters | ForEach-Object {
        Write-Host "Name: $($_.Name)"
        Write-Host "Description: $($_.InterfaceDescription)"
        Write-Host "Status: $($_.Status)"
        Write-Host "MAC Address: $($_.MacAddress)"
        Write-Host "Adapter Type: $($_.MediaType)"
        
        # Get IP configuration for the adapter
        $ipConfig = Get-NetIPAddress -InterfaceIndex $_.ifIndex | Where-Object { $_.AddressFamily -eq 'IPv4' }
        if ($ipConfig) {
            Write-Host "IPv4 Address: $($ipConfig.IPAddress)"
            Write-Host "Subnet Mask: $($ipConfig.PrefixLength)"
            Write-Host "Default Gateway: $($ipConfig.DefaultGateway)"
        }
        
        # Get DNS settings for the adapter
        $dnsConfig = Get-DnsClientServerAddress -InterfaceIndex $_.ifIndex
        if ($dnsConfig) {
            Write-Host "DNS Servers:"
            $dnsConfig.ServerAddresses | ForEach-Object {
                Write-Host "  $_"
            }
        }
        
        Write-Host ""
    }
} else {
    Write-Host "No network adapters found."
}
