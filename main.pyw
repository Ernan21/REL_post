import psycopg2
import json
from decimal import Decimal

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

def query_to_json(query_file, output_file):
    db_host = 'seu_host'
    db_port = 'sua_porta'
    db_name = 'seu_banco_de_dados'
    db_user = 'seu_usuario'
    db_password = 'sua_senha'

    try:
        # Lê o arquivo SQL e obtém a consulta
        with open(query_file, 'r') as file:
            query = file.read()

        # Conecta ao banco de dados
        connection = psycopg2.connect(
            host='192.168.0.100',
            port='38561',
            dbname='vr',
            user='ernando',
            password='Lycores123.'
        )
        cursor = connection.cursor()

        # Executa a consulta
        cursor.execute(query)
        results = cursor.fetchall()

        # Obtém o nome dos campos de resultado
        field_names = [desc[0] for desc in cursor.description]

        # Cria uma lista de dicionários com os resultados
        data = []
        for row in results:
            result_dict = dict(zip(field_names, row))
            data.append(result_dict)

        # Converte os resultados em JSON
        json_results = json.dumps(data, indent=4, default=decimal_default)

        # Salva os resultados em um arquivo JSON
        with open(output_file, 'w') as file:
            file.write(json_results)

        print(f"Os resultados da consulta foram salvos em {output_file}.")

    except (Exception, psycopg2.Error) as error:
        print("Erro ao executar a consulta:", error)

    finally:
        # Fecha a conexão com o banco de dados
        if connection:
            cursor.close()
            connection.close()


# Exemplo de uso
query_file = 'query.sql'
output_file ='vendaPIV/resultados.json'
query_to_json(query_file, output_file)