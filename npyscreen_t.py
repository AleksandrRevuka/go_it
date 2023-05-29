"""..."""
import curses
import npyscreen
from datetime import datetime


class EmployeeForm(npyscreen.ActionForm):

    def create(self):
        self.myName = self.add(npyscreen.TitleText, name='Name')
        self.myDepartment = self.add(npyscreen.TitleSelectOne,
                                     scroll_exit=True,
                                     max_height=3,
                                     name='Department',
                                     values=['Department 1',
                                             'Department 2',
                                             'Department 3'
                                             ])
        self.myDate = self.add(npyscreen.TitleDateCombo, name='Date Employed')

    def on_ok(self):
        npyscreen.notify_confirm("Form has been saved", "Saved!", editw=1)
        self.parentApp.setNextForm('MAIN')

    def on_cancel(self):
        exiting = npyscreen.notify_yes_no(
            "Are you sure you want to cancel", editw=2)
        if exiting:
            npyscreen.notify_confirm(
                "OK. From has NOT been saved. Good bye", "Good bye!", editw=1)
            self.parentApp.setNextFormPrevious()
        else:
            npyscreen.notify_confirm(
                "You may continue working", "Okay", editw=1)


class FormObject(npyscreen.ActionFormWithMenus, npyscreen.SplitForm):
    """..."""

    def create(self):
        self.draw_line_at = 16
        self.frame_name = self.add(npyscreen.TitleText, name='Name:')
        self.nextrely += 1
        self.frame_phone = self.add(npyscreen.TitleText, name='Phone number:')
        self.nextrelx = 10
        self.frame_birth_text = self.add(npyscreen.TitleText, name='Year Birth:')
        self.frame_birth = self.add(npyscreen.TitleDateCombo, name='Date Birth:', date_format='%d-%m-%Y',)
        self.frame_birth.when_cursor_moved = self.while_editing
        
        self.menu = self.new_menu(name="Main Menu", shortcut='m')
        self.menu.addItem("Item 1", self.press_1, "1")
        self.menu.addItem("Item 2", self.press_2, "2")
        self.menu.addItem("Exit Form", self.exit_form, "^X")

    def while_editing(self, *args, **kwargs):
        if self.frame_birth_text.value:
            birthday = datetime.strptime(str(int(self.frame_birth_text.value)), '%Y').date()
            self.frame_birth.value = birthday
        # if self.frame_birth.value:
        #     birthday = self.frame_birth.value.strftime('%Y')
        #     self.frame_birth_text.value = birthday

    def press_1(self):
        self.parentApp.switchForm('employee')

    def press_2(self):
        npyscreen.notify_confirm("You press Item_2!", "Item_2", editw=1)

    def exit_form(self):
        self.parentApp.switchForm(None)

    def on_ok(self):
        npyscreen.notify_confirm("Form has been saved", "Saved!", editw=1)
        self.parentApp.setNextForm(None)

    def on_cancel(self):
        exiting = npyscreen.notify_yes_no(
            "Are you sure you want to cancel", editw=2)
        if exiting:
            npyscreen.notify_confirm(
                "OK. From has NOT been saved. Good bye", "Good bye!", editw=1)
            self.parentApp.setNextForm(None)
        else:
            npyscreen.notify_confirm(
                "You may continue working", "Okay", editw=1)



class App(npyscreen.NPSAppManaged):
    """..."""

    def onStart(self):
        self.addForm('MAIN', FormObject, name='npyscreen Form!',
                     lines=20, columns=150, draw_line=10)
        self.addForm('employee', EmployeeForm, name='my_employee!',
                     lines=20, columns=75, draw_line=1)


if __name__ == "__main__":
    app = App().run()