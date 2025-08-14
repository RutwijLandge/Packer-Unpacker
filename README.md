# Packer-Unpacker
Python File Packer &amp; Unpacker – A command-line utility that packs multiple files from a directory into a single binary file with fixed-size headers, and unpacks them back to their original form. Ideal for bundling, backups, and transferring multiple files as one.
# 🗂️ Python File Packer & Unpacker

A simple **command-line utility** written in Python to pack multiple files from a directory into a single binary file with fixed-size headers, and unpack them back to their original form.

---

## 📌 Features
- **Pack Mode** – Combines multiple files into one `.pack` file with metadata headers.
- **Unpack Mode** – Restores all files from the packed file.
- **Fixed-size 100-byte headers** for storing filename and file size.
- Works with **binary data**, so it supports any file type.
- Cross-platform, no extra dependencies.

---

## 📂 How It Works
1. **Packing**
   - Reads each file from the given directory.
   - Stores a header in the format:
     ```
     <filename> <filesize> + padding (total 100 bytes)
     ```
   - Appends the file's binary data right after the header.
2. **Unpacking**
   - Reads the header (100 bytes), extracts the filename and size.
   - Reads the exact number of bytes for that file and writes it back to disk.

---

## 🚀 Installation
Clone this repository:
```bash
git clone https://github.com/yourusername/python-packer-unpacker.git
cd python-packer-unpacker
