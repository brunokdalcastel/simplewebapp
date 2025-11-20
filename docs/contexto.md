# Contexto do Projeto: Simple Web App

Este arquivo serve como um resumo do estado atual do projeto para referência futura.

## Visão Geral

O projeto consiste em uma aplicação web simples desenvolvida em Python com o framework Flask. A aplicação foi containerizada usando Docker e orquestrada com Docker Compose.

## Estrutura de Arquivos

- `app.py`: O código-fonte da aplicação Flask. Ele define uma única rota que retorna "Hello, World!".
- `requirements.txt`: Lista as dependências Python do projeto (atualmente, apenas `Flask`).
- `Dockerfile`: Define as instruções para construir a imagem Docker da aplicação.
- `docker-compose.yml`: Define o serviço da aplicação para ser executado com `docker-compose`.

## Estado Atual

1.  **Aplicação**: A aplicação Flask está funcional.
2.  **Docker**: A imagem Docker e a configuração do Docker Compose estão prontas.
3.  **Git/GitHub**: O código foi versionado com Git e enviado para um repositório no GitHub.
4.  **CI/CD**: Uma pipeline de CI/CD foi criada com GitHub Actions e agora está funcional, incluindo testes automatizados e verificação de estilo (Linting).
5.  **Testes Automatizados**: Foi criado um arquivo de teste inicial (`tests/test_app.py`) para a aplicação.
6.  **Segurança e Produção**: A aplicação agora roda com servidor Gunicorn e usuário não-root no Docker.
7.  **Ambiente Local e Health Check**: O ambiente de desenvolvimento local foi configurado com um ambiente virtual (`venv`) para isolar dependências. Um endpoint de health check (`/health`) foi adicionado à aplicação, junto com seu teste correspondente.

## Próximos Passos

- **Fase 1 (Observabilidade)**: Adicionar logs estruturados e métricas (Prometheus/Grafana).
- **Fase 2 (IaC)**: Migrar infraestrutura para código com Terraform.
- **Fase 3 (Orquestração)**: Preparar aplicação para Kubernetes.
- **Fase 4 (Cloud)**: Deploy em provedor de nuvem (AWS/Azure).

## Metodologia de Trabalho (GitHub Flow)

Para simular um ambiente profissional e demonstrar senioridade, adotaremos o seguinte fluxo para novas features:

1.  **Branch**: Criar uma branch específica (`git checkout -b feat/nome-da-feature`).
2.  **Commit**: Realizar alterações e commits pequenos.
3.  **Push**: Enviar a branch para o remoto (`git push origin feat/nome-da-feature`).
4.  **Pull Request (PR)**: Abrir um PR no GitHub para merge na `master`.
5.  **CI Check**: Aguardar a aprovação da pipeline de testes.
6.  **Merge**: Realizar o merge apenas se a pipeline estiver verde.
