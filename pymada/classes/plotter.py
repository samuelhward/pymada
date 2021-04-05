import pymada
import pymada.errors
import pymada.settings
import pymada.data.tools
import bokeh.plotting, bokeh.models
import numpy as np


class Plotter:
    def __init__(self):
        """

        attrs:
            artists - groups of labels for linked plot objects e.g. ship = ship, arcs, heading [dict]
        """

        self.plot_methods_dispatch = {}
        self.plot_methods_dispatch["Ship"] = self.draw_ship
        self.plot_methods_dispatch["Base"] = self.draw_base
        self.plot_methods_dispatch["HullZone"] = self.draw_hull_zone
        self.plot_methods_dispatch["Board"] = self.draw_board
        bokeh.plotting.output_file(pymada.settings.plot_file_path)
        self.plot = bokeh.plotting.Figure(
            match_aspect=True,
            plot_width=pymada.settings.plot_width,
            plot_height=pymada.settings.plot_height,
        )
        self.artists = {}

    def draw(self, obj, *args, **kwargs):
        """
        args:
            obj - object instance for plotting e.g. ship [-]
        kwargs:
            artist -
        """
        if pymada.settings.plotting_enable:

            clear = kwargs.get("clear", True)

            # create default name for artist if not supplied
            if "artist" not in kwargs:
                if hasattr(obj, "name"):
                    kwargs["artist"] = obj.name
            if "artist" in kwargs:
                # add artist if not already present
                if kwargs["artist"] not in self.artists:
                    self.artists[kwargs["artist"]] = []
                # erase this artist and all child artists
                elif clear is True:
                    self.erase(obj, *args, **kwargs)

            self.plot_methods_dispatch[type(obj).__name__](obj, *args, **kwargs)

    def erase(self, obj=None, artist=None, *args, **kwargs):
        """
        args:
            artist -
        """

        if pymada.settings.plotting_enable:

            if artist is not None:
                pass
            elif obj and hasattr(obj, "name"):
                artist = obj.name

            else:
                raise pymada.errors.PlotError(
                    "Error in plotter.erase() - requires obj.name or artist!"
                )

            if artist in self.artists and self.artists[artist]:
                for artist_name in self.artists[artist]:
                    self.plot.renderers.remove(
                        self.plot.select_one({"name": artist_name})
                    )
                self.artists[artist] = []

    def show(self, *args, **kwargs):
        """"""

        if pymada.settings.plotting_enable:
            bokeh.plotting.show(self.plot)

    def draw_base(self, base, *args, **kwargs):
        """"""

        artist = kwargs.get("artist", None)
        colour = kwargs.get("colour", "#")

        x, y = [], []
        for point in base.outline:
            x.append(point.x)
            y.append(point.y)
        x.append(x[-1])
        y.append(y[-1])
        artist_name = f"{artist}_base"
        self.plot.patch(
            x,
            y,
            name=artist_name,
            fill_color=colour,
            line_color=pymada.settings.colour_base_line,
            alpha=pymada.settings.alpha_base,
        )
        if artist is not None:
            self.artists[artist].append(artist_name)

    def draw_hull_zone(self, hull_zone, *args, **kwargs):
        """"""

        artist = kwargs.get("artist", None)

        for colour in ["red", "blue", "black"]:
            artist_name = f"{artist}_{colour}_{hull_zone.arc_right}_arc"
            self.plot.arc(
                x=hull_zone.position.x,
                y=hull_zone.position.y,
                radius=pymada.data.tools.rulers["range"][colour],
                start_angle=hull_zone.arc_left,
                end_angle=hull_zone.arc_right,
                color=colour,
                line_width=pymada.settings.linewidth_arc,
                name=artist_name,
            )
            if artist is not None:
                self.artists[artist].append(artist_name)
            for counter, arc_angle in enumerate(
                [hull_zone.arc_left, hull_zone.arc_right]
            ):
                artist_name = f"{artist}_{colour}_{hull_zone.arc_right}_line{counter}"
                self.plot.line(
                    [
                        hull_zone.position.x,
                        hull_zone.position.x
                        + pymada.data.tools.rulers["range"][colour]
                        * np.cos((hull_zone.position.theta + arc_angle) * np.pi / 180),
                    ],
                    [
                        hull_zone.position.y,
                        hull_zone.position.y
                        + pymada.data.tools.rulers["range"][colour]
                        * np.sin((hull_zone.position.theta + arc_angle) * np.pi / 180),
                    ],
                    color=colour,
                    line_width=pymada.settings.linewidth_arc,
                    name=artist_name,
                )
                if artist is not None:
                    self.artists[artist].append(artist_name)

    def draw_ship(self, ship, *args, **kwargs):
        """"""

        artist = kwargs.get("artist", None)

        self.draw(ship.base, clear=False, colour=ship.colour, *args, **kwargs)

        for hull_zone in ship.hull_zones.values():
            self.draw(hull_zone, clear=False, *args, **kwargs)

        artist_name = f"{artist}_ship_heading"
        self.plot.line(
            [
                ship.position.x,
                ship.position.x + np.cos(ship.position.theta * np.pi / 180),
            ],
            [
                ship.position.y,
                ship.position.y + np.sin(ship.position.theta * np.pi / 180),
            ],
            color=pymada.settings.colour_heading,
            line_width=pymada.settings.line_width_heading,
            name=artist_name,
        )
        if artist is not None:
            self.artists[artist].append(artist_name)

    def draw_board(self, board, *args, **kwargs):
        """

        args:
            board -
        kwargs:
            artist -
        notes:
            currently cannot erase/redraw board as artist is not added
        """

        x, y = [], []
        for point in board.outline:
            x.append(point.x)
            y.append(point.y)
        x.append(x[-1])
        y.append(y[-1])
        self.plot.patch(
            x,
            y,
            fill_color=pymada.settings.colour_board,
            fill_alpha=0.1,
            line_color=pymada.settings.colour_board_line,
        )
        if hasattr(board, "zones"):
            for zone in board.zones:
                self.draw(board.zones[zone])
