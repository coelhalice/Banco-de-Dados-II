from database import Database
from writeAJson import writeAJson


class ProductAnalyzer:
    def __init__(self, database, collection):
        self.db = Database(database, collection)
    
    #1. Retorne o total de vendas por dia
    def vendas_dia(self):
        result = self.db.collection.aggregate([
        {"$unwind":"$produtos"},
        {"$group": {"_id": "$data_compra", "Total":{"$sum": "$produtos.quantidade"}}},
        {"$sort": {"Total": -1}}

    ])
        writeAJson(result, "Vendas_por_dia")


    #2. Retorne o produto mais vendido em todas as compras.
    def mais_vendido(self):
        result2 = self.db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": "$produtos.descricao", "Total": {"$sum": "$produtos.quantidade"}}},
        {"$sort": {"Total": -1}},
        {"$limit": 1}
    ])
        writeAJson(result2, "Produto_mais_vendido")

    #3. Encontre o cliente que mais gastou em uma única compra.
    def cliente_rico(self):
        result3 = self.db.collection.aggregate([
        {"$unwind":"$produtos"},
        {"$group":{"_id":"$cliente_id","total":{"$sum":{"$multiply":["$produtos.quantidade","$produtos.preco"]}}}},
        {"$sort":{"total": -1}},
        {"$limit": 1}
    ])
        writeAJson(result3, "Cliente_mais_gastos")

    #4. Liste todos os produtos que tiveram uma quantidade vendida acima de 1 unidades.
    def produtos1venda(self):
        result4 = self.db.collection.aggregate([
        {"$unwind":"$produtos"},
        {"$match":{"produtos.quantidade": {"$gt":1}}},
        {"$group":{"_id":"$produtos.descricao"}},
    ])
        writeAJson(result4, "Produtos_mais_de_uma_venda")