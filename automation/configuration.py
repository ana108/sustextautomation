class Configuration:
    # Class attribute (shared by all instances of the class)

    # The __init__ method is a constructor, called when a new object is created
    def __init__(self, variablesFile="variables.env"):
        # Source - https://stackoverflow.com/a
        # Posted by SilentGhost, modified by community. See post 'Timeline' for change history
        # Retrieved 2025-12-05, License - CC BY-SA 4.0
        self.environment_vars = {}
        with open(variablesFile) as file:
            lines = [line.rstrip() for line in file]
            for env_var in lines:
                value_pair = env_var.split('=', 1)
                self.environment_vars[value_pair[0]] = value_pair[1]

            print(self.environment_vars)

    def get_staging_host(self):
        return self.environment_vars["STAGING_HOST"]

    # # Another instance method
    # def get_age_in_dog_years(self):
    #     return self.age * 7