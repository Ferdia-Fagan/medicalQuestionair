
class WindowBase:

    @staticmethod
    def set_application_controller(app_controller):
        WindowBase.APP_CONTROLLER=app_controller


    def change_state(self,new_state_container,**state_args):
        # self.pack_forget()
        # self.destroy()

        WindowBase.APP_CONTROLLER.change_state(new_state_container,**state_args)