import tw2.core as twc, tw2.forms as twf, tw2.yui as twy

opts = [
    'Paj',
    {'label': 'blah', 'children': ['a', 'b', 'c']},
    'Joe',
]

class Index(twf.FormPage):
    title = 'YUI Test'
    attrs = {'class':'yui-skin-sam'}
    class child(twf.Form):
        class child(twf.TableLayout):
            check = twf.CheckBox(validator=twc.Required)
            color = twy.TreeView(options=opts)

if __name__ == '__main__':
    import wsgiref.simple_server as wrs
    wrs.make_server('', 8000, twc.make_middleware(controller_prefix='/')).serve_forever()
