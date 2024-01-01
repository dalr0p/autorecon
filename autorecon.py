import subprocess
import os
import sys
import time

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode('utf-8'), error.decode('utf-8'), process.returncode

def loading_animation(duration=30):
    end_time = time.time() + duration
    while time.time() < end_time:
        for i in range(4):
            sys.stdout.write('\rProcessing' + '.' * i)
            sys.stdout.flush()
            time.sleep(0.5)
    print("\n")

def create_checkpoint(domain):
    with open('checkpoint.txt', 'w') as checkpoint_file:
        checkpoint_file.write(domain)

def load_checkpoint():
    if os.path.exists('checkpoint.txt'):
        with open('checkpoint.txt', 'r') as checkpoint_file:
            return checkpoint_file.read().strip()
    return None

def main():
    print("\033[93m")
    print(r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠠⠤⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠄⠂⠁⠁⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠄⠊⠁⣀⡀⠤⠒⢋⣉⣉⣉⣉⣁⡀⠀⠀⠀⠀⠀⠀⠈⠙⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡀⠂⣁⡔⣒⣭⣵⠶⠿⠛⣻⠖⡲⠖⡲⢒⣻⣷⣶⡦⢤⣄⣀⠀⠀⠀⠀⠉⠲⣄⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡤⠪⣊⡵⠞⠋⠉⠄⢀⠊⠁⡟⡥⣞⡁⠘⠛⣩⣔⠛⡻⣿⡶⡄⠁⠉⠶⣄⡀⠀⠀⠈⠳⡄⠀⠀⠀⠀
⠀⣨⡴⠟⠑⠠⠀⠉⠁⠁⠐⠂⣼⢣⡾⡏⡡⠃⠀⠀⠀⠀⢀⡈⣟⣿⡄⠐⡀⠂⠙⢦⡀⠀⠀⠙⡆⠀⠀⠀⠀
⢰⡿⡅⢁⠁⠄⠀⠀⠀⠀⠀⠀⡇⠀⢠⢹⠀⠀⢠⣿⣿⡆⠀⡟⣟⣻⣇⠀⠀⠀⠉⢁⠙⢦⠀⠀⢹⡀⠀⠀⠀
⢻⣇⡇⠠⠈⠁⠀⠀⠀⠀⠀⠀⢱⢸⣼⢸⠀⠀⠈⠛⢛⣁⠜⠀⡿⣿⣿⠀⠀⠀⠀⡐⠈⡐⡳⡀⠀⢧⠀⠀⠀
⠀⠻⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⣏⣾⡑⣧⡀⠀⠘⠓⠦⠶⢽⣿⡿⠗⠁⠀⠀⠀⠀⠄⢀⡹⡄⠈⡆⠀⠀AUTORECON by dalr0p
⠀⠀⠀⠈⠛⢧⡀⠀⠀⠀⠀⠀⠀⠈⠓⠿⣖⡛⢷⣦⣤⣤⡴⢿⡿⠗⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀
⠀⠀⠀⠀⠦⡄⠉⠳⢦⣄⡀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠋⠉⠉⠉⠀⢀⣀⣀⣀⡤⠤⠶⠶⠛⠛⠳⠽⠄⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠳⣄⡀⠈⠙⠛⠲⠦⠤⠤⠤⠤⠤⠤⠶⠒⠒⠋⠉⠉⠉⠁⢀⡤⠖⠒⠒⠒⠒⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⣀⣀⣀⣀⣀⡤⠤⠤⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)
    print("\033[0m")

    # Prompt the user for the name of the file containing the list of domains
    domains_file = input("Enter the name of the file containing the list of domains: ")

    with open(domains_file, 'r') as file:
        domains = file.read().splitlines()

    result_folder = 'results'
    os.makedirs(result_folder, exist_ok=True)

    # Load checkpoint
    last_completed_domain = load_checkpoint()
    if last_completed_domain:
        start_index = domains.index(last_completed_domain) + 1
        domains = domains[start_index:]

    for domain in domains:
        print(f"\n\033[93mProcessing domain: {domain}\033[0m")
        loading_animation(30)

        current_domain_file = f"{domain}_subdomains.txt"
        http_output_file = f"{domain}_httpsubdomains.txt"
        login_output_file = f"{domain}_login.txt"

        # Subdomain enumeration with Assetfinder
        print("\033[92mRunning Assetfinder...\033[0m")
        command = f'assetfinder {domain} >> {current_domain_file}'
        _, _, return_code = run_command(command)
        if return_code != 0:
            print("\033[91mError running Assetfinder - Skipping to the next domain\033[0m")
            continue

        # Subdomain enumeration with Subfinder
        print("\033[92mRunning Subfinder...\033[0m")
        command = f'subfinder -d {domain} -o {current_domain_file}'
        _, _, return_code = run_command(command)
        if return_code != 0:
            print("\033[91mError running Subfinder - Skipping to the next domain\033[0m")
            continue

        # Subdomain enumeration with Sublist3r
        print("\033[92mRunning Sublist3r...\033[0m")
        command = f'python /home/kali/Sublist3r/sublist3r.py -n -v -d "{domain}" -t 10 -e "baidu,yahoo,google,bing,ask,netcraft,dnsdumpster,threatcrowd,ssl,passivedns" -o {current_domain_file}'
        _, _, return_code = run_command(command)
        if return_code != 0:
            print("\033[91mError running Sublist3r - Skipping to the next domain\033[0m")
            continue

        # Remove duplicates
        print("\033[92mRemoving duplicates...\033[0m")
        run_command(f'sort -u -o {current_domain_file} {current_domain_file}')

        # HTTPX scan
        print("\033[92mRunning HTTPX scan...\033[0m")
        run_command(f'cat {current_domain_file} | /root/go/bin/httpx -silent -title -sc -fr >> {http_output_file}')

        # Remove codes 400
        print("\033[92mRemoving codes 400...\033[0m")
        run_command(f'cat {http_output_file} | grep -v "403\\|404\\|400" > temp.txt && mv temp.txt {http_output_file}')

        # Find login pages
        print("\033[92mFinding login pages...\033[0m")
        run_command(f'cat {http_output_file} | grep "login\\|Login\\|register\\|signup\\|signin" > {login_output_file}')

        # Filter 200 status codes
        print("\033[92mFiltering 200 status codes...\033[0m")
        run_command(f'cat {http_output_file} | grep -v "403\\|404\\|400" | grep "200" | cut -d" " -f1 > temp.txt && mv temp.txt {http_output_file}')

        # Move results to the domain-specific folder
        domain_folder = os.path.join(result_folder, domain)
        os.makedirs(domain_folder, exist_ok=True)

        os.rename(current_domain_file, os.path.join(domain_folder, current_domain_file))
        os.rename(http_output_file, os.path.join(domain_folder, http_output_file))
        os.rename(login_output_file, os.path.join(domain_folder, login_output_file))

        # Create checkpoint
        create_checkpoint(domain)

        print(f"\033[92mFinished processing domain: {domain}\033[0m\n")

    print("\033[96mScript completed successfully\033[0m")

if __name__ == "__main__":
    main()
