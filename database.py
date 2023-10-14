
from dotenv import load_dotenv # pip install dotenv
from sqlalchemy.engine import create_engine # pip instal sqlalchemy
from sqlalchemy import text
from pandas import read_sql # pip install pandas

from os import getenv # Python built-in

def conectar(**kwargs):
    """
    Função que conecta ao banco do SQL
    ----------------------------------

    Returns
    -------
    sqlalchemy.engine.base.Engine
    """

    # Load environment variables from the .env file
    load_dotenv()

    # Extraindo os argumentos de palavra-chave para a string de conexão
    driver = kwargs.pop('driver', 'mysqlconnector')
    host = kwargs.pop('host', getenv("DATABASE_HOST"))
    user = kwargs.pop('user', getenv("DATABASE_USERNAME"))
    password = kwargs.pop('password', getenv("DATABASE_PASSWORD"))
    database = kwargs.pop('database', getenv("DATABASE"))

    # Definindo os kwargs padrões para create_engine
    kwargs['connect_args'] = kwargs.get('connect_args', {'connect_timeout': 10})
    kwargs['echo'] =  kwargs.get('echo', False)
    
    # Conectando ao banco
    conection_string = f"mysql+{driver}://{user}:{password}@{host}/{database}"
    engine = create_engine(conection_string, **kwargs)
    return engine

def executar(sql_code, **kwargs):
    """
    Rotina que executa um comando em SQL
    ------------------------------------
    
    Parameters
    ----------
    sql_code : str
        O comando de projeção em SQL que irá ser executado
        
    Returns
    -------
    None
    """

    conexao = kwargs.pop('conexao', dict())
    with conectar(**conexao).connect() as c:
        c.execute(text(sql_code), **kwargs)
        c.commit()

def leitura(sql_code, **kwargs):
    """
    Função que ler e retorna um dateframe em pandas
    -----------------------------------------------
    
    Parameters
    ----------
    sql_code : str
        O comando de projeção em SQL que irá nos fornecer um dataframe
        
    Returns
    -------
    pandas.core.frame.DataFrame
    """
    
    # Passando para pandas
    conexao = kwargs.pop('conexao', dict())
    with conectar(**conexao).connect() as c:
        df = read_sql(text(sql_code), c, **kwargs)
    return df

def change_password(username, password):
    """
    Função que aletera a senha
    --------------------------
    
    Parameters
    ----------
    username : str
        O login do usário

    password : str
        A nova senha a ser salva
        
    Returns
    -------
    None
    """
    
    executar(f"UPDATE users SET password = '{password}' WHERE user = '{username}';")