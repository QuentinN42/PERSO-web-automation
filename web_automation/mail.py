"""
Define the Mail class.
"""


class Mail:
    """
    Mail class.
    """
    
    subject: str
    content: str
    
    sender: str
    recipient: str
    
    def __init__(self, subject: str = None, content: str = None, sender: str = None, recipient: str = None):
        """
        Init the Mail object with given fields, empty => None.
        """
        self.subject = subject
        self.content = content
        self.sender = sender
        self.recipient = recipient
