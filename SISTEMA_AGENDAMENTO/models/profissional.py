class Profissional:
    def __init__(self, id, nome, especialidade, conselho, email, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_especialidade(especialidade)
        self.set_conselho(conselho)
        self.set_email(email)
        self.set_senha(senha)
    
    def set_id(self, id):
        if id < 0: raise ValueError('Id inválido')
        self.__id = id
    def get_id(self):
        return self.__id
    
    def set_nome(self, nome):
        if id == ' ': raise ValueError('Nome inválido')
        self.__nome = nome
    def get_nome(self):
        return self.__nome
    
    def set_especialidade(self, especialidade):
        if id == ' ': raise ValueError('Especialidade inválido')
        self.__especialidade = especialidade
    def get_especialidade(self):
        return self.__especialidade
    
    def set_conselho(self, conselho):
        if id == ' ': raise ValueError('Conselho inválido')
        self.__conselho = conselho
    def get_conselho(self):
        return self.__conselho
    
    def set_email(self, email):
        if email == ' ': raise ValueError('Email inválido')
        self.__email = email
    def get_email(self):
        return self.__email
    
    def set_senha(self, senha):
        if senha == ' ': raise ValueError('Senha inválida')
        self.__senha = senha
    def get_senha(self):
        return self.__senha
    
    def __str__(self):
        return f'ID - {self.__id} | NOME - {self.__nome} | ESPECIALIDADE - {self.__especialidade} | CONSELHO - {self.__conselho} | EMAIL - {self.__email} | SENHA - {self.__senha}'
    
    def to_json(self):
        dic = {
            'id':self.__id,
            'nome':self.__nome,
            'especialidade':self.__especialidade,
            'conselho':self.__conselho,
            'email':self.__email,
            'senha':self.__senha
        }
        return dic
    
    @staticmethod
    def from_json(dic):
        return Profissional(
            dic['id'],
            dic['nome'],
            dic['especialidade'],
            dic['conselho'],
            dic['email'],
            dic['senha']
        )
    
import json
class ProfissionalDAO():
    __objetos = []

    @classmethod
    def inserir (cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.__objetos:
            if aux.get_id() > id: 
                id = aux.get_id()
        obj.set_id(id + 1)
        cls.__objetos.append(obj)
        cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.__objetos:
            if obj.get_id() == id: return obj
        return None
    
    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.__objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("profissional.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Profissional.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass
    
    @classmethod
    def salvar(cls):
        with open("profissional.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default = Profissional.to_json)