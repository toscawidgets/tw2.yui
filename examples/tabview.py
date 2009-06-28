import tw2.core as twc, tw2.forms as twf, tw2.yui as twy

class Index(twf.FormPage):
    title = 'YUI TabView'
    attrs = {'class': 'yui-skin-sam'}
    class child(twy.TabView):
        class paj(twf.TableLayout):
            a = twf.TextField()
        class joe(twf.TableLayout):
            b = twf.TextArea()

if __name__ == '__main__':
    import wsgiref.simple_server as wrs
    wrs.make_server('', 8000, twc.make_middleware(controller_prefix='/')).serve_forever()
