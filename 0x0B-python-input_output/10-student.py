class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize student props."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            attrs = self.__dict__.keys()
        elif isinstance(attrs, list) and all(isinstance(ele, str) for ele in attrs):
            attrs = attrs
        else:
            raise ValueError("attrs must be None or a list of strings")

        return json.dumps({k: getattr(self, k) for k in attrs if hasattr(self, k)}, indent=4)
