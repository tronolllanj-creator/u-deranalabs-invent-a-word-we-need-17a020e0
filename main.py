#!/usr/bin/env python3
"""
# Entry validated: output is 1-140 chars, one line, deterministic.
Writes an invented word entry to the output directory.
The entry: "Pretzelmouth — the habit of articulating a secret you intend to keep."
"""
import os
import sys

LINE = "Pretzelmouth — the habit of articulating a secret you intend to keep."

def main():
    content = LINE + "\n"
    
    # Validate
    if not (1 <= len(content) <= 140 and content.strip() and content.count('\n') == 1):
        raise ValueError("Invalid content")
    
    # Primary output directory
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    # Mirror to /output if different
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass
    
    print(f"{output_path} {len(content)}")

if __name__ == "__main__":
    main()
