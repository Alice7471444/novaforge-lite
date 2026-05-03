#!/usr/bin/env python3
"""
NovaForge NOVA AI Assistant
Built-in AI assistant for NovaForge OS
"""

import sys
import os
import json
import subprocess
import speech_recognition as sr
import pyttsx3
from datetime import datetime

# Configuration
CONFIG_FILE = os.path.expanduser("~/.config/novaai/config.json")
DEFAULT_MODEL = "llama2"
OLLAMA_URL = "http://localhost:11434"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")

class NOVAAI:
    """NOVA AI Assistant for NovaForge OS"""
    
    def __init__(self):
        self.config = self.load_config()
        self.recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()
        self.online_mode = False
        
    def load_config(self):
        """Load configuration"""
        default = {
            "offline_mode": True,
            "ollama_url": OLLAMA_URL,
            "openai_api_key": OPENAI_API_KEY,
            "voice_enabled": True,
            "tts_engine": "espeak",
            "stt_engine": "whisper",
            "auto_start": True,
            "listen_hotkey": "nova",
        }
        
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r') as f:
                    return {**default, **json.load(f)}
            except:
                return default
        return default
    
    def speak(self, text):
        """Text to speech"""
        if self.config.get("voice_enabled", True):
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
    
    def listen(self):
        """Speech recognition"""
        with sr.Microphone() as source:
            print("[NOVA] Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            
            try:
                query = self.recognizer.recognize_whisper(audio)
                print(f"[NOVA] Recognized: {query}")
                return query
            except sr.UnknownValueError:
                print("[NOVA] Could not understand")
                return None
            except Exception as e:
                print(f"[NOVA] Error: {e}")
                return None
    
    def query_ollama(self, prompt):
        """Query local Ollama"""
        try:
            import requests
            response = requests.post(
                f"{self.config['ollama_url']}/api/generate",
                json={
                    "model": self.config.get("model", DEFAULT_MODEL),
                    "prompt": prompt,
                    "stream": False
                }
            )
            return response.json().get("response", "")
        except Exception as e:
            print(f"[NOVA] Ollama error: {e}")
            return None
    
    def query_openai(self, prompt):
        """Query OpenAI API"""
        if not self.config.get("openai_api_key"):
            return None
            
        try:
            import openai
            openai.api_key = self.config["openai_api_key"]
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"[NOVA] OpenAI error: {e}")
            return None
    
    def generate_response(self, prompt):
        """Generate AI response"""
        # Try offline first if enabled
        if self.config.get("offline_mode", True):
            response = self.query_ollama(prompt)
            if response:
                return response
        
        # Try online mode
        if self.config.get("openai_api_key"):
            response = self.query_openai(prompt)
            if response:
                return response
        
        return "I'm currently in offline mode. Please configure Ollama or OpenAI API for AI responses."
    
    def handle_command(self, command):
        """Handle voice commands"""
        command = command.lower()
        
        # Gaming commands
        if "fps" in command or "optimize" in command:
            return self.optimize_gaming()
        elif "launch game" in command or "play game" in command:
            return self.launch_game()
        
        # System commands
        elif "screenshot" in command:
            return self.take_screenshot()
        elif "volume" in command:
            return self.adjust_volume(command)
        elif "wifi" in command:
            return self.toggle_wifi(command)
        elif "bluetooth" in command:
            return self.toggle_bluetooth(command)
        
        # Search commands
        elif "search" in command or "find" in command:
            return self.search_internet(command)
        elif "file" in command and "find" in command:
            return self.find_file(command)
        
        # AI Chat
        else:
            return self.generate_response(command)
    
    def optimize_gaming(self):
        """Optimize system for gaming"""
        try:
            # Apply gamemode
            subprocess.run(["gamemoded"], check=False)
            return "Gaming mode activated. System optimized for maximum performance."
        except:
            return "Could not enable gaming mode."
    
    def launch_game(self):
        """Launch game"""
        # Check for Steam, Heroic, etc
        steam_paths = [
            "~/.local/share/Steam/steam.sh",
            "/usr/bin/steam",
            "~/.local/bin/heroic",
        ]
        
        for path in steam_paths:
            if os.path.exists(os.path.expanduser(path)):
                subprocess.Popen([path, "steam://open大型"])
                return "Launching game launcher..."
        
        return "No game launchers found."
    
    def take_screenshot(self):
        """Take screenshot"""
        import tempfile
        from PIL import ImageGrab
        
        path = os.path.join(tempfile.gettempdir(), f"nova_screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        ImageGrab.grab().save(path)
        return f"Screenshot saved to {path}"
    
    def adjust_volume(self, command):
        """Adjust volume"""
        try:
            if "up" in command:
                subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", "+5%"])
                return "Volume increased."
            elif "down" in command:
                subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", "-5%"])
                return "Volume decreased."
            elif "mute" in command:
                subprocess.run(["pactl", "set-sink-mute", "@DEFAULT_SINK@", "toggle"])
                return "Volume muted."
        except:
            return "Could not adjust volume."
    
    def toggle_wifi(self, command):
        """Toggle WiFi"""
        try:
            if "on" in command:
                subprocess.run(["nmcli", "radio", "wifi", "on"])
            else:
                subprocess.run(["nmcli", "radio", "wifi", "off"])
        except:
            return "Could not toggle WiFi."
    
    def toggle_bluetooth(self, command):
        """Toggle Bluetooth"""
        try:
            if "on" in command:
                subprocess.run(["rfkill", "unblock", "bluetooth"])
            else:
                subprocess.run(["rfkill", "block", "bluetooth"])
        except:
            return "Could not toggle Bluetooth."
    
    def search_internet(self, command):
        """Search internet"""
        query = command.replace("search", "").replace("find", "").strip()
        if query:
            import webbrowser
            webbrowser.open(f"https://duckduckgo.com/?q={query}")
            return f"Searching for {query}..."
        return "What would you like to search for?"
    
    def find_file(self, command):
        """Find file"""
        filename = command.replace("find file", "").strip()
        if filename:
            import subprocess
            try:
                result = subprocess.run(
                    ["find", os.path.expanduser("~"), "-name", filename],
                    capture_output=True, text=True
                )
                return result.stdout if result.stdout else "File not found."
            except:
                return "Could not search for file."
        return "What file are you looking for?"
    
    def run(self):
        """Run NOVA AI"""
        print("[NOVA AI] Starting...")
        self.speak("NOVA AI is ready.")
        
        while True:
            try:
                command = self.listen()
                if command:
                    response = self.handle_command(command)
                    print(f"[NOVA] {response}")
                    self.speak(response)
            except KeyboardInterrupt:
                print("[NOVA] Shutting down...")
                break
            except Exception as e:
                print(f"[NOVA] Error: {e}")


if __name__ == "__main__":
    nova = NOVAAI()
    nova.run()