from operacoesbd import *

conn = criarConexao('127.0.0.1', 'root', '12345678', 'ouvidoriabd') 

def listarManifestacoes(conn):
    sql = "select * from comentarios"
    lista = listarBancoDados(conn, sql)
    return (lista)
    

def criarNovaManifestacao(conn, descricao, autor, ouvidor, tipo):
    sql = "INSERT INTO comentarios (descricao, autor, ouvidor, tipo) VALUES (%s, %s, %s, %s)"
    dados = (descricao,autor, ouvidor, tipo)
    resultado = insertNoBancoDados (conn, sql , dados)
    return(resultado)


def exibirQuantidadeManifestacoes (conn) :
    sql = "SELECT COUNT(*) FROM comentarios;"
    quantidade = listarBancoDados(conn, sql)
    return(quantidade[0][0])


def pesquisarManifestacaoPorCodigo(conn, codigo):
    sql = "select * from comentarios where codigo = %s"
    resultadoPesquisa = listarBancoDados(conn,sql, tuple([codigo]))
    return(resultadoPesquisa)


def listarManifestacoesPorTipo (conn, tipo):
    sql = "select * from comentarios where tipo = %s"
    listaFiltrada = listarBancoDados(conn, sql, tuple([tipo]))
    return (listaFiltrada)


def excluirManifestacao (conn, codigo):
    #resultado vai ser 0 ou 1
    sql = "delete from comentarios where codigo = %s"
    resultadoExclusao = excluirBancoDados(conn, sql, tuple([codigo]))
    return(resultadoExclusao)

def filtrarTipo(tipo):
    if tipo == 1:
        tipo = 'reclamacao'
    elif tipo == 2:
        tipo = 'sugestao'
    elif tipo == 3:
        tipo = 'elogio'
    else:
        return
    return(tipo)
        

encerrarConexao(conn)

