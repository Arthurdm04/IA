print("=" * 80)
print("LABORATÓRIO DE MODELAGEM (BRAINSTORMING EM GRUPO)")
print("=" * 80)
 
# ==================== PROBLEMA 1: CONFORTO TÉRMICO ====================
print("\n" + "=" * 80)
print("1️⃣  CONFORTO TÉRMICO")
print("=" * 80)
print("Modelar um ar-condicionado de shopping que esfrie o ambiente")
print("sem 'congelar' as pessoas quando o local esvaziar.\n")
 
def controle_ar_condicionado(temperatura_atual, pessoas_presentes, horario):

    
    temperatura_alvo = None
    intensidade_ac = None
    justificativa = ""
    
    if pessoas_presentes == 0:
        if temperatura_atual < 20:
            intensidade_ac = 0  
            temperatura_alvo = 18
            justificativa = "Loja vazia → AC desligado para economizar"
        else:
            intensidade_ac = 20  
            temperatura_alvo = 22
            justificativa = "Loja vazia → AC em modo manutenção"
    
    elif pessoas_presentes < 10:
        if temperatura_atual > 26:
            intensidade_ac = 40
            temperatura_alvo = 24
            justificativa = "Poucas pessoas → Refrigeração moderada"
        else:
            intensidade_ac = 20
            temperatura_alvo = 24
            justificativa = "Poucas pessoas → AC em nível baixo"
    
    elif pessoas_presentes < 50:
        if temperatura_atual > 28:
            intensidade_ac = 70
            temperatura_alvo = 23
            justificativa = "Ocupação média → Refrigeração normal"
        else:
            intensidade_ac = 50
            temperatura_alvo = 23
            justificativa = "Ocupação média → AC moderado"
    
    else:
        if temperatura_atual > 30:
            intensidade_ac = 100 
            temperatura_alvo = 21
            justificativa = "Muita gente → AC no máximo"
        else:
            intensidade_ac = 80
            temperatura_alvo = 21
            justificativa = "Muita gente → AC intenso"
    
    if horario >= 22 or horario < 6:
        intensidade_ac = max(0, intensidade_ac - 20)
        justificativa += " | Ajuste noturno: economia"
    
    return {
        "intensidade": intensidade_ac,
        "temperatura_alvo": temperatura_alvo,
        "status": f"AC em {intensidade_ac}%",
        "justificativa": justificativa
    }
 
print("\n📊 Testes do Sistema:")
testes_conforto = [
    (25, 0, 14),    
    (28, 45, 14),   
    (22, 5, 3),     
    (30, 100, 15),  
]
 
for temp, pessoas, hora in testes_conforto:
    resultado = controle_ar_condicionado(temp, pessoas, hora)
    print(f"\n🌡️  Temp: {temp}°C | Pessoas: {pessoas} | Hora: {hora:02d}h")
    print(f"   → {resultado['status']}")
    print(f"   → Alvo: {resultado['temperatura_alvo']}°C")
    print(f"   → {resultado['justificativa']}")