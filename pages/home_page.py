from locators.locator import Locators
from playwright.sync_api import expect
from pages.base_page import BasePage

class HomePage(BasePage):
    
    def home_search(self):
        popup= self.page.get_by_text(Locators.close_popup)
        if popup.is_visible():
            popup.click()
        
    
        self.page.locator(Locators.search).fill('Software')
        self.page.locator(Locators.search_button).click()  
        self.page.wait_for_timeout(5000)
        expect(self.page.get_by_text(Locators.search_page_header)).to_be_visible()
        
        search_page_element = self.page.get_by_role("link", name="Top 20 Open Source Python")
        search_page_element.scroll_into_view_if_needed()
        search_page_element.click()
        # self.page.pause()
        
        search_redirection =  self.page.get_by_role("heading", name="Top 20 Open Source Python")
        
        expect(search_redirection).to_be_visible()
        a=search_redirection.text_content()

        print(a)
        
        
    def home_buttons(self):
        self.page.locator(Locators.tab_button).click()
        self.page.wait_for_timeout(5000)
        # element= self.page.locator(Locators.tab_simple_accordion).first
        
        frame=self.page.frame_locator(Locators.iframe) 
        #above line mai frame m ja rhe hai ab us frame k andar wale locator ko dhudega 
        # element.scroll_into_view_if_needed()
        # # expect(element).to_be_visible()
        
        frame.locator(Locators.section_4).click()
        self.page.wait_for_timeout(3000)
        
        frame.locator(Locators.section_4).click()
        self.page.wait_for_timeout(3000)

    def hover_tab_options(self):
        self.page.locator(Locators.tab_button).click()
        self.page.wait_for_timeout(5000)
        self.page.wait_for_selector("#sidebar")
        items=self.page.locator(Locators.all_options)
        
        count=items.count()
        print("Total Items:", count)


        for i in range(count):
            item= items.nth(i)
            item.scroll_into_view_if_needed()
            item.hover()
            print(f"Hovering on item {i}")
            print("Hovereing completed")
        
        
        
        
        
        
        
        
        
        