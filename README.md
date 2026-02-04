# Projeto Jockey

Projeto Jockey é um wearable bioneural focado em segurança e saúde,
desenvolvido para operar em Edge AI com foco em baixo consumo,
privacidade e resposta rápida a eventos críticos.

## Objetivo

Detectar situações de:
- Pré-crise de estresse neurológico
- Agressões verbais e bullying
- Picos sonoros anormais

E responder localmente, sem depender de nuvem.

## Arquitetura

- Edge-first
- Event-driven
- Segurança by design
- OTA segura
- Secure Boot
- Perfis de energia dinâmicos (Jetson)

## Módulos

### Saúde (Tourette)
- Frequência cardíaca
- Acelerômetro
- Detecção de padrão pré-crise
- Feedback de áudio calmante

### Segurança (Bullying)
- Análise de áudio
- Detecção de palavras-chave
- Buffer circular de gravação
- Criptografia local

## Segurança

- Secure Boot
- Firmware assinado
- Criptografia de dados sensíveis
- Escalonamento de alertas

## Estado Atual

Projeto em fase de arquitetura e prototipação offline.

## Próximos Passos

- Integração com NVIDIA Jetson
- DeepStream Audio Analytics
- Quantização de modelos
- Testes de consumo energético