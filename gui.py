from appJar import gui

class interface:
	
    app_ = None
    state_ = -1

    def __init__(self, ):
        self.display_login()

    def display_login(self):
        self.state_ = 0
        self.app_ = gui("Login", "400x200")
        self.app_.setBg("purple")
        self.app_.setFont(18)

        # handle button events
        def press(button):
            if button == "Cancel":
                self.invalid_login()
            else:
                usr = self.app_.getEntry("Username")
                pwd = self.app_.getEntry("Password")
                print("User:", usr, "Pass:", pwd)

        # add & configure widgets - widgets get a name, to help referencing them later
        self.app_.addLabel("title", "Welcome to Doorcode")
        self.app_.setLabelBg("title", "blue")
        self.app_.setLabelFg("title", "orange")

        self.app_.addLabelEntry("Username")
        self.app_.addLabelSecretEntry("Password")

        # link the buttons to the function called press
        self.app_.addButtons(["Submit", "Cancel"], press)

        self.app_.setFocus("Username")

        # start the GUI
        self.app_.go()

    def display_app(self):
        raise NotImplementedError

    def invalid_login(self):
        self.app_.setLabelBg("title", "red")

    def display_event_config(self):
        raise NotImplementedError

    def display_verification(self):
        self.app_ = gui("Doorcode", "800x400")
