# Get a list of network adapters
$adapters = Get-NetAdapter | Where-Object { $_.MediaType -eq 'Ethernet' }

# Check if any Ethernet adapters are found
if ($adapters.Count -gt 0) {
    Write-Host "Ethernet Adapter(s) found:"
    
    # Display the names of the Ethernet adapters
    $adapters | ForEach-Object {
        Write-Host $_.Name
    }
} else {
    Write-Host "No Ethernet adapters found."
}
