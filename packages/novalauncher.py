#!/usr/bin/env python3
"""
NovaForge Lite App Launcher
Simple application launcher with cyberpunk styling
"""

import os
import sys

# App categories and icons
APPS = {
    # Internet
    "Firefox": {"cmd": "firefox", "cat": "Internet", "icon": "firefox"},
    "Files": {"cmd": "dolphin", "cat": "Files", "icon": "folder"},
    
    # Settings
    "Settings": {"cmd": "systemsettings", "cat": "System", "icon": "settings"},
    "WiFi": {"cmd": "nm-connection-editor", "cat": "Network", "icon": "wifi"},
    "Bluetooth": {"cmd": "blueman-manager", "cat": "Network", "icon": "bluetooth"},
    
    # Media
    "VLC": {"cmd": "vlc", "cat": "Media", "icon": "media"},
    
    # Gaming
    "Steam": {"cmd": "steam", "cat": "Gaming", "icon": "steam"},
    
    # Tools
    "Terminal": {"cmd": "konsole", "cat": "Tools", "icon": "terminal"},
    "NOVA AI": {"cmd": "nova-ai-lite", "cat": "AI", "icon": "robot"},
    "Updates": {"cmd": "pamac-manager", "cat": "System", "icon": "update"},
}

def launch_app(app_name):
    """Launch an application"""
    if app_name in APPS:
        os.system(APPS[app_name]["cmd"] + " &")
        return True
    return False

def show_launcher():
    """Show launcher menu"""
    print("""
╔═══════════════════════════════════════════════╗
║     🚀 NovaForge Lite App Launcher          ║
╚═══════════════════════════════════════════════╝

Internet:
  • Firefox    - Web browser
  • Files      - File manager

Settings:
  • Settings   - System settings
  • WiFi       - Network manager
  • Bluetooth  - Bluetooth devices

Media:
  • VLC        - Media player

Gaming:
  • Steam      - Game launcher

Tools:
  • Terminal  - Command terminal
  • NOVA AI   - AI assistant
  • Updates  - Update manager

Type app name to launch, or 'quit' to exit

""")

def main():
    if len(sys.argv) < 2:
        show_launcher()
        
        # Interactive mode
        while True:
            try:
                choice = input("NovaForge > ").strip()
                if choice.lower() in ["quit", "exit", "q"]:
                    break
                if choice:
                    launch_app(choice)
            except (EOFError, KeyboardInterrupt):
                break
    else:
        # Command line mode
        launch_app(sys.argv[1])

if __name__ == "__main__":
    main()