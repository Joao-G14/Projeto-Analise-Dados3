Dashboard de Gestão de RH com Python e Power BI
<img width="1426" height="802" alt="Captura de tela 2026-05-07 160835" src="https://github.com/user-attachments/assets/c6c6bd81-2b32-4623-90e8-1973f2fd0210" />

Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de realizar a análise de dados de capital humano utilizando Python para tratamento dos dados e Power BI para visualização das informações
A proposta do projeto é transformar registros administrativos de funcionários em indicadores estratégicos que auxiliam na gestão de pessoas e no controle de custos operacionais

Tecnologias Utilizadas

Python
Pandas
Numpy
Power BI

Estrutura do Projeto

BaseFuncionarios.xlsx → Base de dados com informações cadastrais e salariais
analise_rh.py → Script Python responsável pelo tratamento e cálculos de RH
Dashboard_RH.pbix → Dashboard desenvolvido no Power BI

Tratamento de Dados com Python

O tratamento dos dados foi realizado utilizando Pandas e Numpy
O script realiza:
Leitura da base de dados de funcionários
Limpeza de valores ausentes em salários e avaliações
Conversão de colunas de contratação para análise temporal
Cálculo de custos totais de folha de pagamento
Cálculo de médias de desempenho por setor
Agrupamentos por área cargo e gênero
Geração de tabelas agregadas para o Power BI

Indicadores Desenvolvidos

O projeto realiza o cálculo dos seguintes indicadores:
Total de colaboradores ativos
Custo total de salários mensal
Média de avaliação de desempenho
Total de horas extras acumuladas
Quantidade de funcionários por área
Média salarial por nível hierárquico
Proporção de gênero no quadro de funcionários

Com base na sua solicitação, atualizei o README para incluir a menção à Página 2 no Dashboard de Gestão de RH, mantendo o estilo padronizado, sem emojis e sem pontos.

Dashboard de Gestão de RH com Python e Power BI
Sobre o Projeto
Este projeto foi desenvolvido com o objetivo de realizar a análise de dados de capital humano utilizando Python para tratamento dos dados e Power BI para visualização das informações
A proposta do projeto é transformar registros administrativos de funcionários em indicadores estratégicos que auxiliam na gestão de pessoas e no controle de custos operacionais

Tecnologias Utilizadas
Python
Pandas
Numpy
Power BI

Estrutura do Projeto
BaseFuncionarios.xlsx → Base de dados com informações cadastrais e salariais
analise_rh.py → Script Python responsável pelo tratamento e cálculos de RH
Dashboard_RH.pbix → Dashboard desenvolvido no Power BI com navegação entre páginas

Tratamento de Dados com Python
O tratamento dos dados foi realizado utilizando Pandas e Numpy
O script realiza:
Leitura da base de dados de funcionários
Limpeza de valores ausentes em salários e avaliações
Conversão de colunas de contratação para análise temporal
Cálculo de custos totais de folha de pagamento
Cálculo de médias de desempenho por setor
Agrupamentos por área cargo e gênero
Geração de tabelas agregadas para o Power BI

Indicadores Desenvolvidos
O projeto realiza o cálculo dos seguintes indicadores:
Total de colaboradores ativos
Custo total de salários mensal
Média de avaliação de desempenho
Total de horas extras acumuladas
Quantidade de funcionários por área
Média salarial por nível hierárquico
Proporção de gênero no quadro de funcionários

Dashboard no Power BI
O dashboard foi desenvolvido para apresentar os principais indicadores de RH de forma visual e interativa dividindo as análises em duas visões principais

Página 1: Visão Geral e Custos

Cards com headcount total e custo de folha
Gráfico de barras de funcionários por área
Gráfico de pizza com distribuição por gênero
Gráfico de colunas com média salarial por cargo

Página 2: Desempenho e Detalhamento
<img width="1423" height="794" alt="Captura de tela 2026-05-07 161453" src="https://github.com/user-attachments/assets/cfaaaad6-5bd4-430c-a91f-c0ab031b0a68" />

Análise detalhada de avaliações por departamento
Cruzamento de horas extras por cargo
Matriz de desempenho dos colaboradores
Visão analítica da evolução de contratações

Filtros Interativos

O dashboard possui filtros por:
Cidade
Área
Cargo
Ao selecionar uma cidade ou área específica todos os gráficos e indicadores são atualizados automaticamente permitindo analisar a demografia e os custos de cada unidade da empresa nas duas páginas do relatório

Objetivo do Projeto

O projeto foi desenvolvido para prática de:
Análise de dados de recursos humanos
Tratamento de dados administrativos com Python
Desenvolvimento de KPIs de gestão de pessoas
Visualização de dados de performance
Criação de dashboards de People Analytics no Power BI com múltiplas visões

Autor:

João Gabriel Amaral
