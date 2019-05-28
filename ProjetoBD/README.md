Criar maquina virtual usando virtualenv para evitar conflitos de biblioteca ou pacotes python

	Para instalar
		sudo pip3 install virtualenv
	
	Para criar a maquina
		virtualenv -p python3 <nome_maquina>
	Para executar
		. <nome_maquina>/bin/activate
	Para desligar a maquina virtual
		deactivate

	Instalar as bibliotecas usadas
		pip3 install -r requirements.txt

	Para executar
		python3 run.py

	Para criar o banco de dados
		python3 run.py db migrate
		python3 run.py db upgrade
	//Verificar o arquivo ProjetoBD/storage.db

