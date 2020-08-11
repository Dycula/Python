"""
    程序入口模块
"""

from View import GameConsoleView

if __name__ == "__main__":
    view = GameConsoleView()
    view.start()
    view.update()
