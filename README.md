



# 🤖 Automação de Cadastro de Produtos com Python e PyAutoGUI

Este projeto automatiza o processo de cadastro de produtos em um sistema web utilizando **Python** e a biblioteca **PyAutoGUI**. O script simula ações humanas, como abrir o navegador, preencher formulários e interagir com a interface gráfica do sistema.

---

## 🧰 Tecnologias Utilizadas

- Python 3  
- PyAutoGUI (automação de mouse e teclado)  
- Pandas (leitura de arquivos CSV)  
- Time (controle de pausas no script)

---

## ⚙️ Como o Código Funciona

1. **Importação das bibliotecas:**  
   - `pyautogui` para controlar mouse e teclado  
   - `time` para pausas entre comandos  
   - `pandas` para ler os dados dos produtos a partir de um arquivo CSV

2. **Configuração de pausa entre comandos:**  
   Define um intervalo de 0.5 segundos entre cada comando do PyAutoGUI para evitar execuções muito rápidas que possam falhar.

3. **Abrir o navegador e acessar o sistema:**  
   - Abre o menu Iniciar do Windows  
   - Digita e abre o navegador Google Chrome  
   - Acessa a URL do sistema web da empresa  
   - Aguarda o carregamento da página

4. **Realizar login no sistema:**  
   - Clica no campo de e-mail  
   - Digita o e-mail de login  
   - Pressiona TAB e Enter para fazer o login  
   - Aguarda a próxima página carregar

5. **Ler a planilha de produtos:**  
   - Lê o arquivo `produtos.csv` que contém os dados dos produtos a serem cadastrados  
   - Exibe a tabela no terminal para conferência

6. **Cadastrar os produtos automaticamente:**  
   Para cada produto na tabela:  
   - Clica no botão “Novo Produto”  
   - Preenche os campos (código, marca, tipo, categoria, preço unitário, custo, observações)  
   - Pressiona Enter para enviar o cadastro  
   - Dá scroll para manter o botão visível para o próximo cadastro

---

## 📋 Como Executar

1. Certifique-se de ter Python 3 instalado.  
2. Instale as dependências:  

   pip install pyautogui pandas

   ## 📋 Execute o Script
   
   python seu_script.py

   O programa abrirá o navegador, fará login e começará a cadastrar os produtos automaticamente.

