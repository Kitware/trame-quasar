from trame_client.ui.core import AbstractLayout
from trame_quasar.widgets import quasar

__all__ = [
    "QLayout",
]


class QLayout(AbstractLayout):
    """
    Layout composed of just a `<q-layout view="" />`

    :param _server: Server to bound the layout to
    :param template_name: Name of the template (default: main)
    :param view: Quasar QLayout param (default: hHh lpR fFf)
    """

    def __init__(self, _server, template_name="main", view="hHh lpR fFf", **kwargs):
        super().__init__(
            _server,
            quasar.QLayout(trame_server=_server, view=view, **kwargs),
            template_name=template_name,
            **kwargs,
        )
