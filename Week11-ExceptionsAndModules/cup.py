
class Cup:

    def __init__(self, max_volume_in_milliliters):
        self._current_volume_in_milliliters = 0
        self._max_volume_in_milliliters = max_volume_in_milliliters

    def get_current_volume_in_milliliters(self):
        return self._current_volume_in_milliliters

    def get_max_volume_in_milliliters(self):
        return self._max_volume_in_milliliters

    def add_liquid(self, milliliters_to_add):
        if self._current_volume_in_milliliters + milliliters_to_add > self._max_volume_in_milliliters:
            # as soon as an exception is raised, the rest of the function is skipped
            raise ValueError("This would overflow the cup!")
        if milliliters_to_add < 0:
            raise ValueError("You can't add a negative amount")
        self._current_volume_in_milliliters += milliliters_to_add

# this makes the code only run if this specific python file was selected to run
# won't run just on import
if __name__ == "__main__":
    print("cup module")