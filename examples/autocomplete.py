import tw2.core as twc, tw2.forms as twf, tw2.yui as twy

class MyDataSource(twy.DataSource):
    @classmethod
    def ajax_request(self, req):
        return {'result': ['a','b','c']}

class Index(twf.FormPage):
    title = "YUI AutoComplete"
    attrs = {"class": "yui-skin-sam"}
    class child(twf.TableForm):
        paj = twy.AutoComplete(datasrc=MyDataSource())
        fred = twy.LogReader()

if __name__ == "__main__":
    import wsgiref.simple_server as wrs
    wrs.make_server("", 8000, twc.make_middleware(controller_prefix="/")).serve_forever()
