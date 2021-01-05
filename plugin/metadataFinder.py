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
            quadrant = format_coordinates(coord), location
            quadrants.append(quadrant)

        return quadrants

    def runExample(self, event):
        print("DEBUG: Metadata Finder Ran.")


def createMode():
    return Package_MetadataFinder()


def format_coordinates(coord_string):
    """

    Args:
        coord_string: The pixel coordinates as a string. Eg.: '0,0,1024,1024'

    Returns: a tuple where the first element are two floats that represent the x axis and the second
             element are two floats that represent the y axis. Eg.: ([0.0, 0.0], [1024.0, 1024.0])

    """

    all_coord_list = coord_string.split(",")
    all_coord_list = [float(i) for i in all_coord_list]
    formatted_coord = all_coord_list[:2], all_coord_list[2:]

    return formatted_coord


def find_highest_pixel(coord_list):
    """
    Given a list containing pixel coordinate values, returns the highest 'y' value

    Args:
        coord_list: list of tuples containing the lower and top corner of a quadrant
                    Eg.: [([0.0, 0.0], [1024.0, 1024.0]), ([1024.0, 0.0], [2048.0, 1024.0]), ]

    Returns: float

    """
    y_list = []

    for lower_corner, top_corner in coord_list:
        x, y = top_corner
        y_list.append(y)

    return max(y_list)


def get_pointer_pixel_value(imgPointerCoords, pixel_height):
    """
    Converts the pointer values from RV into pixel values.
    The pointer data from RV (imgPointerCoords) is a tuple were the lower left corner of the image is (0,0),
    the height of the image is 1 and the width varies depending on the image aspect.
    Knowing the highest pixel value allows us to define the '1' ratio.

    Args:
        imgPointerCoords: (tuple) RV pointer location
        pixel_height: (float) The highest 'y' pixel value

    Returns: tuple

    """
    pointer_x, pointer_y = imgPointerCoords
    pixel_x = pixel_height * pointer_x

    # Because the RV defines the pointer values from the lower left instead of the upper left corner, we need
    # to invert the 'y' values.
    revert_y_pointer = abs(pointer_y - 1)
    pixel_y = pixel_height * revert_y_pointer

    return pixel_x, pixel_y
