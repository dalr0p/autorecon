# AUT0 R3C0N
# ![bannermolon](https://github.com/dalr0p/autorecon/assets/137183562/7eae688a-37f5-4c9c-9ae9-c14f58a2ce36)


BUG BOUNTY AUTORECON
AUTO RECON PYTHON SCRIPT
**NOTE THE SCRIPT IS STEP UP TO WORK IN MY COMPUTER IF USED PLEASE MODIFY PATH OF TOOLS AND MAKE SURE HAVE ALL REQUIREMENTS:
  -Assetfinder, Subfinder, Sublist3r, HTTPX
Here's a step-by-step explanation of what the script does:

User Input:

The script iterates through each domain in the provided list.
For each domain, it performs subdomain enumeration using three tools: Assetfinder, Subfinder, and Sublist3r.
Results from each tool are saved in a file named <domain>_subdomains.txt.
Removing Duplicates:

Subdomain Enumeration:

The script iterates through each domain in the provided list.
For each domain, it performs subdomain enumeration using three tools: Assetfinder, Subfinder, and Sublist3r.
Results from each tool are saved in a file named <domain>_subdomains.txt.

![image](https://github.com/dalr0p/autorecon/assets/137183562/23f3aa04-874b-468d-bc9b-3f4a96f0b997)


It removes duplicate subdomains from the results file.
HTTPX Scan:

It runs an HTTPX scan on the obtained subdomains to gather information like titles, status codes, and fingerprints.
The HTTPX results are saved in a file named <domain>_httpsubdomains.txt.
Removing 400 Status Codes:

It removes subdomains with HTTP status codes 400 (Bad Request) from the HTTPX results.
Finding Login Pages:

It searches for subdomains with keywords like "login," "Login," "register," "signup," and "signin" in the HTTPX results.
The login pages are saved in a file named <domain>_login.txt.
Filtering 200 Status Codes:

It filters subdomains with HTTP status code 200 from the HTTPX results.
The filtered subdomains are saved in the same <domain>_httpsubdomains.txt file.
Results Organization:

It organizes the results by creating a folder named 'results' and subfolders for each domain.
The subdomain, HTTPX, and login files are moved to their respective domain-specific folders.

![image](https://github.com/dalr0p/autorecon/assets/137183562/c1857e51-1984-4442-98c3-8abe64fbc880)

Checkpoint Update:
After processing each domain, the script updates the checkpoint to remember the last completed domain.
Completion Message:
Finally, it prints a completion message in cyan.
The script provides a comprehensive approach to subdomain enumeration and information gathering for a list of domains, and it's designed to be user-friendly with an interactive and visually appealing interface.
