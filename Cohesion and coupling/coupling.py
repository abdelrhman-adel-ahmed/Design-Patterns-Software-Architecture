class Validate:
    
#here the function is tight coupled with the mail object implementation so if the email object 
#structre changes we will need to change the function here also, the solution is directly send what 
#we need through indirection layer (helper method)
    def validate_email(email):
        if email.headr[...] == ...:
            pass
        elif email.headr[...] == ...:
            pass


#-----------------------------

class email:
    def _validate_email(self):
        """the logic goes here"""

    def email_validator(self):
        """
        another indirection layer we will use inside the class it self so if the implmentation of validate_email changes we will not 
        need to change any thing in the other classes that uses it ,another good way is to not expose the implementation of the course this is python 
        but who cares :) !
        """
        self._validate_email()


class Validate2():
    def validate_email(email):
      email.email_validator()
