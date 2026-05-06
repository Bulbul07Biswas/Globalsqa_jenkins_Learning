from pages.home_page import HomePage


def test_home_page(page):
    home= HomePage(page)
    home.home_search()
    
    
    
def test_home_tabs(page):
    home_tab= HomePage(page)
    home_tab.home_buttons()

def test_hover(page):
    home_hover = HomePage(page)
    home_hover.hover_tab_options()
    
    