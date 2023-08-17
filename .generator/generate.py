import re
import json
import yaml
from pathlib import Path

camel_pattern = re.compile(r"(?<!^)(?=[A-Z])")

ROOT = Path(__file__).parent.parent.absolute()
SETTINGS = ROOT / ".generator/settings"
API_DIRECTORY = ROOT / ".download/dist/api"

MODULE_CONFIG = yaml.safe_load((SETTINGS / "default.yaml").read_text(encoding="utf-8"))


def name_to_vue(value):
    return camel_pattern.sub("-", value).lower()


def attr_to_py(value):
    py_name = value.replace("-", "_")
    if "." in value or ":" in value:
        py_name = py_name.replace(".", "_").replace(":", "_")
        return [py_name, value]
    return py_name


def generate_config():
    all_directives = []
    widgets = {"directives": all_directives}
    for file_entry in API_DIRECTORY.iterdir():
        entry_config = json.loads(file_entry.read_text())
        class_name = file_entry.stem
        entry_type = entry_config.get("type")
        if entry_type == "directive":
            all_directives.append(f"v-{name_to_vue(class_name)}")
        elif entry_type == "component":
            properties = []
            events = []
            widgets[class_name] = {
                "component": name_to_vue(class_name),
                "properties": properties,
                "events": events,
            }
            for name, prop_info in entry_config.get("props", {}).items():
                help = prop_info.get("desc")
                properties.append(dict(name=attr_to_py(name), help=help))
            for name, event_info in entry_config.get("events", {}).items():
                help = event_info.get("desc")
                events.append(dict(name=attr_to_py(name), help=help))

    output_file = ROOT / ".generator" / "config.yaml"
    output_file.write_text(
        yaml.dump(
            {
                "trame_quasar": {
                    "module": {"quasar": {"vue3": MODULE_CONFIG}},
                    "widgets": {
                        "quasar": widgets,
                    },
                }
            }
        )
    )


if __name__ == "__main__":
    generate_config()
