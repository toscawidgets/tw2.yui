import tw2.core as twc, tw2.forms as twf, tw2.yui as twy

class Index(twf.FormPage):
    title = 'YUI Example'
    css_class = 'yui-skin-sam'
    class child(twf.TableLayout):
        class auto_complete(twy.AutoComplete):
            label = 'Enter a state'
            class datasrc(twy.XHRDataSource):
                @classmethod
                def ajax_request(self, req):
                    q = req.GET['query'].lower()
                    return {'result': [s for s in arrayStates if s.lower().startswith(q)]}

        color_picker = twy.ColorPicker()
        calendar = twy.Calendar()
        slider = twy.Slider()
        editor = twy.Editor()
        class tab_view(twy.TabView):
            tab1 = twf.Label(label='Tab 1', text='This is the first tab')
            tab2 = twf.Label(label='Tab 2', text='And this is the other tab')
        class tree_view(twy.TreeView):
            content = [
                {'type':'Text', 'label':'Label 1', 'children':['Sub label %d' % i for i in range(1,11)]},
                {'type':'Text', 'label':'Label 2', 'children':['Sub label %d' % i for i in range(1,11)]},
                {'type':'Text', 'label':'Label 3', 'children':['Sub label %d' % i for i in range(1,11)]},
            ]


arrayStates = [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Dakota",
    "North Carolina",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming"
]

if __name__ == '__main__':
    import wsgiref.simple_server as wrs
    wrs.make_server('', 8000, twc.make_middleware(controller_prefix='/')).serve_forever()
