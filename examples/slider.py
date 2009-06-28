import tw2.core as twc, tw2.forms as twf, tw2.yui as twy

class Index(twf.FormPage):
    title = 'YUI Slider'
    class child(twf.Form):
        class child(twf.TableLayout):
            check = twf.CheckBox(validator=twc.Required)
            value = twy.Slider()

if __name__ == '__main__':
    import wsgiref.simple_server as wrs
    wrs.make_server('', 8000, twc.make_middleware(controller_prefix='/')).serve_forever()
