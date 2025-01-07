tldrr – Enhanced TLDR with GPT-Powered Examples

tldrr is a command-line tool that extends the functionality of the popular tldr command by providing enhanced, GPT-generated examples for command-line tools. It queries tldr to get concise command examples and supplements them with additional, more detailed scenarios powered by OpenAI’s GPT models.

🚀 Features
    •    Concise tldr-Style Output – GPT responses are formatted to match the tldr style for easy readability.
    •    Interactive Mode – Users can request additional examples (y/n prompt) until satisfied.
    •    Caching – Results are cached for 30 days to reduce redundant API calls and improve performance.
    •    Seamless Integration – Works like the tldr command but with added AI-driven insights.
    •    Configurable – Users can clear the cache or disable GPT-enhanced examples for offline use.

🛠️ Installation

1. Clone the Repository

git clone https://github.com/emtoor/tldrr.git
cd tldrr

2. Install the Tool w/ Python using pip.

#Linux -

sudo apt install -y python3 python3-pip || sudo dnf install -y python3 python3-pip || sudo pacman -S python python-pip
pip install tldrr

#OSX -

brew install python3 || curl https://bootstrap.pypa.io/get-pip.py | python3
pip install tldrr

#Windows -
winget install --id Python.Python.3 --source winget
pip install tldrr

3. Ensure tldr is Installed as well!

sudo apt install tldr  # Ubuntu/Debian
brew install tldr      # macOS
scoop install tldr     # Windows

🔑 API Key Setup

tldrr uses the OpenAI API to generate enhanced examples.
    1.    Get your API key from https://platform.openai.com/.
    2.    Export the API key as an environment variable:

export OPENAI_API_KEY="your_api_key_here"

    3.    Add the export line to your .bashrc or .zshrc to make it persistent:

Linux/OSX:
echo 'export OPENAI_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc

Windows:
echo %OPENAI_API_KEY%

📦 Usage

Basic Command

tldrr <command>

Example:

<!--$tldrr tcpdump-->
<!---->
<!--    •    This queries tldr for tcpdump and enhances the output with additional GPT-generated examples.-->
<!---->
<!----- TLDR Output ----->
<!---->
<!--  tcpdump-->
<!---->
<!--  Dump traffic on a network.-->
<!--  More information: https://www.tcpdump.org.-->
<!---->
<!--  - List available network interfaces:-->
<!--    tcpdump -D-->
<!---->
<!--  - Capture the traffic of a specific interface:-->
<!--    tcpdump -i eth0-->
<!---->
<!--  - Capture all TCP traffic showing contents (ASCII) in console:-->
<!--    tcpdump -A tcp-->
<!---->
<!--  - Capture the traffic from or to a host:-->
<!--    tcpdump host www.example.com-->
<!---->
<!--  - Capture the traffic from a specific interface, source, destination and destination port:-->
<!--    tcpdump -i eth0 src 192.168.1.1 and dst 192.168.1.2 and dst port 80-->
<!---->
<!--  - Capture the traffic of a network:-->
<!--    tcpdump net 192.168.1.0/24-->
<!---->
<!--  - Capture all traffic except traffic over port 22 and save to a dump file:-->
<!--    tcpdump -w dumpfile.pcap port not 22-->
<!---->
<!--  - Read from a given dump file:-->
<!--    tcpdump -r dumpfile.pcap-->
<!---->
<!---->
<!---->
<!----- Enhanced Examples from GPT ----->
<!---->
<!--  tcpdump-->
<!--  Analyze network packets. Commonly used for troubleshooting network issues.-->
<!--  More information: https://www.tcpdump.org.-->
<!---->
<!--- Display and save packet data to a file:-->
<!--  tcpdump -w myfile.pcap-->
<!---->
<!--- Display packets from a file in a user-readable format:-->
<!--  tcpdump -r myfile.pcap-->
<!---->
<!--- Display only ICMP (ping) packets:-->
<!--  tcpdump icmp-->
<!---->
<!--- Display packets for a specific port (example: 80):-->
<!--  tcpdump port 80-->
<!---->
<!--- Display packets for a specific protocol using port numbers, like HTTPS (443):-->
<!--  tcpdump port 443-->
<!---->
<!--- Display packets from a specific IP address:-->
<!--  tcpdump src 192.168.1.100-->

<!--Prompt for More Examples-->
<!---->
<!--Would you like more examples? (y/n):-->
<!---->
<!--    •    Press y to fetch more examples.-->
<!--    •    Press n to exit the loop.-->

Misc Commands:

Clear Cache

tldrr --clear-cache

    •    This clears cached tldr and GPT results.

🧑‍💻 Example Output

tldrr ls

--- TLDR Output ---

- List files in the current directory:
    ls

- List all files, including hidden ones:
    ls -a

--- Enhanced Examples from GPT ---

- List files sorted by size:
    ls -lS

- List files by modification time:
    ls -lt

Would you like more examples? (y/n): y

--- Additional Examples from GPT ---

- List directories only:
    ls -d */

- List files recursively in subdirectories:
    ls -R

⚙️ Configuration Options
    •    Cache Expiry – Cached results expire after 30 days by default.
    •    Offline Mode – If GPT is unavailable, the script falls back to tldr results.
    •    Interactive Prompt – Users can continuously query GPT for more examples or stop when satisfied.

🐛 Troubleshooting
    •    Command Not Found: Ensure tldr is installed and in your system’s PATH.
    •    Invalid API Key: Double-check your OpenAI API key and re-export it.
    •    Repeating GPT Results: The script dynamically prompts GPT for new examples to avoid redundancy.

🌟 Why Use tldrr?
    •    Advanced Learning – Get more comprehensive command-line examples beyond standard tldr outputs.
    •    Saves Time – Quickly grasp complex command-line options with curated, GPT-driven insights.
    •    Interactive and Scalable – Request as much or as little detail as you need.

📜 License

This project is licensed under the MIT License.

🤝 Contributing

Contributions are welcome! Please submit issues or pull requests to enhance the tool further.

🗂️ Future Improvements
    •    Batch Mode – Support querying multiple commands at once.
    •    Command History – Track previously queried commands.
    •    Offline GPT Cache – Save GPT results for offline access.    
    •    API Access to other commercial AI or local AI (Ollama) instead of relying on just OpenAI.
    
📧 Contact

For questions or collaboration, feel free to reach out at emtoor@gmail.com or open an issue on GitHub.

