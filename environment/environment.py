import venv
import os
import platform
import subprocess

class EnvironmentManager:
    def __init__(self, env_dir="fintimepro"):
        self.env_dir = env_dir

    def create(self):
        """Create a virtual environment for the project with error handling."""
        if not os.path.exists(self.env_dir):
            print(f"📦 Creating virtual environment at: {self.env_dir}")
            try:
                venv.EnvBuilder(with_pip=True).create(self.env_dir)
                print("✅ Virtual environment 'fintimepro' created successfully!")
            except Exception as e:
                print(f"❌ Failed to create environment: {e}")
                return
        else:
            print(f"⚠️ Environment already exists at: {self.env_dir}")

        self.activate_and_run()

    def activate_and_run(self):
        """Activate the environment and start a shell inside it."""
        system = platform.system()

        if system == "Windows":
            activate_script = os.path.join(self.env_dir, "Scripts", "activate.bat")
            if os.path.exists(activate_script):
                print("🚀 Activating environment (Windows)...")
                subprocess.call(["cmd.exe", "/k", activate_script])
            else:
                print("❌ Could not find activation script for Windows.")
        else:  # Linux / Mac
            activate_script = os.path.join(self.env_dir, "bin", "activate")
            if os.path.exists(activate_script):
                print("🚀 Activating environment (Linux/Mac)...")
                subprocess.call(["bash", "--rcfile", activate_script])
            else:
                print("❌ Could not find activation script for Linux/Mac.")

if __name__ == "__main__":
    manager = EnvironmentManager()
    manager.create()
