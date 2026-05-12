
class Locators:
#Home+search
  close_popup= 'Close'
  search='#s'
  search_button= '.button_search'
  search_page_header='SEARCH RESULTS FOR: SOFTWARE'
  search_page_option ="(//div[@class='post_item'])[4]"
  
  #Check Jenkins for auto trigger
  
#Home

  tab_button="li.price_footer a:has-text('Tabs')"
  
#tab_page
  iframe= "(//p//iframe[@class='demo-frame'])[1]"
  section_4="//h3[@id='ui-id-7' and text()='Section 4']"
  # tab_simple_accordion= "//h3[@id='ui-id-1' and text()='Section 1']"
  # all_options="//a//span[@class='link_span']"
  all_options = "#sidebar .link_span"
  