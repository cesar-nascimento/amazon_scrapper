# Web Scrapper Simples

## Instalação: 

1. Clonar o repositório:
    * `git clone https://github.com/cesar-nascimento/amazon_scrapper.git`
1. Instalar "requirements.txt":
    * `pip install -r requirements.txt`

## Utilização
Para buscar outros produtos é necessário mudar o valor da variável "query".

Para buscar na Amazon.com em vez da Amazon.com.br basta remover o par chave/valor
`'__mk_pt_BR': '%C3%85M%C3%85%C5%BD%C3%95%C3%91',` dentro da função get_data.

Após finalizar a busca, a lista de produtos será salva dentro de um arquivo
chamado `products_data.xlsx`, dentro da própria pasta onde o script foi executado. 
