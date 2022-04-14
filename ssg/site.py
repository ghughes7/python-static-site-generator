from pathlib import Path

class Site:
    """Site Class Constructor

    """
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source) 
        #?: do I need to reassign to directory?
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        #?: do I need to store in a variable?
        self.dest.mkdir(parents=True, exist_ok=True)
        
        for path in self.source.rglob("*"):
            # call the current iteration of path
            if (path.is_dir()):
                self.create_dir(path)



