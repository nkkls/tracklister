from ui.app import spot2grind
from ui.css.generator import generate_css
if __name__ == "__main__":
    generate_css("default")

    app = spot2grind()
    app.run()