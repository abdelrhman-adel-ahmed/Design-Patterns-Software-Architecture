class Validate:

    # here the function is tight coupled with the mail object implementation so if the email object
    # structre changes we will need to change the function here also the solution is directly send what
    # we need through indirection layer
    def validate_email(email):
        if email.headr[...] == ...:
            pass
        elif email.headr[...] == ...:
            pass


# -----------------------------


class Email:
    email: str
    var1: str
    var2: str

    def _validate_email(self) -> bool:
        """the logic go here"""
        self.var1
        self.var2

    def email_validator(self):
        """
        indirection layer we will use so if the implmentation of validate_email changes we will not
        need to change any thing in the other classes that use that class
        """
        self._validate_email()


class Validate2:
    def validate_email(email):
        email.email_validator()
