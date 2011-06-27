"""
ToscaWidgets wrappers for Yahoo User Interface (YUI) widgets.
"""
import tw2.core as twc, tw2.forms as twf, simplejson, webob, re
encoder = simplejson.encoder.JSONEncoder()

yui_version = '2.9.0'

class YuiWidget(twc.Widget):
    resources = [
        twc.DirLink(modname=__name__, filename="static/"+yui_version+"/"),
        twc.CSSLink(modname=__name__, filename="static/"+yui_version+"/fonts/fonts-min.css"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/yahoo-dom-event/yahoo-dom-event.js"),
    ]
    options = twc.Param('Configuration options for the widget. See the YUI docs for available options.', default={})
    def prepare(self):
        super(YuiWidget, self).prepare()
        self.options = encoder.encode(self.options)


class Slider(YuiWidget):
    resources = YuiWidget.resources + [
        twc.CSSLink(modname=__name__, filename="static/"+yui_version+"/slider/assets/skins/sam/slider.css"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/animation/animation-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/dragdrop/dragdrop-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/slider/slider-min.js"),
        twc.Link(id='thumb', modname=__name__, filename='static/'+yui_version+'/slider/assets/thumb-n.gif'),
    ]
    template = "genshi:tw2.yui.templates.slider"

    size = twc.Param('Size in pixels of control', default=200)
    min = twc.Param('Minimum effective value', default=0)
    max = twc.Param('Maximum effective value', default=100)


class TabView(twf.widgets.BaseLayout):
    resources = YuiWidget.resources + [
        twc.CSSLink(modname=__name__, filename="static/"+yui_version+"/tabview/assets/skins/sam/tabview.css"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/element/element-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/tabview/tabview-min.js"),
    ]
    template = "genshi:tw2.yui.templates.tabview"
    # These don't apply; hide from widget browser
    hover_help = twc.Variable()
    help_text = twc.Variable()
    container_attrs = twc.Variable()


class AutoComplete(twf.TextField, YuiWidget):
    resources = YuiWidget.resources + [
        twc.CSSLink(modname=__name__, filename="static/"+yui_version+"/autocomplete/assets/skins/sam/autocomplete.css"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/connection/connection-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/json/json-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/element/element-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/animation/animation-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/datasource/datasource-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/autocomplete/autocomplete-min.js"),
    ]
    template = "genshi:tw2.yui.templates.autocomplete"
    attrs = {'style': 'width:15em;'}
    datasrc = twc.Param('DataSource to use')
    value = twc.Param(attribute=True)

    @classmethod
    def post_define(cls):
        if hasattr(cls, 'datasrc'):
            cls.datasrc = cls.datasrc(parent=cls, id='datasrc')

    def __init__(self, **kw):
        super(AutoComplete, self).__init__(**kw)
        self.datasrc = self.datasrc.req()

    def prepare(self):
        super(AutoComplete, self).prepare()
        self.datasrc.prepare()


class DataSource(YuiWidget):
    resources = [ # don't use YuiWidget.resources
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/datasource/datasource-min.js"),
    ]
    responseSchema = twc.Param('TBD', default={'resultsList':'result'})

    def prepare(self):
        self.safe_modify('options')
        self.options['responseSchema'] = self.responseSchema
        super(DataSource, self).prepare()


class XHRDataSource(DataSource):
    template = "genshi:tw2.yui.templates.xhrdatasource"
    options = {
        'responseType': 3, # YAHOO.util.XHRDataSource.TYPE_JSON
    }

    @classmethod
    def request(self, req):
        resp = webob.Response(request=req, content_type="application/json; charset=UTF8")
        resp.body = encoder.encode(self.ajax_request(req))
        return resp


class LocalDataSource(DataSource):
    template = "genshi:tw2.yui.templates.localdatasource"
    data = twc.Param('Name of the JavaScript array to use as the data source')


class ColorPicker(YuiWidget):
    resources = YuiWidget.resources + [
        twc.CSSLink(modname=__name__, filename="static/"+yui_version+"/colorpicker/assets/skins/sam/colorpicker.css"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/dragdrop/dragdrop-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/animation/animation-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/slider/slider-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/element/element-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/colorpicker/colorpicker-min.js"),
        twc.Link(id='picker_thumb', modname=__name__, filename="static/"+yui_version+"/colorpicker/assets/picker_thumb.png"),
        twc.Link(id='hue_thumb', modname=__name__, filename="static/"+yui_version+"/colorpicker/assets/hue_thumb.png"),
    ]
    template = "genshi:tw2.yui.templates.colorpicker"
    rgb = twc.Variable(default='[0xFF,0xFF,0xFF]')

    def prepare(self):
        self.safe_modify('options')
        if self.value and re.match('^#[0-9a-fA-F]{6}$', self.value):
            self.rgb = encoder.encode([int(self.value[i:i+2], 16) for i in (1, 3, 5)])
        self.options['images'] = {
            'PICKER_THUMB': '/resources/tw2.yui.widgets/static/'+yui_version+'/colorpicker/assets/picker_thumb.png',
            'HUE_THUMB': '/resources/tw2.yui.widgets/static/'+yui_version+'/colorpicker/assets/hue_thumb.png',
        }
        super(ColorPicker, self).prepare()


class Calendar(YuiWidget):
    resources = YuiWidget.resources + [
        twc.CSSLink(modname=__name__, filename="static/"+yui_version+"/calendar/assets/skins/sam/calendar.css"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/calendar/calendar-min.js"),
    ]
    template = "genshi:tw2.yui.templates.calendar"


class Editor(twf.TextArea, YuiWidget):
    resources = YuiWidget.resources + [
        twc.CSSLink(modname=__name__, filename="static/"+yui_version+"/menu/assets/skins/sam/menu.css"),
        twc.CSSLink(modname=__name__, filename="static/"+yui_version+"/button/assets/skins/sam/button.css"),
        twc.CSSLink(modname=__name__, filename="static/"+yui_version+"/container/assets/skins/sam/container.css"),
        twc.CSSLink(modname=__name__, filename="static/"+yui_version+"/editor/assets/skins/sam/editor.css"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/animation/animation-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/element/element-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/container/container-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/menu/menu-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/button/button-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/editor/editor-min.js"),
    ]
    template = "genshi:tw2.yui.templates.editor"
    options = {'handleSubmit': 1}

    # default to a fairly large size
    rows = 20
    cols = 100


class TreeView(YuiWidget):
    resources = YuiWidget.resources + [
        twc.CSSLink(modname=__name__, filename="static/"+yui_version+"/treeview/assets/skins/sam/treeview.css"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/treeview/treeview-min.js"),
    ]
    template = "genshi:tw2.yui.templates.treeview"
    content = twc.Param('Content', default=[])
    def prepare(self):
        super(TreeView, self).prepare()
        self.content = encoder.encode(self.content)


class LogReader(YuiWidget):
    resources = YuiWidget.resources + [
        twc.CSSLink(modname=__name__, filename="static/"+yui_version+"/logger/assets/skins/sam/logger.css"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/logger/logger-min.js"),
    ]
    template = "genshi:tw2.yui.templates.logreader"


class DataTable(YuiWidget, twc.CompoundWidget):
    resources = YuiWidget.resources + [
        twc.CSSLink(modname=__name__, filename="static/"+yui_version+"/datatable/assets/skins/sam/datatable.css"),
        twc.CSSLink(modname=__name__, filename="static/"+yui_version+"/button/assets/skins/sam/button.css"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/dom/dom-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/event/element-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/dragdrop/dragdrop-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/element/element-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/datasource/datasource-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/event-delegate/event-delegate-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/datatable/datatable-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/button/button-min.js"),
        twc.JSLink(modname=__name__, filename="static/"+yui_version+"/connection/connection-min.js"),
    ]
    template = "genshi:tw2.yui.templates.datatable"
    datasrc = twc.Param('DataSource to use')
    columns = twc.Variable()

    @classmethod
    def post_define(cls):
        if hasattr(cls, 'datasrc'):
            cls.datasrc = cls.datasrc(parent=cls, id='datasrc')

    def __init__(self, **kw):
        super(DataTable, self).__init__(**kw)
        self.datasrc = self.datasrc.req()

    def prepare(self):
        super(DataTable, self).prepare()
        self.datasrc.prepare()
        self.columns = encoder.encode([c.options for c in self.c])


class Column(twc.Widget):
    """A column in a DataTable."""
    options = twc.Param('Configuration options for the widget. See the YUI docs for available options.', 
        default={'sortable':True, 'resizeable':True})
    def prepare(self):
        super(Column, self).prepare()
        self.safe_modify('options')
        self.options['key'] = self.id
