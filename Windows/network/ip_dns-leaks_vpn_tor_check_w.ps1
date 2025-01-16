# Script tocheck Tor and VPN connected
Write-Host "Checking Tor and VPN connection ..."
Write-Host ""

Write-Host "         _nnnn_"
Write-Host "        dGGGGMMb"
Write-Host "       @p~qp~~qMb"
Write-Host "       M|@||@) M|"
Write-Host "       @,----.JM|"
Write-Host "      JS^\__/  qKL"
Write-Host "     dZP        qKRb"
Write-Host "    dZP          qKKb"
Write-Host "   fZP            SMMb"
Write-Host "   HZM            MMMM"
Write-Host "   FqM            MMMM"
Write-Host " __| "".        |\dS""qML"
Write-Host " |    `.       | `' \Zq"
Write-Host "_)      \.___.,|     .'"
Write-Host "\____   )MMMMMP|   .'"
Write-Host "     `-'       `--' dtk"

# Rest of your script below...
Write-Host ""

# Using ASCII Art Progress Bar

# Function to display colored text in green
Function Write-GreenText {
    param (
        [string] $Text
    )

    Write-Host "`e[32m$Text`e[0m"
}

Function Show-ProgressBar {
    param (
        [int] $Total,
        [int] $Current
    )
    $PercentComplete = ($Current / $Total) * 100
    Write-GreenText ("[" + "-" * [math]::Round($PercentComplete) + "]" + "$PercentComplete%")
}

# Usage:
$TotalItems = 100
for ($i = 1; $i -le $TotalItems; $i++) {
    Show-ProgressBar -Total $TotalItems -Current $i
    Start-Sleep -Milliseconds 50  # Simulate some work being done
}


Write-Host  # Add a newline after the progress bar is complete
Write-Host ""


# Function to fetch the external IP address from api.ipify.org
Function Get-ExternalIpAddress {
    $externalIp = Invoke-RestMethod -Uri "https://api.ipify.org?format=text"
    return $externalIp
}

# Function to extract the IP address from dnsleaktest.com
Function Get-DnsLeakIpAddress {
    $html = (Invoke-WebRequest -Uri "https://dnsleaktest.com").Content
    $regex = '<p class="hello">Hello ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)</p>'
    
    $matches = [regex]::Matches($html, $regex)
    
    if ($matches.Count -gt 0) {
        $ipAddress = $matches[0].Groups[1].Value
        return $ipAddress
    } else {
        return "IP Address not found."
    }
}

Write-Host ""
Write-Host "IP Address found"
Write-Host ""
# Fetch the external IP address
$externalIp = Get-ExternalIpAddress
Write-Host "IP address from ipinfo.io is: $externalIp"

# Extract the IP address from dnsleaktest.com
$dnsLeakIp = Get-DnsLeakIpAddress
Write-Host "IP Address from dnsleaktest.com is: $dnsLeakIp"


# Function to run a PowerShell command and handle errors
Function Run-PowerShellCommand {
    param (
        [string] $command,
        [int] $timeout_seconds = 15
    )
    
    try {
        $result = Invoke-Expression -Command $command
        return $result.Trim()
    }
    catch {
        return "Error executing command: $_"
    }
}


Write-Host ""
Write-Host "Checking system for VPN connection"
Write-Host ""


# Using ASCII Art Progress Bar
Function Show-NeatProgressBar {
    param (
        [int] $Total,
        [int] $Current,
        [switch] $IsSuccess
    )

    $PercentComplete = [math]::Round(($Current / $Total) * 100)
    $ProgressBar = "[" + ("#" * [math]::Round($PercentComplete / 2)).PadRight(50) + "] $PercentComplete%"

    if ($IsSuccess) {
        # Green color for success
        $ProgressBar = "`e[32m" + $ProgressBar + "`e[0m"  # ANSI escape codes for green color
    } else {
        # Red color for failure
        $ProgressBar = "`e[31m" + $ProgressBar + "`e[0m"  # ANSI escape codes for red color
    }

    Write-Host -NoNewline $ProgressBar
}

# Usage with green color (success):
$TotalItems = 100
for ($i = 1; $i -le $TotalItems; $i++) {
    Show-NeatProgressBar -Total $TotalItems -Current $i -IsSuccess
    Start-Sleep -Milliseconds 50  # Simulate some work being done
    Write-Host -NoNewline "`r"  # Move the cursor back to the beginning of the line
}

# Usage with red color (failure):
for ($i = 1; $i -le 10; $i++) {
    Show-NeatProgressBar -Total 10 -Current $i
    Start-Sleep -Milliseconds 200  # Simulate some work being done
    Write-Host -NoNewline "`r"  # Move the cursor back to the beginning of the line
}


Write-Host  # Add a newline after the progress bar is complete
Write-Host ""
Write-Host "VPN Results"

# Function to check if ProtonVPN is being used
Function Check-ProtonVPNUsage {
    $dnsServers = (Get-DnsClientServerAddress).ServerAddresses

    # Check if the ProtonVPN DNS server is present
    $protonVpnDnsServers = @("10.2.0.1")  # ProtonVPN DNS server addresses
    $isProtonVpnUsed = $dnsServers -contains $protonVpnDnsServers[0] -or $dnsServers -contains $protonVpnDnsServers[1]

    if ($isProtonVpnUsed) {
        # If ProtonVPN DNS server is detected, return "yes"
        Write-Host "Yes, ProtonVPN is being used. IP Address: $externalIp."

        # Fetch additional information
        $externalIp = (Invoke-RestMethod -Uri "https://api.ipify.org?format=text")
        $apiUrl = "https://ipinfo.io/$externalIp/json"
        $response = Invoke-RestMethod -Uri $apiUrl

Write-Host ""
Write-Host "IP Address information Search"
Write-Host ""

# Using ASCII Art Progress Bar
Function Show-NeatProgressBar {
    param (
        [int] $Total,
        [int] $Current,
        [switch] $IsSuccess
    )

    $PercentComplete = [math]::Round(($Current / $Total) * 100)
    $ProgressBar = "[" + ("#" * [math]::Round($PercentComplete / 2)).PadRight(50) + "] $PercentComplete%"

    if ($IsSuccess) {
        # Green color for success
        $ProgressBar = "`e[32m" + $ProgressBar + "`e[0m"  # ANSI escape codes for green color
    } else {
        # Red color for failure
        $ProgressBar = "`e[31m" + $ProgressBar + "`e[0m"  # ANSI escape codes for red color
    }

    Write-Host -NoNewline $ProgressBar
}

# Usage with green color (success):
$TotalItems = 100
for ($i = 1; $i -le $TotalItems; $i++) {
    Show-NeatProgressBar -Total $TotalItems -Current $i -IsSuccess
    Start-Sleep -Milliseconds 50  # Simulate some work being done
    Write-Host -NoNewline "`r"  # Move the cursor back to the beginning of the line
}

# Usage with red color (failure):
for ($i = 1; $i -le 10; $i++) {
    Show-NeatProgressBar -Total 10 -Current $i
    Start-Sleep -Milliseconds 200  # Simulate some work being done
    Write-Host -NoNewline "`r"  # Move the cursor back to the beginning of the line
}

        # Extract and display the desired information
        Write-Host "My IP Address"
        Write-Host ""
        Write-Host "IP address: $($response.ip)"
        Write-Host ""
        Write-Host "Hostname: $($response.hostname)"
        Write-Host ""
        Write-Host "IP Address Location"
        Write-Host "Country: $($response.country)"
        Write-Host "State/Region: $($response.region)"
        Write-Host "City: $($response.city)"
        Write-Host "ISP: $($response.org)"
        Write-Host "Network: $($response.asn)"
        Write-Host "Usage Type: $($response.usage)"
         Write-Host ""
        Write-Host "Timezone: $($response.timezone)"
        Write-Host "Local Time: $($response.datetime)"
        Write-Host "Coordinates: $($response.loc)"
        Write-Host "Postal: $($response.postal)"
    } else {
        # If the ProtonVPN DNS server is not detected, return "no"
        Write-Host "No, ProtonVPN is not being used."
    }
}
Write-Host ""
# Call the function to check ProtonVPN usage
Check-ProtonVPNUsage

# DNS Test Leakage

Write-Host ""
Write-Host "DNS Test Leaks"
Write-Host ""

Function Show-NeatProgressBar {
    param (
        [int] $Total,
        [int] $Current,
        [switch] $IsSuccess
    )

    $PercentComplete = [math]::Round(($Current / $Total) * 100)
    $ProgressBar = "[" + ("#" * [math]::Round($PercentComplete / 2)).PadRight(50) + "] $PercentComplete%"

    if ($IsSuccess) {
        # Green color for success
        $ProgressBar = "`e[32m" + $ProgressBar + "`e[0m"  # ANSI escape codes for green color
    } else {
        # Red color for failure
        $ProgressBar = "`e[31m" + $ProgressBar + "`e[0m"  # ANSI escape codes for red color
    }

    Write-Host -NoNewline $ProgressBar
}

# Usage with green color (success):
$TotalItems = 100
for ($i = 1; $i -le $TotalItems; $i++) {
    Show-NeatProgressBar -Total $TotalItems -Current $i -IsSuccess
    Start-Sleep -Milliseconds 50  # Simulate some work being done
    Write-Host -NoNewline "`r"  # Move the cursor back to the beginning of the line
}

# Usage with red color (failure):
for ($i = 1; $i -le 10; $i++) {
    Show-NeatProgressBar -Total 10 -Current $i
    Start-Sleep -Milliseconds 200  # Simulate some work being done
    Write-Host -NoNewline "`r"  # Move the cursor back to the beginning of the line
}

Write-Host ""

$html = (Invoke-WebRequest -Uri "https://dnsleaktest.com/").Content
$regex = '<p class="hello">Hello ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)</p>'
Write-Host ""
Write-Host "DNS Test Leaks Results"
Write-Host ""
$matches = [regex]::Matches($html, $regex)

if ($matches.Count -gt 0) {
    $ipAddress = $matches[0].Groups[1].Value
    Write-Host "IP Address: $ipAddress"
} else {
    Write-Host "IP Address not found."
}

Write-Host ""
# Tor connection status
Write-Host ""
Write-Host "Tor Connection Status"
Write-Host ""

# App Description and Author
$AppDescription = "This tool tests Tor connection."
$AppAuthor = "Made by Dave"

# Run Get-Process with Path filter
$processesWithPath = Get-Process | Where-Object { $_.Path -eq "C:\Tor\tor\tor.exe" }
$processesWithPath

Write-Host ""

# Run Get-Process with Name filter and select the first one
$firstTorProcess = Get-Process -Name tor | Select-Object -First 1

if ($firstTorProcess) {
    Write-Host "Tor process is running, my friend. The hidden world awaits."
} else {
    Write-Host "Tor is not running. The darkness remains concealed."
    Write-Host ""
    $response = Read-Host "Do you want to start Tor? (yes/no)"
    if ($response -eq "yes") {
        Write-Host ""
        Start-Process -FilePath "C:\Users\david\OneDrive\Projects_Mac\Projects\August-Projects\ps1-projects\tor_connect\tor_start.exe"
        Write-Host "Tor is starting. Please wait..."
        Write-Host ""
        Start-Sleep -Seconds 20  # Wait for 20 seconds
        Write-Host "Tor should now be running. Re-run this script to check the status."
    } else {
        Write-Host "Tor will not be started. You can manually start it when needed."
    }
}

Write-Host ""

# Test network connection to localhost on port 9150
$netTestResult = Test-NetConnection -ComputerName 127.0.0.1 -Port 9150

if ($netTestResult.TcpTestSucceeded) {
    Write-Host "Successful connection to Tor is established, my friend. The hidden world awaits"
} else {
    Write-Host "Connection to Tor could not be established. The darkness remains concealed"
}
Write-Host ""

# Function to fetch the external IP address using Tor SocksPort
Function Get-ExternalIpAddress {
    $externalIp = Invoke-Expression -Command 'curl --socks5 127.0.0.1:9150 https://api.ipify.org?format=text'
    return $externalIp
}

# Usage:
$externalIp = Get-ExternalIpAddress
Write-Host "Your external IP address is, and will check every few minutes: $externalIp"

Write-Host ""
# Function to display colored text
Function Write-ColoredText {
    param (
        [string] $Text,
        [string] $Color
    )

    Write-Host "`e[$Color$Text`e[0m"
}

# Function to display the colored banner
Function Add-ColoredBanner {
    Write-Host -ForegroundColor Red $coloredBanner
}

# Colored banner content
$coloredBanner = @"
            ____  ___    _   __________________       _____ __  _____  __________  __
           / __ \/   |  / | / / ____/ ____/ __ \     / ___//  |/  /\ \/ /_  __/ / / /
          / /_/ / /| | /  |/ / / __/ __/ / /_/ /_____\__ \/ /|_/ /  \  / / / / /_/ /
         / _, _/ ___ |/ /|  / /_/ / /___/ _, _/_____/__/ / /  / /   / / / / / __  /
        /_/ |_/_/  |_/_/ |_/\____/_____/_/ |_|     /____/_/  /_/   /_/ /_/ /_/ /_/


                                          __    _
                                    _wr""        "-q__
                                 _dP                 9m_
                               _#P                     9#_
                              d#@                       9#m
                             d##                         ###
                            J###                         ###L
                            {###K                       J###K
                            ]####K      ___aaa___      J####F
                        __gmM######_  w#P""   ""9#m  _d#####Mmw__
                     _g##############mZ_         __g#############@@#m_
                   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_
                  a###""          ,Z"#####@" '######"\g          ""M##m_
                 J#@"             0L  "*##     ##@"  J#              *#K
                 #"               `#    "_gmwgm_~    dF               `#_
                7F                 "#_   ]#####F   _dK                 JE
                ]                    *m__ ##### __g@"                   F
                                       "PJ#####LP"
                 `                       0######_                      '
                                       _0########_
                     .               _d#####^#####m__              ,
                      "*w_________am#####P"   ~9#####mw_________w*"
                          ""9@#####@M""           ""P@#####@M""

"@

# Check if the user wants to exit
Write-Host "Press 'Y' to exit or 'N' to continue..."
$choice = Read-Host
if ($choice -eq 'Y' -or $choice -eq 'y') {
    # Display the colored banner
    Add-ColoredBanner
    exit
}

if ($choice -eq 'N' -or $choice -eq 'n') {
    # Continue running the script
    
    # Run the Python file
    $pythonScriptPath = "C:\Users\david\OneDrive\Projects_Mac\Projects\August-Projects\hack_firefox\pretend_hack.py"
    if (Test-Path $pythonScriptPath) {
        Write-Host "Running the Python script..."
        python.exe $pythonScriptPath
    } else {
        Write-Host "Python script not found at $pythonScriptPath"
    }
}
