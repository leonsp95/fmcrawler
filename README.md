# FMCrawler

<div align="center">
   <img alt="License: MIT" src="https://img.shields.io/github/license/leonsp95/fmcrawler.svg" />
   <br/>
   <img alt="Made with Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />

</div>

Crawler para recuperar filmes das suas listas do Filmow e gerar um arquivo CSV contendo *nome*, *ano* *de lançamento* e *link* do IMDb.

## Índice

- [FMCrawler](#fmcrawler)
  * [Instalação](#instalação)
    + [Linux](#linux)
    + [Windows](#windows)
  * [Uso](#uso)
    + [Como o programa funciona](#como-o-programa-funciona)
    + [Utilizando o programa](#utilizando-o-programa)
  * [Pontos a se considerar](#pontos-a-se-considerar)

------

## Instalação



### Linux

1. Extraia o arquivo fmcrawler.tar.gz para um diretório de sua preferência

2. Acesse o diretório pelo terminal

   ```
   $ cd fmcrawler
   ```

   

3. Execute a aplicação

   ```
   $ ./fmcrawler
   ```

   

### Windows

Execute o instalador do FMCrawler e aguarde até o fim da instalação. Execute a aplicação dando duplo clique no atalho que aparecerá na sua Área de Trabalho



------



## Uso



### Como o programa funciona

O programa é dividido em basicamente três processos:

1. Recuperação de dados básicos (nome do usuário, mídia e categoria da mídia)

2. Análise das listas de filmes/séries/curtas

3. Geração de lista de mídia em um arquivo CSV 




### Utilizando o programa

1. Após iniciado o programa, digite o seu nome de usuário, escolha a mídia e a categoria que deseja extrair

   <details>
   <summary>Abrir</summary>
   
   ![Tela inicial](https://i.imgur.com/LZcx12w.png)
   ![Seleção de mídia](https://i.imgur.com/GaJyvQJ.png)
   ![Seleção de categoria](https://i.imgur.com/3voqllr.png)
   </details>

2. O programa agora fará a análise das listas

   <details>
   <summary>Abrir</summary>
   
      ![Análise das listas](https://i.imgur.com/nMPXp8y.png)
   </details>

3. Se tudo ocorreu bem, a tela a seguir aparecerá noticiando que a lista CSV foi gerada com sucesso no diretório principal do usuário (em ambientes Windows, `C:\Users\SeuNome` e, em ambientes Linux, `/home/SeuNome` )

   <details>
   <summary>Abrir</summary>
   
      ![Processo finalizado com sucesso](https://i.imgur.com/nTUENGG.png)
   </details>

------

## Pontos a se considerar



1.  O programa depende dos dados fo Filmow para verificação e depois pesquisa através de uma API. Tenha em mente que há filmes cujos ano de lançamento podem estar equivocados. Também há títulos que podem não ser reconhecidos durante a busca pela API (especialmente se não estiver indicado o nome em inglês ou original). Consequentemente esses filmes não serão encontrados.

2.  Pode ocorrer algum erro no arquivo CSV a depender do software utilizado para abri-lo, considerando que o padrão inglês do CSV utiliza a vírgula (,) para separar as colunas, e o padrão português, ponto-e-vírgula (;). Verifique no seu software editor de planilhas.





