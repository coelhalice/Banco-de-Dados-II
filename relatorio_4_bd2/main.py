from productAnalyzer import ProductAnalyzer
from database import Database

db = Database(database="mercado", collection="compras")
db.resetDatabase()

productAnalyzer = ProductAnalyzer("mercado", "compras")

productAnalyzer.vendas_dia()
productAnalyzer.mais_vendido()
productAnalyzer.cliente_rico()
productAnalyzer.produtos1venda()