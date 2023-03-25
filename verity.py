from playwright.sync_api import Playwright, sync_playwright
import time


def verify_cultura_e_tech():
    print("Caso de teste 01 - Cenario 01 - verificar se o elemento 'Cultura e Tech' esta presente")
    try:
        assert page.is_visible("text=Culture e Tech")
        print("APROVADO - Elemento'Cultara e Tech' - localizado")
    except AssertionError:
        print("REAPROVADO - Elemento'Cultara e Tech' - não localizado")


def verify_nossas_solucoes():
    print("Caso de teste 01 - Cenario 02 - verificar se o elemento 'Nossas soluções_' esta presente")
    try:
        assert page.is_visible("text=Nossas soluções_")
        print("APROVADO - Elemento 'Nossas soluções_ - localizado")
    except AssertionError:
        print("REAPROVADO - Elemento'Cultara e Tech' - não localizado")


def contact_form():
    print("Caso de Teste 02 - Enviando Formulado de contato")
    page.click("text=Contato")
    print("Clicando no link 'Contato'")
    print("Preencher nome 'Álvaro QA")
    page.get_by_label("Nome").type("Álvaro QA")
    time.sleep(1)
    print("Preencher email 'alvaro.bapt@teste.com'")
    page.get_by_label("Email").type("alvaro.bapt@test.com")
    time.sleep(2)
    print("Preencher celular '11982082001'")
    page.get_by_label("Telefone / Celular").type("11982082001")
    time.sleep(1)
    print("Preencher meu desafio 'Meu desafio é ser um QA melhor a cada dia!'")
    page.locator("#textarea_comp-kwz6tqfr").type("Meu desafio é ser um QA melhor a cada dia!")
    time.sleep(2)
    print("Check o checkbox'")
    page.get_by_test_id("checkbox").check()
    time.sleep(1)
    print("Clicando em enviar")
    page.get_by_test_id("buttonElement").click()
    time.sleep(1)


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://verity.com.br")
    print("Acessando a pagina 'https://verity.com.br")

    # Teste Cenário 1: validar títulos
    verify_cultura_e_tech()
    verify_nossas_solucoes()

    # Teste Cenário 2: preencher formulário de contato
    contact_form()

