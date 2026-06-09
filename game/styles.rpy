
################################################################################
## Style Initialization
################################################################################

init offset = -1

################################################################################
## Styles
################################################################################

style default:
    font gui.text_font
    size gui.text_size
    language gui.language

style input:
    adjust_spacing False

style hyperlink_text:
    hover_underline True
    color "#6b90ee"

style gui_text:
    color '#444'
    size gui.text_size
    font gui.interface_text_font

style button:
    xysize (None, None)
    padding (0, 0)

style button_text:
    is gui_text
    yalign 0.5
    xalign 0.0
    ## The color used for a text button when it is neither selected nor hovered.
    idle_color '#eee'
    ## The color that is used for buttons and bars that are hovered.
    hover_color '#6b90ee'
    ## The color used for a text button when it is selected but not focused. A
    ## button is selected if it is the current screen or preference value.
    selected_color '#ffffff'
    ## The color used for a text button when it cannot be selected.
    insensitive_color '#444444'

style label_text:
    is gui_text
    size 36
    color '#f93c3e'


style bar:
    ysize 38
    left_bar Frame("gui/bar/left.png", 6, 6, 6, 6, tile=False)
    right_bar Frame("gui/bar/right.png", 6, 6, 6, 6, tile=False)

style vbar:
    xsize 38
    top_bar Frame("gui/bar/top.png", 6, 6, 6, 6, tile=False)
    bottom_bar Frame("gui/bar/bottom.png", 6, 6, 6, 6, tile=False)

style scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", 6, 6, 6, 6, tile=False)
    unscrollable 'hide'

style vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", 6, 6, 6, 6, tile=False)
    unscrollable 'hide'

style slider:
    ysize 38
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize 38
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding (6, 6, 6, 6)
    background Frame("gui/frame.png", 6, 6, 6, 6, tile=False)
