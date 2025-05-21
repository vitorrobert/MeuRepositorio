# CONEXAO SUPABASE E GERACAO DE GRAFICO #

{
  "nodes": [
    {
      "parameters": {
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "typeVersion": 1.1,
      "position": [
        -340,
        -200
      ],
      "id": "7da68d0f-215f-4ca4-a13d-2171dd06ffe5",
      "name": "When chat message received",
      "webhookId": "2e5f0871-8e93-49f0-a6ee-30ed6acc6182"
    },
    {
      "parameters": {
        "options": {
          "systemMessage": "Você é um analista inteligente que interpreta dados de um grande banco de restaurantes e bares registrados no Brasil.\n\nVocê tem acesso a uma tabela (restaurantes) contendo os seguintes campos por estabelecimento:\n\n* *cnpj\\_inscricao (character varying)* – Número de Inscrição do CNPJ: CNPJ do estabelecimento\n* *nome\\_fantasia (text)* – Nome Fantasia: Nome pelo qual o estabelecimento é conhecido\n* *tipo\\_estabelecimento (text)* – Tipo de Estabelecimento: Indica se é uma matriz ou filial\n* *natureza\\_juridica (text)* – Natureza Jurídica: Tipo jurídico da empresa (ex: Sociedade Ltda, Empresário Individual etc.)\n* *endereco\\_receita (text)* – Endereço Completo Receita Federal: Endereço completo cadastrado na Receita Federal\n* *uf (character(2))* – UF: Unidade Federativa (sigla do estado)\n* *municipio (text)* – Município: Cidade onde o estabelecimento está localizado\n* *data\\_abertura (date)* – Data de Abertura: Data em que a empresa foi aberta\n* *telefone\\_comercial (text)* – Telefone Comercial: Número de telefone principal do estabelecimento\n* *email\\_comercial (text)* – E-mail de contato do estabelecimento\n* *website (text)* – Website: Site ou rede social do estabelecimento, se disponível\n* *numero\\_certificado (character varying)* – Número do Certificado: CNPJ ou número de registro relacionado ao certificado\n* *validade\\_certificado (date)* – Validade do Certificado: Data de validade do certificado digital ou sanitário\n* *idiomas (text)* – Idiomas: Idiomas falados ou atendidos no estabelecimento\n* *tipo (text)* – Tipo: Categoria do estabelecimento (ex: Restaurante, Bar, Cafeteria)\n* *especialidade (text)* – Especialidade: Tipos de culinária ou serviços oferecidos (ex: Brasileira, Italiana, Árabe)\n\n---\n\nSua tarefa é entender a pergunta do usuário e, com base nessa tabela, responder com dados que ajudem na *tomada de decisão sobre negócios gastronômicos no Brasil*.\n\n### Ferramentas disponíveis:\n\n* *Thinker\\_Tool*: Use esta ferramenta para refletir profundamente sobre perguntas complexas antes de responder. Ideal para análises estratégicas, identificação de padrões e inferências inteligentes.\n* *grafico\\_linhas*: Use esta ferramenta para gerar gráficos de linha com dados temporais ou comparativos em série.\n---\n\nReflita estrategicamente sobre questões como:\n\n* *Concentração de estabelecimentos* por cidade ou estado;\n* *Diversidade de especialidades* por região;\n* *Lacunas de mercado* (tipos ou especialidades pouco exploradas);\n* *Idade média dos estabelecimentos* por cidade (para avaliar maturidade de mercado);\n* *Idiomas atendidos* que possam indicar o perfil do público;\n* *Tipos predominantes de negócios* (restaurante, bar, cafeteria) por localidade.\n\nSempre que possível:\n\n* Use as ferramentas de visualização de forma complementar às análises;\n* Apresente *exemplos práticos, **percentuais* ou *listas resumidas*;\n* Entregue uma resposta clara, *objetiva, orientada à **ação* e *baseada em dados*."
        }
      },
      "type": "@n8n/n8n-nodes-langchain.agent",
      "typeVersion": 1.8,
      "position": [
        180,
        -440
      ],
      "id": "8d7b5cb5-0869-45bf-8a5d-c6155b20f44d",
      "name": "AI Agent"
    },
    {
      "parameters": {},
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "typeVersion": 1.3,
      "position": [
        420,
        220
      ],
      "id": "dbd44a99-aec1-499f-a41b-7a8968ed74f1",
      "name": "Simple Memory"
    },
    {
      "parameters": {
        "operation": "executeQuery",
        "query": "{{ $fromAI(\"query\") }}",
        "options": {}
      },
      "type": "n8n-nodes-base.postgresTool",
      "typeVersion": 2.6,
      "position": [
        580,
        220
      ],
      "id": "d9919cd2-cfe1-4480-8464-f8311c75b41c",
      "name": "Postgres",
      "credentials": {
        "postgres": {
          "id": "KOPF3mt6sMlFIICo",
          "name": "supabase"
        }
      }
    },
    {
      "parameters": {
        "description": "Use esta ferramenta para refletir profundamente sobre uma pergunta ou problema. Ela não acessa novas informações nem altera o banco de dados, mas registra o raciocínio realizado para referência futura. Ideal para análises complexas, inferências contextuais ou quando é necessário manter uma \"memória\" de pensamento para fundamentar respostas mais inteligentes e estratégicas."
      },
      "type": "@n8n/n8n-nodes-langchain.toolThink",
      "typeVersion": 1,
      "position": [
        880,
        -340
      ],
      "id": "c958749e-184a-4978-9b26-2ef06aa5e6bb",
      "name": "Think"
    },
    {
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini"
        },
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "typeVersion": 1.2,
      "position": [
        220,
        -220
      ],
      "id": "db3c0ab5-6c55-46d6-8670-3043ab60229e",
      "name": "OpenAI Chat Model",
      "credentials": {
        "openAiApi": {
          "id": "BYV0Lv4e5HP9qUbr",
          "name": "OpenAi account"
        }
      }
    },
    {
      "parameters": {
        "toolDescription": "Use quando precisar usar graficos",
        "chartType": "line",
        "data": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Data', ``, 'json') }}",
        "output": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('Put_Output_In_Field', ``, 'string') }}",
        "chartOptions": {},
        "datasetOptions": {}
      },
      "type": "n8n-nodes-base.quickChartTool",
      "typeVersion": 1,
      "position": [
        560,
        -200
      ],
      "id": "d8713c81-80c1-4f30-a053-85ed429370ac",
      "name": "QuickChart"
    }
  ],
  "connections": {
    "When chat message received": {
      "main": [
        [
          {
            "node": "AI Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Simple Memory": {
      "ai_memory": [
        [
          {
            "node": "AI Agent",
            "type": "ai_memory",
            "index": 0
          }
        ]
      ]
    },
    "Postgres": {
      "ai_tool": [
        [
          {
            "node": "AI Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Think": {
      "ai_tool": [
        [
          {
            "node": "AI Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "AI Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "QuickChart": {
      "ai_tool": [
        [
          {
            "node": "AI Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    }
  },
  "pinData": {},
  "meta": {
    "templateCredsSetupCompleted": true,
    "instanceId": "33738330930e3881dd5571eca013f36ddf8aab20e4ea5c1f2ebaf4a2b4668ac6"
  }
}