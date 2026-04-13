print("\n\n" + "=" * 80)
print("3️⃣  FINANÇAS")
print("=" * 80)
print("Modelar um algoritmo de aprovação de crédito baseado em")
print("'Idade' e 'Renda Mensal'.\n")
 
def analisa_credito(idade, renda_mensal, historico_credito, dividas_atuais):
    
    aprovacao = None
    limite_credito = 0
    juros = 0
    motivo = ""
    
    if idade < 18:
        aprovacao = False
        motivo = "❌ Menor de idade"
        return {
            "aprovado": aprovacao,
            "limite": limite_credito,
            "juros": juros,
            "motivo": motivo
        }
    
    if idade > 70:
        aprovacao = False
        motivo = "❌ Acima da idade limite (70 anos)"
        return {
            "aprovado": aprovacao,
            "limite": limite_credito,
            "juros": juros,
            "motivo": motivo
        }

    if renda_mensal < 1500:
        aprovacao = False
        motivo = "❌ Renda insuficiente (mínimo R$ 1.500)"
        return {
            "aprovado": aprovacao,
            "limite": limite_credito,
            "juros": juros,
            "motivo": motivo
        }
    
    if historico_credito < 300:
        aprovacao = False
        motivo = "❌ Histórico de crédito muito ruim (<300)"
        return {
            "aprovado": aprovacao,
            "limite": limite_credito,
            "juros": juros,
            "motivo": motivo
        }

    razao_divida_renda = dividas_atuais / renda_mensal
    if razao_divida_renda > 0.5:
        aprovacao = False
        motivo = f"❌ Muito endividado (dívida = {razao_divida_renda:.1%} da renda)"
        return {
            "aprovado": aprovacao,
            "limite": limite_credito,
            "juros": juros,
            "motivo": motivo
        }
    
    aprovacao = True
    
    limite_credito = renda_mensal * 5  
    
    if historico_credito >= 700:
        juros = 8.5  
        motivo = "✅ APROVADO | Score excelente → Juros 8.5% a.a."
    elif historico_credito >= 600:
        juros = 12.0  
        motivo = "✅ APROVADO | Score bom → Juros 12% a.a."
    elif historico_credito >= 450:
        juros = 18.5  
        motivo = "✅ APROVADO | Score aceitável → Juros 18.5% a.a."
    else:
        juros = 24.0  
        motivo = "✅ APROVADO | Score baixo → Juros 24% a.a."
    
    if 25 <= idade <= 45:
        juros -= 2
        motivo += " (desconto por idade)"
    
    return {
        "aprovado": aprovacao,
        "limite": round(limite_credito, 2),
        "juros": juros,
        "motivo": motivo
    }

print("\n📊 Testes do Sistema:")
testes_financas = [
    (30, 5000, 750, 5000),    
    (25, 2000, 650, 2000),     
    (35, 1800, 500, 8000),      
    (45, 1200, 400, 1000),     
    (75, 8000, 800, 10000),     
]
 
for idade, renda, score, dividas in testes_financas:
    resultado = analisa_credito(idade, renda, score, dividas)
    status = "✅" if resultado['aprovado'] else "❌"
    print(f"\n💳 Idade: {idade} | Renda: R$ {renda:.0f} | Score: {score} | Dívidas: R$ {dividas:.0f}")
    print(f"   → {resultado['motivo']}")
    if resultado['aprovado']:
        print(f"   → Limite: R$ {resultado['limite']:,.2f}")
        print(f"   → Juros: {resultado['juros']}% a.a.")
 
print("\n\n" + "=" * 80)
print("FIM DO LABORATÓRIO")
print("=" * 80)