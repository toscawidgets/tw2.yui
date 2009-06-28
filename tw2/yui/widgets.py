import tw2.core as twc, tw2.forms as twf, simplejson
encoder = simplejson.encoder.JSONEncoder()


class Slider(twc.Widget):
    resources = [
        twc.DirLink(modname=__name__, filename="static/2.7.0/"),
        twc.CSSLink(modname=__name__, filename="static/2.7.0/fonts/fonts-min.css"),
        twc.CSSLink(modname=__name__, filename="static/2.7.0/slider/assets/skins/sam/slider.css"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/yahoo-dom-event/yahoo-dom-event.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/animation/animation-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/dragdrop/dragdrop-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/slider/slider-min.js"),
        twc.Link(id='thumb', modname=__name__, filename='static/2.7.0/slider/assets/thumb-n.gif'),
    ]
    template = "genshi:tw2.yui.templates.slider"

    size = twc.Param('Size in pixels of control', default=200)
    min = twc.Param('Minimum effective value', default=0)
    max = twc.Param('Maximum effective value', default=100)


class TabView(twf.widgets.BaseLayout):
    resources = [
        twc.DirLink(modname=__name__, filename="static/2.7.0/"),
        twc.CSSLink(modname=__name__, filename="static/2.7.0/fonts/fonts-min.css"),
        twc.CSSLink(modname=__name__, filename="static/2.7.0/tabview/assets/skins/sam/tabview.css"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/yahoo-dom-event/yahoo-dom-event.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/element/element-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/tabview/tabview-min.js"),
        twc.Link(modname=__name__, filename='static/2.7.0/assets/skins/sam/sprite.png'),
    ]
    template = "genshi:tw2.yui.templates.tabview"


class AutoComplete(twc.Widget):
    resources = [
        twc.DirLink(modname=__name__, filename="static/2.7.0/"),
        twc.CSSLink(modname=__name__, filename="static/2.7.0/fonts/fonts-min.css"),
        twc.CSSLink(modname=__name__, filename="static/2.7.0/autocomplete/assets/skins/sam/autocomplete.css"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/yahoo-dom-event/yahoo-dom-event.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/animation/animation-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/datasource/datasource-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/autocomplete/autocomplete-min.js"),

        twc.JSLink(modname=__name__, filename="static/data.js"), # TBD
    ]
    template = "genshi:tw2.yui.templates.autocomplete"


class ColorPicker(twc.Widget):
    resources = [
        twc.DirLink(modname=__name__, filename="static/2.7.0/"),
        twc.CSSLink(modname=__name__, filename="static/2.7.0/slider/assets/skins/sam/slider.css"),
        twc.CSSLink(modname=__name__, filename="static/2.7.0/fonts/fonts-min.css"),
        twc.CSSLink(modname=__name__, filename="static/2.7.0/colorpicker/assets/skins/sam/colorpicker.css"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/yahoo-dom-event/yahoo-dom-event.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/dragdrop/dragdrop-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/animation/animation-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/slider/slider-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/element/element-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/colorpicker/colorpicker-min.js"),
    ]
    template = "genshi:tw2.yui.templates.colorpicker"

    config = twc.Param('config - see yui docs', default={})

    def prepare(self):
        super(ColorPicker, self).prepare()
        self.safe_modify('config')
        self.config['images'] = {
            'PICKER_THUMB': "/resources/tw2.yui.widgets/static/2.7.0/colorpicker/assets/picker_thumb.png",
            'HUE_THUMB': "/resources/tw2.yui.widgets/static/2.7.0/colorpicker/assets/hue_thumb.png"
        }
        self.config = encoder.encode(self.config)


class Calendar(twc.Widget):
    resources = [
        twc.DirLink(modname=__name__, filename="static/2.7.0/"),
        twc.CSSLink(modname=__name__, filename="static/2.7.0/fonts/fonts-min.css"),
        twc.CSSLink(modname=__name__, filename="static/2.7.0/calendar/assets/skins/sam/calendar.css"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/yahoo-dom-event/yahoo-dom-event.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/calendar/calendar-min.js"),
    ]
    template = "genshi:tw2.yui.templates.calendar"

    config = twc.Param('config - see yui docs', default={})

    def prepare(self):
        super(Calendar, self).prepare()
        self.config = encoder.encode(self.config)


class Editor(twc.Widget):
    resources = [
        twc.DirLink(modname=__name__, filename="static/2.7.0/"),
        twc.CSSLink(modname=__name__, filename="static/2.7.0/menu/assets/skins/sam/menu.css"),
        twc.CSSLink(modname=__name__, filename="static/2.7.0/button/assets/skins/sam/button.css"),
        twc.CSSLink(modname=__name__, filename="static/2.7.0/fonts/fonts-min.css"),
        twc.CSSLink(modname=__name__, filename="static/2.7.0/container/assets/skins/sam/container.css"),
        twc.CSSLink(modname=__name__, filename="static/2.7.0/editor/assets/skins/sam/editor.css"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/yahoo-dom-event/yahoo-dom-event.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/animation/animation-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/element/element-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/container/container-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/menu/menu-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/button/button-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/editor/editor-min.js"),
    ]
    template = "genshi:tw2.yui.templates.editor"

    config = twc.Param('config - see yui docs', default={})

    def prepare(self):
        super(Editor, self).prepare()
        self.config = encoder.encode(self.config)
