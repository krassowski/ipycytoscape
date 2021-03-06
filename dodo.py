# this uses https://pydoit.org/ to run tasks/chores
# pip install doit
# $ doit
import pkg_resources
from ipycytoscape._version import __version__ as version
import re


def task_mybinder():
    """Make the mybinder files up to date"""

    def action(targets):
        for filename in targets:
            with open(filename) as f:
                content = f.read()
            content = re.sub(
                "cytoscape(?P<cmp>[^0-9]*)([0-9\.].*)",
                rf"cytoscape\g<cmp>{version}",
                content,
            )
            with open(filename, "w") as f:
                f.write(content)
            print(f"{filename} updated")

    return {
        "actions": [action],
        "targets": ["environment.yml", "postBuild"],
        "file_dep": ["ipycytoscape/_version.py"],
    }
