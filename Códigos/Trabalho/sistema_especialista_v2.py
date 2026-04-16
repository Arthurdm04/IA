from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from enum import Enum
import json


# ============================================================================
# PARTE 1: REPRESENTAÇÃO DO CONHECIMENTO - ONTOLOGIA DO DOMÍNIO
# ============================================================================

class Sintoma(Enum):
    """Sintomas observáveis que podem indicar problemas no computador"""
    COMPUTADOR_NAO_LIGA = "computador_nao_liga"
    FONTE_NAO_LIGADA = "fonte_nao_ligada"
    SEM_ENERGIA_ELETRICA = "sem_energia_eletrica"
    COMPUTADOR_LENTO = "computador_lento"
    RAM_ALTA = "ram_alta"
    DISCO_CHEIO = "disco_cheio"
    SEM_INTERNET = "sem_internet"
    WIFI_DESCONECTADO = "wifi_desconectado"
    TELA_PRETA_CONGELADA = "tela_preta_ou_congelada"
    NAO_RESPONDE_TECLADO = "nao_responde_teclado"
    COMPUTADOR_QUENTE = "computador_quente"
    VENTILADORES_ALTOS = "ventiladores_altos"
    POP_UPS_FREQUENTES = "pop_ups_frequentes"
    PROGRAMAS_ESTRANHOS = "programas_estranhos"


class Categoria(Enum):
    """Categorias de problemas para organização"""
    HARDWARE_BASICO = "Hardware básico"
    ENERGIA = "Energia"
    PERFORMANCE = "Performance"
    STORAGE = "Storage"
    CONECTIVIDADE = "Conectividade"
    SISTEMA = "Sistema"
    THERMAL = "Thermal"
    SEGURANCA = "Segurança"


@dataclass
class Condicao:
    """Representa uma condição em uma regra"""
    sintoma: Sintoma
    valor_esperado: bool
    confianca_condicao: float  # 0.0 a 1.0
    
    def __post_init__(self):
        if not (0.0 <= self.confianca_condicao <= 1.0):
            raise ValueError("Confiança deve estar entre 0.0 e 1.0")


@dataclass
class Regra:
    id: str
    nome: str
    condicoes: List[Condicao]
    conclusao: str
    confianca_regra: float 
    categoria: Categoria
    justificativa: str 
    
    def __post_init__(self):
        if not (0.0 <= self.confianca_regra <= 1.0):
            raise ValueError("Confiança da regra deve estar entre 0.0 e 1.0")
        if not self.condicoes:
            raise ValueError("Regra deve ter pelo menos uma condição")


# ============================================================================
# PARTE 2: BASE DE REGRAS (Conhecimento do Especialista)
# ============================================================================

class BaseDeRegras:
    
    @staticmethod
    def criar_regras() -> List[Regra]:
        return [
            # ===== CATEGORIA: HARDWARE BÁSICO =====
            Regra(
                id="R1",
                nome="Computador não liga - Fonte desligada",
                condicoes=[
                    Condicao(Sintoma.COMPUTADOR_NAO_LIGA, True, 0.9),
                    Condicao(Sintoma.FONTE_NAO_LIGADA, True, 0.95),
                ],
                conclusao="Ligue a fonte no botão power",
                confianca_regra=0.95,
                categoria=Categoria.HARDWARE_BASICO,
                justificativa="A fonte de energia é requisito fundamental. Se computador não liga E "
                            "fonte não está ligada, é causa muito provável."
            ),
            
            # ===== CATEGORIA: ENERGIA =====
            Regra(
                id="R2",
                nome="Sem energia elétrica",
                condicoes=[
                    Condicao(Sintoma.COMPUTADOR_NAO_LIGA, True, 0.8),
                    Condicao(Sintoma.SEM_ENERGIA_ELETRICA, True, 0.9),
                ],
                conclusao="Verifique a energia elétrica / Use nobreak",
                confianca_regra=0.90,
                categoria=Categoria.ENERGIA,
                justificativa="Falta de energia elétrica impede qualquer funcionamento. "
                            "Solução: verificar circuito ou usar fonte auxiliar."
            ),
            
            # ===== CATEGORIA: PERFORMANCE =====
            Regra(
                id="R3",
                nome="Lentidão por RAM alta",
                condicoes=[
                    Condicao(Sintoma.COMPUTADOR_LENTO, True, 0.85),
                    Condicao(Sintoma.RAM_ALTA, True, 0.88),
                ],
                conclusao="Feche programas abertos e reinicie o computador",
                confianca_regra=0.85,
                categoria=Categoria.PERFORMANCE,
                justificativa="RAM alta causa thrashing de memória, degradando performance. "
                            "Reinicialização libera memória e resolve temporariamente."
            ),
            
            Regra(
                id="R4",
                nome="Lentidão por disco cheio",
                condicoes=[
                    Condicao(Sintoma.COMPUTADOR_LENTO, True, 0.8),
                    Condicao(Sintoma.DISCO_CHEIO, True, 0.85),
                ],
                conclusao="Libere espaço no disco (delete arquivos antigos ou faça backup)",
                confianca_regra=0.80,
                categoria=Categoria.STORAGE,
                justificativa="Disco cheio prejudica paginação de memória virtual e I/O. "
                            "Liberação de espaço restaura performance."
            ),
            
            # ===== CATEGORIA: CONECTIVIDADE =====
            Regra(
                id="R5",
                nome="Problema WiFi",
                condicoes=[
                    Condicao(Sintoma.SEM_INTERNET, True, 0.9),
                    Condicao(Sintoma.WIFI_DESCONECTADO, True, 0.88),
                ],
                conclusao="Reconecte ao WiFi ou reinicie o roteador",
                confianca_regra=0.88,
                categoria=Categoria.CONECTIVIDADE,
                justificativa="WiFi desconectado é causa direta de falta de internet. "
                            "Reconexão ou reinicialização restabelece conexão."
            ),
            
            # ===== CATEGORIA: SISTEMA =====
            Regra(
                id="R6",
                nome="Sistema congelado",
                condicoes=[
                    Condicao(Sintoma.TELA_PRETA_CONGELADA, True, 0.9),
                    Condicao(Sintoma.NAO_RESPONDE_TECLADO, True, 0.85),
                ],
                conclusao="Faça um reset: aperte Ctrl+Alt+Delete ou desligue o computador",
                confianca_regra=0.90,
                categoria=Categoria.SISTEMA,
                justificativa="Tela congelada + falta de resposta indica travamento do SO. "
                            "Reset forçado é solução padrão."
            ),
            
            # ===== CATEGORIA: THERMAL =====
            Regra(
                id="R7",
                nome="Superaquecimento",
                condicoes=[
                    Condicao(Sintoma.COMPUTADOR_QUENTE, True, 0.9),
                    Condicao(Sintoma.VENTILADORES_ALTOS, True, 0.85),
                ],
                conclusao="Limpe o ventilador/cooler e verifique a pasta térmica",
                confianca_regra=0.85,
                categoria=Categoria.THERMAL,
                justificativa="Calor excessivo + barulho de ventiladores indica obstrução. "
                            "Limpeza restaura dissipação térmica."
            ),
            
            # ===== CATEGORIA: SEGURANÇA =====
            Regra(
                id="R8",
                nome="Possível vírus/malware",
                condicoes=[
                    Condicao(Sintoma.POP_UPS_FREQUENTES, True, 0.8),
                    Condicao(Sintoma.PROGRAMAS_ESTRANHOS, True, 0.85),
                ],
                conclusao="Execute antivírus (Windows Defender/Avast) e faça varredura completa",
                confianca_regra=0.80,
                categoria=Categoria.SEGURANCA,
                justificativa="Pop-ups + programas desconhecidos indicam infecção. "
                            "Varredura antivírus é procedimento padrão de segurança."
            ),
        ]


# ============================================================================
# PARTE 3: MOTOR DE INFERÊNCIA COM TRATAMENTO DE INCERTEZA
# ============================================================================

@dataclass
class ResultadoDiagnostico:
    regra_id: str
    nome: str
    conclusao: str
    categoria: Categoria
    confianca: float  # 0.0 a 1.0
    raciocinio: List[str]  # Explicação passo a passo


class MotorInferencia:
    def __init__(self, regras: List[Regra]):
        self.regras = regras
        self.fatos = {}
        self.diagnosticos = []
        self.raciocinio_detalhado = []
    
    def registrar_fato(self, sintoma: Sintoma, valor: bool) -> None:
        self.fatos[sintoma] = valor
    
    def inferir(self) -> List[ResultadoDiagnostico]:
        """
        Executa o ciclo de inferência:
        1. Para cada regra, verifica se condições são satisfeitas
        2. Calcula confiança usando abordagem bayesiana simplificada
        3. Ordena resultados por confiança
        """
        self.raciocinio_detalhado = []
        self.diagnosticos = []
        
        for regra in self.regras:
            resultado = self._avaliar_regra(regra)
            if resultado:
                self.diagnosticos.append(resultado)

        self.diagnosticos.sort(key=lambda x: x.confianca, reverse=True)
        return self.diagnosticos
    
    def _avaliar_regra(self, regra: Regra) -> Optional[ResultadoDiagnostico]:
        raciocinio = [f"Avaliando regra {regra.id}: {regra.nome}"]

        for condicao in regra.condicoes:
            if condicao.sintoma not in self.fatos:
                raciocinio.append(f"  ✗ Fato '{condicao.sintoma.value}' não foi coletado")
                return None 
            
            valor_observado = self.fatos[condicao.sintoma]
            valor_esperado = condicao.valor_esperado
            
            if valor_observado == valor_esperado:
                raciocinio.append(
                    f"  ✓ Condição satisfeita: {condicao.sintoma.value} = {valor_observado} "
                    f"(confiança: {condicao.confianca_condicao:.1%})"
                )
            else:
                raciocinio.append(
                    f"  ✗ Condição NOT satisfeita: {condicao.sintoma.value} = {valor_observado} "
                    f"(esperado: {valor_esperado})"
                )
                return None 
        
        confianca_condicoes = 1.0
        for condicao in regra.condicoes:
            confianca_condicoes *= condicao.confianca_condicao
        
        confianca_final = confianca_condicoes * regra.confianca_regra
        
        raciocinio.append(
            f"  → Todas as condições satisfeitas!"
        )
        raciocinio.append(
            f"  → Cálculo: {confianca_condicoes:.2f} (condições) × {regra.confianca_regra:.2f} (regra) = {confianca_final:.2f}"
        )
        raciocinio.append(
            f"  → CONCLUSÃO: {regra.conclusao} (Confiança: {confianca_final:.1%})"
        )
        
        self.raciocinio_detalhado.extend(raciocinio)
        
        return ResultadoDiagnostico(
            regra_id=regra.id,
            nome=regra.nome,
            conclusao=regra.conclusao,
            categoria=regra.categoria,
            confianca=confianca_final,
            raciocinio=raciocinio
        )


# ============================================================================
# PARTE 4: INTERFACE COM USUÁRIO
# ============================================================================

class InterfaceUsuario:
    PERGUNTAS = [
        (Sintoma.COMPUTADOR_NAO_LIGA, "O computador não liga quando você aperta o botão power?"),
        (Sintoma.FONTE_NAO_LIGADA, "A fonte de energia está conectada e ligada?"),
        (Sintoma.SEM_ENERGIA_ELETRICA, "Há energia elétrica na tomada?"),
        (Sintoma.COMPUTADOR_LENTO, "O computador está lento/travando?"),
        (Sintoma.RAM_ALTA, "A RAM está acima de 80% de uso?"),
        (Sintoma.DISCO_CHEIO, "O disco está quase cheio (>90%)?"),
        (Sintoma.SEM_INTERNET, "Você não tem acesso à internet?"),
        (Sintoma.WIFI_DESCONECTADO, "O WiFi aparece desconectado?"),
        (Sintoma.TELA_PRETA_CONGELADA, "A tela está preta ou congelada?"),
        (Sintoma.NAO_RESPONDE_TECLADO, "O computador não responde ao teclado/mouse?"),
        (Sintoma.COMPUTADOR_QUENTE, "O computador está muito quente?"),
        (Sintoma.VENTILADORES_ALTOS, "Os ventiladores estão fazendo barulho alto?"),
        (Sintoma.POP_UPS_FREQUENTES, "Aparecem muitos pop-ups na tela?"),
        (Sintoma.PROGRAMAS_ESTRANHOS, "Há programas desconhecidos instalados?"),
    ]
    
    @staticmethod
    def coletar_sintomas() -> Dict[Sintoma, bool]:
        print("\n" + "="*80)
        print("SISTEMA ESPECIALISTA - DIAGNÓSTICO DE COMPUTADOR")
        print("="*80)
        print("\nResponda as perguntas abaixo (s/n):\n")
        
        sintomas = {}
        for sintoma, pergunta in InterfaceUsuario.PERGUNTAS:
            while True:
                resposta = input(f"  {pergunta} (s/n): ").lower().strip()
                if resposta in ['s', 'n']:
                    sintomas[sintoma] = (resposta == 's')
                    break
                print("  ❌ Digite apenas 's' ou 'n'")
        
        return sintomas
    
    @staticmethod
    def apresentar_diagnosticos(diagnosticos: List[ResultadoDiagnostico]) -> None:
        if not diagnosticos:
            print("\n❌ Nenhum diagnóstico específico encontrado.")
            print("   Recomendação: Leve o computador para uma assistência técnica.")
            return
        
        print("\n" + "="*80)
        print("DIAGNÓSTICOS ENCONTRADOS (ordenados por confiança)")
        print("="*80 + "\n")
        
        for i, diag in enumerate(diagnosticos, 1):
            barra = "█" * int(diag.confianca * 20) + "░" * (20 - int(diag.confianca * 20))
            
            print(f"\n{i}. {diag.nome} [{diag.categoria.value}]")
            print(f"   Confiança: {diag.confianca:.1%} [{barra}]")
            print(f"   Solução: {diag.conclusao}")
            print(f"   Regra: {diag.regra_id}")
    
    @staticmethod
    def mostrar_raciocinio(diagnostico: ResultadoDiagnostico) -> None:
        print(f"\n📋 EXPLICAÇÃO DETALHADA - {diagnostico.nome}")
        print(f"   Confiança Final: {diagnostico.confianca:.1%}")
        print("   Raciocínio:\n")
        for linha in diagnostico.raciocinio:
            print(f"   {linha}")


# ============================================================================
# PARTE 5: SISTEMA PRINCIPAL
# ============================================================================

class SistemaEspecialista:
    def __init__(self):
        self.regras = BaseDeRegras.criar_regras()
        self.motor = MotorInferencia(self.regras)
        self.ui = InterfaceUsuario()
    
    def executar(self):
        try:
            sintomas = self.ui.coletar_sintomas()
            
            for sintoma, valor in sintomas.items():
                self.motor.registrar_fato(sintoma, valor)
            
            print("\n" + "="*80)
            print("ANALISANDO...")
            print("="*80)
            
            diagnosticos = self.motor.inferir()
            
            self.ui.apresentar_diagnosticos(diagnosticos)
            
            if diagnosticos:
                print("\n" + "="*80)
                resposta = input("\nDeseja ver a explicação detalhada do principal diagnóstico? (s/n): ")
                if resposta.lower() == 's':
                    self.ui.mostrar_raciocinio(diagnosticos[0])
            
            print("\n" + "="*80)
            print("✓ Obrigado por usar o Sistema Especialista!")
            print("="*80 + "\n")
        
        except KeyboardInterrupt:
            print("\n\n❌ Operação cancelada pelo usuário.")
        except Exception as e:
            print(f"\n❌ Erro: {e}")


# ============================================================================
# PONTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    sistema = SistemaEspecialista()
    sistema.executar()
