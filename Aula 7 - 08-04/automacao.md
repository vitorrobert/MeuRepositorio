
## PRIMEIROS TESTES COM N8N##

{
  "nodes": [
    {
      "parameters": {},
      "type": "n8n-nodes-base.manualTrigger",
      "typeVersion": 1,
      "position": [
        0,
        0
      ],
      "id": "7de74737-c465-484c-be41-657946962425",
      "name": "When clicking ‘Test workflow’"
    },
    {
      "parameters": {
        "operation": "instance-connect",
        "instanceName": "vitorTestes"
      },
      "type": "n8n-nodes-evolution-api.evolutionApi",
      "typeVersion": 1,
      "position": [
        440,
        0
      ],
      "id": "03fa17f3-1a87-45e8-9104-746754d1af91",
      "name": "Evolution API",
      "credentials": {
        "evolutionApi": {
          "id": "8cex2SwlYGZhN0rZ",
          "name": "Evolution account"
        }
      }
    },
    {
      "parameters": {
        "path": "9bd5a0b4-3b56-4d0e-9513-382fbae4db0b",
        "options": {}
      },
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        220,
        0
      ],
      "id": "6579a8f7-8a68-4a3d-b6f1-38b91fb38ff8",
      "name": "Webhook",
      "webhookId": "9bd5a0b4-3b56-4d0e-9513-382fbae4db0b"
    }
  ],
  "connections": {
    "When clicking ‘Test workflow’": {
      "main": [
        []
      ]
    },
    "Webhook": {
      "main": [
        [
          {
            "node": "Evolution API",
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