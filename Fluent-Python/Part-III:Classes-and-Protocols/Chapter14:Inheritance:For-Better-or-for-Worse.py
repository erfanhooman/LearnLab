class Root:
    def __init__(self):
        print("init called")

    def call(self):
        print("calling root")


class Sub(Root):
    def call2(self):
        print("calling 2 sub")


"""
Inheritance in python is that every thing declare in the self.(..) will also inheritance from it 
    - you can override them or keep them to using them
    - if you want to keep them also add something to them use the super() function
        super keep the previous method and add the new one to it
"""


class SubSuper(Root):
    def call(self):
        super().call()
        print("call from subclass")


"""
when using multiple inheritance and there is a method with the same name in multiple superclasses, 
the method resolution order (MRO) determines which method will be used. 
The MRO is the order in which Python searches for methods and attributes in a class hierarchy.
Note: that the class will be called and show that trigger to showed by the super() function
The MRO can be viewed using the __mro__ attribute or the mro() method of a class. For example:
"""


class A:
    def method(self):
        print("Method from A")


class B:
    def method(self):
        print("Method from B")


class C(A, B):
    pass


print(C.__mro__)
# Output: (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

"""
In this example, the MRO for class C is C, A, B, and finally object. 
This means that when you call the method on an instance of C, Python will first search for the method in C, 
then in A, then in B, and finally in the base class object.
"""

"""
Generally we have three use of the inheritance:
1. Normal Inheritance: Inheritance is a fundamental concept where a class (child or subclass) inherits properties and 
methods from another class (parent or superclass). It represents an "is-a" relationship.

2. Interfaces: They specify what methods a class should implement, but not how these methods should be implemented.
Python doesn't have formal interfaces like some other languages (e.g., Java), but you can achieve similar behavior 
using abstract base classes from the abc module.

3. Mixin class: Mixins are a way to compose classes by including methods from other classes. They don't represent an 
"is-a" relationship but rather an "has-a" or "can-do" relationship. Mixins are used to add reusable functionality 
to classes.

"""


class MyMixin:
    def mixin_method(self):
        print("This is a mixin method")


# A class can use this mixin to gain the functionality provided by mixin_method:

class User:
    def __init__(self, username):
        self.username = username

    def get_username(self):
        return self.username


class AdminUser(User):
    def has_admin_rights(self):
        return True


# Mixins for additional capabilities
class EmailMixin:
    def send_email(self, subject, message):
        return f"Email sent to {self.username} with subject: {subject}"


class SMSMixin:
    def send_sms(self, message):
        return f"SMS sent to {self.username}: {message}"


# Combined class with mixins
class SupportUser(User, EmailMixin, SMSMixin):
    def __init__(self, username, support_level):
        super().__init__(username)
        self.support_level = support_level

    def get_support_level(self):
        return self.support_level


# Usage
support_user = SupportUser("erfan_support", "Level 2")
print(support_user.get_username())  # Output: erfan_support
print(support_user.get_support_level())  # Output: Level 2
print(
    support_user.send_email("Help", "How can I assist you?"))  # Output: Email sent to erfan_support with subject: Help
print(support_user.send_sms("Please respond ASAP"))  # Output: SMS sent to erfan_support: Please respond ASAP

"""
Here, SupportUser inherits from User and includes additional capabilities through EmailMixin and SMSMixin.
"""


"""
few tips on the inheritance:

1. use Favoring Composition for a better flexible design (like QT and Tkinter)
2. understand why inheritance is used in each case
3. make interface explicit with ABCs
4. use explicit mixins, each mixin dose not define a new type, each mixin should provide single specific behavior,
    concrete classes should not only inherit only from mixin
5. if some combination of ABCs or mixins is useful, provide a class that brings them together 
    (see the ListView example in django)
6. avoid overriding methods or at least retain yourself to subclassing classes
7. avoid subclassing from concrete class
8. 
"""
