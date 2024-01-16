import asyncio
import inspect

class LoggerDecorator:
    def __init__(self, fn):
        self.fn = fn

    async def __call__(self, *args, **kwargs):
        print(f"Logging {self.fn.__name__}")
        print(f"Argumentos: {args}, {kwargs}")
        self.realy_weird_func()
        result = await self.fn(*args, **kwargs)
        print(f"Exiting {self.fn.__name__}")
        return result

    def realy_weird_func(self):
        print("""
        
        Make Something Really Weird First

        """)

@LoggerDecorator
async def main_function():
    print(f'Estou Rodando {inspect.currentframe().f_code.co_name}')
    task = asyncio.create_task(other())
    return_from_other = await task
    print(f'Estou em {inspect.currentframe().f_code.co_name}, e vou mostrar o valor que recebi de other: {return_from_other}')
    return f"Valor Final da {inspect.currentframe().f_code.co_name}"
    
@LoggerDecorator
async def other():
    print(f'Estou Rodando {inspect.currentframe().f_code.co_name}')
    return "Valor Retornado"

pega_valor_final = asyncio.run(main_function())

print(f'Peguei o valor final: {pega_valor_final}')


