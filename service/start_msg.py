from pyfiglet import Figlet
from colorama import Fore, Style

def message(m):
    print(m)

viewer = Figlet(font='moscow', width=250)
messages = [
    Style.NORMAL + Fore.CYAN,
    viewer.renderText('Welcome to Attack LLM'),
    Style.NORMAL + Fore.WHITE + "Vulnerable Chatbot Service - http://localhost:5000",
    Style.NORMAL + Fore.WHITE + "Vulnerable Text Summarization Service - http://localhost:9089\n",
    Style.NORMAL + Fore.RED + 'Created by' + Style.NORMAL + Fore.GREEN + ' Sang-Hoon Choi\n',
    Style.NORMAL + Fore.YELLOW + 'Contact: csh0052@gmail.com \t\n'
]

for msg in messages:
    message(msg)
