"""
Script para testar a aplicação Estatistinga.
Este script deve ser executado preferencialmente com:
py manage.py shell
>>> exec(open('test_aplicacao.py', encoding='utf-8').read())
"""
import os
import django
from datetime import date, timedelta
from analise.models.atleta import Atleta
from analise.models.evento import Evento
from analise.models.estatistica import Estatistica
from analise.models.esporte import Esporte 

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estatistinga.settings')
django.setup()

def limpar_dados():
    """Limpa todos os dados para começar do zero"""
    print("=" * 80)
    print("LIMPANDO DADOS ANTERIORES...")
    print("=" * 80)
    Estatistica.objects.all().delete()
    Atleta.objects.all().delete()
    Evento.objects.all().delete()
    print("Dados limpos com sucesso!\n")


def criar_atletas():
    """Cria pelo menos 3 atletas"""
    print("=" * 80)
    print("CRIANDO ATLETAS...")
    print("=" * 80)
    
    atletas = []
    
    # Atleta 1 - Corredor Brasileiro
    atleta1 = Atleta.objects.create(
        nome="João Silva Santos",
        cpf="12345678901",
        email="joao.silva@email.com",
        data_nascimento=date(2000, 5, 15),
        nacionalidade="Brasil",
        altura=1.75,
        peso=70.5,
        esporte=Esporte.CORRIDA,
        ativo=True
    )
    atletas.append(atleta1)
    print(f"-> Criado: {atleta1}")
    
    # Atleta 2 - Jogador de Futebol Argentino
    atleta2 = Atleta.objects.create(
        nome="Carlos Rodriguez Gomez",
        cpf="98765432109",
        email="carlos.rodriguez@email.com",
        data_nascimento=date(1998, 8, 20),
        nacionalidade="Argentina",
        altura=1.80,
        peso=75.0,
        esporte=Esporte.FUTEBOL,
        ativo=True
    )
    atletas.append(atleta2)
    print(f"-> Criado: {atleta2}")
    
    # Atleta 3 - Jogador de Basquete Americano
    atleta3 = Atleta.objects.create(
        nome="Michael Johnson Davis",
        cpf="11122233344",
        email="michael.johnson@email.com",
        data_nascimento=date(1995, 3, 10),
        nacionalidade="Estados Unidos",
        altura=1.98,
        peso=95.0,
        esporte=Esporte.BASQUETE,
        ativo=True
    )
    atletas.append(atleta3)
    print(f"-> Criado: {atleta3}")
    
    # Atleta 4 - Corredor Queniano
    atleta4 = Atleta.objects.create(
        nome="Kipchoge Kiptum",
        cpf="55566677788",
        email="kipchoge@email.com",
        data_nascimento=date(1997, 11, 25),
        nacionalidade="Quênia",
        altura=1.67,
        peso=52.0,
        esporte=Esporte.CORRIDA,
        ativo=True
    )
    atletas.append(atleta4)
    print(f"-> Criado: {atleta4}")
    
    print(f"\nTotal de atletas criados: {len(atletas)}\n")
    return atletas


def criar_eventos():
    """Cria pelo menos 3 eventos"""
    print("=" * 80)
    print("CRIANDO EVENTOS...")
    print("=" * 80)
    
    eventos = []
    
    # Evento 1 - Maratona do Rio (Corrida)
    evento1 = Evento.objects.create(
        nome="Maratona Internacional do Rio",
        local="Orla de Copacabana",
        cidade="Rio de Janeiro",
        pais="Brasil",
        data=date(2025, 6, 15),
        esporte=Esporte.CORRIDA,
        oficial=True,
        organizador="Federação de Atletismo",
        capacidade=5000
    )
    eventos.append(evento1)
    print(f"-> Criado: {evento1}")
    
    # Evento 2 - Campeonato Sul-Americano de Futebol
    evento2 = Evento.objects.create(
        nome="Copa Sul-Americana Sub-25",
        local="Estádio Beira-Rio",
        cidade="Porto Alegre",
        pais="Brasil",
        data=date(2025, 7, 20),
        esporte=Esporte.FUTEBOL,
        oficial=True,
        organizador="CONMEBOL",
        capacidade=50000
    )
    eventos.append(evento2)
    print(f"-> Criado: {evento2}")
    
    # Evento 3 - Torneio de Basquete
    evento3 = Evento.objects.create(
        nome="NBA Summer League Brazil",
        local="Ginásio do Ibirapuera",
        cidade="São Paulo",
        pais="Brasil",
        data=date(2025, 8, 10),
        esporte=Esporte.BASQUETE,
        oficial=False,
        organizador="NBA Brasil",
        capacidade=15000
    )
    eventos.append(evento3)
    print(f"-> Criado: {evento3}")
    
    # Evento 4 - Corrida de Rua
    evento4 = Evento.objects.create(
        nome="Corrida de São Silvestre",
        local="Avenida Paulista",
        cidade="São Paulo",
        pais="Brasil",
        data=date(2024, 12, 31),
        esporte=Esporte.CORRIDA,
        oficial=True,
        organizador="Fundação Cásper Líbero",
        capacidade=30000
    )
    eventos.append(evento4)
    print(f"-> Criado: {evento4}")
    
    print(f"\nTotal de eventos criados: {len(eventos)}\n")
    return eventos


def criar_estatisticas(atletas, eventos):
    """Cria pelo menos 5 estatísticas relacionando atletas e eventos"""
    print("=" * 80)
    print("CRIANDO ESTATÍSTICAS...")
    print("=" * 80)
    
    estatisticas = []
    
    # Estatística 1 - João (Corrida/Brasil) na Maratona do Rio (Brasil) - 1o lugar (OFICIAL)
    est1 = Estatistica.objects.create(
        atleta=atletas[0],    # João - Corredor
        evento=eventos[0],    # Maratona do Rio
        pontuacao=1,          # 1o lugar (Melhor para corrida)
        distancia=42.195,
        observacoes="Vencedor da maratona com tempo recorde"
    )
    estatisticas.append(est1)
    print(f"-> Criada: {est1}")
    
    # Estatística 2 - Carlos (Futebol/Argentina) no Campeonato Sul-Americano (Brasil) - ESTRANGEIRO
    est2 = Estatistica.objects.create(
        atleta=atletas[1],    # Carlos - Futebol
        evento=eventos[1],    # Copa Sul-Americana
        pontuacao=2,          # 2 gols (Maior para futebol)
        assistencias=3,
        faltas=1,
        cartoes="Amarelo",
        minutos_jogados=90,
        observacoes="Melhor em campo, contribuiu com 2 gols e 3 assistências."
    )
    estatisticas.append(est2)
    print(f"-> Criada: {est2}")
    
    # Estatística 3 - Michael (Basquete/EUA) na NBA Summer League Brazil (Brasil) - ESTRANGEIRO (NÃO OFICIAL)
    est3 = Estatistica.objects.create(
        atleta=atletas[2],    # Michael - Basquete
        evento=eventos[2],    # NBA Summer League Brazil
        pontuacao=35,         # 35 pontos (Maior para basquete)
        assistencias=10,
        minutos_jogados=38,
        observacoes="Maior pontuador da partida, evento não oficial"
    )
    estatisticas.append(est3)
    print(f"-> Criada: {est3}")
    
    # Estatística 4 - Kipchoge (Corrida/Quênia) na São Silvestre (Brasil) - 1o lugar (OFICIAL) - ESTRANGEIRO
    est4 = Estatistica.objects.create(
        atleta=atletas[3],    # Kipchoge - Corredor Queniano
        evento=eventos[3],    # Corrida de São Silvestre
        pontuacao=1,          # 1o lugar
        distancia=15.0,
        observacoes="Vencedor da São Silvestre."
    )
    estatisticas.append(est4)
    print(f"-> Criada: {est4}")
    
    # Estatística 5 - João (Corrida/Brasil) na São Silvestre (Brasil) - 3o lugar (OFICIAL)
    est5 = Estatistica.objects.create(
        atleta=atletas[0],    # João - Corredor Brasileiro
        evento=eventos[3],    # Corrida de São Silvestre
        pontuacao=3,          # 3o lugar
        distancia=15.0,
        observacoes="Bom desempenho, mas ficou em 3o."
    )
    estatisticas.append(est5)
    print(f"-> Criada: {est5}")
    
    print(f"\nTotal de estatísticas criadas: {len(estatisticas)}\n")
    return estatisticas


# --------------------------------------------------------------------------------------------------

def executar_testes(atletas, eventos):
    """Executa os testes para os métodos dos Managers customizados"""
    print("=" * 80)
    print("EXECUTANDO TESTES DE CONSULTA (MANAGERS)...")
    print("=" * 80)
    
    # --- VARIÁVEIS DE TESTE ---
    data_passada = date(2024, 1, 1) 
    
    # --- 1. Testar AtletaManager.buscar_corredores_vencedores ---
    print("\n--- TESTE 1: Corredores Vencedores (pontuacao=1) desde 01/01/2024 ---")
    vencedores = Atleta.objects.buscar_corredores_vencedores(data=data_passada)
    nomes_vencedores = [a.nome for a in vencedores]
    print(f"Resultado ({len(vencedores)}): {nomes_vencedores}")
    
    assert len(vencedores) == 2, f"Erro: Esperava 2 corredores vencedores, encontrou {len(vencedores)}"
    assert atletas[0].nome in nomes_vencedores, "Erro: João não listado como vencedor de corrida"
    assert atletas[3].nome in nomes_vencedores, "Erro: Kipchoge não listado como vencedor de corrida"
    print("-> Teste 1 (Corredores Vencedores) OK.")
    
    # --- 2. Testar AtletaManager.buscar_maiores_pontuadores_eventos_oficiais (Corrida) ---
    print("\n--- TESTE 2: Maiores Pontuadores em Eventos Oficiais (Corrida) ---")
    
    # Para CORRIDA, maior pontuador tem a menor pontuação (1o lugar = 1)
    maiores_pontuadores_corrida = Atleta.objects.buscar_maiores_pontuadores_eventos_oficiais(Esporte.CORRIDA)
    nomes_maiores_corrida = [a.nome for a in maiores_pontuadores_corrida]
    print(f"Resultado ({len(maiores_pontuadores_corrida)}): {nomes_maiores_corrida}")
    
    assert len(maiores_pontuadores_corrida) == 2, f"Erro: Esperava 2 atletas com melhor pontuação (1), encontrou {len(maiores_pontuadores_corrida)}"
    print("-> Teste 2 (Maiores Pontuadores Corrida) OK.")
    
    # --- 3. Testar AtletaManager.buscar_maiores_pontuadores_eventos_oficiais (Futebol) ---
    print("\n--- TESTE 3: Maiores Pontuadores em Eventos Oficiais (Futebol) ---")
    
    # Para FUTEBOL, maior pontuador tem a maior pontuação (2 gols)
    maiores_pontuadores_futebol = Atleta.objects.buscar_maiores_pontuadores_eventos_oficiais(Esporte.FUTEBOL)
    nomes_maiores_futebol = [a.nome for a in maiores_pontuadores_futebol]
    print(f"Resultado ({len(maiores_pontuadores_futebol)}): {nomes_maiores_futebol}")
    
    assert len(maiores_pontuadores_futebol) == 1, f"Erro: Esperava 1 atleta de futebol, encontrou {len(maiores_pontuadores_futebol)}"
    assert atletas[1].nome in nomes_maiores_futebol, "Erro: Carlos não listado como maior pontuador de futebol"
    print("-> Teste 3 (Maiores Pontuadores Futebol) OK.")

    # --- 4. Testar EventoManager.buscar_evento_participantes_estrangeiros ---
    print("\n--- TESTE 4: Eventos com Participantes Estrangeiros desde 01/01/2024 ---")
    
    eventos_estrangeiros = Evento.objects.buscar_evento_participantes_estrangeiros(data=data_passada)
    nomes_eventos_estrangeiros = [e.nome for e in eventos_estrangeiros]
    print(f"Resultado ({len(eventos_estrangeiros)}): {nomes_eventos_estrangeiros}")
    
    assert len(eventos_estrangeiros) == 3, f"Erro: Esperava 3 eventos com estrangeiros, encontrou {len(eventos_estrangeiros)}"
    assert eventos[1].nome in nomes_eventos_estrangeiros, "Erro: Copa Sul-Americana não listado"
    assert eventos[2].nome in nomes_eventos_estrangeiros, "Erro: NBA Summer League Brazil não listado"
    assert eventos[3].nome in nomes_eventos_estrangeiros, "Erro: Corrida de São Silvestre não listado"
    print("-> Teste 4 (Eventos c/ Estrangeiros) OK.")
    
    # --- 5. Testar AtletaManager.buscar_participantes ---
    print("\n--- TESTE 5: Participantes do Evento: Corrida de São Silvestre ---")
    
    participantes_ss = Atleta.objects.buscar_participantes(evento=eventos[3])
    nomes_participantes_ss = [a.nome for a in participantes_ss]
    print(f"Resultado ({len(participantes_ss)}): {nomes_participantes_ss}")
    
    assert len(participantes_ss) == 2, f"Erro: Esperava 2 participantes, encontrou {len(participantes_ss)}"
    assert atletas[0].nome in nomes_participantes_ss, "Erro: João não listado como participante"
    assert atletas[3].nome in nomes_participantes_ss, "Erro: Kipchoge não listado como participante"
    print("-> Teste 5 (Participantes do Evento) OK.")
    
    print("\n" + "=" * 80)
    print("TODOS OS TESTES DE CONSULTA CONCLUÍDOS COM SUCESSO!")
    print("=" * 80 + "\n")


# --------------------------------------------------------------------------------------------------
# IMPLEMENTAÇÃO DO RELATÓRIO FINAL (REQUISITO H.V)
# --------------------------------------------------------------------------------------------------

def imprimir_relatorio_estatisticas():
    """
    Imprime um relatório das estatísticas agrupadas por atleta e ordenadas pela data do evento.
    (Requisito h.v do PDF)
    """
    print("=" * 80)
    print("RELATÓRIO FINAL: ESTATÍSTICAS POR ATLETA")
    print("=" * 80)
    
    # Consulta: Seleciona todas as estatísticas, pré-carrega Atleta e Evento (select_related)
    # Ordena: Pelo nome do atleta (agrupamento) e pela data do evento (ordenação)
    estatisticas = Estatistica.objects.all().select_related('atleta', 'evento').order_by('atleta__nome', 'evento__data')
    
    atleta_atual = None
    
    for est in estatisticas:
        # Se o atleta mudar, imprime o cabeçalho do novo grupo
        if est.atleta.nome != atleta_atual:
            print(f"\n--- ATLETA: {est.atleta.nome} ({est.atleta.esporte}) ---")
            atleta_atual = est.atleta.nome
        
        # Imprime os detalhes da estatística
        # Formato DD/MM/AAAA conforme a prova
        data_evento = est.evento.data.strftime('%d/%m/%Y') 
        print(f"  > Evento: {est.evento.nome} ({data_evento})")
        # Pega a primeira linha da observação para ser conciso no relatório
        print(f"    - Pontuação: {est.pontuacao} | Observação: {est.observacoes.splitlines()[0] if est.observacoes else 'N/A'}")
        
    print("\n" + "=" * 80)
    print("FIM DO RELATÓRIO.")
    print("=" * 80 + "\n")


# --------------------------------------------------------------------------------------------------

# --- BLOCO PRINCIPAL DE EXECUÇÃO ---
if __name__ == "__main__":
    
    try:
        limpar_dados()
        
        atletas_criados = criar_atletas()
        eventos_criados = criar_eventos()
        
        # Criação de estatísticas (Requisito h.iii)
        criar_estatisticas(atletas_criados, eventos_criados)
            
        # Executa a bateria de testes de consulta (Requisito g.i a g.iv)
        executar_testes(atletas_criados, eventos_criados)
        
        # Imprime o relatório de estatísticas (Requisito h.v)
        imprimir_relatorio_estatisticas()
        
    except Exception as e:
        print(f"\n!!! ERRO CRÍTICO DURANTE A EXECUÇÃO DO SCRIPT !!!\nDetalhes: {e}")
        print("Certifique-se de que os Managers e Models estão configurados corretamente.")