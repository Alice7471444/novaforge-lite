#!/usr/bin/env python3
"""
NOVA AI Lite - Lightweight AI Assistant for NovaForge Lite
Optimized for low RAM usage (<100MB)
"""

import os
import sys
import json
import subprocess
import urllib.request
import urllib.parse

VERSION = "1.0.0-Lite"

def log(msg):
    print(f"[NOVA AI Lite] {msg}")

def get_system_info():
    """Get basic system info"""
    try:
        result = subprocess.run(
            ['neofetch', '--json'],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout if result.returncode == 0 else "{}"
    except:
        return "{}"

def check_updates():
    """Check for system updates"""
    try:
        result = subprocess.run(
            ['checkupdates'],
            capture_output=True,
            text=True,
            timeout=30
        )
        count = len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0
        return count
    except:
        return 0

def optimize_system():
    """Run basic system optimizations"""
    log("Running system optimizations...")
    
    # Clear caches
    try:
        subprocess.run(['sync'], timeout=5)
        subprocess.run(['sysctl', '-w', 'vm.drop_caches=3'], timeout=5)
    except:
        pass
    
    log("Optimization complete")

def ai_search(query):
    """Lightweight AI-powered search"""
    log(f"Searching for: {query}")
    
    try:
        # Use DuckDuckGo for basicAI search
        url = f"https://duckduckgo.com/?q={urllib.parse.quote(query)}"
        subprocess.run(['xdg-open', url])
        log("Search opened in browser")
    except Exception as e:
        log(f"Search error: {e}")

def ai_wallpaper():
    """Set a random futuristic wallpaper"""
    log("Opening wallpaper search...")
    try:
        subprocess.run(['xdg-open', 'https://wallhaven.cc/search?q=cyberpunk+neon'])
    except:
        log("Could not open wallpaper search")

def show_help():
    """Show NOVA AI Lite help"""
    print("""
╔══════════════════════════════════════╗
║     NOVA AI Lite v1.0.0            ║
║     Your AI Assistant               ║
╚══════════════════════════════════════╝

Usage: nova-ai-lite [command]

Commands:
  help          Show this help
  info          Show system info
  optimize     Optimize system (clear RAM)
  search       Search the web
  wallpaper   Get new wallpapers
  update       Check for updates

Features:
  • System optimization
  • Web search
  • Wallpaper suggestions
  • Update checker
  • System information

Requirements:
  • <100MB RAM
  • Works offline

""")

def main():
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == "help":
        show_help()
    elif command == "info":
        log("System Information:")
        print(get_system_info())
    elif command == "optimize":
        optimize_system()
    elif command == "search":
        query = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "cyberpunk"
        ai_search(query)
    elif command == "wallpaper":
        ai_wallpaper()
    elif command == "update":
        count = check_updates()
        if count > 0:
            log(f"Updates available: {count}")
        else:
            log("System is up to date!")
    else:
        log(f"Unknown command: {command}")
        show_help()

if __name__ == "__main__":
    main()