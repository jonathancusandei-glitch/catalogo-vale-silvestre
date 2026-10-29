import os
import shutil
import html
import urllib.parse
import json

src_base = r"G:\Meu Drive\01 - Profissional e Negócios\Vale Silvestre\Fotos_Selecionadas_Desbravador_Site\00_Selecao_Resumida_Para_Envio"
site_dir = r"C:\Users\danie\vale-silvestre-catalogo"
img_dest_root = os.path.join(site_dir, "img")

# Accommodation & Experience Catalog Definition
# Tailored to be 100% contextual (no door signs or "chalé" buttons on Leisure/Food!)
items = [
    {
        "id": "panoramico-02",
        "category": "panoramicos",
        "category_label": "Chalé Panorâmico",
        "badge": "Mais Procurado • Vista Panorâmica 360°",
        "title": "Chalé Panorâmico — Piso 02 Superior",
        "tag_label": "🏷️ Placa na Porta: Arara",
        "capacity_label": "👥 Casal + 2 camas de solteiro (acomoda até 4 pessoas)",
        "btn_text": "💬 Consultar Disponibilidade deste Chalé",
        "wa_msg": "Olá! Estou vendo o catálogo oficial do Vale Silvestre e gostaria de consultar a disponibilidade do *Chalé Panorâmico — Piso 02 Superior*!",
        "desc": "Localizado no ponto mais nobre da colina com rampa suave de madeira. Possui pé-direito alto, ambiente super arejado e uma varanda panorâmica de madeira privativa com a vista mais deslumbrante de todo o lago e das montanhas. Uma experiência romântica e inesquecível!",
        "features": ["Varanda Panorâmica 360°", "Vista Privilegiada da Lagoa", "Cama Box de Casal", "2 Camas de Solteiro", "TV LCD", "Frigobar", "Ventilador de Teto", "Banheiro Privativo"],
        "src_folder": "06_Chale_Panoramico_Piso_02",
        "dest_folder": "chale-panoramico-piso-02",
        "allowed_files": [
            ("03_Quarto_Casal_Coracao_Toalha_e_Petalas.jpg", "Cama de Casal com Coração de Pétalas"),
            ("04_Detalhe_Cama_com_Carta_Boas_Vindas.jpg", "Mimo de Boas-Vindas Vale Silvestre"),
            ("05_Quarto_Amplo_com_Camas_Solteiro_e_TV.jpg", "Quarto Amplo e Aconchegante"),
            ("06_Bancada_da_Pia_Decorada_com_Flores.jpg", "Bancada da Pia com Flores Naturais"),
            ("07_Varanda_de_Madeira_Mesa_sobre_a_Lagoa.jpg", "Varanda Panorâmica Debruçada na Lagoa"),
            ("08_Vista_Panoramica_Espetacular_da_Lagoa.jpg", "Vista Espetacular da Lagoa e Natureza")
        ]
    },
    {
        "id": "panoramico-01",
        "category": "panoramicos",
        "category_label": "Chalé Panorâmico",
        "badge": "Acesso Plano • Varanda com Jardim",
        "title": "Chalé Panorâmico — Piso 01 Térreo",
        "tag_label": "🏷️ Placa na Porta: Orquídea e Paraju",
        "capacity_label": "👥 Casal + 2 camas de solteiro (acomoda até 4 pessoas)",
        "btn_text": "💬 Consultar Disponibilidade deste Chalé",
        "wa_msg": "Olá! Estou vendo o catálogo oficial do Vale Silvestre e gostaria de consultar a disponibilidade do *Chalé Panorâmico — Piso 01 Térreo*!",
        "desc": "Conforto absoluto com acesso térreo direto, perfeito para quem busca comodidade e acessibilidade sem escadas. Conta com hall de entrada com poema decorativo, varanda ampla com jardim e vista charmosa.",
        "features": ["Acesso Térreo Plano (Sem Escadas)", "Varanda com Jardim", "Hall com Poema Rústico", "Cama Box de Casal", "2 Camas de Solteiro", "TV LCD", "Frigobar", "Banheiro Privativo"],
        "src_folder": "05_Chale_Panoramico_Piso_01",
        "dest_folder": "chale-panoramico-piso-01",
        "allowed_files": [
            ("01_Fachada_dos_Chales_Panoramicos_na_Colina.jpg", "Fachada dos Chalés Panorâmicos na Colina"),
            ("02_Entrada_Terreo_e_Placa_Orquidea.jpg", "Entrada Térrea com Placa Orquídea"),
            ("03_Hall_com_Poema_na_Parede_e_Mesa_Rustica.jpg", "Hall com Poema e Decoração Rústica"),
            ("04_Quarto_com_Cama_Casal_e_Solteiro.jpg", "Quarto Confortável Casal e Solteiro"),
            ("05_Quarto_Decoracao_Romantica_com_Petalas.jpg", "Decoração Romântica Especial"),
            ("06_Bancada_da_Pia_Granito_Preto.jpg", "Bancada da Pia com Cestinha de Amenities")
        ]
    },
    {
        "id": "lago-01",
        "category": "lago",
        "category_label": "Chalés do Lago",
        "badge": "Em Frente ao Lago • Quarto e Sala",
        "title": "Chalé do Lago — 01 Quarto e Sala",
        "tag_label": "🏷️ Placa na Porta: Bouganville",
        "capacity_label": "👥 Até 5 pessoas (Quarto com cama de casal + solteiro | Sala com 2 sofás-cama)",
        "btn_text": "💬 Consultar Disponibilidade deste Chalé",
        "wa_msg": "Olá! Estou vendo o catálogo oficial do Vale Silvestre e gostaria de consultar a disponibilidade do *Chalé do Lago — 01 Quarto e Sala*!",
        "desc": "Localização paradisíaca às margens da lagoa e coladinho ao restaurante principal. A divisão entre quarto privativo e sala de estar ampla oferece total privacidade aos pais enquanto as crianças dormem confortavelmente na sala. Varanda charmosa de frente para a água!",
        "features": ["Em Frente à Lagoa", "Ao Lado do Restaurante", "Quarto Privativo", "Sala de Estar com Sofás-Cama", "Geladeira", "Bancada Americana", "Varanda com Vista da Água"],
        "src_folder": "03_Chale_do_Lago_Quarto_e_Sala",
        "dest_folder": "chale-do-lago-1-quarto",
        "allowed_files": [
            ("01_Varanda_Beira_do_Lago_Placa_Bouganville.jpg", "Varanda na Beira do Lago"),
            ("06_Fachada_Geral_Chales_do_Lago.jpg", "Vista Geral dos Chalés do Lago"),
            ("02_Sala_de_Estar_com_Sofas_Cama.jpg", "Sala de Estar Ampla com Sofás-Cama"),
            ("03_Bancada_Americana_e_Geladeira.jpg", "Bancada Americana e Geladeira"),
            ("04_Quarto_Cama_de_Casal_e_Solteiro.jpg", "Quarto Privativo Casal e Solteiro")
        ]
    },
    {
        "id": "lago-02",
        "category": "lago",
        "category_label": "Chalés do Lago",
        "badge": "Espaço Família • 2 Quartos Privativos",
        "title": "Chalé do Lago — 02 Quartos e Sala",
        "tag_label": "🏷️ Placa na Porta: Bromélia e Gameleira",
        "capacity_label": "👥 Até 7 pessoas (Quarto 1: casal + solteiro | Quarto 2: 3 solteiro | Sala: 2 sofás-cama)",
        "btn_text": "💬 Consultar Disponibilidade deste Chalé",
        "wa_msg": "Olá! Estou vendo o catálogo oficial do Vale Silvestre e gostaria de consultar a disponibilidade do *Chalé do Lago — 02 Quartos e Sala*!",
        "desc": "A maior acomodação da pousada, projetada com carinho para famílias grandes ou pequenos grupos. Conta com dois dormitórios independentes, sala espaçosa com sofás-cama, frigobar retrô Coca-Cola e varanda com brisa refrescante do lago.",
        "features": ["2 Quartos Privativos", "Acomoda até 7 Pessoas", "Sala com Sofás-Cama", "Frigobar Retrô Coca-Cola", "Bancada e Pia", "Varanda na Beira do Lago", "Excelente Conforto"],
        "src_folder": "04_Chale_do_Lago_2_Quartos_e_Sala",
        "dest_folder": "chale-do-lago-2-quartos",
        "allowed_files": [
            ("01_Varanda_Externa_e_Placa_Bromelia.jpg", "Varanda Externa com Vista do Lago"),
            ("07_Varanda_com_Vista_para_o_Lago.jpg", "Varanda Privativa na Margem da Lagoa"),
            ("02_Sala_de_Estar_com_Sofas_Cama.jpg", "Sala de Estar Aconchegante"),
            ("03_Bancada_Pia_e_Frigobar_Retro_CocaCola.jpg", "Bancada Americana e Frigobar Retrô"),
            ("04_Quarto_01_Casal_e_Solteiro.jpg", "Quarto Principal Casal com Decoração"),
            ("05_Quarto_02_Tres_Camas_Solteiro.jpg", "Segundo Quarto com 3 Camas de Solteiro")
        ]
    },
    {
        "id": "suite-central",
        "category": "suites",
        "category_label": "Suítes",
        "badge": "Ótimo Custo-Benefício • Localização Central",
        "title": "Suíte Central",
        "tag_label": "🏷️ Placa na Porta: Braúna",
        "capacity_label": "👥 Casal + 2 camas de solteiro (acomoda até 4 pessoas)",
        "btn_text": "💬 Consultar Disponibilidade desta Suíte",
        "wa_msg": "Olá! Estou vendo o catálogo oficial do Vale Silvestre e gostaria de consultar a disponibilidade da *Suíte Central*!",
        "desc": "Acomodação acolhedora situada próxima à praça central e ao restaurante. Excelente opção de custo-benefício com cama de casal, duas de solteiro, frigobar, TV LCD e varanda térrea com jardim.",
        "features": ["Próxima ao Restaurante", "Cama de Casal + 2 Solteiro", "TV LCD", "Frigobar", "Banheiro com Gabinete de Madeira", "Varanda Térrea"],
        "src_folder": "02_Suite_Central",
        "dest_folder": "suite-central",
        "allowed_files": [
            ("01_Varanda_Externa_e_Placa_Brauna.jpg", "Varanda Térrea com Placa Braúna"),
            ("02_Cama_de_Casal_com_Almofadas_Coracao.jpg", "Cama de Casal com Almofadas de Coração"),
            ("03_Quarto_com_Camas_de_Solteiro_e_TV.jpg", "Quarto Arejado com Camas de Solteiro e TV"),
            ("04_Visao_Ampla_do_Quarto.jpg", "Visão Ampla e Iluminação Natural"),
            ("05_Banheiro_Gabinete_Madeira.jpg", "Bancada com Gabinete Rústico de Madeira")
        ]
    },
    {
        "id": "suite-mangueira",
        "category": "suites",
        "category_label": "Suítes",
        "badge": "Grande Porte • Até 7 Pessoas",
        "title": "Suíte Mangueira",
        "tag_label": "🏷️ Placa na Porta: Paca e Jaguatirica",
        "capacity_label": "👥 Casal + 2 beliches de madeira + 1 solteiro (acomoda até 7 pessoas)",
        "btn_text": "💬 Consultar Disponibilidade desta Suíte",
        "wa_msg": "Olá! Estou vendo o catálogo oficial do Vale Silvestre e gostaria de consultar a disponibilidade da *Suíte Mangueira*!",
        "desc": "Suíte espaçosa em meio a uma área verde tranquila e sombreada por mangueiras nativas. Muito confortável para famílias que desejam ficar juntas no mesmo ambiente.",
        "features": ["Espaço para até 7 Pessoas", "1 Cama Casal + 2 Beliches", "Banheiro Privativo", "Área Verde Tranquila", "Ideal para Grupos e Famílias"],
        "src_folder": "01_Suite_Mangueira",
        "dest_folder": "suite-mangueira",
        "allowed_files": [
            ("01_Fachada_e_Placa_Paca.jpg", "Fachada Rústica com Pintura da Flora"),
            ("07_Entrada_e_Jardim_Mangueira.jpg", "Entrada Arborizada sob Mangueiras Nativas"),
            ("02_Quarto_Geral_Casal_e_Beliches.jpg", "Quarto Familiar Amplo para até 7 Pessoas"),
            ("03_Cama_de_Casal_Principal.jpg", "Cama de Casal com Enxoval Branco"),
            ("04_Beliches_de_Madeira_e_Cama_Solteiro.jpg", "Beliches de Madeira Maciça")
        ]
    },
    {
        "id": "lazer-natureza",
        "category": "lazer",
        "category_label": "Lazer & Natureza",
        "badge": "Incluso em Todas as Diárias",
        "title": "Lazer Completo, Lagoa & Atrações",
        "tag_label": "🌳 Estrutura & Atrações ao Ar Livre",
        "capacity_label": "✨ 100% Liberado e Incluso em Todas as Hospedagens",
        "btn_text": "💬 Consultar Pacotes com Lazer Liberado",
        "wa_msg": "Olá! Vi as opções de lazer e atrações no catálogo e gostaria de consultar os pacotes de hospedagem do Vale Silvestre!",
        "desc": "Viva momentos mágicos ao ar livre! O parque oferece passeios livres de caiaque e pedalinhos (cisne e dragão), ponte pênsil suspensa, deck com iluminação noturna, píer com moldura de coração para fotos, balanço na árvore gigante, pesca esportiva e trilhas ecológicas.",
        "features": ["Passeio de Caiaque", "Pedalinho Cisne & Dragão", "Deck Panorâmico Iluminado", "Ponte Pênsil Suspensa", "Píer Moldura Coração", "Balanço na Árvore Gigante", "Pesca Esportiva", "Trilhas Ecológicas"],
        "src_folder": "08_Lazer_Lagoa_Deck_e_Natureza",
        "dest_folder": "lazer-natureza",
        "allowed_files": [
            ("01_Deck_de_Madeira_sobre_o_Lago_com_Varal_Luzes.jpg", "Deck de Madeira com Iluminação Noturna"),
            ("02_Passeio_de_Caiaque_no_Lago.jpg", "Passeio de Caiaque no Lago"),
            ("03_Pedalinho_Cisne_na_Lagoa.jpg", "Pedalinho Cisne na Lagoa"),
            ("04_Pedalinho_Dragao_na_Lagoa.jpg", "Pedalinho Dragão Divertido"),
            ("05_Ponte_Pensil_Suspensa_sobre_o_Lago.jpg", "Ponte Pênsil Suspensa"),
            ("06_Pier_com_Moldura_de_Coracao_Fotos.jpg", "Píer Moldura Coração para Fotos"),
            ("07_Arvore_Gigante_com_Balanco_e_Pergolados.jpg", "Balanço na Árvore Gigante"),
            ("08_Portaria_e_Entrada_Vale_Silvestre_Eco_Park.jpg", "Portaria do Parque Ecológico")
        ]
    },
    {
        "id": "gastronomia",
        "category": "gastronomia",
        "category_label": "Gastronomia Mineira",
        "badge": "Pensão Completa Inclusa",
        "title": "Gastronomia Mineira & Restaurante",
        "tag_label": "🍽️ Culinária Típica Mineira em Panelas de Barro",
        "capacity_label": "🍲 Jantar, Café da Manhã e Almoço com Sobremesas Inclusos",
        "btn_text": "💬 Consultar Pacotes com Pensão Completa",
        "wa_msg": "Olá! Vi as fotos da gastronomia no catálogo e gostaria de consultar os pacotes com pensão completa inclusa!",
        "desc": "A autêntica tradição mineira servida com fartura e carinho! Desfrute de buffet completo com pratos tradicionais servidos em panelas de barro, sobremesas caseiras deliciosas, farto café da manhã com bolos artesanais e quitandas, além de música ao vivo no almoço aos fins de semana.",
        "features": ["Pensão Completa Inclusa", "Panelas de Barro Tradicionais", "Sobremesas Típicas", "Café da Manhã Farto", "Bolos e Quitandas Caseiras", "Música ao Vivo aos Fins de Semana", "Salão e Varanda com Vista"],
        "src_folder": "09_Gastronomia_Restaurante_Buffet",
        "dest_folder": "gastronomia",
        "allowed_files": [
            ("01_Buffet_Comida_Tipica_Panelas_de_Barro.jpg", "Buffet Mineiro em Panelas de Barro"),
            ("02_Pratos_Mineiros_Tradicionais_e_Saladas.jpg", "Pratos Mineiros Tradicionais e Saladas"),
            ("03_Cafe_da_Manha_Bolos_Caseiros_do_Vale.jpg", "Café da Manhã com Bolos Caseiros"),
            ("04_Bolo_de_Fuba_e_Quitandas_Mineiras.jpg", "Quitandas e Bolos Tradicionais"),
            ("05_Salao_e_Varanda_do_Restaurante.jpg", "Salão e Varanda do Restaurante"),
            ("06_Musica_ao_Vivo_no_Quiosque_do_Almoco.jpg", "Música ao Vivo no Almoço")
        ]
    }
]

# Copy approved photos
for item in items:
    src_dir = os.path.join(src_base, item["src_folder"])
    dest_dir = os.path.join(img_dest_root, item["dest_folder"])
    os.makedirs(dest_dir, exist_ok=True)
    item_photos = []
    for idx, (orig_file, title) in enumerate(item["allowed_files"], 1):
        clean_name = f"foto_{idx:02d}.jpg"
        item_photos.append({
            "rel_path": f"img/{item['dest_folder']}/{clean_name}",
            "title": title,
            "clean_name": clean_name
        })
    item["photos"] = item_photos

# Generate index.html matching EXACTLY valesilvestre.com.br
html_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Catálogo Oficial de Acomodações & Lazer — Pousada Vale Silvestre Ecopark</title>
  <meta name="description" content="Conecte-se à Natureza, Viva Experiências Inesquecíveis. Conheça nossos chalés, gastronomia típica e parque ecológico em Governador Valadares/MG.">
  <meta name="theme-color" content="#395902">
  <meta property="og:title" content="Catálogo Oficial de Acomodações — Vale Silvestre Ecopark">
  <meta property="og:description" content="Chalés aconchegantes com vista para a lagoa, pensão completa e lazer liberado em Governador Valadares/MG.">
  <meta property="og:image" content="img/logo_branca.png">
  <meta property="og:type" content="website">
  
  <!-- GOOGLE FONTS FROM VALESILVESTRE.COM.BR -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Semi+Condensed:wght@400;500;600;700;800&family=DM+Sans:wght@400;500;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <style>
    :root {
      /* PALETA OFICIAL VALE SILVESTRE */
      --vs-forest-green: #395902;     /* Verde Principal Elementor Kit */
      --vs-dark-green: #284001;       /* Verde Escuro / Fundo Banner / Rodapé */
      --vs-night-green: #0D1A00;      /* Verde Profundo */
      --vs-gold: #FBB03B;             /* Amarelo Dourado Oficial (Botões/Destaques) */
      --vs-gold-hover: #E59B24;       /* Dourado Escuro no Hover */
      --vs-light-green: #85CF04;      /* Verde Folha Vivo no Hover */
      --vs-beige: #F2EFEB;            /* Areia Suave / Background Secundário */
      --vs-offwhite: #F5F5F7;         /* Fundo Limpo da Página */
      --vs-card-bg: #FFFFFF;          /* Fundo dos Cards */
      --vs-card-border: #E5E9DC;      /* Borda Suave */
      --vs-text-dark: #22252A;        /* Títulos Escuros */
      --vs-text-muted: #717580;       /* Texto Descritivo Oficial */
      --vs-whatsapp: #25D366;
      
      /* FONTES OFICIAIS */
      --font-heading: "Barlow Semi Condensed", sans-serif;
      --font-body: "Inter", "DM Sans", sans-serif;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }
    
    body {
      font-family: var(--font-body);
      background-color: var(--vs-offwhite);
      color: var(--vs-text-muted);
      line-height: 1.5;
      padding-bottom: 95px;
      overflow-x: hidden;
    }

    .container {
      width: 100%;
      max-width: 860px;
      margin: 0 auto;
      padding: 0 16px;
    }

    /* HEADER OFICIAL NO PADRÃO VALESILVESTRE.COM.BR */
    .hero-header {
      background: linear-gradient(135deg, #284001 0%, #395902 65%, #466e03 100%);
      padding: 36px 16px 28px;
      text-align: center;
      color: #fff;
      position: relative;
      box-shadow: 0 4px 20px rgba(40, 64, 1, 0.25);
    }
    .header-logo-wrap {
      margin-bottom: 16px;
    }
    .header-logo {
      max-width: 220px;
      height: auto;
      display: inline-block;
    }
    .badge-nature {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(251, 176, 59, 0.2);
      border: 1px solid var(--vs-gold);
      color: #FFF;
      font-family: var(--font-heading);
      font-size: 13px;
      font-weight: 600;
      padding: 5px 14px;
      border-radius: 20px;
      margin-bottom: 12px;
      text-transform: uppercase;
      letter-spacing: 0.8px;
    }
    .hero-title {
      font-family: var(--font-heading);
      font-size: 32px;
      font-weight: 700;
      color: #FFFFFF;
      letter-spacing: -0.5px;
      margin-bottom: 6px;
      line-height: 1.15;
      text-transform: uppercase;
    }
    .hero-subtitle {
      font-size: 15px;
      color: #F2EFEB;
      max-width: 580px;
      margin: 0 auto 18px;
      line-height: 1.5;
    }
    .hero-highlights {
      display: flex;
      justify-content: center;
      gap: 10px;
      flex-wrap: wrap;
    }
    .highlight-pill {
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.22);
      color: #FFFFFF;
      font-family: var(--font-heading);
      font-size: 13px;
      font-weight: 600;
      padding: 6px 14px;
      border-radius: 6px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      text-transform: uppercase;
      letter-spacing: 0.4px;
    }

    /* STICKY FILTER BAR */
    .sticky-filter-wrapper {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--vs-card-border);
      padding: 10px 0;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04);
    }
    .filter-scroll {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding: 4px 16px;
      scrollbar-width: none;
      -webkit-overflow-scrolling: touch;
    }
    .filter-scroll::-webkit-scrollbar { display: none; }
    .filter-btn {
      background: var(--vs-beige);
      border: 1px solid #E1DEC8;
      color: var(--vs-forest-green);
      padding: 8px 18px;
      border-radius: 24px;
      font-family: var(--font-heading);
      font-size: 14px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      white-space: nowrap;
      cursor: pointer;
      transition: all 0.25s ease;
    }
    .filter-btn:hover, .filter-btn.active {
      background: var(--vs-forest-green);
      color: #FFFFFF;
      border-color: var(--vs-forest-green);
      box-shadow: 0 4px 12px rgba(57, 89, 2, 0.25);
    }

    /* CATALOG FEED */
    .catalog-feed {
      margin-top: 24px;
      display: flex;
      flex-direction: column;
      gap: 28px;
    }

    .room-card {
      background: var(--vs-card-bg);
      border: 1px solid var(--vs-card-border);
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 10px 30px rgba(57, 89, 2, 0.08);
      transition: transform 0.2s, box-shadow 0.2s;
    }
    .room-card:hover {
      box-shadow: 0 14px 38px rgba(57, 89, 2, 0.14);
    }

    /* CAROUSEL / MAIN IMAGE */
    .card-gallery-wrap {
      position: relative;
      background: #111;
    }
    .main-photo-link {
      display: block;
      position: relative;
      width: 100%;
      height: 260px;
      overflow: hidden;
      cursor: pointer;
    }
    @media (min-width: 600px) {
      .main-photo-link { height: 360px; }
    }
    .main-photo-link img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.4s ease;
    }
    .room-card:hover .main-photo-link img {
      transform: scale(1.03);
    }
    .top-badge {
      position: absolute;
      top: 14px;
      left: 14px;
      background: var(--vs-forest-green);
      color: #FFFFFF;
      font-family: var(--font-heading);
      font-size: 12px;
      font-weight: 700;
      padding: 5px 12px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      z-index: 2;
      box-shadow: 0 2px 8px rgba(0,0,0,0.3);
    }
    .photo-count-btn {
      position: absolute;
      bottom: 14px;
      right: 14px;
      background: rgba(40, 64, 1, 0.85);
      backdrop-filter: blur(8px);
      color: #fff;
      border: 1px solid rgba(255, 255, 255, 0.3);
      font-family: var(--font-heading);
      font-size: 13px;
      font-weight: 600;
      text-transform: uppercase;
      padding: 7px 14px;
      border-radius: 20px;
      display: flex;
      align-items: center;
      gap: 6px;
      z-index: 2;
      cursor: pointer;
    }

    /* THUMBNAILS ROW */
    .thumbs-row {
      display: flex;
      gap: 8px;
      padding: 12px 16px;
      overflow-x: auto;
      background: #F8FAF5;
      border-bottom: 1px solid var(--vs-card-border);
      scrollbar-width: none;
    }
    .thumbs-row::-webkit-scrollbar { display: none; }
    .thumb-item {
      width: 68px;
      height: 54px;
      border-radius: 6px;
      overflow: hidden;
      flex-shrink: 0;
      cursor: pointer;
      border: 2px solid transparent;
      transition: all 0.2s;
    }
    .thumb-item:hover, .thumb-item.active {
      border-color: var(--vs-forest-green);
      transform: scale(1.06);
    }
    .thumb-item img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    /* CARD BODY */
    .card-body {
      padding: 24px;
    }
    .card-header-info {
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-bottom: 14px;
    }
    .door-sign-tag {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: var(--vs-forest-green);
      font-family: var(--font-heading);
      font-size: 13px;
      font-weight: 700;
      background: var(--vs-beige);
      padding: 4px 12px;
      border-radius: 4px;
      align-self: flex-start;
      border: 1px solid #E1DEC8;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .room-title {
      font-family: var(--font-heading);
      font-size: 24px;
      font-weight: 700;
      color: var(--vs-forest-green);
      line-height: 1.25;
      margin-top: 4px;
    }
    .capacity-tag {
      color: var(--vs-gold);
      font-family: var(--font-heading);
      font-size: 15px;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .room-desc {
      color: var(--vs-text-muted);
      font-size: 14.5px;
      line-height: 1.6;
      margin: 12px 0 18px;
    }

    /* FEATURES GRID */
    .features-list {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 22px;
    }
    .feature-chip {
      background: var(--vs-offwhite);
      border: 1px solid var(--vs-card-border);
      color: #4A4E57;
      font-family: var(--font-heading);
      font-size: 13px;
      font-weight: 600;
      padding: 5px 12px;
      border-radius: 4px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    /* CARD ACTION BUTTON */
    .btn-reserve-card {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      width: 100%;
      background-color: var(--vs-gold);
      color: #FFFFFF;
      font-family: var(--font-heading);
      font-size: 17px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 14px 20px;
      border-radius: 4px;
      text-decoration: none;
      box-shadow: 0 4px 14px rgba(251, 176, 59, 0.4);
      transition: all 0.25s ease;
    }
    .btn-reserve-card:hover {
      background-color: var(--vs-light-green);
      color: #FFFFFF;
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(133, 207, 4, 0.45);
    }

    /* FIXED BOTTOM CONVERSION BAR */
    .fixed-bottom-bar {
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      background: rgba(40, 64, 1, 0.97);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-top: 2px solid var(--vs-gold);
      padding: 12px 16px;
      z-index: 990;
      display: flex;
      justify-content: center;
      box-shadow: 0 -8px 25px rgba(0,0,0,0.25);
    }
    .btn-whatsapp-fixed {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      background: var(--vs-gold);
      color: #FFFFFF;
      font-family: var(--font-heading);
      font-size: 16px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      padding: 14px 24px;
      border-radius: 4px;
      text-decoration: none;
      width: 100%;
      max-width: 500px;
      box-shadow: 0 4px 16px rgba(251, 176, 59, 0.4);
      animation: pulse 2.5s infinite;
    }
    .btn-whatsapp-fixed:hover {
      background: var(--vs-light-green);
    }
    @keyframes pulse {
      0% { box-shadow: 0 0 0 0 rgba(251, 176, 59, 0.6); }
      70% { box-shadow: 0 0 0 12px rgba(251, 176, 59, 0); }
      100% { box-shadow: 0 0 0 0 rgba(251, 176, 59, 0); }
    }

    /* LIGHTBOX MODAL */
    .lightbox-modal {
      display: none;
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      background: rgba(13, 26, 0, 0.96);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      z-index: 9999;
      flex-direction: column;
      justify-content: space-between;
      padding: 16px;
      touch-action: none;
    }
    .lightbox-modal.active { display: flex; }
    .lightbox-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 8px 4px;
    }
    .lightbox-counter {
      color: #F2EFEB;
      font-family: var(--font-heading);
      font-size: 15px;
      font-weight: 600;
      text-transform: uppercase;
    }
    .lightbox-close-btn {
      background: rgba(255, 255, 255, 0.15);
      border: none;
      color: #fff;
      font-size: 26px;
      width: 42px;
      height: 42px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .lightbox-center {
      position: relative;
      flex: 1;
      display: flex;
      justify-content: center;
      align-items: center;
      overflow: hidden;
    }
    .lightbox-main-img {
      max-width: 100%;
      max-height: 72vh;
      object-fit: contain;
      border-radius: 8px;
      box-shadow: 0 15px 35px rgba(0,0,0,0.8);
      border: 1px solid rgba(255, 255, 255, 0.15);
    }
    .lb-nav {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      background: rgba(40, 64, 1, 0.8);
      border: 1px solid rgba(251, 176, 59, 0.4);
      color: #fff;
      font-size: 24px;
      width: 46px;
      height: 46px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 5;
    }
    .lb-prev { left: 8px; }
    .lb-next { right: 8px; }
    .lightbox-bottom {
      padding: 12px 4px 6px;
      text-align: center;
    }
    .lightbox-title {
      font-family: var(--font-heading);
      font-size: 16px;
      color: #FFFFFF;
      font-weight: 600;
      margin-bottom: 2px;
    }
    .lightbox-subtitle {
      font-size: 13px;
      color: #F2EFEB;
    }

    /* FOOTER OFICIAL VALE SILVESTRE */
    .site-footer {
      background: #284001;
      color: #F2EFEB;
      text-align: center;
      padding: 42px 16px 28px;
      font-size: 14px;
      margin-top: 48px;
      border-top: 3px solid var(--vs-gold);
    }
    .footer-logo {
      max-width: 180px;
      margin-bottom: 16px;
    }
    .site-footer a { color: var(--vs-gold); text-decoration: none; font-weight: 600; }
  </style>
</head>
<body>

  <!-- HERO HEADER COM LOGO OFICIAL -->
  <header class="hero-header">
    <div class="header-logo-wrap">
      <img src="img/logo_branca.png" alt="Vale Silvestre Ecopark" class="header-logo">
    </div>
    <div class="badge-nature">🌿 Conecte-se à Natureza • Ecopark & Pousada</div>
    <h1 class="hero-title">Catálogo Oficial de Acomodações</h1>
    <p class="hero-subtitle">Conheça nossos chalés aconchegantes com vista privilegiada para o lago, cercados de natureza exuberante, pensão completa e lazer liberado.</p>
    
    <div class="hero-highlights">
      <span class="highlight-pill">🍽️ Pensão Completa Inclusa</span>
      <span class="highlight-pill">🏊 Piscinas Adulto & Infantil</span>
      <span class="highlight-pill">🚣 Caiaques & Pedalinhos</span>
      <span class="highlight-pill">🐾 Espaço Pet Friendly</span>
    </div>
  </header>

  <!-- STICKY FILTER BAR -->
  <div class="sticky-filter-wrapper">
    <div class="container">
      <div class="filter-scroll">
        <button class="filter-btn active" onclick="filterCategory('all', this)">🌟 Todos</button>
        <button class="filter-btn" onclick="filterCategory('panoramicos', this)">🌅 Chalés Panorâmicos</button>
        <button class="filter-btn" onclick="filterCategory('lago', this)">🏡 Chalés do Lago</button>
        <button class="filter-btn" onclick="filterCategory('suites', this)">🌿 Suítes</button>
        <button class="filter-btn" onclick="filterCategory('lazer', this)">🚣 Lazer & Atrações</button>
        <button class="filter-btn" onclick="filterCategory('gastronomia', this)">🍽️ Gastronomia</button>
      </div>
    </div>
  </div>

  <!-- CATALOG FEED -->
  <main class="container">
    <div class="catalog-feed" id="catalogFeed">
"""

for item in items:
    photos_json = json.dumps(item["photos"])
    features_html = "".join([f'<span class="feature-chip">✓ {html.escape(f)}</span>' for f in item["features"]])
    first_photo = item["photos"][0]["rel_path"] if item["photos"] else ""
    
    msg_encoded = urllib.parse.quote(item["wa_msg"])
    wa_url = f"https://wa.me/553399989100?text={msg_encoded}"
    
    thumbs_html = ""
    for idx, p in enumerate(item["photos"]):
        thumbs_html += f"""
          <div class="thumb-item" onclick="setCardPhoto('{item['id']}', {idx})">
            <img src="{p['rel_path']}" alt="{html.escape(p['title'])}">
          </div>
        """
        
    html_template += f"""
      <article class="room-card" data-category="{item['category']}" id="card-{item['id']}">
        <div class="card-gallery-wrap">
          <span class="top-badge">{html.escape(item['badge'])}</span>
          <div class="main-photo-link" onclick="openLightboxFromCard('{item['id']}', 0)">
            <img id="main-img-{item['id']}" src="{first_photo}" alt="{html.escape(item['title'])}">
          </div>
          <button class="photo-count-btn" onclick="openLightboxFromCard('{item['id']}', 0)">
            📸 Ver {len(item['photos'])} fotos
          </button>
        </div>

        <div class="thumbs-row">
          {thumbs_html}
        </div>

        <div class="card-body">
          <div class="card-header-info">
            <span class="door-sign-tag">{item['tag_label']}</span>
            <h2 class="room-title">{html.escape(item['title'])}</h2>
            <span class="capacity-tag">{item['capacity_label']}</span>
          </div>

          <p class="room-desc">{html.escape(item['desc'])}</p>

          <div class="features-list">
            {features_html}
          </div>

          <a href="{wa_url}" target="_blank" class="btn-reserve-card">
            {item['btn_text']}
          </a>
        </div>
      </article>
    """

html_template += """
    </div>
  </main>

  <!-- FIXED BOTTOM WHATSAPP BAR -->
  <div class="fixed-bottom-bar">
    <a href="https://wa.me/553399989100?text=Ol%C3%A1%21+Estou+vendo+o+cat%C3%A1logo+oficial+da+pousada+e+gostaria+de+consultar+valores+e+disponibilidade%21" target="_blank" class="btn-whatsapp-fixed">
      💬 Falar com a Central de Reservas
    </a>
  </div>

  <!-- LIGHTBOX MODAL -->
  <div id="lightbox" class="lightbox-modal">
    <div class="lightbox-top">
      <span id="lbCounter" class="lightbox-counter">1 / 6</span>
      <button class="lightbox-close-btn" onclick="closeLightbox()">&times;</button>
    </div>
    <div class="lightbox-center">
      <button class="lb-nav lb-prev" onclick="prevPhoto(event)">&#10094;</button>
      <img id="lbImg" class="lightbox-main-img" src="" alt="">
      <button class="lb-nav lb-next" onclick="nextPhoto(event)">&#10095;</button>
    </div>
    <div class="lightbox-bottom">
      <div id="lbTitle" class="lightbox-title">Título da Foto</div>
      <div id="lbSubtitle" class="lightbox-subtitle">Pousada Vale Silvestre Ecopark</div>
    </div>
  </div>

  <!-- FOOTER NO PADRÃO OFICIAL -->
  <footer class="site-footer">
    <img src="img/logo_branca.png" alt="Vale Silvestre Ecopark" class="footer-logo">
    <p><strong>Pousada Vale Silvestre Ecopark</strong> — Governador Valadares/MG</p>
    <p style="margin: 8px 0;">Central de Reservas WhatsApp: <a href="https://wa.me/553399989100">(33) 99989-9100</a></p>
    <p style="font-size: 13px; color: #DCDDE8;">Pensão Completa • Parque Aquático • Lago com Caiaques • Trilhas</p>
    <p style="margin-top: 14px; font-size: 12px; color: #ABB8C3;">© Vale Silvestre Eco Park. Todos os direitos reservados.</p>
  </footer>

  <script>
    const catalogData = """ + json.dumps({item["id"]: item["photos"] for item in items}) + """;
    let activeCardId = null;
    let activeIndex = 0;

    function setCardPhoto(cardId, photoIdx) {
      const photos = catalogData[cardId];
      if (!photos || !photos[photoIdx]) return;
      const imgEl = document.getElementById('main-img-' + cardId);
      if (imgEl) {
        imgEl.src = photos[photoIdx].rel_path;
      }
      const card = document.getElementById('card-' + cardId);
      if (card) {
        card.querySelectorAll('.thumb-item').forEach((t, i) => {
          if (i === photoIdx) t.classList.add('active');
          else t.classList.remove('active');
        });
      }
    }

    function openLightboxFromCard(cardId, startIdx) {
      activeCardId = cardId;
      activeIndex = startIdx || 0;
      updateLightbox();
      document.getElementById('lightbox').classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    function updateLightbox() {
      const photos = catalogData[activeCardId];
      if (!photos || photos.length === 0) return;
      const cur = photos[activeIndex];
      document.getElementById('lbImg').src = cur.rel_path;
      document.getElementById('lbTitle').innerText = cur.title;
      document.getElementById('lbCounter').innerText = (activeIndex + 1) + ' / ' + photos.length;
    }

    function prevPhoto(e) {
      if (e) e.stopPropagation();
      const photos = catalogData[activeCardId];
      if (!photos) return;
      activeIndex = (activeIndex - 1 + photos.length) % photos.length;
      updateLightbox();
    }

    function nextPhoto(e) {
      if (e) e.stopPropagation();
      const photos = catalogData[activeCardId];
      if (!photos) return;
      activeIndex = (activeIndex + 1) % photos.length;
      updateLightbox();
    }

    function closeLightbox() {
      document.getElementById('lightbox').classList.remove('active');
      document.body.style.overflow = '';
    }

    document.addEventListener('keydown', (e) => {
      if (!document.getElementById('lightbox').classList.contains('active')) return;
      if (e.key === 'Escape') closeLightbox();
      if (e.key === 'ArrowLeft') prevPhoto();
      if (e.key === 'ArrowRight') nextPhoto();
    });

    let touchStartX = 0;
    let touchEndX = 0;
    const lbModal = document.getElementById('lightbox');
    lbModal.addEventListener('touchstart', e => {
      touchStartX = e.changedTouches[0].screenX;
    }, false);
    lbModal.addEventListener('touchend', e => {
      touchEndX = e.changedTouches[0].screenX;
      handleSwipe();
    }, false);

    function handleSwipe() {
      if (touchEndX < touchStartX - 50) nextPhoto();
      if (touchEndX > touchStartX + 50) prevPhoto();
    }

    function filterCategory(cat, btn) {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      document.querySelectorAll('.room-card').forEach(card => {
        if (cat === 'all' || card.dataset.category === cat) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    }
  </script>
</body>
</html>
"""

with open(os.path.join(site_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_template)

print("SUCCESS! Updated prepare_site.py and index.html with customized buttons and tags!")
