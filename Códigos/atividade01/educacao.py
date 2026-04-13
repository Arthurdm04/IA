print("\n\n" + "=" * 80)
print("2️⃣  EDUCAÇÃO JUSTA")
print("=" * 80)
print("Modelar um sistema de avaliação que calcula a nota final combinando")
print("'Esforço nas Aulas' e 'Desempenho na Prova'.\n")
 
def calcula_nota_final(esforco_aulas, desempenho_prova, frequencia):
    
    nota_final = None
    conceito = None
    recomendacao = ""
    
    if frequencia < 75:
        nota_final = 0
        conceito = "REPROVADO"
        recomendacao = "❌ Frequência insuficiente (<75%). Necessário 75% de presença."
        return {"nota": nota_final, "conceito": conceito, "recomendacao": recomendacao}
    
    if esforco_aulas >= 7 and desempenho_prova >= 7:
        nota_final = (esforco_aulas * 0.4) + (desempenho_prova * 0.6)

        if esforco_aulas >= 9:
            nota_final = min(10, nota_final + 0.5)
            recomendacao = "✅ Excelente esforço! Bônus de +0.5"
    
    elif esforco_aulas >= 8 and desempenho_prova < 7:
        nota_final = (esforco_aulas * 0.5) + (desempenho_prova * 0.5)
        recomendacao = "⚠️  Esforço compensou performance"
    
    elif esforco_aulas < 7 and desempenho_prova >= 7:
        nota_final = (esforco_aulas * 0.3) + (desempenho_prova * 0.7)
        recomendacao = "⚠️  Prova boa, mas esforço baixo"
    
    else:
        nota_final = (esforco_aulas * 0.4) + (desempenho_prova * 0.6)
        recomendacao = "❌ Desempenho insuficiente em ambas"

    if nota_final >= 9:
        conceito = "A (Excelente)"
    elif nota_final >= 7:
        conceito = "B (Bom)"
    elif nota_final >= 5:
        conceito = "C (Satisfatório)"
    else:
        conceito = "D (Insuficiente)"
    
    return {
        "nota": round(nota_final, 2),
        "conceito": conceito,
        "recomendacao": recomendacao
    }
 
print("\n📊 Testes do Sistema:")
testes_educacao = [
    (9, 8, 95),    
    (8, 5, 80),     
    (5, 8, 90),     
    (4, 3, 50),     
    (7, 7, 100),    
]
 
for esforco, prova, freq in testes_educacao:
    resultado = calcula_nota_final(esforco, prova, freq)
    print(f"\n📚 Esforço: {esforco}/10 | Prova: {prova}/10 | Frequência: {freq}%")
    print(f"   → Nota Final: {resultado['nota']}")
    print(f"   → Conceito: {resultado['conceito']}")
    print(f"   → {resultado['recomendacao']}")