# Owner: Maitreya Sapariya
# Project: Crest Training

"""Main entry point for the Interview Prep Agent"""

from src.ui import create_app


def main():
    """Launch the interview prep agent"""
    print("🚀 Starting Interview Prep Agent with YouTube Search!")
    print("📝 Features:")
    print("   - Company research & custom prep guides")
    print("   - YouTube video recommendations")
    print("   - Up to 3 refinement iterations")
    print("\n💡 Tip: Ask for 'YouTube videos' during refinement")
    print("─" * 50)
    
    app = create_app()
    app.launch()


if __name__ == "__main__":
    main()

