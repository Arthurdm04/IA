"""
SCRIPT DE TESTES AUTOMATIZADOS
Valida o sistema especialista com casos predefinidos
"""

from sistema_especialista import (
    SistemaEspecialista, Sintoma, MotorInferencia, BaseDeRegras
)

class TestadorSistemaEspecialista:
    """Executa testes automatizados no sistema"""
    
    def __init__(self):
        self.testes_passaram = 0
        self.testes_falharam = 0
        self.resultados = []
    
    def teste_1_computador_nao_liga(self):
        """Teste R1: Computador não liga - Fonte desligada"""
        print("\n" + "="*70)
        print("TESTE 1: Computador não liga - Fonte desligada")
        print("="*70)
        
        sistema = SistemaEspecialista()
        
        # Simular entrada
        sistema.motor.registrar_fato(Sintoma.COMPUTADOR_NAO_LIGA, True)
        sistema.motor.registrar_fato(Sintoma.FONTE_NAO_LIGADA, True)
        
        # Executar inferência
        diagnosticos = sistema.motor.inferir()
        
        # Validar resultado
        if diagnosticos and diagnosticos[0].regra_id == "R1":
            confianca = diagnosticos[0].confianca
            esperado = 0.8122  # 0.9 * 0.95 * 0.95
            
            if abs(confianca - esperado) < 0.01:
                print(f"✓ PASSOU")
                print(f"  Diagnóstico: {diagnosticos[0].nome}")
                print(f"  Confiança: {confianca:.2%}")
                print(f"  Esperado: ~{esperado:.2%}")
                self.testes_passaram += 1
                return True
            else:
                print(f"✗ FALHOU - Confiança incorreta")
                print(f"  Obtido: {confianca:.2%}")
                print(f"  Esperado: ~{esperado:.2%}")
                self.testes_falharam += 1
                return False
        else:
            print(f"✗ FALHOU - Regra R1 não foi ativada")
            if diagnosticos:
                print(f"  Obtido: {diagnosticos[0].regra_id}")
            self.testes_falharam += 1
            return False
    
    def teste_2_computador_lento_ram(self):
        """Teste R3: Computador lento por RAM alta"""
        print("\n" + "="*70)
        print("TESTE 2: Computador lento - RAM alta")
        print("="*70)
        
        sistema = SistemaEspecialista()
        
        # Simular entrada
        sistema.motor.registrar_fato(Sintoma.COMPUTADOR_LENTO, True)
        sistema.motor.registrar_fato(Sintoma.RAM_ALTA, True)
        
        # Executar inferência
        diagnosticos = sistema.motor.inferir()
        
        # Validar resultado
        if diagnosticos and diagnosticos[0].regra_id == "R3":
            confianca = diagnosticos[0].confianca
            esperado = 0.6292  # 0.85 * 0.88 * 0.85
            
            if abs(confianca - esperado) < 0.01:
                print(f"✓ PASSOU")
                print(f"  Diagnóstico: {diagnosticos[0].nome}")
                print(f"  Confiança: {confianca:.2%}")
                print(f"  Esperado: ~{esperado:.2%}")
                self.testes_passaram += 1
                return True
            else:
                print(f"✗ FALHOU - Confiança incorreta")
                print(f"  Obtido: {confianca:.2%}")
                print(f"  Esperado: ~{esperado:.2%}")
                self.testes_falharam += 1
                return False
        else:
            print(f"✗ FALHOU - Regra R3 não foi ativada")
            self.testes_falharam += 1
            return False
    
    def teste_3_nenhuma_regra_ativada(self):
        """Teste: Nenhuma sintoma = Nenhum diagnóstico"""
        print("\n" + "="*70)
        print("TESTE 3: Nenhuma regra ativada")
        print("="*70)
        
        sistema = SistemaEspecialista()
        
        # Registrar todos os sintomas como FALSOS
        for sintoma in Sintoma:
            sistema.motor.registrar_fato(sintoma, False)
        
        # Executar inferência
        diagnosticos = sistema.motor.inferir()
        
        # Validar resultado
        if len(diagnosticos) == 0:
            print(f"✓ PASSOU")
            print(f"  Nenhum diagnóstico retornado (correto!)")
            self.testes_passaram += 1
            return True
        else:
            print(f"✗ FALHOU - Deveria retornar lista vazia")
            print(f"  Obtido {len(diagnosticos)} diagnósticos")
            self.testes_falharam += 1
            return False
    
    def teste_4_multiplos_diagnosticos(self):
        """Teste: Múltiplas regras ativadas (ordenação por confiança)"""
        print("\n" + "="*70)
        print("TESTE 4: Múltiplas regras ativadas (validação de ordenação)")
        print("="*70)
        
        sistema = SistemaEspecialista()
        
        # Ativar R1 (alta confiança) e R3 (média confiança)
        sistema.motor.registrar_fato(Sintoma.COMPUTADOR_NAO_LIGA, True)
        sistema.motor.registrar_fato(Sintoma.FONTE_NAO_LIGADA, True)
        sistema.motor.registrar_fato(Sintoma.COMPUTADOR_LENTO, True)
        sistema.motor.registrar_fato(Sintoma.RAM_ALTA, True)
        
        # Resto como falso
        for sintoma in Sintoma:
            if sintoma not in [Sintoma.COMPUTADOR_NAO_LIGA, 
                              Sintoma.FONTE_NAO_LIGADA,
                              Sintoma.COMPUTADOR_LENTO,
                              Sintoma.RAM_ALTA]:
                sistema.motor.registrar_fato(sintoma, False)
        
        # Executar inferência
        diagnosticos = sistema.motor.inferir()
        
        # Validar resultado
        if len(diagnosticos) >= 2:
            # Verificar ordenação
            if diagnosticos[0].confianca > diagnosticos[1].confianca:
                print(f"✓ PASSOU")
                print(f"  {len(diagnosticos)} diagnósticos retornados")
                print(f"  Ordenados por confiança:")
                for i, diag in enumerate(diagnosticos[:3], 1):
                    print(f"    {i}. {diag.nome} ({diag.confianca:.1%})")
                self.testes_passaram += 1
                return True
            else:
                print(f"✗ FALHOU - Diagnósticos não estão ordenados corretamente")
                self.testes_falharam += 1
                return False
        else:
            print(f"✗ FALHOU - Esperava 2+ diagnósticos, obteve {len(diagnosticos)}")
            self.testes_falharam += 1
            return False
    
    def teste_5_condicoes_parcialmente_satisfeitas(self):
        """Teste: Apenas uma condição de uma regra satisfeita (não deve ativar)"""
        print("\n" + "="*70)
        print("TESTE 5: Condições parcialmente satisfeitas (regra não ativa)")
        print("="*70)
        
        sistema = SistemaEspecialista()
        
        # Apenas uma condição de R1
        sistema.motor.registrar_fato(Sintoma.COMPUTADOR_NAO_LIGA, True)
        sistema.motor.registrar_fato(Sintoma.FONTE_NAO_LIGADA, False)  # Segunda condição FALSA
        
        # Resto como falso
        for sintoma in Sintoma:
            if sintoma not in [Sintoma.COMPUTADOR_NAO_LIGA, 
                              Sintoma.FONTE_NAO_LIGADA]:
                sistema.motor.registrar_fato(sintoma, False)
        
        # Executar inferência
        diagnosticos = sistema.motor.inferir()
        
        # Validar resultado
        regra_1_presente = any(d.regra_id == "R1" for d in diagnosticos)
        
        if not regra_1_presente:
            print(f"✓ PASSOU")
            print(f"  R1 não foi ativada (correto - precisa de 2 condições)")
            self.testes_passaram += 1
            return True
        else:
            print(f"✗ FALHOU - R1 foi ativada sem satisfazer todas as condições")
            self.testes_falharam += 1
            return False
    
    def teste_6_estrutura_de_dados(self):
        """Teste: Validar estrutura de dados das regras"""
        print("\n" + "="*70)
        print("TESTE 6: Validação da estrutura de dados")
        print("="*70)
        
        base = BaseDeRegras()
        regras = base.criar_regras()
        
        # Validar
        erros = []
        
        if len(regras) != 8:
            erros.append(f"Esperava 8 regras, obteve {len(regras)}")
        
        for regra in regras:
            if not (0.0 <= regra.confianca_regra <= 1.0):
                erros.append(f"Regra {regra.id}: confiança fora de range")
            if len(regra.condicoes) < 1:
                erros.append(f"Regra {regra.id}: sem condições")
            for condicao in regra.condicoes:
                if not (0.0 <= condicao.confianca_condicao <= 1.0):
                    erros.append(f"Regra {regra.id}: confiança da condição fora de range")
        
        if not erros:
            print(f"✓ PASSOU")
            print(f"  ✓ 8 regras encontradas")
            print(f"  ✓ Todas as confiança em range [0.0, 1.0]")
            print(f"  ✓ Todas as regras tem condições")
            self.testes_passaram += 1
            return True
        else:
            print(f"✗ FALHOU - Erros de estrutura:")
            for erro in erros:
                print(f"  - {erro}")
            self.testes_falharam += 1
            return False
    
    def teste_7_explicabilidade(self):
        """Teste: Validar raciocínio e explicabilidade"""
        print("\n" + "="*70)
        print("TESTE 7: Validação de Explicabilidade")
        print("="*70)
        
        sistema = SistemaEspecialista()
        
        # Ativar R1
        sistema.motor.registrar_fato(Sintoma.COMPUTADOR_NAO_LIGA, True)
        sistema.motor.registrar_fato(Sintoma.FONTE_NAO_LIGADA, True)
        
        # Resto como falso
        for sintoma in Sintoma:
            if sintoma not in [Sintoma.COMPUTADOR_NAO_LIGA, 
                              Sintoma.FONTE_NAO_LIGADA]:
                sistema.motor.registrar_fato(sintoma, False)
        
        # Executar inferência
        diagnosticos = sistema.motor.inferir()
        
        # Validar
        if diagnosticos and diagnosticos[0].raciocinio:
            linhas = diagnosticos[0].raciocinio
            
            # Verificar se tem explicação passo-a-passo
            tem_avaliacao = any("Avaliando" in str(l) for l in linhas)
            tem_conclusao = any("CONCLUSÃO" in str(l) for l in linhas)
            
            if tem_avaliacao and tem_conclusao:
                print(f"✓ PASSOU")
                print(f"  Raciocínio contém {len(linhas)} linhas de explicação")
                print(f"  Inclui: avaliação de condições + conclusão")
                self.testes_passaram += 1
                return True
            else:
                print(f"✗ FALHOU - Raciocínio incompleto")
                self.testes_falharam += 1
                return False
        else:
            print(f"✗ FALHOU - Sem raciocínio gerado")
            self.testes_falharam += 1
            return False
    
    def executar_todos_testes(self):
        """Executa todos os 7 testes"""
        print("\n" + "="*70)
        print("INICIANDO BATERIA DE TESTES")
        print("="*70)
        
        self.teste_1_computador_nao_liga()
        self.teste_2_computador_lento_ram()
        self.teste_3_nenhuma_regra_ativada()
        self.teste_4_multiplos_diagnosticos()
        self.teste_5_condicoes_parcialmente_satisfeitas()
        self.teste_6_estrutura_de_dados()
        self.teste_7_explicabilidade()
        
        # Relatório final
        print("\n" + "="*70)
        print("RELATÓRIO FINAL")
        print("="*70)
        print(f"✓ Testes que passaram: {self.testes_passaram}")
        print(f"✗ Testes que falharam: {self.testes_falharam}")
        print(f"Total: {self.testes_passaram + self.testes_falharam}")
        print(f"Taxa de sucesso: {self.testes_passaram / (self.testes_passaram + self.testes_falharam) * 100:.1f}%")
        
        if self.testes_falharam == 0:
            print("\n🎉 TODOS OS TESTES PASSARAM! Sistema validado!")
        else:
            print("\n⚠️  Alguns testes falharam. Verifique os erros acima.")
        
        print("="*70 + "\n")


if __name__ == "__main__":
    testador = TestadorSistemaEspecialista()
    testador.executar_todos_testes()
