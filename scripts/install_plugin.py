from pathlib import Path
import configparser


def enable_plugin(plugin_name: str) -> None:
    config_file = Path(__file__).parent.parent / Path(
        ".pixi/qgis_env/profiles/default/QGIS/QGIS3.ini"
    )
    config_file.parent.mkdir(parents=True, exist_ok=True)
    config_file.touch()

    config = configparser.ConfigParser()
    config.read(config_file)

    plugins_section = "PythonPlugins"
    if not config.has_section(plugins_section):
        config.add_section(plugins_section)

    config[plugins_section][plugin_name] = "true"

    with config_file.open("w") as f:
        config.write(f)


target_path = Path(__file__).absolute().parent.parent
plugins_path = Path(".pixi/qgis_env/profiles/default/python/plugins")
source_path = plugins_path / "reloader"

plugins_path.mkdir(parents=True, exist_ok=True)
source_path.unlink(missing_ok=True)
source_path.symlink_to(target_path, target_is_directory=True)

enable_plugin("reloader")
