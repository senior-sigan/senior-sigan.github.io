from ssg.main_pipeline import compile_all
from ssg.models import Site, default_site
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Static site generator')
    parser.add_argument(
        '--config',
        default='config.toml',
        help='Path to the toml config')

    return parser.parse_args()


def site_from_config(config_path: str) -> Site:
    import toml
    config = toml.load(config_path)
    site = default_site()
    site.update(config)
    return site


def main():
    args = parse_args()
    site = site_from_config(args.config)
    compile_all(site)


if __name__ == '__main__':
    main()
