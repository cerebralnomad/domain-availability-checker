#! /usr/bin/env python3

import argparse
import whois

def check_domain_availability(domain_name):
    try:
        w = whois.whois(domain_name)
        if w.status == None:
            return domain_name + " is available"
        else:
            expiry_date = w.expiration_date
            if expiry_date:
                return domain_name + " is not available. Expiry date: " + str(expiry_date)
            else:
                return domain_name + " is not available"
    except whois.parser.PywhoisError:
        return domain_name + " is available"
    except:
        return "Error: Invalid domain name or unable to connect to WHOIS server."

parser = argparse.ArgumentParser(description='Check domain availability')
parser.add_argument('-d', '--domain', type=str, help='Domain name')
args = parser.parse_args()

# Example usage
print(check_domain_availability(args.domain))

