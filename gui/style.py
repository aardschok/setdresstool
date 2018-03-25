frame_layout = """
QFrame {
    background-color: grey;
    
    border-top: 1px solid rgba(64, 64, 64, 255);
    border-left: 1px solid rgba(64, 64, 64, 255);
    border-right: 1px solid rgba(192, 192, 192, 255);
    border-bottom: 1px solid rgba(192, 192, 192, 255);
    
    margin: 0px, 0px, 0px, 0px;
    
    padding: 0px, 0px, 0px, 0px;
}"""


frame_layout_collapsed = """
QFrame {
    border: 0px solid;
    margin: 0px, 0px, 0px, 0px;
    padding: 0px, 0px, 0px, 0px;
}"""


collapisbe_arrow = """
QFrame {
    background-color: QLinearGradient(x1: 0,
                                      y1: 0, 
                                      x2: 0, 
                                      y2: 1, 
                                      stop: 0 #545454, 
                                      stop: 1 #232323);
        
    border-top: 1px solid rgba(192, 192, 192, 255);
    border-left: 1px solid rgba(192, 192, 192, 255);
    border-right: 1px solid rgba(32, 32, 32, 255);
    border-bottom: 1px solid rgba(64, 64, 64, 255);
    
    margin: 0px, 0px, 0px, 0px;
    padding: 0px, 0px, 0px, 0px;
    }
QFrame:hover 
    {background-color: QLinearGradient(x1: 0,
                                       y1: 0,
                                       x2: 0,
                                       y2: 1,
                                       stop: 0 #232323, 
                                       stop: 1 #545454);
    }"""


title_label = """
TitleLabel {
    background-color: rgba(0, 0, 0, 0);
    
    color: white;
    
    border-left: 1px solid rgba(128, 128, 128, 255);
    border-top: 0px transparent;
    border-right: 0px transparent;
    border-bottom: 0px transparent;
}"""


title_frame = """
QFrame {
    background-color: QLinearGradient( x1: 0, 
                                       y1: 0, 
                                       x2: 0, 
                                       y2: 1, 
                                       stop: 0 #545454, 
                                       stop: 1 #232323);
    
    border-top: 1px solid rgba(192, 192, 192, 255);
    border-left: 1px solid rgba(192, 192, 192, 255);
    border-right: 1px solid rgba(64, 64, 64, 255);
    border-bottom: 1px solid rgba(64, 64, 64, 255);
    
    margin: 0px, 0px, 0px, 0px;
    padding: 0px, 0px, 0px, 0px;
}"""

