from datetime import datetime
import json
class MyClass():
    def __init__(self, conexao:str=None):
        """
        Se você fizer:
        def __init__(self):
            self.a = None

        Isso não permitirá você trocar o valor de 'a'
        """
        self.conexao = conexao    if conexao is None    else conexao
        self.logger  = {'Eventos':{}}

    def __str__(self):
        return "MyClass"

    def __repr__(self):
        return f'MyClass(conexao={self.conexao})'


    def __log(func):
        def inner(*args, **kwargs):
            self = args[0]
            timer = datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')
            temp = {timer:{
                "Classe": str(self),
                "Objeto": repr(self),
                "Funcao": str(func.__name__),
                "Argumentos posicionais":{f"Argumento {i}":arg if i>0 else repr(self) for i,arg in enumerate(args)},
                "Argumentos nomeados":{f"Argumento {nome}":arg for nome,arg in kwargs.items()}
            }}
            try:
                func( *args, **kwargs)
                temp[timer].update({'Status':'Sucesso'})
                self.logger['Eventos'].update(temp)
            except Exception as e:
                temp[timer].update({'Status':'Falha'})
                temp[timer].update({'Erro':f'{e}'})
                self.logger['Eventos'].update(temp)
                print(e)
                raise e
        return inner
    
    @__log
    def get_connection(self, conexao:str=None):
        if conexao is None: conexao = self.conexao
        
        conditions = [conexao is not None, isinstance(conexao, str)]
        if all(conditions):
            print('Inputs bem sucedidos. Estabelecendo conexao...')
            return True
        else:
            return false
    @__log
    def save_logger(self):

        with open("arquivo.json", "w") as arquivo:
            json.dump(self.logger, arquivo)
        


i = MyClass(conexao='Minha string de conexao')
i.get_connection(conexao=i.conexao)
i.save_logger()
print(json.dumps(str(i.logger)))