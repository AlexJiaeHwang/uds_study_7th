from IPython.html.widgets import DOMWidget
from IPython.utils.traitlets import Bool
from IPython.core.display import display, HTML, Javascript
from uuid import uuid4

class SevenSegWidget(DOMWidget):
    disabled = Bool(False)
    led_0 = Bool(False, sync=True)
    led_1 = Bool(False, sync=True)
    led_2 = Bool(False, sync=True)
    led_3 = Bool(False, sync=True)
    led_4 = Bool(False, sync=True)
    led_5 = Bool(False, sync=True)
    led_6 = Bool(False, sync=True)

    def __init__(self, **kwargs):
        super(SevenSegWidget, self).__init__(**kwargs)
        self._id = str(uuid4())

    def _notify_trait(self, name, old_value, new_value):
        if name.startswith('led_'):
            num = name[4:]
            if new_value:
                tpl_js = '''
                    $('#{id} .ssd-led-{num}').addClass('on');
                '''
            else:
                tpl_js = '''
                    $('#{id} .ssd-led-{num}').removeClass('on');
                '''
            js = tpl_js.format(id=self._id, num=num)
            display(Javascript(js))
        return new_value

    def _ipython_display_(self):
        display(HTML('''
        <style>
            .ssd-holder {
                position: relative;
                height: 140px;
            }
            .ssd-led {
                position: absolute;
                background-color: #000000;
                border-radius: 5px;
            }
            .ssd-led.on {
                background-color: #9C1A1C;
            }
            .ssd-led.h {
                width: 50px;
                height: 10px;
            }
            .ssd-led.v {
                width: 10px;
                height: 50px;
            }
            .ssd-led-0 {
                top: 0;
                left: 10px;
            }
            .ssd-led-1 {
                top: 10px;
                left: 0;
            }
            .ssd-led-2 {
                top: 10px;
                left: 60px;
            }
            .ssd-led-3 {
                top: 60px;
                left: 10px;
            }
            .ssd-led-4 {
                top: 70px;
                left: 0;
            }
            .ssd-led-5 {
                top: 70px;
                left: 60px;
            }
            .ssd-led-6 {
                top: 120px;
                left: 10px;
            }
        </style>
        '''))

        html = '''
            <div id="{id}" class="ssd-holder">
                <div class="ssd-led ssd-led-0 h"></div>
                <div class="ssd-led ssd-led-1 v"></div>
                <div class="ssd-led ssd-led-2 v"></div>
                <div class="ssd-led ssd-led-3 h"></div>
                <div class="ssd-led ssd-led-4 v"></div>
                <div class="ssd-led ssd-led-5 v"></div>
                <div class="ssd-led ssd-led-6 h"></div>
            </div>
        '''.format(id=self._id)

        display(HTML(html))