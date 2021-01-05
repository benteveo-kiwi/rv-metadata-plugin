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
        quadrantData = self.obtainQuadrantData(imgAttributes)
        print(quadrantData)

    def obtainQuadrantData(self, imgAttributes):
        """

        Args:
            imgAttributes (list): List of tuples containing the keys and values of the JPEG image attributes.
                                 It expects the first key to be 'EXIF/Make' and the second to be 'EXIF/Artist',
                                 where ... is a string with pixel coordinates and 'EXIF/Artist' is a string of
                                 locations on disk.

        Returns: (list) The quadrant data from the image JPEG attributes as follows:
                [( coords, location_on_disk ),]

        """
        coord_string = None
        location_string = None

        for attrib in imgAttributes:
            name = attrib[0]
            value = attrib[1]

            if name == "EXIF/Make":
                coord_string = value
            if name == "EXIF/Artist":
                location_string = value

        if not coord_string or not location_string:
            print("Unable to obtain the coordinate values, image does not follow metadata format")
            return

        coords = coord_string.split(';')
        locations = location_string.split(';')

        quadrants = []

        for coord, location in zip(coords, locations):
            quadrant = coord, location
            quadrants.append(quadrant)

        return quadrants

    def runExample(self, event):
        print("DEBUG: Metadata Finder Ran.")


def createMode():
    return Package_MetadataFinder()

