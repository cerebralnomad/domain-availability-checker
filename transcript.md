# Transcript of ChatGPT conversation that generated this script

Me: write a python script that checks whether a domain name is available

ChatGPT: Here's a Python script that uses the `whois` library to check whether a domain name is available:
```
import whois

def check_domain_availability(domain_name):
    try:
        w = whois.whois(domain_name)
        if w.status == None:
            return True
        else:
            return False
    except:
        return "Error: Invalid domain name or unable to connect to WHOIS server."

# Example usage
print(check_domain_availability("example.com"))
```


