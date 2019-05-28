from app import db

'''
TODO
	Adicionar alguns relacionamentos
	

'''
db.metadata.clear()
class Usuario(db.Model):
	__tablename__ = "Usuarios"
	##Nullable = pode ser nulo?? = True || False
	# Unique = é unico? = True || False
	id_usuario = db.Column(db.Integer, primary_key = True, autoincrement = True)
	fnome = db.Column(db.String(45), nullable = False) 
	lnome = db.Column(db.String(45), nullable = False)
	nascimento = db.Column(db.Date, nullable = False)
	idade = db.Column(db.Integer, nullable = False) #Tirar a idade dos nascimento???
	login = db.Column(db.String(45), nullable = False, unique = True)
	senha = db.Column(db.String(100), nullable = False)
	# ????????????? Mudar de tabela? ??????????????????????
	diaReceberSalario = db.Column(db.Date, nullable = False)

	def __init__(self, fnome, lnome, nascimento, idade, login, senha, diaReceberSalario):
		self.fnome = fname
		self.lnome = lnome
		self.nascimento = nascimento
		self.idade = idade
		self.login = login
		self.senha = senha
		self.diaReceberSalario = diaReceberSalario

	def __repr__():
		return '<Usuario %r>' % fnome + ' ' + lname

	def toString(self):
		return({'id_usuario':self.id_usuario,
				'fnome':self.fnome,
				'lname':self.lname,
				'nascimento': self.nascimento,
				'idade':self.idade,
				'login':self.login,
				'senha':self.senha,
				'diaReceberSalario':self.diaReceberSalario})

class Familia(db.Model):
	__tablename__ = "Familias"
	id_familia = db.Column(db.Integer, primary_key = True, autoincrement = True)
	rendaMensal = db.Column(db.Integer, nullable = False)
	
	def __init__(self, rendaMensal):
		self.rendaMensal = rendaMensal

	def toString(self):
		return({'id_familia':self.id_familia,
				'rendaMensal':self.rendaMensal})

class Integrante(db.Model):
	__tablename__ = "Integrantes"
	id = db.Column(db.Integer, primary_key = True, autoincrement = True)
	id_integrante = db.Column(db.Integer, db.ForeignKey('Familias.id_familia'), unique = True, nullable = False, autoincrement = True)
	id_familia = db.Column(db.Integer, db.ForeignKey('Usuarios.id_usuario'), nullable = False, unique = True)

	def __init__(self, id_integrante, id_familia):
		self.id_integrante = id_integrante
		self.id_familia = id_familia

	def toString(self):
		return({'id_integrante':self.id_integrante,
				'id_familia':self.id_familia})

		
class Gerenciador(db.Model):
	__tablename__ = "Gerenciadores"
	id = db.Column(db.Integer, primary_key = True, autoincrement = True)
	id_gerenciador = db.Column(db.Integer, db.ForeignKey('Integrantes.id_integrante'), nullable = False)
	salario = db.Column(db.Integer, nullable = False)
	def __init__(self, id_gerenciador, salario):
		self.id_gerenciador = id_gerenciador
		self.salario = salario
	def toString(self):
		return({'id_gerenciador':self.id_gerenciador,
				'salario':self.salario})

class Dependente(db.Model):
	__tablename__ = "Dependentes"
	id = db.Column(db.Integer, primary_key = True, autoincrement = True)
	id_dependente = db.Column(db.Integer, db.ForeignKey('Integrantes.id_integrante'), unique = True, nullable = False)

	def __init__(self, id_dependente):
		self.id_dependente = id_dependente

	def toString(self):
		return ({'id_dependente':self.id_dependente})

class Contribuinte(db.Model):
	__tablename__ = "Contribuintes"
	id = db.Column(db.Integer, primary_key = True, autoincrement = True)
	id_contribuinte = db.Column(db.Integer, db.ForeignKey('Integrantes.id_integrante'), unique = True, nullable = False)
	dinheiroRecebido = db.Column(db.Integer, nullable = False)
	def __init__(self, dinheiroRecebido):
		self.dinheiroRecebido = dinheiroRecebido

	def toString(self):
		return ({'id_contribuinte': id_contribuinte,
				 'dinheiroRecebido':dinheiroRecebido})

class Recurso(db.Model):
	__tablename__ = "Recursos"
	id_recurso = db.Column(db.Integer, primary_key = True, autoincrement = True)
	usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('Usuarios.id_usuario'))
	valor = db.Column(db.Integer, nullable = True)
	dataPagamento = db.Column(db.DateTime, nullable = True)
	nome = db.Column(db.String(45), nullable = True)
	dataCancelamento = db.Column(db.DateTime, nullable = True)
	dataAnotacao = db.Column(db.DateTime, nullable = True)
	
	def __init__(self, usuario_id_usuario, valor, dataPagamento, nome, dataCancelamento, dataAnotacao):
		self.valor = valor
		self.dataPagamento = dataPagamento
		self.nome = nome
		self.dataCancelamento = dataCancelamento
		self.dataAnotacao = dataAnotacao

	def toString(self):
		return ({'id_recurso': id_recurso,
				 'usuario_id_usuario':usuario_id_usuario,
				 'valor':valor,
				 'dataPagamento':dataPagamento,
				 'nome': nome,
				 'dataCancelamento':dataCancelamento,
				 'dataAnotacao':dataAnotacao})

class Despesa(db.Model):
	__tablename__ = "Despesas"
	id_despesa = db.Column(db.Integer, primary_key = True, autoincrement = True)
	id_recurso = db.Column(db.Integer, db.ForeignKey('Recursos.id_recurso'))
	
	def __init__(self, id_recurso):
		self.id_recurso = id_recurso

	def toString(self):
		return ({'id_despesa': id_despesa,
				 'id_recurso':id_recurso}) 

class Receita(db.Model):
	__tablename__ = "Receitas"
	id_receita = db.Column(db.Integer, primary_key = True, autoincrement = True)
	id_recurso = db.Column(db.Integer, db.ForeignKey('Recursos.id_recurso'), nullable = False)
	def __init__(self, id_recurso):
		self.id_recurso = id_recurso

	def toString(self):
		return ({'id_receita': id_receita,
				 'id_recurso':id_recurso})

class ReceitaIncomum(db.Model):
	__tablename__ = "ReceitasIncomuns"
    
	id_receitaIncomum = db.Column(db.Integer, primary_key = True, autoincrement = True)
	receita_id_receita = db.Column(db.Integer, db.ForeignKey('Receitas.id_receita'), nullable = False)
	atualizada = db.Column(db.Boolean, nullable = False)
	emissor = db.Column(db.String(45))
	motivo = db.Column(db.String(45))
	def __init__(self, receita_id_receita, atualizada, emissor, motivo):
		self.receita_id_receita = receita_id_receita
		self.atualizada = atualizada
		self.emissor = emissor
		self.motivo = motivo

	def toString(self):
		return ({'id_receitaIncomum':id_receitaIncomum,
				 'receita_id_receita': receita_id_receita,
				 'atualizada':atualizada,
				 'emissor':emissor,
				 'motivo':motivo})

class ReceitaComun(db.Model):
	__tablename__ = "ReceitasComuns"
	id_receitaComum = db.Column(db.Integer, primary_key = True, autoincrement = True)
	receita_id_receita = db.Column(db.Integer, db.ForeignKey('Receitas.id_receita'), nullable = False)
	is_constante = db.Column(db.Boolean, nullable = False)
	is_automatica = db.Column(db.Boolean, nullable = False)
	diaMes = db.Column(db.Integer)
	status = db.Column(db.String(45)) # Status?? seria motivo? Como funciona na aplicação
	
	def __init__(self, receita_id_receita, is_constante, is_automatica, diaMes, status):
		self.receita_id_receita = receita_id_receita
		self.is_constante = is_constante
		self.is_automatica = is_automatica
		self.diaMes = diaMes
		self.status = status

	def toString(self):
		return ({'id_receitaComum': id_receitaComum,
				 'receita_id_receita': receita_id_receita,
				 'is_constante':is_constante,
				 'is_automatica':is_automatica,
				 'diaMes':diaMes,
				 'status':status})

class DepesaComum(db.Model):
	__tablename__ = "DespesasComuns"
	id_despesaComum = db.Column(db.Integer, primary_key = True, autoincrement = True)
	despesa_id_despesa = db.Column(db.Integer, db.ForeignKey('Despesas.id_despesa'), nullable = False)
	is_constante = db.Column(db.Boolean, nullable = False)
	is_automatica = db.Column(db.Boolean, nullable = False)
	diaMes = db.Column(db.Integer)
	status = db.Column(db.String(45)) # Status?? seria motivo? Como funciona na aplicação
	#Mudar o status para boolean??
	def __init__(self, despesa_id_despesa, is_constante, is_automatica, diaMes, status):
		self.despesa_id_despesa = despesa_id_despesa
		self.is_constante = is_constante
		self.is_automatica = is_automatica
		self.diaMes = diaMes
		self.status = status

	def toString(self):
		return ({'id_despesaComum':id_despesaComum,
				 'receita_id_receita': despesa_id_despesa,
				 'is_constante':is_constante,
				 'is_automatica':is_automatica,
				 'diaMes':diaMes,
				 'status':status})

class DespesaIncomum(db.Model):
	__tablename__ = "DespesasIncomuns"
	id_despesaIncomum = db.Column(db.Integer, primary_key = True, autoincrement = True)
	despesa_id_despesa = db.Column(db.Integer, db.ForeignKey('Despesas.id_despesa'), nullable = False)
	destino = db.Column(db.String(45)) #Pq só destino?? não deveria ser igual a o da receita incomum
	def __init__(self, despesa_id_despesa, destino):
		self.despesa_id_despesa = despesa_id_despesa
		self.destino = destino

	def toString(self):
		return ({'id_despesaIncomum':id_despesaIncomum,
				 'despesa_id_despesa': despesa_id_despesa,
				 'destino':destino})

class DespesaProgramada(db.Model):
	__tablename__ = "DespesasProgramadas"
	id_despesaProgramada = db.Column(db.Integer, primary_key = True, autoincrement = True)
	despesa_id_despesa = db.Column(db.Integer, db.ForeignKey('Despesas.id_despesa'), nullable = False)
	deferido = db.Column(db.Boolean)
	def __init__(self, despesa_id_despesa, deferido):
		self.despesa_id_despesa = despesa_id_despesa
		self.deferido = deferido

	def toString(self):
		return ({'id_despesaProgramada': id_despesaProgramada,
				 'despesa_id_despesa': despesa_id_despesa,
				 'deferido':deferido})

class DespesaEstimada(db.Model):
	__tablename__ = "DespesasEstimadas"
	id_despesaEstimada = db.Column(db.Integer, primary_key = True, autoincrement = True)
	despesa_id_despesa = db.Column(db.Integer, db.ForeignKey('Despesas.id_despesa'), nullable = False)
	confirmada = db.Column(db.Boolean)
	def __init__(self, despesa_id_despesa, confirmada):
		self.despesa_id_despesa = despesa_id_despesa
		self.confirmada = confirmada

	def toString(self):
		return ({'id_despesaEstimada': id_despesaEstimada,
				 'despesa_id_despesa': despesa_id_despesa,
				 'confirmada':confirmada})
		
class AuxilioDependencia(db.Model):
	__tablename__ = "AuxiliosDependencias"
	id_auxilio = db.Column(db.Integer, primary_key = True, autoincrement = True)
	id_dependente = db.Column(db.Integer, db.ForeignKey('Dependentes.id_dependente'), nullable = False)
	valor = db.Column(db.Integer, nullable = True)
	deferido = db.Column(db.Boolean, nullable = True)

	def __init__(self, id_dependente, valor, deferido):
		self.id_dependente = id_dependente
		self.valor = valor
		self.deferido = deferido

	def toString(self):
		return ({'id_auxilio': id_auxilio,
				 'id_dependente':id_dependente,
				 'valor':valor,
				 'deferido':deferido})

		

		
		


		
		
		

		
