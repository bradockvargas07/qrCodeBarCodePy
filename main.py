from barcode import EAN13
from barcode.writer import ImageWriter


codigos_produtos = {
    "Feijao": "551746511111",
    "Arroz": "665789011111",
    "Macarrao": "665887111111",
    "Azeite": "998556211111"}

for produto in codigos_produtos:
    codigo = codigos_produtos[produto]
    codigo_barras = EAN13(codigo, writer=ImageWriter())
    codigo_barras.save(f"codigo_barras_{produto}")
