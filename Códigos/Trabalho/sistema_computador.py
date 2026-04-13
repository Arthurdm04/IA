class SistemaEspecialistaComputador:
    def __init__(self):
        self.fatos = {}
        
        self.regras = self._criar_base_regras()
        
        self.diagnosticos = []
    
    def _criar_base_regras(self):
        return [
            # Regra 1: Computador não liga
            {
                "id": "R1",
                "nome": "Computador não liga",
                "condicoes": [
                    ("computador_nao_liga", True, 0.9),
                    ("fonte_nao_ligada", True, 0.95),
                ],
                "conclusao": "Ligue a fonte no botão power",
                "confianca_regra": 95,
                "categoria": "Hardware básico"
            },
            
            # Regra 2: Sem energia elétrica
            {
                "id": "R2",
                "nome": "Sem energia",
                "condicoes": [
                    ("computador_nao_liga", True, 0.8),
                    ("sem_energia_eletrica", True, 0.9),
                ],
                "conclusao": "Verifique a energia elétrica / Use nobreak",
                "confianca_regra": 90,
                "categoria": "Energia"
            },
            
            # Regra 3: Computador lento - RAM alta
            {
                "id": "R3",
                "nome": "Lentidão por RAM",
                "condicoes": [
                    ("computador_lento", True, 0.85),
                    ("ram_alta", True, 0.88),
                ],
                "conclusao": "Feche programas abertos e reinicie o computador",
                "confianca_regra": 85,
                "categoria": "Performance"
            },
            
            # Regra 4: Computador lento - Disco cheio
            {
                "id": "R4",
                "nome": "Lentidão por disco cheio",
                "condicoes": [
                    ("computador_lento", True, 0.8),
                    ("disco_cheio", True, 0.85),
                ],
                "conclusao": "Libere espaço no disco (delete arquivos antigos ou faça backup)",
                "confianca_regra": 80,
                "categoria": "Storage"
            },
            
            # Regra 5: Sem conexão WiFi
            {
                "id": "R5",
                "nome": "Problema WiFi",
                "condicoes": [
                    ("sem_internet", True, 0.9),
                    ("wifi_desconectado", True, 0.88),
                ],
                "conclusao": "Reconecte ao WiFi ou reinicie o roteador",
                "confianca_regra": 88,
                "categoria": "Conectividade"
            },
            
            # Regra 6: Tela preta/congelada
            {
                "id": "R6",
                "nome": "Sistema congelado",
                "condicoes": [
                    ("tela_preta_ou_congelada", True, 0.9),
                    ("nao_responde_teclado", True, 0.85),
                ],
                "conclusao": "Faça um reset: aperte Ctrl+Alt+Delete ou desligue o computador",
                "confianca_regra": 90,
                "categoria": "Sistema"
            },
            
            # Regra 7: Barulho/superaquecimento
            {
                "id": "R7",
                "nome": "Superaquecimento",
                "condicoes": [
                    ("computador_quente", True, 0.9),
                    ("ventiladores_altos", True, 0.85),
                ],
                "conclusao": "Limpe o ventilador/cooler e verifique a pasta térmica",
                "confianca_regra": 85,
                "categoria": "Thermal"
            },
            
            # Regra 8: Vírus/Malware
            {
                "id": "R8",
                "nome": "Possível vírus",
                "condicoes": [
                    ("pop_ups_frequentes", True, 0.8),
                    ("programas_estranhos", True, 0.85),
                ],
                "conclusao": "Execute antivírus (Windows Defender/Avast) e faça varredura completa",
                "confianca_regra": 80,
                "categoria": "Segurança"
            },
        ]
    
    def coletar_sintomas(self):
        print("\n" + "="*70)
        print("SISTEMA ESPECIALISTA - DIAGNÓSTICO DE COMPUTADOR")
        print("="*70)
        print("\nResponda as perguntas abaixo (s/n):\n")
        
        perguntas = [
            ("computador_nao_liga", "O computador não liga quando você aperta o botão power?"),
            ("fonte_nao_ligada", "A fonte de energia está conectada e ligada?"),
            ("sem_energia_eletrica", "Há energia elétrica na tomada?"),
            ("computador_lento", "O computador está lento/travando?"),
            ("ram_alta", "A RAM está acima de 80% de uso?"),
            ("disco_cheio", "O disco está quase cheio (>90%)?"),
            ("sem_internet", "Você não tem acesso à internet?"),
            ("wifi_desconectado", "O WiFi aparece desconectado?"),
            ("tela_preta_ou_congelada", "A tela está preta ou congelada?"),
            ("nao_responde_teclado", "O computador não responde ao teclado/mouse?"),
            ("computador_quente", "O computador está muito quente?"),
            ("ventiladores_altos", "Os ventiladores estão fazendo barulho alto?"),
            ("pop_ups_frequentes", "Aparecem muitos pop-ups na tela?"),
            ("programas_estranhos", "Há programas desconhecidos instalados?"),
        ]
        
        for chave, pergunta in perguntas:
            while True:
                resposta = input(f"  {pergunta} (s/n): ").lower().strip()
                if resposta in ['s', 'n']:
                    self.fatos[chave] = (resposta == 's')
                    break
                print("  ❌ Digite apenas 's' ou 'n'")
        
        return self.fatos
    
    def inferir(self):
        print("\n" + "="*70)
        print("ANALISANDO...")
        print("="*70 + "\n")
        
        diagnosticos_encontrados = []
        
        for regra in self.regras:
            confianca_total = 100
            regra_ativada = True
            condicoes_satisfeitas = []
            
            for chave, valor_esperado, confianca_condicao in regra["condicoes"]:
                if chave in self.fatos:
                    if self.fatos[chave] == valor_esperado:
                        confianca_total *= (confianca_condicao / 100)
                        condicoes_satisfeitas.append(f"✓ {chave}")
                    else:
                        regra_ativada = False
                        condicoes_satisfeitas.append(f"✗ {chave}")
                        break
                else:
                    regra_ativada = False
                    break
            
            if regra_ativada:
                confianca_final = (confianca_total * regra["confianca_regra"]) / 100
                
                diagnosticos_encontrados.append({
                    "regra_id": regra["id"],
                    "nome": regra["nome"],
                    "conclusao": regra["conclusao"],
                    "categoria": regra["categoria"],
                    "confianca": round(confianca_final, 1),
                    "condicoes": condicoes_satisfeitas
                })
        
        self.diagnosticos = sorted(diagnosticos_encontrados, 
                                   key=lambda x: x["confianca"], 
                                   reverse=True)
        
        return self.diagnosticos
    
    def apresentar_resultados(self):
        if not self.diagnosticos:
            print("❌ Nenhum diagnóstico específico encontrado.")
            print("   Recomendação: Leve o computador para uma assistência técnica.")
            return
        
        print("\n" + "="*70)
        print("DIAGNÓSTICOS ENCONTRADOS (ordenados por confiança)")
        print("="*70 + "\n")
        
        for i, diag in enumerate(self.diagnosticos, 1):
            barra_confianca = "█" * int(diag["confianca"] / 5) + "░" * (20 - int(diag["confianca"] / 5))
            
            print(f"\n{i}. {diag['nome']} [{diag['categoria']}]")
            print(f"   Confiança: {diag['confianca']}% [{barra_confianca}]")
            print(f"   Solução: {diag['conclusao']}")
            print(f"   Regra: {diag['regra_id']}")
    
    def explicar_raciocinio(self, indice=0):
        if indice >= len(self.diagnosticos):
            print("❌ Diagnóstico não encontrado")
            return
        
        diag = self.diagnosticos[indice]
        print(f"\n📋 EXPLICAÇÃO DO DIAGNÓSTICO '{diag['nome']}':")
        print(f"   Confiança: {diag['confianca']}%")
        print("   Raciocínio:")
        for condicao in diag["condicoes"]:
            print(f"   {condicao}")
    
    def executar(self):
        self.coletar_sintomas()
        self.inferir()
        self.apresentar_resultados()
        
        if self.diagnosticos:
            print("\n" + "="*70)
            explicar = input("\nDeseja ver a explicação detalhada do principal diagnóstico? (s/n): ")
            if explicar.lower() == 's':
                self.explicar_raciocinio(0)
        
        print("\n" + "="*70)
        print("Obrigado por usar o Sistema Especialista!")
        print("="*70 + "\n")  

if __name__ == "__main__":
    sistema = SistemaEspecialistaComputador()
    sistema.executar()