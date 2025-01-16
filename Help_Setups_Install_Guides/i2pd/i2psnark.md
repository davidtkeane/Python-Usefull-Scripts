
Here's a detailed step-by-step guide on how to install and use I2PSnark:

Installation of I2PSnark
Prerequisites:
I2P Installed: I2PSnark is a component of I2P, so you need I2P installed on your system. Follow the general I2P installation guide for your OS.

Step 1: Ensure I2P is Running
After installing I2P, ensure it is running. You can check this by navigating to http://127.0.0.1:7657/ in your browser (default I2P router console address).

Step 2: Access I2PSnark
I2PSnark should be available by default if you've installed I2P with the full package or the easy install bundle. 
Navigate to http://127.0.0.1:7657/i2psnark/ in your browser. This should open the I2PSnark interface.

Step 3: For Standalone Installation (Optional)
If you prefer or need a standalone version (like i2psnark-standalone from I2P+):
Download the i2psnark-standalone build from the I2P+ project website.
Ensure you have Java installed since I2PSnark requires it.
Extract the downloaded archive to a directory of your choice.
Run java -jar i2psnark.jar from the command line in the directory where you've extracted the files. 
Configure your I2P instance to allow external connections if necessary, by setting i2cp.enabled=true in your i2pd.conf if using i2pd.


Usage of I2PSnark
Step 1: Adding Torrents
Via Web Interface:
Go to the I2PSnark web console at http://127.0.0.1:8002/i2psnark/ if using standalone or http://127.0.0.1:7657/i2psnark/ if integrated with I2P.
Click on "Add Torrent" or a similar option.
You can either:
Upload a Torrent File: Click "Browse" to select a .torrent file from your computer.
Enter a URL: If the torrent is available online within I2P, enter the I2P link directly.

Step 2: Managing Torrents
Start/Stop Torrents:
Select the torrents you want to control and use the "Start" or "Stop" buttons.
To start all, there's usually a "Start All" button or option.
Change Settings:
Look for a settings or configuration icon (often a gear or cog). Here you can:
Set the download directory for new torrents.
Adjust bandwidth limits for uploading and downloading.
Modify tunnel settings for better performance or privacy.


Step 3: Monitoring Downloads
Monitor the progress in the main interface:
Check the status, speed, and estimated time for completion.
If a download seems stuck, you can force a recheck by selecting the torrent and choosing "Force Recheck".

Step 4: Sharing Files
To share files:
Create a torrent file:
Use the "Create Torrent" feature if available. Select the files or folder you want to share, set the tracker to something like http://tracker.postman.i2p/announce, and save the torrent file.
Share this torrent file or its magnet link with others through I2P communication methods like email or forums.

Step 5: Troubleshooting
Permissions Issues: Ensure you have the right permissions to write to the directories where I2PSnark is trying to save files.

Connection Issues: Check if I2P is properly connected to the network and if your I2CP settings are correct.


Step 6: Security Considerations
Always be cautious with torrents from unknown sources as they could contain malware.
Keep your I2P software updated to benefit from security patches and performance improvements.

By following these steps, you should be able to install and use I2PSnark effectively for sharing and downloading files anonymously within the I2P network. Remember, I2PSnark only works within I2P, providing privacy but with slower speeds due to the nature of the network.