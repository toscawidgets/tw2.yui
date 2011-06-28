import widgets as twy, tw2.forms as twf, tw2.core as twc

page_options = {'css_class': 'yui-skin-sam'}

class DemoTabView(twy.TabView):
    tab1 = twf.Label(label='Tab 1', text='This is the first tab')
    tab2 = twf.Label(label='Tab 2', text='And this is the other tab')

class DemoTreeView(twy.TreeView):
    content = [
        {'type':'Text', 'label':'Label 1', 'children':['Sub label %d' % i for i in range(1,11)]},
        {'type':'Text', 'label':'Label 2', 'children':['Sub label %d' % i for i in range(1,11)]},
        {'type':'Text', 'label':'Label 3', 'children':['Sub label %d' % i for i in range(1,11)]},
    ]

class DemoEditor(twy.Editor):
    rows = 5

class DemoAutoComplete(twy.AutoComplete):
    class datasrc(twy.LocalDataSource):
        resources = twy.DataSource.resources + [
            twc.JSLink(modname=__name__, filename="static/sample-data.js"),
        ]
        data = 'YAHOO.example.Data.arrayStates'
        responseSchema = {'fields': ["state"]};


class DemoDataTable(twy.DataTable):
    id = twy.Column()
    name = twy.Column()
    value = [{'id':1, 'name':'Joe'}, {'id':2, 'name':'Paul'}]
