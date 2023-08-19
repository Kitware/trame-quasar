from trame.app import get_server
from trame.ui.html import DivLayout
from trame.widgets import quasar, html

server = get_server()
server.client_type = "vue3"
server.state.dark = False

with DivLayout(server):
    with quasar.QLayout(
        view="lhh LpR lff",
        container=True,
        style="width: 100vw; height: 100vh;",
        classes=(
            """{
                'shadow-2': 1,
                'rounded-borders': 1,
                'bg-grey-9': dark,
                'bg-grey-3': !dark,
            }""",
        ),
    ):
        with quasar.QHeader(
            reveal=True,
            classes=("{ 'bg-secondary': dark, 'bg-black': !dark}",),
        ):
            with quasar.QToolbar():
                quasar.QBtn(
                    flat=True,
                    click="drawerLeft = !drawerLeft",
                    round=True,
                    dense=True,
                    icon="menu",
                )
                quasar.QToolbarTitle("Header")
                quasar.QBtn(
                    flat=True,
                    click="drawerRight = !drawerRight",
                    round=True,
                    dense=True,
                    icon="menu",
                )

        with quasar.QFooter():
            with quasar.QToolbar():
                quasar.QToolbarTitle("Footer")

        with quasar.QDrawer(
            v_model=("drawerLeft", False),
            width=(200,),
            breakpoint=(700,),
            bordered=True,
        ):
            with quasar.QScrollArea(classes="fit"):
                with html.Div(classes="q-pa-sm"):
                    html.Div("Drawer {{ n }} / 50", v_for="n in 50", key="n")

        with quasar.QDrawer(
            side="right",
            v_model=("drawerRight", False),
            width=(200,),
            breakpoint=(500,),
            bordered=True,
        ):
            with quasar.QScrollArea(classes="fit"):
                with html.Div(classes="q-pa-sm"):
                    html.Div("Drawer {{ n }} / 50", v_for="n in 50", key="n")

        with quasar.QPageContainer():
            with quasar.QPage(style="padding-top: 60px", classes="q-pa-md"):
                with html.P(v_for="n in 15", key="n") as c:
                    c.add_child(
                        "Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugit nihil praesentium molestias a adipisci, dolore vitae odit, quidem consequatur option voluptates asperiores pariatur eos numquam rerum delectus commodi perferendis voluptate?"
                    )


server.start()
