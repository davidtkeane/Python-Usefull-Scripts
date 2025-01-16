#!/usr/bin/env python3
# Created by Ranger

# Generate PowerShell aliases for installed programs

def generate_aliases(programs):
    aliases = {}
    for program in programs:
        alias_name = program.replace(" ", "-").lower()
        aliases[alias_name] = f"Open-{program}"
    return aliases

# List of installed programs
installed_programs = ["ChatGPT", "Tor Browser", "Brave Browser", "Google Chrome", "Web Browser", "Example App"]

# Generate aliases
aliases = generate_aliases(installed_programs)

# Print generated aliases
for alias, command in aliases.items():
    print(f'function {alias} {{\n    Start-Process "C:\\{command}.exe"\n}}\n')

# Rest of your script goes here...
