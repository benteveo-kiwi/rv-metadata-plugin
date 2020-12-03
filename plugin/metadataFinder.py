from rv import commands, rvtypes
from rv.commands import NeutralMenuState

class Package_MetadataFinder(rvtypes.MinorMode):

    def __init__(self):
        rvtypes.MinorMode.__init__(self)

        globalBindings = None #[("Event-Name", self.eventCallback, "DescriptionOfBinding")]
        localBindings = None

        menu = [
            ("Example", [
                    ("Run Example", self.runExample, None, lambda: NeutralMenuState),
            ])
        ]

        self.init("Package_MetadataFinder", globalBindings, localBindings, menu)

    def runExample(self, event):
        print("DEBUG: Metadata Finder Ran.")

def createMode():
    return Package_MetadataFinder()
