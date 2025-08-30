#!/usr/bin/python
# << CODE BASED BY HUNX04
# << MADE BY FARHAN
# << WANT TO RECODE??? PERMISSION FIRST, AT LEAST TAG MIMIN'S GITHUB ACCOUNT THAT LEADS TO THIS ACCOUNT, IT'S EASIER TO USE FORK
# << IF THE ABOVE IS NOT FOLLOWED THEN YOU WILL GET SIN BECAUSE MIMIN IS NOT SINCERE
# "O you who believe! Do not consume each other's wealth in a false way," (QS. An Nisaa': 29). Rasulullah SAW also prohibited his people from taking other people's rights without permission.

# IMPORT MODULES
import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr
import sys
import socket
import re

# COLOR VARIABLES
class Colors:
    BLACK = '\033[30m'
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    CYAN = '\033[1;36m'
    WHITE = '\033[0;37m'
    RESET = '\033[0m'

# VALIDATION FUNCTIONS
def validate_ip(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(pattern, ip):
        parts = ip.split('.')
        if all(0 <= int(part) <= 255 for part in parts):
            return True
    return False

def validate_phone(phone):
    try:
        parsed = phonenumbers.parse(phone, None)
        return phonenumbers.is_valid_number(parsed)
    except:
        return False

# TRACKING FUNCTIONS
def track_ip():
    os.system('clear')
    time.sleep(1)
    stderr.writelines(f"""{Colors.YELLOW}
               ___  __        __       
   | | |\ | __  |  |__)  /\  /  ` |__/ 
\__/ | | \|     |  |  \ /~~\ \__, |  \ 
                                       
    {Colors.WHITE}[ + ]  IP TRACKER  [ + ]{Colors.RESET}
""")
    
    try:
        ip = input(f"\n{Colors.WHITE} Enter IP target : {Colors.GREEN}")
        
        if not validate_ip(ip):
            print(f"{Colors.RED} Invalid IP address format!{Colors.RESET}")
            time.sleep(2)
            return
        
        print(f'\n {Colors.WHITE}============= {Colors.GREEN}SHOW INFORMATION IP ADDRESS {Colors.WHITE}=============')
        
        try:
            req_api = requests.get(f"http://ipwho.is/{ip}", timeout=10)
            ip_data = json.loads(req_api.text)
            
            if not ip_data.get("success", True):
                print(f"{Colors.RED} Error: {ip_data.get('message', 'Unknown error')}{Colors.RESET}")
                return
                
            time.sleep(1)
            
            info_items = [
                ("IP target", ip),
                ("Type IP", ip_data.get("type", "N/A")),
                ("Country", ip_data.get("country", "N/A")),
                ("Country Code", ip_data.get("country_code", "N/A")),
                ("City", ip_data.get("city", "N/A")),
                ("Continent", ip_data.get("continent", "N/A")),
                ("Continent Code", ip_data.get("continent_code", "N/A")),
                ("Region", ip_data.get("region", "N/A")),
                ("Region Code", ip_data.get("region_code", "N/A")),
                ("Latitude", ip_data.get("latitude", "N/A")),
                ("Longitude", ip_data.get("longitude", "N/A")),
                ("EU", ip_data.get("is_eu", "N/A")),
                ("Postal", ip_data.get("postal", "N/A")),
                ("Calling Code", ip_data.get("calling_code", "N/A")),
                ("Capital", ip_data.get("capital", "N/A")),
                ("Borders", ip_data.get("borders", "N/A")),
                ("Country Flag", ip_data.get("flag", {}).get("emoji", "N/A")),
                ("ASN", ip_data.get("connection", {}).get("asn", "N/A")),
                ("ORG", ip_data.get("connection", {}).get("org", "N/A")),
                ("ISP", ip_data.get("connection", {}).get("isp", "N/A")),
                ("Domain", ip_data.get("connection", {}).get("domain", "N/A")),
                ("Timezone ID", ip_data.get("timezone", {}).get("id", "N/A")),
                ("Timezone ABBR", ip_data.get("timezone", {}).get("abbr", "N/A")),
                ("DST", ip_data.get("timezone", {}).get("is_dst", "N/A")),
                ("Offset", ip_data.get("timezone", {}).get("offset", "N/A")),
                ("UTC", ip_data.get("timezone", {}).get("utc", "N/A")),
                ("Current Time", ip_data.get("timezone", {}).get("current_time", "N/A"))
            ]
            
            for key, value in info_items:
                print(f"{Colors.WHITE} {key:<18} :{Colors.GREEN} {value}")
            
            # Generate maps link if coordinates are available
            lat = ip_data.get("latitude")
            lon = ip_data.get("longitude")
            if lat and lon:
                print(f"{Colors.WHITE} Maps{' ':<16} :{Colors.GREEN} https://www.google.com/maps/@{lat},{lon},8z")
            
        except requests.exceptions.RequestException as e:
            print(f"{Colors.RED} Network error: {e}{Colors.RESET}")
        except json.JSONDecodeError:
            print(f"{Colors.RED} Error parsing API response{Colors.RESET}")
            
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW} Operation cancelled by user{Colors.RESET}")

def track_phone():
    os.system('clear')
    time.sleep(1)
    stderr.writelines(f"""{Colors.YELLOW}
               ___  __        __       
   | | |\ | __  |  |__)  /\  /  ` |__/ 
\__/ | | \|     |  |  \ /~~\ \__, |  \ 
                                       
    {Colors.WHITE}[ + ]  PHONE TRACKER  [ + ]{Colors.RESET}
""")
    
    try:
        phone_number = input(f"\n{Colors.WHITE} Enter phone number target {Colors.GREEN}Ex [+8801xxxxxxxxx] {Colors.WHITE}: {Colors.GREEN}")
        
        if not validate_phone(phone_number):
            print(f"{Colors.RED} Invalid phone number format!{Colors.RESET}")
            time.sleep(2)
            return
        
        default_region = "ID"
        
        try:
            parsed_number = phonenumbers.parse(phone_number, default_region)
            
            if not phonenumbers.is_valid_number(parsed_number):
                print(f"{Colors.RED} Invalid phone number!{Colors.RESET}")
                return
                
            region_code = phonenumbers.region_code_for_number(parsed_number)
            provider = carrier.name_for_number(parsed_number, "en")
            location = geocoder.description_for_number(parsed_number, "id")
            is_valid = phonenumbers.is_valid_number(parsed_number)
            is_possible = phonenumbers.is_possible_number(parsed_number)
            formatted_intl = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            formatted_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region, with_formatting=True)
            number_type = phonenumbers.number_type(parsed_number)
            timezones = timezone.time_zones_for_number(parsed_number)
            timezone_str = ', '.join(timezones) if timezones else "N/A"
            
            print(f"\n {Colors.WHITE}========== {Colors.GREEN}SHOW INFORMATION PHONE NUMBERS {Colors.WHITE}==========")
            
            info_items = [
                ("Location", location),
                ("Region Code", region_code),
                ("Timezone", timezone_str),
                ("Operator", provider),
                ("Valid number", is_valid),
                ("Possible number", is_possible),
                ("International format", formatted_intl),
                ("Mobile format", formatted_mobile),
                ("Original number", parsed_number.national_number),
                ("E.164 format", phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)),
                ("Country code", parsed_number.country_code),
                ("Local number", parsed_number.national_number)
            ]
            
            for key, value in info_items:
                print(f" {Colors.WHITE}{key:<22} :{Colors.GREEN} {value}")
            
            # Number type description
            if number_type == phonenumbers.PhoneNumberType.MOBILE:
                print(f" {Colors.WHITE}Type{' ':<20} :{Colors.GREEN} This is a mobile number")
            elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
                print(f" {Colors.WHITE}Type{' ':<20} :{Colors.GREEN} This is a fixed-line number")
            else:
                print(f" {Colors.WHITE}Type{' ':<20} :{Colors.GREEN} This is another type of number")
                
        except Exception as e:
            print(f"{Colors.RED} Error processing phone number: {e}{Colors.RESET}")
            
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW} Operation cancelled by user{Colors.RESET}")

def show_my_ip():
    os.system('clear')
    time.sleep(1)
    stderr.writelines(f"""{Colors.YELLOW}
               ___  __        __       
   | | |\ | __  |  |__)  /\  /  ` |__/ 
\__/ | | \|     |  |  \ /~~\ \__, |  \ 
                                       
    {Colors.WHITE}[ + ]  SHOW MY IP  [ + ]{Colors.RESET}
""")
    
    try:
        print(f"\n {Colors.WHITE}========== {Colors.GREEN}SHOW INFORMATION YOUR IP {Colors.WHITE}==========")
        
        # Get public IP
        try:
            response = requests.get('https://api.ipify.org', timeout=5)
            public_ip = response.text
            print(f"\n {Colors.WHITE}[{Colors.GREEN} + {Colors.WHITE}] Your Public IP Address : {Colors.GREEN}{public_ip}")
        except:
            print(f"\n {Colors.WHITE}[{Colors.RED} ! {Colors.WHITE}] Could not retrieve public IP")
            public_ip = "N/A"
        
        # Get local IP
        try:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            print(f" {Colors.WHITE}[{Colors.GREEN} + {Colors.WHITE}] Your Local IP Address  : {Colors.GREEN}{local_ip}")
        except:
            print(f" {Colors.WHITE}[{Colors.RED} ! {Colors.WHITE}] Could not retrieve local IP")
        
        # Get additional IP information if public IP is available
        if public_ip != "N/A":
            try:
                ip_info = requests.get(f"http://ipwho.is/{public_ip}", timeout=5).json()
                if ip_info.get("success", False):
                    print(f" {Colors.WHITE}[{Colors.GREEN} + {Colors.WHITE}] Your Approx. Location  : {Colors.GREEN}{ip_info.get('city', 'N/A')}, {ip_info.get('country', 'N/A')}")
            except:
                pass
        
        print(f"\n {Colors.WHITE}==============================================")
        
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW} Operation cancelled by user{Colors.RESET}")

def track_username():
    os.system('clear')
    time.sleep(1)
    stderr.writelines(f"""{Colors.YELLOW}
               ___  __        __       
   | | |\ | __  |  |__)  /\  /  ` |__/ 
\__/ | | \|     |  |  \ /~~\ \__, |  \ 
                                       
    {Colors.WHITE}[ + ]  USERNAME TRACKER  [ + ]{Colors.RESET}
""")
    
    try:
        username = input(f"\n{Colors.WHITE} Enter Username : {Colors.GREEN}")
        
        if not username or len(username) < 3:
            print(f"{Colors.RED} Username too short!{Colors.RESET}")
            time.sleep(2)
            return
        
        print(f"\n {Colors.WHITE}========== {Colors.GREEN}SHOW INFORMATION USERNAME {Colors.WHITE}==========")
        print()
        
        social_media = [
            {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.twitter.com/{}", "name": "Twitter"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
            {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
            {"url": "https://www.youtube.com/{}", "name": "Youtube"},
            {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
            {"url": "https://www.behance.net/{}", "name": "Behance"},
            {"url": "https://www.medium.com/@{}", "name": "Medium"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
            {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
            {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
            {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
            {"url": "https://www.telegram.me/{}", "name": "Telegram"}
        ]
        
        found_count = 0
        for site in social_media:
            url = site['url'].format(username)
            try:
                response = requests.get(url, timeout=5, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
                if response.status_code == 200:
                    print(f" {Colors.WHITE}[ {Colors.GREEN}+ {Colors.WHITE}] {site['name']}: {Colors.GREEN}{url}")
                    found_count += 1
                else:
                    print(f" {Colors.WHITE}[ {Colors.RED}- {Colors.WHITE}] {site['name']}: {Colors.RED}Not found")
            except:
                print(f" {Colors.WHITE}[ {Colors.YELLOW}~ {Colors.WHITE}] {site['name']}: {Colors.YELLOW}Connection failed")
        
        print(f"\n {Colors.WHITE}Found {Colors.GREEN}{found_count} {Colors.WHITE}profiles for username {Colors.GREEN}{username}")
        
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW} Operation cancelled by user{Colors.RESET}")

# MAIN MENU
def main_menu():
    os.system('clear')
    stderr.writelines(f"""{Colors.YELLOW}
               ___  __        __       
   | | |\ | __  |  |__)  /\  /  ` |__/ 
\__/ | | \|     |  |  \ /~~\ \__, |  \ 
                                       
    {Colors.WHITE}[ + ]  CODE BY FARHAN-MUH-TASIM  [ + ]{Colors.RESET}
        
    {Colors.WHITE}[ 1 ] {Colors.GREEN}IP Tracker
    {Colors.WHITE}[ 2 ] {Colors.GREEN}Show Your IP
    {Colors.WHITE}[ 3 ] {Colors.GREEN}Phone Tracker
    {Colors.WHITE}[ 4 ] {Colors.GREEN}Username Tracker
    {Colors.WHITE}[ 0 ] {Colors.GREEN}Exit
    {Colors.WHITE}[ * ] {Colors.GREEN}About
""")

    try:
        choice = input(f'\n   {Colors.WHITE}@JIN~# {Colors.GREEN}')
        
        if choice == '1':
            track_ip()
        elif choice == '2':
            show_my_ip()
        elif choice == '3':
            track_phone()
        elif choice == '4':
            track_username()
        elif choice == '0':
            print(f"\n  {Colors.WHITE}[{Colors.YELLOW}!{Colors.WHITE}] {Colors.YELLOW}THANK'S FOR USING TOOL Create BY FARHAN-MUH-TASIM JIN-TRACK!{Colors.RESET}")
            sys.exit(0)
        elif choice == '*':
            show_about()
        else:
            print(f" {Colors.YELLOW}Invalid option! Please try again.{Colors.RESET}")
            time.sleep(2)
        
        input(f"\n{Colors.WHITE}Press Enter to return to main menu...{Colors.RESET}")
        main_menu()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW} Exiting... Thank you for using JIN-TRACKER!{Colors.RESET}")
        sys.exit(0)

def show_about():
    os.system('clear')
    print(f"""
{Colors.YELLOW}
               ___  __        __       
   | | |\ | __  |  |__)  /\  /  ` |__/ 
\__/ | | \|     |  |  \ /~~\ \__, |  \ 
                                       
{Colors.RESET}
{Colors.WHITE}JIN-TRACKER - Multi-purpose OSINT Tool
{Colors.GREEN}Created by: FARHAN-MUH-TASIM
{Colors.YELLOW}Version: 2.0 (Improved)

{Colors.WHITE}Features:
{Colors.GREEN}• IP Address Tracking
{Colors.GREEN}• Phone Number Information
{Colors.GREEN}• Username Search across platforms
{Colors.GREEN}• Show Your IP Information

{Colors.YELLOW}Note: This tool is for educational purposes only.
Always get proper authorization before scanning any target.

{Colors.WHITE}Inspired by Islamic teachings:
"O you who believe! Do not consume each other's wealth 
in a false way," (QS. An Nisaa': 29). 
Rasulullah SAW also prohibited his people from taking 
other people's rights without permission.
{Colors.RESET}
""")
    input(f"\n{Colors.WHITE}Press Enter to return to main menu...{Colors.RESET}")
    main_menu()

# ENTRY POINT
if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW} Exiting... Thank you for using JIN-TRACKER!{Colors.RESET}")
