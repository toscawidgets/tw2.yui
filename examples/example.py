import tw2.core as twc, tw2.forms as twf, tw2.yui as twy

treeview_content = [
    {'type':'Text', 'label':'Label 1', 'children':['Sub label %d' % i for i in range(1,11)]},
    {'type':'Text', 'label':'Label 2', 'children':['Sub label %d' % i for i in range(1,11)]},
    {'type':'Text', 'label':'Label 3', 'children':['Sub label %d' % i for i in range(1,11)]},
]

class Index(twf.FormPage):
    title = 'YUI Example'
    attrs = {'class': 'yui-skin-sam'}
    class child(twf.TableLayout):
#        auto_complete = twy.AutoComplete()
        color_picker = twy.ColorPicker()
        calendar = twy.Calendar()
        slider = twy.Slider()
        editor = twy.Editor()
        class tabview(twy.TabView):
            tab1 = twf.Label(label='Tab 1', text='This is the first tab')
            tab2 = twf.Label(label='Tab 2', text='And this is the other tab')
        treeview = twy.TreeView(content=treeview_content)

if __name__ == '__main__':
    import wsgiref.simple_server as wrs
    wrs.make_server('', 8000, twc.make_middleware(controller_prefix='/')).serve_forever()
