import json
import yaml
from pathlib import Path
from trame.tools.widgets.utils import camel_to_dash, attr_to_py


ROOT = Path(__file__).parent.parent.absolute()
SETTINGS = ROOT / ".generator/settings"
API_DIRECTORY = ROOT / ".download/dist/api"

MODULE_CONFIG = {
    "scripts": [
        "https://cdn.jsdelivr.net/npm/quasar@2.12.4/dist/quasar.umd.prod.js",
        dict(
            name="trame_utils.js",
            content="""
                (function () {
                    function bindQuasar() {
                        if (window.Quasar) {
                            window.trame.utils.quasar = window.Quasar;
                        } else {
                            setTimeout(bindQuasar, 100);
                        }
                    }
                    bindQuasar();
                })();
            """,
        ),
    ],
    "styles": [
        "fonts.css",
        "https://cdn.jsdelivr.net/npm/quasar@2.12.4/dist/quasar.prod.css",
    ],
    "vue_use": ["Quasar"],
}


def generate_config():
    all_directives = []
    widgets = {"directives": all_directives}
    for file_entry in API_DIRECTORY.iterdir():
        entry_config = json.loads(file_entry.read_text())
        class_name = file_entry.stem
        entry_type = entry_config.get("type")
        if entry_type == "directive":
            all_directives.append(f"v-{camel_to_dash(class_name)}")
        elif entry_type == "component":
            properties = []
            events = []
            widgets[class_name] = {
                "component": camel_to_dash(class_name),
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
