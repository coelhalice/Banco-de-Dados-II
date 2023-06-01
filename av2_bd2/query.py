class Query:
    def __init__ (self,db):
        self.db = db
    
#------------------------------------------------------------------------------------------------------------#
## Questão 01

#1. Busque pelo professor `“Teacher”` cujo nome seja “Renzo”, retorne o **ano_nasc** e o **CPF**.
    def renZo(self):
        print("1-1)")
        query = "MATCH (t:Teacher {name: 'Renzo'}) RETURN t.ano_nasc, t.cpf"
        results = self.db.execute_query(query)
        return [(result["t.ano_nasc"],result["t.cpf"]) for result in results]

#2. Busque pelos professores `“Teacher”` cujo nome comece com a letra **“M”**, retorne o **name** e o **cpf**.
    def m(self):
        print("1-2)")
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.cpf"
        results = self.db.execute_query(query)
        return [(result["t.name"],result["t.cpf"]) for result in results]

#3. Busque pelos nomes de todas as cidades `“City”` e retorne-os.
    def city(self):
        print("1-3)")
        query = "MATCH (c:City) RETURN c.name"
        results = self.db.execute_query(query)
        return [result["c.name"] for result in results]

#4. Busque pelas escolas `“School”`, onde o number seja maior ou igual a 150 e menor ou igual a 550, retorne o nome da escola, o endereço e o número.
    def school(self):
        print("1-4)")
        query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number"
        results = self.db.execute_query(query)
        return [(result["s.name"],result["s.address"],result["s.number"]) for result in results]

#------------------------------------------------------------------------------------------------------------#
## Questão 02

#1. Encontre o ano de nascimento do professor mais jovem e do professor mais velho.
    def ano(self):
        print("2-1)")
        query = "MATCH (t:Teacher) RETURN t.ano_nasc ORDER BY t.ano_nasc ASC LIMIT 1"
        results = self.db.execute_query(query)
        return [result["t.ano_nasc"] for result in results]

#2. Encontre a média aritmética para os habitantes de todas as cidades, use a propriedade **“population”**.
    def media(self):
        print("2-2)")
        query = "MATCH (c:City) RETURN AVG(c.population)"
        results = self.db.execute_query(query)
        return [result["AVG(c.population)"] for result in results]

#3. Encontre a cidade cujo **CEP** seja igual a **“37540-000”** e retorne o nome com todas as letras **“a”** substituídas por **“A”** .
    def cep(self):
        print("2-3)")
        query = "MATCH (c:City {cep: '37540-000'}) RETURN REPLACE(c.name, 'a', 'A')"
        results = self.db.execute_query(query)
        return [result["REPLACE(c.name, 'a', 'A')"] for result in results]

#4. Para todos os professores, retorne um caractere, iniciando a partir da 3ª letra do nome.
    def terceiraLetra(self):
        print("2-4)")
        query = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 2, 1)"
        results = self.db.execute_query(query)
        return [result["SUBSTRING(t.name, 2, 1)"] for result in results]