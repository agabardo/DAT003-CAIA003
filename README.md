# DAT003-CAIA003
## Data Mining & Knowledge Discovery
### (Mineração Grafos)

Atualizado em: 31 de agosto de 2024

# Projeto de Análise de Redes Complexas

Este repositório contém diversos scripts e arquivos relacionados à análise de redes complexas, incluindo métodos para detecção de comunidades, clustering, e visualização de grafos.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```
.
├── Source.gv
├── Source.gv.pdf
├── __pycache__
├── arquivos.txt
├── datasets_comuns
│   ├── Rhesus
│   ├── dolphins
│   ├── jazz
│   ├── polbooks
│   ├── StarWars-social-network-master
│   ├── football
│   └── karate
├── girvan-newman
│   ├── Source.gv
│   ├── karate_club_label_propagation.graphml
│   ├── louvain_colored.dot
│   ├── Source.gv.pdf
│   ├── karate_club_louvain.graphml
│   ├── readme.md
│   ├── girvan_newman.py
│   ├── louvain.py
│   └── visualizar.py
├── k-means
│   ├── k-means.py
│   ├── karate.dot
│   ├── readme.md
│   └── visualizar.py
├── spotify.dot
├── pygraphviz.py
├── graph_tool.py
└── requerimentos.txt
```

## Configuração do Ambiente

Para configurar o ambiente de desenvolvimento, siga os passos abaixo:

### 1. Criar um Ambiente Virtual

1. Navegue até o diretório do projeto.

   ```bash
   cd /caminho/para/seu/projeto
   ```

2. Crie um ambiente virtual.

   ```bash
   python -m venv venv
   ```

   Isso criará um diretório chamado `venv` contendo o ambiente virtual.

### 2. Ativar o Ambiente Virtual

- No Windows:

  ```bash
  venv\Scripts\activate
  ```

- No macOS e Linux:

  ```bash
  source venv/bin/activate
  ```

### 3. Instalar Dependências

Com o ambiente virtual ativado, instale as dependências necessárias listadas no arquivo `requerimentos.txt`.

```bash
pip install -r requerimentos.txt
```

## Estrutura dos Diretórios

- **datasets_comuns/**: Contém conjuntos de dados comuns para análise de redes.
- **girvan-newman/**: Scripts e arquivos relacionados à detecção de comunidades usando o algoritmo de Girvan-Newman e outras abordagens.
- **k-means/**: Scripts e arquivos para análise de clustering usando o algoritmo k-means.
- **spotify.dot**: Arquivo DOT utilizado em slides de explicações.
- **pygraphviz.py**: Script para visualizar o arquivo `spotify.dot`.
- **graph_tool.py**: Gera um grafo utilizando a biblioteca `Graph` com o modelo de Barabási-Albert.

## Uso dos Scripts

- **girvan-newman/**: Scripts para visualização e análise de comunidades com Girvan-Newman e outros métodos. Execute `girvan_newman.py`, `louvain.py`, ou `visualizar.py` conforme necessário.

- **k-means/**: Scripts para clustering. Execute `k-means.py` ou `visualizar.py` para análise e visualização.

- **pygraphviz.py**: Utilizado para visualizar o grafo definido em `spotify.dot`.

- **graph_tool.py**: Gera e visualiza um grafo com o modelo Barabási-Albert.

## Arquivos Adicionais

- **Source.gv** e **Source.gv.pdf**: Arquivos de exemplo para visualização e análise.
- **arquivos.txt**: Lista de arquivos ou informações adicionais.

Se você tiver alguma dúvida ou problema, sinta-se à vontade para abrir uma issue no repositório ou entrar em contato.