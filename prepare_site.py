import os
import shutil
import html
import urllib.parse
import json

src_base = r"G:\Meu Drive\01 - Profissional e Negócios\Vale Silvestre\Fotos_Selecionadas_Desbravador_Site\00_Selecao_Resumida_Para_Envio"
site_dir = r"C:\Users\danie\vale-silvestre-catalogo"
img_dest_root = os.path.join(site_dir, "img")

# Accommodation Catalog Definition - Curated strictly after Viviane's inspection
# Filtered out: dirty floors, bathroom trash, rotated images
items = [
    {
        "id": "panoramico-02",
        "category": "panoramicos",
        "category_label": "Chalé Panorâmico",
        "badge": "Mais Procurado • Vista Panorâmica 360°",
        "title": "Chalé Panorâmico — Piso 02 Superior",
        "door_sign": "Arara",
        "capacity": "Casal + 2 camas de solteiro (acomoda até 4 pessoas)",
        "desc": "Localizado no ponto mais nobre da colina com rampa suave de madeira. Possui pé-direito alto, ambiente super arejado e uma varanda panorâmica de madeira privativa com a vista mais deslumbrante de todo o lago e das montanhas. Uma experiência romântica e inesquecível!",
        "features": ["Varanda Panorâmica 360°", "Vista Privilegiada da Lagoa", "Cama Box de Casal", "2 Camas de Solteiro", "TV LCD", "Frigobar", "Ventilador de Teto", "Banheiro Privativo"],
        "src_folder": "06_Chale_Panoramico_Piso_02",
        "dest_folder": "chale-panoramico-piso-02",
        # Only clean, magazine-standard photos:
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
        "door_sign": "Orquídea e Paraju",
        "capacity": "Casal + 2 camas de solteiro (acomoda até 4 pessoas)",
        "desc": "Conforto absoluto com acesso térreo direto, perfeito para quem busca comodidade e acessibilidade sem escadas. Conta com hall de entrada com poema decorativo, varanda ampla com jardim e vista charmosa.",
        "features": ["Acesso Térreo Plano (Sem Escadas)", "Varanda com Jardim", "Hall com Poema Rústico", "Cama Box de Casal", "2 Camas de Solteiro", "TV LCD", "Frigobar", "Banheiro Privativo"],
        "src_folder": "05_Chale_Panoramico_Piso_01",
        "dest_folder": "chale-panoramico-piso-01",
        # Filtered out: 07_Banheiro_Privativo (rotated)
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
        "door_sign": "Bouganville",
        "capacity": "Até 5 pessoas (Quarto com cama de casal + solteiro | Sala com 2 sofás-cama)",
        "desc": "Localização paradisíaca às margens da lagoa e coladinho ao restaurante principal. A divisão entre quarto privativo e sala de estar ampla oferece total privacidade aos pais enquanto as crianças dormem confortavelmente na sala. Varanda charmosa de frente para a água!",
        "features": ["Em Frente à Lagoa", "Ao Lado do Restaurante", "Quarto Privativo", "Sala de Estar com Sofás-Cama", "Geladeira", "Bancada Americana", "Varanda com Vista da Água"],
        "src_folder": "03_Chale_do_Lago_Quarto_e_Sala",
        "dest_folder": "chale-do-lago-1-quarto",
        # Filtered out: 05_Banheiro (dusty floor/trash)
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
        "door_sign": "Bromélia e Gameleira",
        "capacity": "Até 7 pessoas (Quarto 1: casal + solteiro | Quarto 2: 3 solteiro | Sala: 2 sofás-cama)",
        "desc": "A maior acomodação da pousada, projetada com carinho para famílias grandes ou pequenos grupos. Conta com dois dormitórios independentes, sala espaçosa com sofás-cama, frigobar retrô Coca-Cola e varanda com brisa refrescante do lago.",
        "features": ["2 Quartos Privativos", "Acomoda até 7 Pessoas", "Sala com Sofás-Cama", "Frigobar Retrô Coca-Cola", "Bancada e Pia", "Varanda na Beira do Lago", "Excelente Conforto"],
        "src_folder": "04_Chale_do_Lago_2_Quartos_e_Sala",
        "dest_folder": "chale-do-lago-2-quartos",
        # REMOVED: 06_Banheiro_Privativo (toilet with trash bag on seat lid!)
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
        "category_label": "Suítes Coloniais",
        "badge": "Ótimo Custo-Benefício • Localização Central",
        "title": "Suíte Central",
        "door_sign": "Braúna",
        "capacity": "Casal + 2 camas de solteiro (acomoda até 4 pessoas)",
        "desc": "Acomodação acolhedora situada próxima à praça central e ao restaurante. Excelente opção de custo-benefício com cama de casal, duas de solteiro, frigobar, TV LCD e varanda térrea com jardim.",
        "features": ["Próxima ao Restaurante", "Cama de Casal + 2 Solteiro", "TV LCD", "Frigobar", "Banheiro com Gabinete de Madeira", "Varanda Térrea"],
        "src_folder": "02_Suite_Central",
        "dest_folder": "suite-central",
        # Filtered out: 06_Banheiro_Box_Blindex (rotated sideways)
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
        "category_label": "Suítes Coloniais",
        "badge": "Grande Porte • Até 7 Pessoas",
        "title": "Suíte Mangueira",
        "door_sign": "Paca e Jaguatirica",
        "capacity": "Casal + 2 beliches de madeira + 1 solteiro (acomoda até 7 pessoas)",
        "desc": "Suíte espaçosa em meio a uma área verde tranquila e sombreada por mangueiras nativas. Muito confortável para famílias que desejam ficar juntas no mesmo ambiente.",
        "features": ["Espaço para até 7 Pessoas", "1 Cama Casal + 2 Beliches", "Banheiro Privativo", "Área Verde Tranquila", "Ideal para Grupos e Famílias"],
        "src_folder": "01_Suite_Mangueira",
        "dest_folder": "suite-mangueira",
        # REMOVED: 05_Bancada_da_Pia (dirty footprints on floor & bucket) and 06_Banheiro (dusty floor)
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
        "door_sign": "Parque Ecológico",
        "capacity": "Lazer liberado para todos os hóspedes",
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
        "door_sign": "Restaurante do Vale",
        "capacity": "Jantar, Café da Manhã e Almoço Mineiro",
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

print("Applying Viviane housekeeping standards to photos...")
for item in items:
    src_dir = os.path.join(src_base, item["src_folder"])
    dest_dir = os.path.join(img_dest_root, item["dest_folder"])
    
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.makedirs(dest_dir, exist_ok=True)
    
    item_photos = []
    for idx, (orig_file, title) in enumerate(item["allowed_files"], 1):
        src_file = os.path.join(src_dir, orig_file)
        if os.path.exists(src_file):
            clean_name = f"foto_{idx:02d}.jpg"
            dest_file = os.path.join(dest_dir, clean_name)
            shutil.copy2(src_file, dest_file)
            item_photos.append({
                "rel_path": f"img/{item['dest_folder']}/{clean_name}",
                "title": title,
                "clean_name": clean_name
            })
        else:
            print(f"WARNING: File not found: {src_file}")
            
    item["photos"] = item_photos
    print(f"Curated {len(item_photos)} approved photos for {item['title']}")

# Generate index.html
html_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Catálogo Oficial de Acomodações & Lazer — Vale Silvestre Eco Park</title>
  <meta name="description" content="Conheça os chalés panorâmicos, chalés do lago, gastronomia mineira e opções de lazer do Vale Silvestre Eco Park em Governador Valadares/MG.">
  <meta name="theme-color" content="#0a0f18">
  <meta property="og:title" content="Catálogo Oficial de Acomodações — Vale Silvestre Eco Park">
  <meta property="og:description" content="Chalés aconchegantes com vista para a lagoa, pensão completa e lazer liberado em Governador Valadares/MG.">
  <meta property="og:type" content="website">
  
  <style>
    :root {
      --bg: #0a0f18;
      --card-bg: #121927;
      --card-border: #1f2a3f;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --accent: #10b981;
      --accent-hover: #059669;
      --gold: #f59e0b;
      --gold-light: #fef3c7;
      --whatsapp: #25d366;
      --whatsapp-hover: #20ba5a;
      --font-main: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }
    
    body {
      font-family: var(--font-main);
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.5;
      padding-bottom: 90px;
      overflow-x: hidden;
    }

    .container {
      width: 100%;
      max-width: 860px;
      margin: 0 auto;
      padding: 0 16px;
    }

    .hero-header {
      background: radial-gradient(circle at top, #162238 0%, #0a0f18 100%);
      padding: 32px 16px 20px;
      text-align: center;
      border-bottom: 1px solid var(--card-border);
    }
    .badge-nature {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid rgba(16, 185, 129, 0.3);
      color: #34d399;
      font-size: 12px;
      font-weight: 600;
      padding: 5px 12px;
      border-radius: 20px;
      margin-bottom: 12px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .hero-title {
      font-size: 26px;
      font-weight: 800;
      color: #fff;
      letter-spacing: -0.5px;
      margin-bottom: 6px;
    }
    .hero-subtitle {
      font-size: 14.5px;
      color: var(--text-muted);
      max-width: 580px;
      margin: 0 auto 16px;
      line-height: 1.45;
    }
    .hero-highlights {
      display: flex;
      justify-content: center;
      gap: 12px;
      flex-wrap: wrap;
    }
    .highlight-pill {
      background: #172033;
      border: 1px solid var(--card-border);
      color: #e2e8f0;
      font-size: 12px;
      font-weight: 500;
      padding: 5px 12px;
      border-radius: 8px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .sticky-filter-wrapper {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(10, 15, 24, 0.94);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--card-border);
      padding: 10px 0;
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
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      color: var(--text-muted);
      padding: 8px 16px;
      border-radius: 24px;
      font-size: 13.5px;
      font-weight: 600;
      white-space: nowrap;
      cursor: pointer;
      transition: all 0.2s;
    }
    .filter-btn:hover, .filter-btn.active {
      background: var(--accent);
      color: #fff;
      border-color: var(--accent);
      box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
    }

    .catalog-feed {
      margin-top: 20px;
      display: flex;
      flex-direction: column;
      gap: 24px;
    }

    .room-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 18px;
      overflow: hidden;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
      transition: transform 0.2s;
    }

    .card-gallery-wrap {
      position: relative;
      background: #000;
    }
    .main-photo-link {
      display: block;
      position: relative;
      width: 100%;
      height: 250px;
      overflow: hidden;
      cursor: pointer;
    }
    @media (min-width: 600px) {
      .main-photo-link { height: 340px; }
    }
    .main-photo-link img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.3s ease;
    }
    .room-card:hover .main-photo-link img {
      transform: scale(1.02);
    }
    .top-badge {
      position: absolute;
      top: 12px;
      left: 12px;
      background: rgba(10, 15, 24, 0.85);
      backdrop-filter: blur(8px);
      color: var(--gold);
      border: 1px solid rgba(245, 158, 11, 0.4);
      font-size: 11px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 8px;
      text-transform: uppercase;
      letter-spacing: 0.4px;
      z-index: 2;
    }
    .photo-count-btn {
      position: absolute;
      bottom: 12px;
      right: 12px;
      background: rgba(10, 15, 24, 0.85);
      backdrop-filter: blur(8px);
      color: #fff;
      border: 1px solid rgba(255, 255, 255, 0.2);
      font-size: 12px;
      font-weight: 600;
      padding: 6px 12px;
      border-radius: 20px;
      display: flex;
      align-items: center;
      gap: 6px;
      z-index: 2;
      cursor: pointer;
    }

    .thumbs-row {
      display: flex;
      gap: 6px;
      padding: 10px 12px;
      overflow-x: auto;
      background: #0d131f;
      scrollbar-width: none;
    }
    .thumbs-row::-webkit-scrollbar { display: none; }
    .thumb-item {
      width: 62px;
      height: 52px;
      border-radius: 8px;
      overflow: hidden;
      flex-shrink: 0;
      cursor: pointer;
      border: 1.5px solid transparent;
      transition: all 0.2s;
    }
    .thumb-item:hover, .thumb-item.active {
      border-color: var(--accent);
      transform: scale(1.05);
    }
    .thumb-item img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .card-body {
      padding: 20px;
    }
    .card-header-info {
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-bottom: 12px;
    }
    .door-sign-tag {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: var(--gold);
      font-size: 12.5px;
      font-weight: 700;
      background: rgba(245, 158, 11, 0.1);
      padding: 3px 10px;
      border-radius: 6px;
      align-self: flex-start;
      border: 1px solid rgba(245, 158, 11, 0.25);
    }
    .room-title {
      font-size: 20px;
      font-weight: 700;
      color: #fff;
      line-height: 1.3;
    }
    .capacity-tag {
      color: #38bdf8;
      font-size: 13.5px;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .room-desc {
      color: #cbd5e1;
      font-size: 14px;
      line-height: 1.55;
      margin: 10px 0 16px;
    }

    .features-list {
      display: flex;
      flex-wrap: wrap;
      gap: 7px;
      margin-bottom: 18px;
    }
    .feature-chip {
      background: #182235;
      border: 1px solid var(--card-border);
      color: #94a3b8;
      font-size: 12px;
      padding: 4px 10px;
      border-radius: 6px;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }

    .btn-reserve-card {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      width: 100%;
      background: linear-gradient(135deg, #10b981 0%, #059669 100%);
      color: #fff;
      font-size: 14.5px;
      font-weight: 700;
      padding: 13px;
      border-radius: 12px;
      text-decoration: none;
      box-shadow: 0 4px 14px rgba(16, 185, 129, 0.35);
      transition: all 0.2s;
    }
    .btn-reserve-card:hover {
      background: #059669;
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(16, 185, 129, 0.45);
    }

    .fixed-bottom-bar {
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      background: rgba(10, 15, 24, 0.96);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-top: 1px solid var(--card-border);
      padding: 12px 16px;
      z-index: 990;
      display: flex;
      justify-content: center;
      box-shadow: 0 -8px 25px rgba(0,0,0,0.6);
    }
    .btn-whatsapp-fixed {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      background: var(--whatsapp);
      color: #fff;
      font-size: 15px;
      font-weight: 700;
      padding: 14px 24px;
      border-radius: 30px;
      text-decoration: none;
      width: 100%;
      max-width: 500px;
      box-shadow: 0 4px 16px rgba(37, 211, 102, 0.4);
      animation: pulse 2.5s infinite;
    }
    @keyframes pulse {
      0% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.6); }
      70% { box-shadow: 0 0 0 12px rgba(37, 211, 102, 0); }
      100% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
    }

    .lightbox-modal {
      display: none;
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      background: rgba(5, 8, 14, 0.97);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
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
      color: var(--text-muted);
      font-size: 13.5px;
      font-weight: 600;
    }
    .lightbox-close-btn {
      background: rgba(255, 255, 255, 0.1);
      border: none;
      color: #fff;
      font-size: 24px;
      width: 40px;
      height: 40px;
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
      border-radius: 10px;
      box-shadow: 0 15px 35px rgba(0,0,0,0.8);
      transition: transform 0.2s;
    }
    .lb-nav {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      background: rgba(18, 25, 39, 0.7);
      border: 1px solid rgba(255,255,255,0.2);
      color: #fff;
      font-size: 22px;
      width: 44px;
      height: 44px;
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
      font-size: 14.5px;
      color: #fff;
      font-weight: 600;
      margin-bottom: 2px;
    }
    .lightbox-subtitle {
      font-size: 12px;
      color: var(--text-muted);
    }

    .site-footer {
      text-align: center;
      padding: 36px 16px 20px;
      color: var(--text-muted);
      font-size: 13px;
      border-top: 1px solid var(--card-border);
      margin-top: 40px;
    }
    .site-footer a { color: var(--accent); text-decoration: none; }
  </style>
</head>
<body>

  <header class="hero-header">
    <div class="badge-nature">🌿 Refúgio Ecológico & Lazer</div>
    <h1 class="hero-title">Vale Silvestre Eco Park</h1>
    <p class="hero-subtitle">Conheça nossos chalés aconchegantes com vista privilegiada para o lago, cercados de natureza exuberante e tranquilidade.</p>
    
    <div class="hero-highlights">
      <span class="highlight-pill">🍽️ Pensão Completa Inclusa</span>
      <span class="highlight-pill">🏊 Parque Aquático & Piscinas</span>
      <span class="highlight-pill">🚣 Caiaques & Pedalinhos</span>
      <span class="highlight-pill">🐾 Espaço Pet Friendly</span>
    </div>
  </header>

  <div class="sticky-filter-wrapper">
    <div class="container">
      <div class="filter-scroll">
        <button class="filter-btn active" onclick="filterCategory('all', this)">🌟 Todos</button>
        <button class="filter-btn" onclick="filterCategory('panoramicos', this)">🌅 Chalés Panorâmicos</button>
        <button class="filter-btn" onclick="filterCategory('lago', this)">🏡 Chalés do Lago</button>
        <button class="filter-btn" onclick="filterCategory('suites', this)">🌿 Suítes Coloniais</button>
        <button class="filter-btn" onclick="filterCategory('lazer', this)">🚣 Lazer & Atrações</button>
        <button class="filter-btn" onclick="filterCategory('gastronomia', this)">🍽️ Gastronomia</button>
      </div>
    </div>
  </div>

  <main class="container">
    <div class="catalog-feed" id="catalogFeed">
"""

for item in items:
    photos_json = json.dumps(item["photos"])
    features_html = "".join([f'<span class="feature-chip">✓ {html.escape(f)}</span>' for f in item["features"]])
    first_photo = item["photos"][0]["rel_path"] if item["photos"] else ""
    
    msg_encoded = urllib.parse.quote(f"Olá! Estou vendo o catálogo do Vale Silvestre e gostaria de saber a disponibilidade do *{item['title']}*!")
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
            📸 Ver todas as {len(item['photos'])} fotos
          </button>
        </div>

        <div class="thumbs-row">
          {thumbs_html}
        </div>

        <div class="card-body">
          <div class="card-header-info">
            <span class="door-sign-tag">🏷️ Placa na Porta: {html.escape(item['door_sign'])}</span>
            <h2 class="room-title">{html.escape(item['title'])}</h2>
            <span class="capacity-tag">👥 {html.escape(item['capacity'])}</span>
          </div>

          <p class="room-desc">{html.escape(item['desc'])}</p>

          <div class="features-list">
            {features_html}
          </div>

          <a href="{wa_url}" target="_blank" class="btn-reserve-card">
            💬 Consultar Disponibilidade deste Chalé
          </a>
        </div>
      </article>
    """

html_template += """
    </div>
  </main>

  <div class="fixed-bottom-bar">
    <a href="https://wa.me/553399989100?text=Ol%C3%A1%21+Estou+vendo+o+cat%C3%A1logo+de+fotos+da+pousada+e+gostaria+de+fazer+uma+reserva%21" target="_blank" class="btn-whatsapp-fixed">
      💬 Falar com a Central de Reservas
    </a>
  </div>

  <div id="lightbox" class="lightbox-modal">
    <div class="lightbox-top">
      <span id="lbCounter" class="lightbox-counter">1 / 8</span>
      <button class="lightbox-close-btn" onclick="closeLightbox()">&times;</button>
    </div>
    <div class="lightbox-center">
      <button class="lb-nav lb-prev" onclick="prevPhoto(event)">&#10094;</button>
      <img id="lbImg" class="lightbox-main-img" src="" alt="">
      <button class="lb-nav lb-next" onclick="nextPhoto(event)">&#10095;</button>
    </div>
    <div class="lightbox-bottom">
      <div id="lbTitle" class="lightbox-title">Título da Foto</div>
      <div id="lbSubtitle" class="lightbox-subtitle">Vale Silvestre Eco Park</div>
    </div>
  </div>

  <footer class="site-footer">
    <p><strong>Vale Silvestre Eco Park</strong> — Governador Valadares, MG</p>
    <p>Central de Reservas WhatsApp: <a href="https://wa.me/553399989100">(33) 99989-9100</a></p>
    <p style="margin-top:6px; font-size:12px;">Pensão Completa • Piscinas • Lago com Caiaques • Trilhas</p>
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

print("SUCCESS! Generated mobile-friendly client website in index.html with Viviane's standards!")
