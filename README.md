![Screenshot_2025-06-09_10_17_39](https://github.com/user-attachments/assets/1f9a2803-f47d-431f-ad62-cc3cb3231f94)
===========================
🔥 Hashunter v2.0 🔥
Created by: devil659
===========================

📌 Description:
Hashunter is a command-line tool for Kali Linux that cracks hashed passwords using brute-force from wordlists.

✅ Works ONLY on Kali Linux
✅ Best used with: /usr/share/wordlists/rockyou.txt
✅ Supports: MD5, SHA1, SHA256, SHA512

---------------------------
📁 Required Files:
1. A file with hashes (one per line)
2. A wordlist file (rockyou.txt or custom)
3. Output file name to save cracked hashes

---------------------------
📤 Output Format:
Each cracked hash is saved as:
<hash>:<password>

Example:
5f4dcc3b5aa765d61d8327deb882cf99:password

---------------------------
🚀 How to Run:

Command:
hashunter <hash_file> <wordlist_file> <output_file>

Example:
hashunter hashes.txt rockyou.txt cracked.txt

---------------------------
⚠️ Important Notes:
- Only for Kali Linux users
- Use for ethical and educational purposes only
- Make sure there are no empty lines in input files

===========================
Tool by devil659 | Powered by Python
===========================

python3 Hashunter.py hash.txt /home/kali/Desktop/rockyou.txt cracked.txt (most important)
