import os
import shutil
import click

from .manifest import read_manifest, NoManifestFound

ICONS_DIR = os.path.join('static', 'description')


@click.command()
@click.option("--addons-dir", default=".")
@click.option("--icon-file", default=None)
def main(addons_dir, icon_file):
    """ Put default ProcessControl icon.
    Do nothing if the icon already exists in ICONS_DIR, otherwise put the default icon.
    """
    icon_file = icon_file or os.path.join(os.path.dirname(__file__), 'icon.png')
    for addon_dir in os.listdir(addons_dir):
        try:
            read_manifest(addon_dir)
        except NoManifestFound:
            continue
        icon_dir = os.path.join(addon_dir, ICONS_DIR)
        if os.path.exists(os.path.join(icon_dir, 'icon.png')):
            continue
        if not os.path.exists(icon_dir):
            os.makedirs(icon_dir)
        shutil.copyfile(icon_file, os.path.join(icon_dir, 'icon.png'))


if __name__ == '__main__':
    main()
