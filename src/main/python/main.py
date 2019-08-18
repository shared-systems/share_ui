from fbs_runtime.application_context.PyQt5 import ApplicationContext
from os import environ

from mainapp import MainApp

# Removed by sgomena on 1/29/19 after directory structure refactoring
# sys.path.append(path.join(path.dirname(__file__), '..'))


class AppContext(ApplicationContext):

    # def __init__(self):
    #     popup_style = self.get_resource("popup.qss")
    #     resources_add_view_style = self.get_resource("add_view.qss")
    #     resources_controller_style = self.get_resource("controller.qss")

    def run(self):
        # Save reference to main application so it's not garbage collected
        dont_garbage_collect_me = MainApp()
        return self.app.exec_()


if __name__ == '__main__':
    from sys import exit, argv

    # check we're in correct directory
    # if os.path.abspath(os.getcwd()).split(os.sep)[-1] != "PLUTO":
    #     exit("Must be in the root project directory to run main app!")

    # Enable headless for testing
    if environ.get('HEADLESS'):
        argv += ['-platform', 'minimal']

    appctxt = AppContext()
    exit_code = appctxt.run()
    exit(exit_code)
