# Owner: Maitreya Sapariya
# Project: Crest Training

#!/usr/bin/env python3
"""
Quick launcher for Deep Research with Pushover Notifications

This script quickly launches the Gradio web interface with proper error handling
and setup validation.
"""

import os
import sys
from dotenv import load_dotenv

def check_requirements():
    """Check if all requirements are met"""
    errors = []
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        errors.append("❌ .env file not found in current directory")
    
    # Load environment variables
    load_dotenv(override=True)
    
    # Check Pushover credentials
    if not os.getenv('PUSHOVER_TOKEN'):
        errors.append("❌ PUSHOVER_TOKEN not found in .env file")
    
    if not os.getenv('PUSHOVER_USER'):
        errors.append("❌ PUSHOVER_USER not found in .env file")
    
    # Check OpenAI API key
    if not os.getenv('OPENAI_API_KEY'):
        errors.append("❌ OPENAI_API_KEY not found in .env file")
    
    return errors

def main():
    """Main launcher function"""
    print("🚀 Deep Research with Pushover - Quick Launcher")
    print("=" * 50)
    
    # Check requirements
    errors = check_requirements()
    
    if errors:
        print("❌ Setup issues found:")
        for error in errors:
            print(f"   {error}")
        print("\n📋 Setup instructions:")
        print("   1. Create a .env file in this directory")
        print("   2. Add your API keys:")
        print("      OPENAI_API_KEY=your_openai_key")
        print("      PUSHOVER_TOKEN=your_pushover_token")
        print("      PUSHOVER_USER=your_pushover_user")
        print("\n💡 See README_PUSHOVER.md for detailed setup instructions")
        sys.exit(1)
    
    print("✅ All requirements met!")
    print("🔑 Credentials found:")
    print(f"   - OpenAI API Key: ...{os.getenv('OPENAI_API_KEY', '')[-8:]}")
    print(f"   - Pushover Token: ...{os.getenv('PUSHOVER_TOKEN', '')[-6:]}")
    print(f"   - Pushover User: ...{os.getenv('PUSHOVER_USER', '')[-6:]}")
    
    print("\n🌐 Launching web interface...")
    
    try:
        # Import and launch the interface
        from deep_research_pushover import ui
        ui.launch(inbrowser=True, share=False)
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Make sure you're in the correct directory and all dependencies are installed")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error launching interface: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
