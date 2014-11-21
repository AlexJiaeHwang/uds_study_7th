from IPython.html.widgets import DOMWidget
from IPython.utils.traitlets import Bool
from IPython.core.display import display, HTML, Javascript
from uuid import uuid4

class BulbWidget(DOMWidget):
    # _view_name =
    disabled = Bool(False)
    status = Bool(False, sync=True)

    def __init__(self, **kwargs):
        super(BulbWidget, self).__init__(**kwargs)
        self._id = str(uuid4())

    def _notify_trait(self, name, old_value, new_value):
        print new_value

        if new_value:
            tpl_js = '''
                $('#{id}').addClass('on');
            '''
        else:
            tpl_js = '''
                $('#{id}').removeClass('on');
            '''
        js = tpl_js.format(id=self._id)

        display(Javascript(js))


    def _ipython_display_(self):
        display(HTML('''
        <style>
        .bulb-widget {
            position: relative;
            width: 256px;
            height: 256px;
            background: url('widget/static/img/bulb_off.png') no-repeat;
        }
        .bulb-widget.on {
            background: url('widget/static/img/bulb_on.png') no-repeat;
        }
        </style>
        '''))

        html = '''
        <div id="{id}" class="bulb-widget"></div>
        '''.format(id=self._id)

        display(HTML(html))