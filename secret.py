from playwright.sync_api import sync_playwright
import os




def main():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page

        page.goto('https://souhrada.github.io/playwright-exam/')
        
        page.fill('input[id="login"]', 'Jarmil')
        page.fill('input[id="pass"]', 'Admin123')

        page.click('button[class="login-btn"]')


        text = page.locator('p[class="super-secret-text"]').text_content()
        print(text)

        # !!!
        # na page.locator(selector) se dá použít funkce .text_content(), která vypíše text daného prvku
        # !!!


        # browser.close()
    

if __name__ == "__main__":
    main()