import tw2.core as twc, tw2.forms as twf, tw2.yui as twy

class MyDataSource(twy.DataSource):
    @classmethod
    def ajax_request(self, req):
        return """
        {"ResultSet":{
            "Result":[
                {'title': 'billy'},
                {'title': 'betty'},
                {'title': 'joe'},
            ]}
        }
"""
#        return "Bob,1\nBilly,2\nBrian,3"

class Index(twf.FormPage):
    title = "YUI AutoComplete"
    attrs = {"class": "yui-skin-sam"}
    class child(twf.TableForm):
        paj = twy.AutoComplete(datasrc=MyDataSource(id="bobby"))

if __name__ == "__main__":
    import wsgiref.simple_server as wrs
    wrs.make_server("", 8000, twc.make_middleware(controller_prefix="/")).serve_forever()

