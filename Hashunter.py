import hashlib
import sys
from tqdm import tqdm
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
from datetime import datetime

console = Console()

# ==== ASCII Banner ====
def show_banner():
    banner = Text("""
██╗  ██╗ █████╗ ███████╗██╗  ██╗██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
██║  ██║██╔══██╗██╔════╝██║  ██║██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
███████║███████║███████╗███████║███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
██╔══██║██╔══██║╚════██║██╔══██║██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
██║  ██║██║  ██║███████║██║  ██║██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
    """, style="bold blue")
    panel = Panel(
        banner,
        title="[bold red]HashHunter v2.0[/bold red]",
        subtitle="[italic]by devil659 | Powered by Python[/italic]",
        box=box.ROUNDED,
        padding=(1, 2),
        border_style="bright_magenta"
    )
    console.print(panel)

# ==== Detect Hash Type ====
def detect_hash_type(hash_value):
    hash_value = hash_value.strip().lower()
    hlen = len(hash_value)
    if hlen == 32:
        return "md5"
    elif hlen == 40:
        return "sha1"
    elif hlen == 64:
        return "sha256"
    elif hlen == 128:
        return "sha512"
    else:
        return "unknown"

# ==== Cracking Engine ====
def crack_hashes(hash_file, wordlist_path, output_file):
    try:
        with open(hash_file, 'r') as f:
            hashes = [line.strip().lower() for line in f if line.strip()]

        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            words = [line.strip() for line in f if line.strip()]

        cracked = {}
        total_hashes = len(hashes)

        console.print(f"[cyan]✓ Loaded {total_hashes} hashes and {len(words)} words...[/cyan]")

        for hash_value in hashes:
            hash_type = detect_hash_type(hash_value)
            if hash_type == "unknown":
                console.print(f"[red]✗ Unsupported hash type for: {hash_value}[/red]")
                continue

            console.print(f"[yellow]⌛ Cracking {hash_value[:10]}... ({hash_type.upper()})[/yellow]")
            for word in tqdm(words, desc=f"Testing {hash_type.upper()}"):
                try:
                    if hash_type == "md5":
                        hashed = hashlib.md5(word.encode()).hexdigest()
                    elif hash_type == "sha1":
                        hashed = hashlib.sha1(word.encode()).hexdigest()
                    elif hash_type == "sha256":
                        hashed = hashlib.sha256(word.encode()).hexdigest()
                    elif hash_type == "sha512":
                        hashed = hashlib.sha512(word.encode()).hexdigest()

                    if hashed == hash_value:
                        cracked[hash_value] = word
                        console.print(f"[green]✓ Cracked: {hash_value} → {word}[/green]")
                        break
                except UnicodeEncodeError:
                    continue  # Skip non-UTF-8 words

        with open(output_file, 'w') as f:
            for h, p in cracked.items():
                f.write(f"{h}:{p}\n")

        success_rate = (len(cracked) / total_hashes) * 100
        console.print(f"\n[bold green]✓ Done! Cracked {len(cracked)}/{total_hashes} hashes ({success_rate:.2f}%).[/bold green]")
        console.print(f"[blue]↳ Saved to: {output_file}[/blue]")

    except FileNotFoundError as e:
        console.print(f"[red]✗ File not found: {e.filename}[/red]")

# ==== Main ====
if __name__ == "__main__":
    show_banner()
    if len(sys.argv) != 4:
        console.print("[bold red]Usage:[/bold red] python3 hashhunter.py <hash_file> <wordlist> <output_file>")
        console.print("Example: python3 hashhunter.py hashes.txt rockyou.txt cracked.txt")
        sys.exit(1)
    else:
        hash_file = sys.argv[1]
        wordlist_path = sys.argv[2]
        output_file = sys.argv[3]
        crack_hashes(hash_file, wordlist_path, output_file)
