"""
ToscaWidgets wrappers for Yahoo User Interface (YUI) widgets.
"""
import tw2.core as twc, tw2.forms as twf, simplejson, webob
encoder = simplejson.encoder.JSONEncoder()


class YuiWidget(twc.Widget):
    resources = [
        twc.DirLink(modname=__name__, filename="static/2.7.0/"),
        twc.CSSLink(modname=__name__, filename="static/2.7.0/fonts/fonts-min.css"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/yahoo-dom-event/yahoo-dom-event.js"),
    ]
    options = twc.Param('Configuration options for the widget. See the YUI docs for available options.', default={})
    def prepare(self):
        super(YuiWidget, self).prepare()
        self.options = encoder.encode(self.options)


class Slider(YuiWidget):
    resources = YuiWidget.resources + [
        twc.CSSLink(modname=__name__, filename="static/2.7.0/slider/assets/skins/sam/slider.css"),
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
    resources = YuiWidget.resources + [
        twc.CSSLink(modname=__name__, filename="static/2.7.0/tabview/assets/skins/sam/tabview.css"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/element/element-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/tabview/tabview-min.js"),
    ]
    template = "genshi:tw2.yui.templates.tabview"


class AutoComplete(YuiWidget):
    resources = YuiWidget.resources + [
        twc.CSSLink(modname=__name__, filename="static/2.7.0/autocomplete/assets/skins/sam/autocomplete.css"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/connection/connection-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/json/json-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/element/element-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/animation/animation-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/datasource/datasource-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/autocomplete/autocomplete-min.js"),
    ]
    template = "genshi:tw2.yui.templates.autocomplete"
    datasrc = twc.Param('DataSource to use')

    @classmethod
    def post_define(cls):
        if hasattr(cls, 'datasrc'):
            cls.datasrc = cls.datasrc(parent=cls, id='datasrc')


class DataSource(YuiWidget):
    # TBD: resources
    template = "genshi:tw2.yui.templates.datasource"

    @classmethod
    def request(self, req):
        resp = webob.Response(request=req, content_type="text/plain; charset=UTF8")
        x = self.ajax_request(req)
        resp.body = x
        return resp


class ColorPicker(YuiWidget):
    resources = YuiWidget.resources + [
        twc.CSSLink(modname=__name__, filename="static/2.7.0/colorpicker/assets/skins/sam/colorpicker.css"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/dragdrop/dragdrop-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/animation/animation-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/slider/slider-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/element/element-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/colorpicker/colorpicker-min.js"),
    ]
    template = "genshi:tw2.yui.templates.colorpicker"

    def prepare(self):
        self.safe_modify('options')
        self.options['images'] = {
            'PICKER_THUMB': "/resources/tw2.yui.widgets/static/2.7.0/colorpicker/assets/picker_thumb.png",
            'HUE_THUMB': "/resources/tw2.yui.widgets/static/2.7.0/colorpicker/assets/hue_thumb.png"
        }
        super(ColorPicker, self).prepare()


class Calendar(YuiWidget):
    resources = YuiWidget.resources + [
        twc.CSSLink(modname=__name__, filename="static/2.7.0/calendar/assets/skins/sam/calendar.css"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/calendar/calendar-min.js"),
    ]
    template = "genshi:tw2.yui.templates.calendar"


class Editor(twf.TextArea, YuiWidget):
    resources = YuiWidget.resources + [
        twc.CSSLink(modname=__name__, filename="static/2.7.0/menu/assets/skins/sam/menu.css"),
        twc.CSSLink(modname=__name__, filename="static/2.7.0/button/assets/skins/sam/button.css"),
        twc.CSSLink(modname=__name__, filename="static/2.7.0/container/assets/skins/sam/container.css"),
        twc.CSSLink(modname=__name__, filename="static/2.7.0/editor/assets/skins/sam/editor.css"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/animation/animation-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/element/element-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/container/container-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/menu/menu-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/button/button-min.js"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/editor/editor-min.js"),
    ]
    template = "genshi:tw2.yui.templates.editor"

    # default to a fairly large size
    rows = 20
    cols = 75


class TreeView(YuiWidget):
    resources = YuiWidget.resources + [
        twc.CSSLink(modname=__name__, filename="static/2.7.0/treeview/assets/skins/sam/treeview.css"),
        twc.JSLink(modname=__name__, filename="static/2.7.0/treeview/treeview-min.js"),
    ]
    template = "genshi:tw2.yui.templates.treeview"
