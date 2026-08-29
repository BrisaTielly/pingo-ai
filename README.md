<div align="center">

<img src="frontend/images/mascots/pingo-penguin-accomplice-study.png" alt="Pingo, o pinguim mascote do projeto, em três poses" width="520">

# Pingo - Em desenvolvimento...

### Gaste. O Pingo acompanha.

Mande uma mensagem como você fala.<br>
O Pingo transforma seus gastos em registros simples de entender.

</div>


## A conversa

Não tem app pra abrir, categoria pra escolher, nem planilha pra manter. Tem o WhatsApp que você já usa o dia inteiro.

```text
  você    gastei 32 no almoço
  pingo   R$ 32.00 - almoço

  você    mercado deu 74,50
  pingo   R$ 74.50 - mercado
```

O trabalho dele é achar duas coisas numa frase solta: **quanto** e **no quê**. Se faltar alguma, marca como `null` em vez de inventar. Chutar valor de gasto é pior do que não registrar.

## As tecnologias

**Em uso agora:** Python 3.12, FastAPI, uv, Pydantic, httpx, `google-genai` pro Gemini, e a Kapso como gateway da WhatsApp Cloud API.

**Planejado:** PostgreSQL pra guardar os gastos, pytest e GitHub Actions pros testes e automações, AWS pra colocar no ar, e a landing page servida pelo próprio FastAPI.

Essas escolhas ainda podem mudar conforme eu for entendendo melhor as necessidades do projeto. Ainda em estagio embrionário, sendo desenvolvido aos poucos.


## A cara do Pingo

<div align="center">
<img src="frontend/images/mascots/pingo-penguin-natural-2d.png" alt="Pingo em quatro poses do dia a dia" width="420">
</div>

Ele é camarada, não fiscal. Entende que você escreve com pressa, não corrige seu português e não transforma um almoço de 32 reais em lição de moral. Acompanha, que já é bastante.

```text
  Névoa         #F4FBF8
  Menta         #91D6BE
  Verde-pingo   #26A18B
  Petróleo      #07565A
  Grafite       #20282C
```

Outfit no display, DM Sans no texto, IBM Plex Mono nos valores. O verde-pingo é o único acento.

<br>

---

<div align="center">
<sub>Projeto de estudo. Feito devagar, de propósito.</sub>
</div>
