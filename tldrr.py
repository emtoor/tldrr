#!/usr/bin/env python3

import subprocess
import os
import shelve
import hashlib
from datetime import datetime, timedelta
from openai import OpenAI

CACHE_FILE = "/tmp/tldrr_cache"  # Cache location
CACHE_EXPIRY_DAYS = 30           # Cache expires after 30 days

def get_cache_key(command, data_type):
    """Generate a cache key based on command and data type (tldr/gpt)."""
    return hashlib.sha256(f"{command}_{data_type}".encode()).hexdigest()

def cache_result(key, value):
    """Cache result with a timestamp."""
    with shelve.open(CACHE_FILE) as cache:
        cache[key] = {
            "value": value,
            "timestamp": datetime.now()
        }

def get_cached_result(key):
    """Retrieve cached result if not expired."""
    with shelve.open(CACHE_FILE) as cache:
        try:
            if key in cache:
                cached_data = cache[key]
                if datetime.now() - cached_data['timestamp'] < timedelta(days=CACHE_EXPIRY_DAYS):
                    return cached_data['value']
        except Exception as e:
            print(f"Error accessing cache: {e}")
    return None

def query_tldr(command):
    """Query tldr and cache the result."""
    cache_key = get_cache_key(command, "tldr")
    cached_result = get_cached_result(cache_key)
    if cached_result:
        return cached_result
    
    try:
        result = subprocess.run(["tldr", command], capture_output=True, text=True, check=True, timeout=10)
        cache_result(cache_key, result.stdout)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return None  # Return None if tldr doesn't know the app
    except FileNotFoundError:
        return "tldr not found. Please install tldr."

def query_openai(prompt):
    """Query GPT for enhanced examples and cache the result."""
    try:
        client = OpenAI()  # Initialize OpenAI client
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful Linux terminal assistant. Format your responses like tldr pages."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500
        )
        gpt_response = response.choices[0].message.content.strip()
        return format_as_tldr(gpt_response)
    except Exception as e:
        return f"Error querying OpenAI API: {e}"

def format_as_tldr(response):
    """Format the GPT response to match the concise tldr style."""
    if not response:
        return "No response provided."
    lines = response.split(os.linesep)  # Use os.linesep for cross-platform compatibility
    formatted_lines = []
    
    for line in lines:
        line = line.strip()
        if line.startswith("- "):  # Main description bullet point
            formatted_lines.append(f"\n{line}")  # Add spacing before descriptions
        elif line and not line.startswith("-"):  # Command lines
            formatted_lines.append(f"  {line}")  # Indent commands properly
    
    return "\n".join(formatted_lines)

def add_to_path():
    """Add this script to the PATH for easier execution."""
    script_path = os.path.abspath(__file__)
    symlink_path = "/usr/local/bin/tldrr"

    try:
        if not os.path.exists(symlink_path):
            os.symlink(script_path, symlink_path)  # Create a symlink to the script
            print(f"Script linked to {symlink_path}. You can now use 'tldrr' globally.")
        else:
            print(f"Symlink already exists at {symlink_path}.")
    except PermissionError:
        print("Permission denied: Try running with sudo to add the script to PATH.")
    except Exception as e:
        print(f"Error adding script to PATH: {e}")

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: tldrr <command>\nExample: tldrr ls")
        sys.exit(1)

    if sys.argv[1] == '--install':
        add_to_path()
        sys.exit(0)

    command = sys.argv[1]
    tldr_output = query_tldr(command)
    print("\n--- TLDR Output ---\n")
    if tldr_output:
        print(tldr_output)
    else:
        print(f"No TLDR entry found for '{command}'. Fetching examples from OpenAI instead...")

    previous_examples = []  # Limit size to avoid excessive memory usage
    MAX_EXAMPLES = 10
    prompt = f"""
    The following is the TLDR result for the command '{command}':
    {tldr_output or "No TLDR entry available."}
    
    Provide more helpful and detailed examples of how to use this command with different options and scenarios. 
    Format the output concisely in the tldr style, avoiding long explanations.
    """
    
    print("\n--- Enhanced Examples from GPT ---\n")
    gpt_response = query_openai(prompt)
    print(gpt_response)
    previous_examples.append(gpt_response)

    # Ask the user if they want more examples
    while True:
        more_examples = input("\nWould you like more examples? (y/n): ").strip().lower()
        if more_examples == 'y':
            # Update the prompt with previous examples to avoid repetition
            additional_prompt = f"""
            Here are the examples provided so far:
            {''.join(previous_examples)}
            
            Provide new and unique examples not already listed above. Keep the response in the tldr style.
            """
            print("\n--- Additional Examples from GPT ---\n")
            new_response = query_openai(additional_prompt)
            print(new_response)
            previous_examples.append(new_response)  # Add to the list of examples
        elif more_examples == 'n':
            print("Exiting.")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
