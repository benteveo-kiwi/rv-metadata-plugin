from rv import commands, rvtypes
from rv.commands import NeutralMenuState


class Package_MetadataFinder(rvtypes.MinorMode):

    def __init__(self):
        rvtypes.MinorMode.__init__(self)

        globalBindings = [("pointer-1--push", self.pointerEvent, "Left mouse button click")]
        localBindings = None

        self.init("Package_MetadataFinder", globalBindings, localBindings)

    def pointerEvent(self, event):
        """
        Callback function that uses the pointer position to find the image coordinates.
        Args:
            event:

        """

        pointer = event.pointer()
        # The name of the image in the sequence for rv
        sourceName = commands.sourceAtPixel(pointer)[0]['name']

        # Tuple containing the coordinates of the point event with regards to the image,
        # where the lower left corner of the image is (0,0)
        imgPointerCoords = commands.eventToImageSpace(sourceName, pointer)
        print(imgPointerCoords)

        # An array of image attribute name/value pairs at the current frame
        imgAttributes = commands.sourceAttributes(sourceName)
        print(imgAttributes)

    def runExample(self, event):
        print("DEBUG: Metadata Finder Ran.")


def createMode():
    return Package_MetadataFinder()

