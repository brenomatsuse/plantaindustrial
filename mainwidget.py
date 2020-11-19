from kivy.uix.boxlayout import BoxLayout
from popups import GraphPopup,HistGraphPopup,MotorPopup,SolenoidePopup

class MainWidget(BoxLayout):
    """
    widget principal
    """
    def __init__(self):
        """
        construtor do main widget
        """
        super().__init__()
        self._graphPopup=GraphPopup()
        self._hgraphPopup=HistGraphPopup()
        self._motorPopup=MotorPopup()
        self._solenoidePopup=SolenoidePopup()
