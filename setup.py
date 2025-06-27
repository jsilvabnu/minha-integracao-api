#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

def check_mysql_connection():
    """Verifica se o MySQL está rodando e acessível"""
    try:
        import pymysql
        from database import engine
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        print("✅ Conexão com MySQL estabelecida com sucesso!")
        return True
    except Exception as e:
        print(f"❌ Erro na conexão com MySQL: {e}")
        print("\n📋 Verifique se:")
        print("   1. O MySQL está instalado e rodando")
        print("   2. As credenciais no arquivo .env estão corretas")
        print("   3. O banco de dados 'meu_projeto' existe")
        return False

def create_database():
    """Cria o banco de dados se não existir"""
    try:
        import pymysql
        from database import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME
        
        # Conecta sem especificar o banco
        connection = pymysql.connect(
            host=DB_HOST,
            port=int(DB_PORT),
            user=DB_USER,
            password=DB_PASSWORD
        )
        
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print(f"✅ Banco de dados '{DB_NAME}' criado/verificado com sucesso!")
        
        connection.close()
        return True
    except Exception as e:
        print(f"❌ Erro ao criar banco de dados: {e}")
        return False

def install_dependencies():
    """Instala as dependências do projeto"""
    try:
        print("📦 Instalando dependências...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependências instaladas com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False

def setup_environment():
    """Configura o ambiente do projeto"""
    print("🚀 Configurando ambiente do projeto...")
    
    # Verifica se o arquivo .env existe
    if not os.path.exists(".env"):
        print("📝 Criando arquivo .env...")
        with open(".env", "w") as f:
            f.write("""# Configurações do Banco de Dados MySQL
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=root
DB_NAME=meu_projeto

# Configurações da API
API_HOST=127.0.0.1
API_PORT=5000
DEBUG=True
""")
        print("✅ Arquivo .env criado!")
    else:
        print("✅ Arquivo .env já existe!")

def main():
    """Função principal de configuração"""
    print("🔧 Configuração do Projeto - API MySQL")
    print("=" * 50)
    
    # 1. Instala dependências
    if not install_dependencies():
        return False
    
    # 2. Configura ambiente
    setup_environment()
    
    # 3. Cria banco de dados
    if not create_database():
        return False
    
    # 4. Testa conexão
    if not check_mysql_connection():
        return False
    
    print("\n🎉 Configuração concluída com sucesso!")
    print("\n📋 Para iniciar a aplicação, execute:")
    print("   python main.py")
    print("\n📋 Para testar a API, acesse:")
    print("   http://127.0.0.1:5000")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 