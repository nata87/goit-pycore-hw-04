import sys
from colorama import init, Fore, Style
from pathlib import Path

init(autoreset=True)

def visualize_directory(directory_path: Path, indent: str = '', level: int = 0):
    if not directory_path.is_dir():
        print(f"{Fore.RED} Помилка: {directory_path} не є директорією або не існує.")
        return
    
    items = sorted(directory_path.iterdir())  

    for index, item in enumerate(items):
        prefix = "├── " if index < len(items) - 1 else "└── " 
        indent_str = indent + ("" if level == 0 else "│   ")

        if item.is_dir():
            print(f"{indent_str}{prefix}{Fore.BLUE}📂 {Style.BRIGHT}{item.name}") 
            visualize_directory(item, indent + "│   ", level + 1)  
        else:
          
            if item.suffix in ['.txt', '.md', '.log']:
                color = Fore.YELLOW  
                icon = "📜"
            elif item.suffix in ['.py', '.sh', '.exe']:
                color = Fore.RED  
                icon = "⚙️"
            else:
                color = Fore.GREEN 
                icon = "📄"

            print(f"{indent_str}{prefix}{color}{icon} {item.name}") 

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED} Помилка: необхідно вказати шлях до директорії.")
        sys.exit(1)

    visualize_directory(Path(sys.argv[1]))
