from connect import mycursor, mydb
import random
from datetime import datetime
from datetime import date

class Transacoes

    id = ''
    saldo = ''
    extrato = ''
    def __init__(self, parametro1):
        self.id = parametro1
    def create(self):
    # criar usuários "falsos"
        saldo_ent = float(input("Digite o saldo: "))
        extrato_ent = str(input("Digite o extrato:  "))
        
        values = (self.id, saldo_ent, extrato_ent, datetime.utcnow(), datetime.utcnow())
        
        try:
            mycursor.execute(
                "INSERT INTO usuarios(id_usuario, saldo, extrato, criado_data, atualizado_data) VALUES(%s, %s, %s, %s, %s)", values)
            mydb.commit()
        
        except ConnectionError:
            print("Ocorreu um erro ao cadastrar um novo usuário!")
            
            
        return 'Created', 201
            
    def query(self):
        # para inquerir...
        query_id = mycursor.execute(f"SELECT id_usuario, saldo FROM usuarios WHERE id_usuario={self.id}")
        
        origem_val = mycursor.fetchall()
        for i in origem_val:
            print(f"Número-da-Conta: {i[0]}\nSaldo: {i[1]}")
        return 200
    def transference(self):
        # para transferir os dados
        data_at = datetime.now().strftime('%y-%m-%d %H:%M:%S')
        
        chegada = int(input("Digite qual o número da conta que você deseja depositar: "))
        # se for igual...
        if self.id == chegada:
            print("Método não permitido!")
            exit()
        
        query_id = mycursor.execute(f"SELECT id_usuario, saldo FROM usuarios WHERE id_usuario={chegada}")
        chegada_val = mycursor.fetchall()
        
        id_ori = ''
        saldo_ori = ''
        # para a variavel no origem val
        for i in origem_val:
            id_ori = i[0]
            saldo_ori = i[1]
        
        id_dest = ''
        saldo_dest = ''
        # para a variavel no chegada_val
        for i in chegada_val:
            id_dest = i[0]
            saldo_dest = i[1]
        
        # se qualquer um dos dois forem diferente...
        if self.id != id_ori or chegada != id_dest:
            print("Conta Inexistente...")
            exit()
        
        val_retirada = float(input("Qual poderá ser o valor da transferência??"))
        # se for menor que 0
        if saldo_ori - val_retirada < 0:
            print("Saldo Insuficiente...")
        else:    
            try:
                muda = saldo_ori - val_retirada
                mycursor.execute(f"UPDATE usuarios SET saldo={muda} WHERE id_usuario={id_ori}")
                mycursor.execute(f"INSERT INTO extrato(id_conta, id_origem, id_destino, valor, data_extrato) VALUES({id_ori},{id_ori},{id_dest},{val_retirada},'Retirada','{data_at}')")
                
                saldo_fim = saldo_dest + val_retirada
                mycursor.execute(f"UPDATE usuarios SET saldo={saldo_fim} WHERE id_usuario={id_dest}")
                mycursor.execute(f"INSERT INTO extrato(id_conta, id_origem, id_destino, valor, data_extrato) VALUES({id_dest},{id_ori},{id_dest},{val_retirada},'Entrada','{data_at}')")
                # executar no banco
                mydb.commit()
                
                
            except ConnectionError:
                print("Não foi possivel realizar a operação.")
                
            return 'Updated',201
    def statement(self):
        try:
            parametro = "SELECT id_origem, id_destino, valor, tipo, data_extrato FROM extrato WHERE id_conta" + \
                str(self.id)
            mycursor.execute(parametro)
            extratos = mycursor.fetchall()
            # para a linha em "extratos"
            for row in extratos
                print("--------------------------------")
                print("Conta Origem: ", row[0])
                print("Conta Destino: ", row[1])
                print("Valor: ", row[2])
                print("Tipo: ", row[3])
                print("Data: ", row[4].strftime('%d/%m/%Y %H:%M:%S'))
                print("--------------------------------\n")
                
            except ConnectionError:
                print("Não foi possível realizar a operação.")
                
            return 200