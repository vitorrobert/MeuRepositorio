# TESTANDO FORMULÁRIO E CONEXÃO GOOGLE API - SHEETS  #

{
  "nodes": [
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "82c5a404-d0fa-4be5-9d60-5fce82c7fb2f",
              "name": "base64",
              "value": "={{ $json.base64 }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        1920,
        1560
      ],
      "id": "51522d19-155d-4c42-beb0-774a5758c215",
      "name": "GetBase64"
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://api.groq.com/openai/v1/chat/completions",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "groqApi",
        "sendBody": true,
        "specifyBody": "json",
        "jsonBody": "={\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": [\n        {\n          \"type\": \"text\",\n          \"text\": \"What plate is in the image?\"\n        },\n        {\n          \"type\": \"image_url\",\n          \"image_url\": {\n              \"url\": \"data:image/jpeg;base64,{{$('GetBase64').item.json.base64}}\"\n          }\n        }\n      ]\n    }\n  ],\n  \"model\": \"meta-llama/llama-4-scout-17b-16e-instruct\",\n  \"temperature\": 1,\n  \"max_completion_tokens\": 1024,\n  \"top_p\": 1,\n  \"stream\": false,\n  \"stop\": null\n}",
        "options": {}
      },
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [
        2200,
        1540
      ],
      "id": "34a1bda6-2af5-4ba4-8d05-638837cba971",
      "name": "Groq LLama4",
      "credentials": {
        "groqApi": {
          "id": "91bVrtrOR3qmKfKN",
          "name": "Groq account"
        }
      }
    },
    {
      "parameters": {
        "url": "https://img.cdndsgni.com/preview/10172338.jpg",
        "options": {}
      },
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [
        500,
        1580
      ],
      "id": "11a481b8-1201-4349-b441-c08c33e9d1e1",
      "name": "HTTP Request"
    },
    {
      "parameters": {
        "operation": "binaryToPropery",
        "binaryPropertyName": "FOTO_DA_PLACA",
        "destinationKey": "base64",
        "options": {}
      },
      "type": "n8n-nodes-base.extractFromFile",
      "typeVersion": 1,
      "position": [
        600,
        900
      ],
      "id": "698a51e1-23ab-45a7-a9b2-6d0b4cca4612",
      "name": "Extract from File"
    },
    {
      "parameters": {
        "formTitle": "Registro de Veiculos",
        "formDescription": "Registro de Placas",
        "formFields": {
          "values": [
            {
              "fieldLabel": "Envie uma imagem da placa",
              "fieldType": "file",
              "requiredField": true
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.formTrigger",
      "typeVersion": 2.2,
      "position": [
        -180,
        1000
      ],
      "id": "65144691-7423-44b6-ba91-31eb9b10f6cb",
      "name": "On form submission",
      "webhookId": "f6b4a531-f5b4-4f6d-a524-cfe781f8bcee",
      "disabled": true
    },
    {
      "parameters": {
        "pollTimes": {
          "item": [
            {
              "mode": "custom"
            }
          ]
        },
        "documentId": {
          "__rl": true,
          "value": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
          "mode": "list",
          "cachedResultName": "Controle  de Estacionamento",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 1761021973,
          "mode": "list",
          "cachedResultName": "Respostas ao formulário 1",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit#gid=1761021973"
        },
        "event": "rowAdded",
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheetsTrigger",
      "typeVersion": 1,
      "position": [
        680,
        2220
      ],
      "id": "8e44d73e-c491-4755-8285-a59f60c7ec36",
      "name": "Google Sheets Trigger",
      "credentials": {
        "googleSheetsTriggerOAuth2Api": {
          "id": "hrhM9gHkETeEPg33",
          "name": "Google Sheets Trigger account"
        }
      },
      "disabled": true
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict",
            "version": 2
          },
          "conditions": [
            {
              "id": "2e17071c-78f6-434e-ae8b-2aea9ed8019c",
              "leftValue": "={{ $json.Registrado }}",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "empty",
                "singleValue": true
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        3940,
        -1060
      ],
      "id": "48bed887-b104-4a93-b8e1-913f7901689c",
      "name": "If"
    },
    {
      "parameters": {
        "authentication": "oAuth2",
        "operation": "update",
        "sheetId": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
        "range": "='Mapa - Cacamba'",
        "dataStartRow": "=2",
        "keyRow": "=1",
        "key": "=",
        "options": {}
      },
      "name": "Read sheet1",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        4180,
        -1380
      ],
      "typeVersion": 1,
      "id": "19cecdbf-d331-458a-aa13-3a5534e04b70",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "0x9DM57RnZheyKnl",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "operation": "appendOrUpdate",
        "documentId": {
          "__rl": true,
          "value": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
          "mode": "list",
          "cachedResultName": "Controle  de Estacionamento",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 83682236,
          "mode": "list",
          "cachedResultName": "Mapa - Cacamba",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit#gid=83682236"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "FILA": "2",
            "VEICULO": "AAA-3456"
          },
          "matchingColumns": [
            "FILA"
          ],
          "schema": [
            {
              "id": "FILA",
              "displayName": "FILA",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "VEICULO",
              "displayName": "VEICULO",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [
        4280,
        -1080
      ],
      "id": "4eee106c-5ac2-4f60-9375-548dd57e26dd",
      "name": "Google Sheets2",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "0x9DM57RnZheyKnl",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "operation": "update",
        "documentId": {
          "__rl": true,
          "value": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
          "mode": "list",
          "cachedResultName": "Controle  de Estacionamento",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 83682236,
          "mode": "list",
          "cachedResultName": "Mapa - Caçamba",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit#gid=83682236"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "Fila": "={{ $json.Fila }}",
            "Vaga 1": "={{ $('Switch').item.json['Placa '] }}"
          },
          "matchingColumns": [
            "Fila"
          ],
          "schema": [
            {
              "id": "Fila",
              "displayName": "Fila",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Vaga 1",
              "displayName": "Vaga 1",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Vaga 2",
              "displayName": "Vaga 2",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Vaga 3",
              "displayName": "Vaga 3",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Vaga 4",
              "displayName": "Vaga 4",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Vaga 5",
              "displayName": "Vaga 5",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "row_number",
              "displayName": "row_number",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "readOnly": true,
              "removed": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [
        2700,
        -460
      ],
      "id": "371de505-e4eb-4c25-b95a-d2d8762a6c6d",
      "name": "Google Sheets3",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "0x9DM57RnZheyKnl",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "operation": "update",
        "documentId": {
          "__rl": true,
          "value": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
          "mode": "list",
          "cachedResultName": "Controle  de Estacionamento",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 83682236,
          "mode": "list",
          "cachedResultName": "Mapa - Cacamba",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit#gid=83682236"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "FILA": "={{ $json['Fila '] }}",
            "VEICULO": "={{ $json['Placa '] }}"
          },
          "matchingColumns": [
            "FILA"
          ],
          "schema": [
            {
              "id": "FILA",
              "displayName": "FILA",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "VEICULO",
              "displayName": "VEICULO",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "row_number",
              "displayName": "row_number",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "readOnly": true,
              "removed": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [
        820,
        1760
      ],
      "id": "19c09096-33f1-4659-862d-d32da25567a6",
      "name": "Google Sheets5",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "0x9DM57RnZheyKnl",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict",
            "version": 2
          },
          "conditions": [
            {
              "id": "6ec71727-0709-4c11-be24-dfb0bc996214",
              "leftValue": "={{ $json['VAGA 1'] }}  ",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "notEmpty",
                "singleValue": true
              }
            },
            {
              "id": "32ed90d7-6d1f-4b38-a771-69f6a2062d1c",
              "leftValue": "={{ $json['VAGA 2'] }}",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "notEmpty",
                "singleValue": true
              }
            },
            {
              "id": "f0a8b266-10b3-4319-98db-bc6af9b27f5d",
              "leftValue": "={{ $json['VAGA 3'] }}",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "notEmpty",
                "singleValue": true
              }
            },
            {
              "id": "9e18c0f5-9805-4ffe-99de-e13b3cab4d28",
              "leftValue": "={{ $json['VAGA 4'] }}",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "notEmpty",
                "singleValue": true
              }
            }
          ],
          "combinator": "or"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        1760,
        -420
      ],
      "id": "44753835-8b50-4d81-bf10-a134dc845d74",
      "name": "VAGAS DISPONIVEIS NA FILA"
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict",
            "version": 2
          },
          "conditions": [
            {
              "id": "94e5dc4d-9512-4ac1-9a78-1d44aa54de50",
              "leftValue": "={{ $json['VAGA 1'] }}",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "empty",
                "singleValue": true
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        2280,
        -440
      ],
      "id": "47998143-b14c-491c-be68-be1183452ecb",
      "name": "VAGA 1"
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict",
            "version": 2
          },
          "conditions": [
            {
              "id": "fea16305-a4f7-4058-978f-f7897ed17c16",
              "leftValue": "={{ $json['VAGA 2'] }}",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "empty",
                "singleValue": true
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        2600,
        -120
      ],
      "id": "a6efa2fd-4f5e-49da-8fa0-bf6f2e63652f",
      "name": "VAGA 2"
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict",
            "version": 2
          },
          "conditions": [
            {
              "id": "5fbcdb71-03dd-41e3-a9b7-8530f02bfd66",
              "leftValue": "={{ $json['VAGA 3'] }}",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "empty",
                "singleValue": true
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        2920,
        200
      ],
      "id": "c55c5558-a68e-4cfa-bdb1-f412c63a9138",
      "name": "VAGA 3"
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict",
            "version": 2
          },
          "conditions": [
            {
              "id": "45955bd6-3d9f-4019-acd7-ae489b33ce9c",
              "leftValue": "={{ $json['VAGA 4'] }}",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "empty",
                "singleValue": true
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        3200,
        560
      ],
      "id": "64be5285-a075-4187-9601-27594f2c1ad1",
      "name": "VAGA 4"
    },
    {
      "parameters": {
        "formTitle": "REGISTROS DE VEICULOS",
        "formDescription": "INSIRA OS DADOS DO VEICULO",
        "formFields": {
          "values": [
            {
              "fieldLabel": "PLACA",
              "placeholder": "INSIRA A PLACA",
              "requiredField": true
            },
            {
              "fieldLabel": "FILA",
              "fieldType": "number",
              "placeholder": "INSIRA O NUMERO DA FILA",
              "requiredField": true
            },
            {
              "fieldLabel": "TIPO",
              "fieldType": "dropdown",
              "fieldOptions": {
                "values": [
                  {
                    "option": "CAÇAMBA"
                  },
                  {
                    "option": "GRANELEIRO"
                  }
                ]
              }
            }
          ]
        },
        "responseMode": "lastNode",
        "options": {
          "appendAttribution": false,
          "respondWithOptions": {
            "values": {
              "respondWith": "redirect",
              "redirectUrl": "https://webhook.vitor.autom.my/form/1e553ec3-b844-40fe-bb77-d1b47d43c174"
            }
          }
        }
      },
      "type": "n8n-nodes-base.formTrigger",
      "typeVersion": 2.2,
      "position": [
        300,
        -300
      ],
      "id": "79d1f426-9127-43a0-8d7a-081a279289a8",
      "name": "On form submission1",
      "webhookId": "1e553ec3-b844-40fe-bb77-d1b47d43c174"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "4d4fc779-afa1-4478-adc2-b3ebe753eb8d",
              "name": "PLACA",
              "value": "={{ $json.PLACA }}",
              "type": "string"
            },
            {
              "id": "fdb3301b-04fa-44dd-885b-3ee481a70dc1",
              "name": "FILA",
              "value": "={{ $('On form submission1').item.json.FILA }}",
              "type": "number"
            },
            {
              "id": "ce2b5666-ff1c-4658-9885-234885dc99c2",
              "name": "submittedAt",
              "value": "={{ $('On form submission1').item.json.submittedAt }}",
              "type": "string"
            },
            {
              "id": "66e06d4c-cfe7-4f73-b95f-c622f6d10b99",
              "name": "TIPO",
              "value": "={{ $('On form submission1').item.json.TIPO }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        740,
        -420
      ],
      "id": "f48da614-7416-46a5-9848-88fd01cd66ac",
      "name": "Edit Fields"
    },
    {
      "parameters": {
        "operation": "update",
        "documentId": {
          "__rl": true,
          "value": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
          "mode": "list",
          "cachedResultName": "Controle  de Estacionamento",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 83682236,
          "mode": "list",
          "cachedResultName": "Mapa - Caçamba",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit#gid=83682236"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {},
          "matchingColumns": [
            "Fila"
          ],
          "schema": [
            {
              "id": "Fila",
              "displayName": "Fila",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Vaga 1",
              "displayName": "Vaga 1",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Vaga 2",
              "displayName": "Vaga 2",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Vaga 3",
              "displayName": "Vaga 3",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Vaga 4",
              "displayName": "Vaga 4",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Vaga 5",
              "displayName": "Vaga 5",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "row_number",
              "displayName": "row_number",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "readOnly": true,
              "removed": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [
        2920,
        -120
      ],
      "id": "7bf9eb5c-6700-4cb4-bf0a-2e411bcfc173",
      "name": "Google Sheets10",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "0x9DM57RnZheyKnl",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "operation": "update",
        "documentId": {
          "__rl": true,
          "value": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
          "mode": "list",
          "cachedResultName": "Controle  de Estacionamento",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 1761021973,
          "mode": "list",
          "cachedResultName": "Respostas ao formulário 1",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit#gid=1761021973"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "Carimbo de data/hora": "={{ $('Edit Fields').item.json.submittedAt }}",
            "Registrado": "INSERIDO NO MAPA"
          },
          "matchingColumns": [
            "Carimbo de data/hora"
          ],
          "schema": [
            {
              "id": "Carimbo de data/hora",
              "displayName": "Carimbo de data/hora",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Fila",
              "displayName": "Fila",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Tipo de Veículo ",
              "displayName": "Tipo de Veículo ",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Placa ",
              "displayName": "Placa ",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Registrado",
              "displayName": "Registrado",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "row_number",
              "displayName": "row_number",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "readOnly": true,
              "removed": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [
        3080,
        -480
      ],
      "id": "28269b5b-475a-4502-b29a-be00d83570fd",
      "name": "Google Sheets11",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "0x9DM57RnZheyKnl",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "operation": "append",
        "documentId": {
          "__rl": true,
          "value": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
          "mode": "list",
          "cachedResultName": "Controle  de Estacionamento",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 1761021973,
          "mode": "list",
          "cachedResultName": "Respostas ao formulário 1",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit#gid=1761021973"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "Carimbo de data/hora": "={{ $json.submittedAt }}",
            "Placa ": "={{ $json.PLACA }}",
            "Tipo de Veículo ": "={{ $('On form submission1').item.json.TIPO }}",
            "Fila ": "={{ $('On form submission1').item.json.FILA }}"
          },
          "matchingColumns": [],
          "schema": [
            {
              "id": "Carimbo de data/hora",
              "displayName": "Carimbo de data/hora",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Fila ",
              "displayName": "Fila ",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Tipo de Veículo ",
              "displayName": "Tipo de Veículo ",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Placa ",
              "displayName": "Placa ",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Registrado",
              "displayName": "Registrado",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [
        960,
        -420
      ],
      "id": "7665d999-a04f-4dcc-86c2-ee9fa7addb46",
      "name": "ADICIONAR A PLANILHA",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "0x9DM57RnZheyKnl",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json['Tipo de Veículo '] }}",
                    "rightValue": "CAÇAMBA",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    },
                    "id": "c5661c37-4d39-4045-8a3c-c6cca37d909f"
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "CAÇAMBA"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "a6aa5612-f0f0-47bb-af5a-cd609b503fb3",
                    "leftValue": "={{ $json['Tipo de Veículo '] }}",
                    "rightValue": "GRANELEIRO",
                    "operator": {
                      "type": "string",
                      "operation": "equals",
                      "name": "filter.operator.equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "GRANELEIRO"
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [
        1180,
        -420
      ],
      "id": "5af26a82-443a-4ad5-b200-119bf27ee2f1",
      "name": "Switch"
    },
    {
      "parameters": {
        "documentId": {
          "__rl": true,
          "value": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
          "mode": "list",
          "cachedResultName": "Controle  de Estacionamento",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 83682236,
          "mode": "list",
          "cachedResultName": "Mapa - Caçamba",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit#gid=83682236"
        },
        "filtersUI": {
          "values": [
            {
              "lookupColumn": "Fila",
              "lookupValue": "={{ $json['Fila '] }}"
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [
        1460,
        -520
      ],
      "id": "3f836da5-daa2-4809-a12a-75be573bc1e4",
      "name": "Google Sheets",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "0x9DM57RnZheyKnl",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "operation": "update",
        "documentId": {
          "__rl": true,
          "value": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
          "mode": "list",
          "cachedResultName": "Controle  de Estacionamento",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 1761021973,
          "mode": "list",
          "cachedResultName": "Respostas ao formulário 1",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit#gid=1761021973"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "Carimbo de data/hora": "={{ $('Edit Fields').item.json.submittedAt }}",
            "Registrado": "INSERIDO NO MAPA"
          },
          "matchingColumns": [
            "Carimbo de data/hora"
          ],
          "schema": [
            {
              "id": "Carimbo de data/hora",
              "displayName": "Carimbo de data/hora",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Fila",
              "displayName": "Fila",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Tipo de Veículo ",
              "displayName": "Tipo de Veículo ",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Placa ",
              "displayName": "Placa ",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Registrado",
              "displayName": "Registrado",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "row_number",
              "displayName": "row_number",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "readOnly": true,
              "removed": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [
        3320,
        -140
      ],
      "id": "b2507912-5dba-43dc-8c5d-bbb9d3e01b94",
      "name": "Google Sheets12",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "0x9DM57RnZheyKnl",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "operation": "update",
        "documentId": {
          "__rl": true,
          "value": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
          "mode": "list",
          "cachedResultName": "Controle  de Estacionamento",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 83682236,
          "mode": "list",
          "cachedResultName": "Mapa - Cacamba",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit#gid=83682236"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "FILA": "={{ $json.FILA }}",
            "VAGA 3": "={{ $('Edit Fields').item.json.PLACA }}"
          },
          "matchingColumns": [
            "FILA"
          ],
          "schema": [
            {
              "id": "FILA",
              "displayName": "FILA",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "VAGA 1",
              "displayName": "VAGA 1",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "VAGA 2",
              "displayName": "VAGA 2",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "VAGA 3",
              "displayName": "VAGA 3",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "VAGA 4",
              "displayName": "VAGA 4",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "row_number",
              "displayName": "row_number",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "readOnly": true,
              "removed": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [
        3300,
        80
      ],
      "id": "2661ed2c-e28e-4e46-8ae2-b39f5ee5615f",
      "name": "Google Sheets13",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "0x9DM57RnZheyKnl",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "operation": "update",
        "documentId": {
          "__rl": true,
          "value": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
          "mode": "list",
          "cachedResultName": "Controle  de Estacionamento",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 83682236,
          "mode": "list",
          "cachedResultName": "Mapa - Cacamba",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit#gid=83682236"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "FILA": "={{ $json.FILA }}",
            "VAGA 4": "={{ $('Edit Fields').item.json.PLACA }}"
          },
          "matchingColumns": [
            "FILA"
          ],
          "schema": [
            {
              "id": "FILA",
              "displayName": "FILA",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "VAGA 1",
              "displayName": "VAGA 1",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "VAGA 2",
              "displayName": "VAGA 2",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "VAGA 3",
              "displayName": "VAGA 3",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "VAGA 4",
              "displayName": "VAGA 4",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "row_number",
              "displayName": "row_number",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "readOnly": true,
              "removed": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [
        3580,
        540
      ],
      "id": "2e85faee-447d-414e-8e70-f2be11725a5d",
      "name": "Google Sheets14",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "0x9DM57RnZheyKnl",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "operation": "update",
        "documentId": {
          "__rl": true,
          "value": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
          "mode": "list",
          "cachedResultName": "Controle  de Estacionamento",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 1761021973,
          "mode": "list",
          "cachedResultName": "Respostas ao formulário 1",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit#gid=1761021973"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "Carimbo de data/hora": "={{ $('Edit Fields').item.json.submittedAt }}",
            "Registrado": "INSERIDO NO MAPA"
          },
          "matchingColumns": [
            "Carimbo de data/hora"
          ],
          "schema": [
            {
              "id": "Carimbo de data/hora",
              "displayName": "Carimbo de data/hora",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Fila",
              "displayName": "Fila",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Tipo de Veículo ",
              "displayName": "Tipo de Veículo ",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Placa ",
              "displayName": "Placa ",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Registrado",
              "displayName": "Registrado",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "row_number",
              "displayName": "row_number",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "readOnly": true,
              "removed": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [
        3620,
        120
      ],
      "id": "e8c7be1d-7e6d-405f-a9dd-953cbc828532",
      "name": "Google Sheets15",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "0x9DM57RnZheyKnl",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "operation": "update",
        "documentId": {
          "__rl": true,
          "value": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
          "mode": "list",
          "cachedResultName": "Controle  de Estacionamento",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 1761021973,
          "mode": "list",
          "cachedResultName": "Respostas ao formulário 1",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit#gid=1761021973"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "Carimbo de data/hora": "={{ $('Edit Fields').item.json.submittedAt }}",
            "Registrado": "INSERIDO NO MAPA"
          },
          "matchingColumns": [
            "Carimbo de data/hora"
          ],
          "schema": [
            {
              "id": "Carimbo de data/hora",
              "displayName": "Carimbo de data/hora",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Fila",
              "displayName": "Fila",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Tipo de Veículo ",
              "displayName": "Tipo de Veículo ",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Placa ",
              "displayName": "Placa ",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Registrado",
              "displayName": "Registrado",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "row_number",
              "displayName": "row_number",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "readOnly": true,
              "removed": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [
        3820,
        420
      ],
      "id": "2fa0dc5f-4132-43ba-8304-2c0bfda509be",
      "name": "Google Sheets16",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "0x9DM57RnZheyKnl",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "operation": "update",
        "documentId": {
          "__rl": true,
          "value": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
          "mode": "list",
          "cachedResultName": "Controle  de Estacionamento",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 513878803,
          "mode": "list",
          "cachedResultName": "Mapa - Graneleiro",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit#gid=513878803"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "Vaga 1": "={{ $('Switch').item.json['Placa '] }}",
            "Fila ": "={{ $json['Fila '] }}"
          },
          "matchingColumns": [
            "Fila "
          ],
          "schema": [
            {
              "id": "Fila ",
              "displayName": "Fila ",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Vaga 1",
              "displayName": "Vaga 1",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Vaga 2",
              "displayName": "Vaga 2",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Vaga 3",
              "displayName": "Vaga 3",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Vaga 4",
              "displayName": "Vaga 4",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Vaga 5",
              "displayName": "Vaga 5",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Vaga 6",
              "displayName": "Vaga 6",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "row_number",
              "displayName": "row_number",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "readOnly": true,
              "removed": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [
        1800,
        320
      ],
      "id": "269c7da0-1d41-4f1f-a71b-63648bc8a854",
      "name": "Google Sheets4",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "0x9DM57RnZheyKnl",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict",
            "version": 2
          },
          "conditions": [
            {
              "id": "6ec71727-0709-4c11-be24-dfb0bc996214",
              "leftValue": "={{ $json['VAGA 1'] }}  ",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "notEmpty",
                "singleValue": true
              }
            },
            {
              "id": "32ed90d7-6d1f-4b38-a771-69f6a2062d1c",
              "leftValue": "={{ $json['VAGA 2'] }}",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "notEmpty",
                "singleValue": true
              }
            },
            {
              "id": "f0a8b266-10b3-4319-98db-bc6af9b27f5d",
              "leftValue": "={{ $json['VAGA 3'] }}",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "notEmpty",
                "singleValue": true
              }
            },
            {
              "id": "9e18c0f5-9805-4ffe-99de-e13b3cab4d28",
              "leftValue": "={{ $json['VAGA 4'] }}",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "notEmpty",
                "singleValue": true
              }
            }
          ],
          "combinator": "or"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        860,
        360
      ],
      "id": "e07f4b88-46ef-4bf4-ac46-371eedfc02a2",
      "name": "VAGAS DISPONIVEIS NA FILA1"
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict",
            "version": 2
          },
          "conditions": [
            {
              "id": "94e5dc4d-9512-4ac1-9a78-1d44aa54de50",
              "leftValue": "={{ $json['VAGA 1'] }}",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "empty",
                "singleValue": true
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        1380,
        340
      ],
      "id": "60505002-f08e-4967-824f-e5636bfe8e29",
      "name": "VAGA "
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict",
            "version": 2
          },
          "conditions": [
            {
              "id": "fea16305-a4f7-4058-978f-f7897ed17c16",
              "leftValue": "={{ $json['VAGA 2'] }}",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "empty",
                "singleValue": true
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        1700,
        660
      ],
      "id": "215e9358-5ac9-43cc-a188-d104b796ce36",
      "name": "VAGA 5"
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict",
            "version": 2
          },
          "conditions": [
            {
              "id": "5fbcdb71-03dd-41e3-a9b7-8530f02bfd66",
              "leftValue": "={{ $json['VAGA 3'] }}",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "empty",
                "singleValue": true
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        2020,
        980
      ],
      "id": "193bd96f-6f50-4ee2-a206-07904c148723",
      "name": "VAGA 6"
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict",
            "version": 2
          },
          "conditions": [
            {
              "id": "45955bd6-3d9f-4019-acd7-ae489b33ce9c",
              "leftValue": "={{ $json['VAGA 4'] }}",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "empty",
                "singleValue": true
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        2300,
        1340
      ],
      "id": "25a49f90-e454-463c-83a9-47d2a1f46b6f",
      "name": "VAGA 7"
    },
    {
      "parameters": {
        "operation": "update",
        "documentId": {
          "__rl": true,
          "value": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
          "mode": "list",
          "cachedResultName": "Controle  de Estacionamento",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 513878803,
          "mode": "list",
          "cachedResultName": "Mapa - Graneleiro",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit#gid=513878803"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {},
          "matchingColumns": [
            "Fila "
          ],
          "schema": [
            {
              "id": "Fila ",
              "displayName": "Fila ",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Vaga 1",
              "displayName": "Vaga 1",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Vaga 2",
              "displayName": "Vaga 2",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            },
            {
              "id": "Vaga 3",
              "displayName": "Vaga 3",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Vaga 4",
              "displayName": "Vaga 4",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Vaga 5",
              "displayName": "Vaga 5",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Vaga 6",
              "displayName": "Vaga 6",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "row_number",
              "displayName": "row_number",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "readOnly": true,
              "removed": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [
        2020,
        660
      ],
      "id": "39a5faff-bae2-4890-adc1-b43de4212c08",
      "name": "Google Sheets17",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "0x9DM57RnZheyKnl",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "operation": "update",
        "documentId": {
          "__rl": true,
          "value": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
          "mode": "list",
          "cachedResultName": "Controle  de Estacionamento",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 1761021973,
          "mode": "list",
          "cachedResultName": "Respostas ao formulário 1",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit#gid=1761021973"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "Carimbo de data/hora": "={{ $('Edit Fields').item.json.submittedAt }}",
            "Registrado": "INSERIDO NO MAPA"
          },
          "matchingColumns": [
            "Carimbo de data/hora"
          ],
          "schema": [
            {
              "id": "Carimbo de data/hora",
              "displayName": "Carimbo de data/hora",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Fila ",
              "displayName": "Fila ",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Tipo de Veículo ",
              "displayName": "Tipo de Veículo ",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Placa ",
              "displayName": "Placa ",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Registrado",
              "displayName": "Registrado",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "row_number",
              "displayName": "row_number",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "readOnly": true,
              "removed": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [
        2180,
        300
      ],
      "id": "2c494ef2-31c0-44f0-9a1f-0b4cb7dce236",
      "name": "Google Sheets18",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "0x9DM57RnZheyKnl",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "documentId": {
          "__rl": true,
          "value": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
          "mode": "list",
          "cachedResultName": "Controle  de Estacionamento",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 513878803,
          "mode": "list",
          "cachedResultName": "Mapa - Graneleiro",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit#gid=513878803"
        },
        "filtersUI": {
          "values": [
            {
              "lookupColumn": "Fila ",
              "lookupValue": "={{ $json['Fila '] }}"
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [
        560,
        260
      ],
      "id": "08763abb-543b-4bf1-807a-ce57999d2cc0",
      "name": "Google Sheets1",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "0x9DM57RnZheyKnl",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "operation": "update",
        "documentId": {
          "__rl": true,
          "value": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
          "mode": "list",
          "cachedResultName": "Controle  de Estacionamento",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 1761021973,
          "mode": "list",
          "cachedResultName": "Respostas ao formulário 1",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit#gid=1761021973"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "Carimbo de data/hora": "={{ $('Edit Fields').item.json.submittedAt }}",
            "Registrado": "INSERIDO NO MAPA"
          },
          "matchingColumns": [
            "Carimbo de data/hora"
          ],
          "schema": [
            {
              "id": "Carimbo de data/hora",
              "displayName": "Carimbo de data/hora",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Fila",
              "displayName": "Fila",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Tipo de Veículo ",
              "displayName": "Tipo de Veículo ",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Placa ",
              "displayName": "Placa ",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Registrado",
              "displayName": "Registrado",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "row_number",
              "displayName": "row_number",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "readOnly": true,
              "removed": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [
        2420,
        640
      ],
      "id": "aa192dd1-1a65-42af-b6aa-d8fe523d1c8a",
      "name": "Google Sheets19",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "0x9DM57RnZheyKnl",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "operation": "update",
        "documentId": {
          "__rl": true,
          "value": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
          "mode": "list",
          "cachedResultName": "Controle  de Estacionamento",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 83682236,
          "mode": "list",
          "cachedResultName": "Mapa - Cacamba",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit#gid=83682236"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "FILA": "={{ $json.FILA }}",
            "VAGA 3": "={{ $('Edit Fields').item.json.PLACA }}"
          },
          "matchingColumns": [
            "FILA"
          ],
          "schema": [
            {
              "id": "FILA",
              "displayName": "FILA",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "VAGA 1",
              "displayName": "VAGA 1",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "VAGA 2",
              "displayName": "VAGA 2",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "VAGA 3",
              "displayName": "VAGA 3",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "VAGA 4",
              "displayName": "VAGA 4",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "row_number",
              "displayName": "row_number",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "readOnly": true,
              "removed": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [
        2400,
        860
      ],
      "id": "183cef21-ff85-4deb-b7fe-26976220c835",
      "name": "Google Sheets20",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "0x9DM57RnZheyKnl",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "operation": "update",
        "documentId": {
          "__rl": true,
          "value": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
          "mode": "list",
          "cachedResultName": "Controle  de Estacionamento",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 83682236,
          "mode": "list",
          "cachedResultName": "Mapa - Cacamba",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit#gid=83682236"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "FILA": "={{ $json.FILA }}",
            "VAGA 4": "={{ $('Edit Fields').item.json.PLACA }}"
          },
          "matchingColumns": [
            "FILA"
          ],
          "schema": [
            {
              "id": "FILA",
              "displayName": "FILA",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "VAGA 1",
              "displayName": "VAGA 1",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "VAGA 2",
              "displayName": "VAGA 2",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "VAGA 3",
              "displayName": "VAGA 3",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "VAGA 4",
              "displayName": "VAGA 4",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "row_number",
              "displayName": "row_number",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "readOnly": true,
              "removed": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [
        2680,
        1320
      ],
      "id": "c8a5a201-7fe9-45d9-9e45-ad83312000a6",
      "name": "Google Sheets21",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "0x9DM57RnZheyKnl",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "operation": "update",
        "documentId": {
          "__rl": true,
          "value": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
          "mode": "list",
          "cachedResultName": "Controle  de Estacionamento",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 1761021973,
          "mode": "list",
          "cachedResultName": "Respostas ao formulário 1",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit#gid=1761021973"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "Carimbo de data/hora": "={{ $('Edit Fields').item.json.submittedAt }}",
            "Registrado": "INSERIDO NO MAPA"
          },
          "matchingColumns": [
            "Carimbo de data/hora"
          ],
          "schema": [
            {
              "id": "Carimbo de data/hora",
              "displayName": "Carimbo de data/hora",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Fila",
              "displayName": "Fila",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Tipo de Veículo ",
              "displayName": "Tipo de Veículo ",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Placa ",
              "displayName": "Placa ",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Registrado",
              "displayName": "Registrado",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "row_number",
              "displayName": "row_number",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "readOnly": true,
              "removed": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [
        2720,
        900
      ],
      "id": "6829900b-2338-4fc2-b012-847840b3408a",
      "name": "Google Sheets22",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "0x9DM57RnZheyKnl",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "operation": "update",
        "documentId": {
          "__rl": true,
          "value": "1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k",
          "mode": "list",
          "cachedResultName": "Controle  de Estacionamento",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": 1761021973,
          "mode": "list",
          "cachedResultName": "Respostas ao formulário 1",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1tnQ4gZxCben1liB63pbPqvyeHqhyiJyjywReTU2g51k/edit#gid=1761021973"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "Carimbo de data/hora": "={{ $('Edit Fields').item.json.submittedAt }}",
            "Registrado": "INSERIDO NO MAPA"
          },
          "matchingColumns": [
            "Carimbo de data/hora"
          ],
          "schema": [
            {
              "id": "Carimbo de data/hora",
              "displayName": "Carimbo de data/hora",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "Fila",
              "displayName": "Fila",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Tipo de Veículo ",
              "displayName": "Tipo de Veículo ",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Placa ",
              "displayName": "Placa ",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": true
            },
            {
              "id": "Registrado",
              "displayName": "Registrado",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "removed": false
            },
            {
              "id": "row_number",
              "displayName": "row_number",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true,
              "readOnly": true,
              "removed": true
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.5,
      "position": [
        2920,
        1200
      ],
      "id": "2184f283-d17a-403d-9167-bd8d3f5e07cc",
      "name": "Google Sheets23",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "0x9DM57RnZheyKnl",
          "name": "Google Sheets account"
        }
      }
    }
  ],
  "connections": {
    "GetBase64": {
      "main": [
        [
          {
            "node": "Groq LLama4",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Groq LLama4": {
      "main": [
        []
      ]
    },
    "HTTP Request": {
      "main": [
        []
      ]
    },
    "Extract from File": {
      "main": [
        [
          {
            "node": "GetBase64",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "On form submission": {
      "main": [
        []
      ]
    },
    "If": {
      "main": [
        [
          {
            "node": "Read sheet1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Read sheet1": {
      "main": [
        [
          {
            "node": "Google Sheets2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets3": {
      "main": [
        [
          {
            "node": "Google Sheets11",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "VAGAS DISPONIVEIS NA FILA": {
      "main": [
        [
          {
            "node": "VAGA 1",
            "type": "main",
            "index": 0
          }
        ],
        []
      ]
    },
    "VAGA 1": {
      "main": [
        [
          {
            "node": "Google Sheets3",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "VAGA 2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "VAGA 2": {
      "main": [
        [
          {
            "node": "Google Sheets10",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "VAGA 3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "VAGA 3": {
      "main": [
        [
          {
            "node": "Google Sheets13",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "VAGA 4",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "VAGA 4": {
      "main": [
        [
          {
            "node": "Google Sheets14",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "On form submission1": {
      "main": [
        [
          {
            "node": "Edit Fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Edit Fields": {
      "main": [
        [
          {
            "node": "ADICIONAR A PLANILHA",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets10": {
      "main": [
        [
          {
            "node": "Google Sheets12",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets11": {
      "main": [
        [
          {
            "node": "If",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "ADICIONAR A PLANILHA": {
      "main": [
        [
          {
            "node": "Switch",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch": {
      "main": [
        [
          {
            "node": "Google Sheets",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Google Sheets1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets": {
      "main": [
        [
          {
            "node": "VAGAS DISPONIVEIS NA FILA",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets13": {
      "main": [
        [
          {
            "node": "Google Sheets15",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets14": {
      "main": [
        [
          {
            "node": "Google Sheets16",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets4": {
      "main": [
        [
          {
            "node": "Google Sheets18",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "VAGAS DISPONIVEIS NA FILA1": {
      "main": [
        [
          {
            "node": "VAGA ",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "VAGA ": {
      "main": [
        [
          {
            "node": "Google Sheets4",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "VAGA 5",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "VAGA 5": {
      "main": [
        [
          {
            "node": "Google Sheets17",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "VAGA 6",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "VAGA 6": {
      "main": [
        [
          {
            "node": "Google Sheets20",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "VAGA 7",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "VAGA 7": {
      "main": [
        [
          {
            "node": "Google Sheets21",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets17": {
      "main": [
        [
          {
            "node": "Google Sheets19",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets1": {
      "main": [
        [
          {
            "node": "VAGAS DISPONIVEIS NA FILA1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets20": {
      "main": [
        [
          {
            "node": "Google Sheets22",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets21": {
      "main": [
        [
          {
            "node": "Google Sheets23",
            "type": "main",
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