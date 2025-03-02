import os



if "VIRTUAL_ENV" in os.environ:

    print("You are currently in a virtual environment")

else:

    print("You are not in a virtual environment")
