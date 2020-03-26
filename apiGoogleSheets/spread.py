# -*- Coding: UTF-8 -*-
#coding: utf-8

from oauth2client.service_account import ServiceAccountCredentials
import datetime
import gspread
import mysql.connector
import json
import time

#------------------------------------------------------------------------------
			#------------------VARIAVEIS DATA -------------------#
date_now = datetime.datetime.now()

date_afterMidNight = date_now.replace(hour=0, minute=0, second=0)
date_beforeMidNight = date_now.replace(hour=23, minute=59, second=59)

one_days_ago = date_afterMidNight - datetime.timedelta(days=1)
one_days_ago_after_23hours = date_beforeMidNight - datetime.timedelta(days=1)

DT_TEMPLATE = one_days_ago.strftime("%d/%m/%Y")
DT_INI = one_days_ago.strftime("%Y-%m-%d %H:%M:%S")
DT_FIM = one_days_ago_after_23hours.strftime("%Y-%m-%d %H:%M:%S")

#------------------------------------------------------------------------------
			#------------------VARIAVEIS QUERYS -------------------#

#------------------------------------------------------------------------------

def querysMysql():
	# Configuracoes do banco de dados 
	con = mysql.connector.connect(user='#', password='#',host='#',database='#')

	#----------------------------------------------------------------------------
	# Criando Statemant
	c = con.cursor(buffered=True , dictionary=True)
	#----------------------------------------------------------------------------
	#---------------###################QUERYS########################---------------#

	# Query Soma de notas NPS
	querySomaNota = """ 
		(SELECT sa.evaluation AS 'NOTA',
		sa.tipoSatisfaction as 'flagNPS'
		FROM sfs AS sa 
		LEFT JOIN ses as se ON se.sessionCode = sa.sessionCode 
		WHERE tipoSatisfaction IS NOT NULL AND sa.createdate >= '{0}' AND sa.createdate <= '{1}' 
		AND se.userRef NOT IN (2357723287650147,3819788814713616,2120042778096110,2546582828765265,2556592324376460,2149525391823920,2039613406150750))
	"""

	# Query NPS
	queryNPS = """
			(SELECT 
				COUNT(sa.evaluation) AS 'Quantidade de notas',
				sa.tipoSatisfaction as 'flagNPS'
				FROM sfs AS sa 
				LEFT JOIN ses as se ON se.sessionCode = sa.sessionCode 
				WHERE tipoSatisfaction IS NOT NULL AND sa.createdate >= '{0}' AND sa.createdate <= '{1}' 
				AND se.userRef NOT IN (2357723287650147,3819788814713616,2120042778096110,2546582828765265,2556592324376460,2149525391823920,2039613406150750)
				group by tipoSatisfaction)
		  	 """

	# Query Diaria
	queryDiaria = """
		(SELECT
		(SELECT COUNT(DISTINCT(us.sessionCode)) FROM us AS us LEFT JOIN session as se ON se.sessionCode = us.sessionCode INNER JOIN answer a ON a.id = us.answerId WHERE us.createDate >= '{1}' AND us.createDate <= '{2}' AND us.userSent = 1 AND us.answerid NOT IN (1817,2098) AND a.projectId = 4 AND se.userRef NOT IN (2973128816032857,3086401944720324,2039613406150750,2357723287650147,2834694949933452,3819788814713616,2120042778096110,2546582828765265,2556592324376460,2149525391823920,2464096286953855,2644601172284521,1866046596847726,3189047334444294)
		) AS 'Total de Sessoes unicas',
		(SELECT DISTINCT(COUNT(*)) FROM us as us LEFT JOIN ses as se ON se.sessionCode = us.sessionCode INNER JOIN answer a ON a.id = us.answerId WHERE us.text NOT IN ('qQs!+eTCh-CDX9a^') AND us.createdate >= '{3}' AND us.createdate <= '{4}' AND  us.answerId NOT IN (1817,2098) AND a.projectId = 4 AND us.usersent = 1 AND se.userRef NOT IN (2973128816032857,3086401944720324,2039613406150750,2357723287650147,2834694949933452,3819788814713616,2120042778096110,2546582828765265,2556592324376460,2149525391823920,2464096286953855,2644601172284521,1866046596847726,3189047334444294)
		) AS 'Total interacoes',
		(SELECT DISTINCT(COUNT(*)) FROM us as us LEFT JOIN ses as se ON se.sessionCode = us.sessionCode INNER JOIN answer a ON a.id = us.answerId WHERE us.createdate >= '{5}' AND us.createdate <= '{6}' AND  us.answerId NOT IN (1817,2098,1891,1890) AND a.projectId = 4 AND us.usersent = 1 AND se.userRef NOT IN (2973128816032857,3086401944720324,2039613406150750,2357723287650147,2834694949933452,3819788814713616,2120042778096110,2546582828765265,2556592324376460,2149525391823920,2464096286953855,2644601172284521,1866046596847726,3189047334444294)
		) AS 'Total interacoes sem IDK',
		(SELECT COUNT(us.answerId) FROM us AS us LEFT JOIN ses as se ON se.sessionCode = us.sessionCode INNER JOIN answer a ON a.id = us.answerId WHERE us.answerId = 1891 AND us.createDate >= '{7}' AND us.createDate <= '{8}'  AND a.projectId = 4 AND us.TEXT IS NULL AND se.userRef NOT IN (2973128816032857,3086401944720324,2039613406150750,2357723287650147,2834694949933452,3819788814713616,2120042778096110,2546582828765265,2556592324376460,2149525391823920,2464096286953855,2644601172284521,1866046596847726,3189047334444294)
		) AS 'Nao entendi')
      """
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	c.execute(queryDiaria.format(DT_FIM,DT_INI,DT_FIM,DT_INI,DT_FIM,DT_INI,DT_FIM,DT_INI,DT_FIM,DT_INI))
	rowsQueryDiaria = c.fetchall()

	c.execute(queryNPS.format(DT_INI,DT_FIM))
	rowsNps = c.fetchall()

	c.execute(querySomaNota.format(DT_INI,DT_FIM))
	rowsNpsNota = c.fetchall()

	armazenaDadosQuery = {
	'Data' : '',
	'Quantidade de sessoes unicas' : 0,
	'Total de interacoes' : 0,
	'Total de interacoes sem IDK' : 0,
	'Total IDK' : 0,
	'Resposta NPS Bot' : 0,
	'NPS Bot':0,
	'Detractors Bot' : 0,
	'Passives bot' : 0,
	'Promoters Bot' : 0,
	'Respostas NPS humano': 0,
	'NPS humano':0,
	'Detractors humano' : 0,	
	'Passives humano' : 0,	
	'PH': 0,
	'Falso positivo':0,
	'Assertividade*':0,	
	'% IDK':0
	}	

	quantidadePessoaDetractrosBot = 0;
	quantidadePessoaPassiveBot = 0;
	quantidadePessoaPromotersBot = 0;

	quantidadePessoaDetractrosATN = 0;
	quantidadePessoaPassiveATN = 0;
	quantidadePessoaPromotersATN = 0;


	for i in rowsQueryDiaria:

		if(i['Total interacoes sem IDK'] > i['Total interacoes']):
			armazenaDadosQuery['Total IDK'] = i['Total interacoes sem IDK'] - i['Total interacoes']
		elif(i['Total interacoes'] > i['Total interacoes sem IDK']):
			armazenaDadosQuery['Total IDK'] = i['Total interacoes'] -  i['Total interacoes sem IDK']

	armazenaDadosQuery['Total de interacoes sem IDK'] = i['Total interacoes sem IDK']
	armazenaDadosQuery['Total de interacoes'] = i['Total interacoes']
	armazenaDadosQuery['Quantidade de sessoes unicas'] = i['Total de Sessoes unicas']
	armazenaDadosQuery['Data'] = DT_TEMPLATE

	for i in rowsNpsNota:

		if(i['flagNPS'] == 5):

			if(i['NOTA'] >= 0 and i['NOTA'] <= 6):
				quantidadePessoaDetractrosBot = quantidadePessoaDetractrosBot + 1
				armazenaDadosQuery['Detractors Bot'] = quantidadePessoaDetractrosBot
			elif(i['NOTA'] >= 6 and i['NOTA'] <= 8):
				quantidadePessoaPassiveBot = quantidadePessoaPassiveBot + 1
				armazenaDadosQuery['Passives bot'] = quantidadePessoaPassiveBot
			elif(i['NOTA'] >= 9 and i['NOTA'] <= 10):
				quantidadePessoaPromotersBot = quantidadePessoaPromotersBot + 1
				armazenaDadosQuery['Promoters Bot'] = quantidadePessoaPromotersBot
				
		elif(i['flagNPS'] == 4):

			if(i['NOTA'] >= 0 and i['NOTA'] <= 6):
				quantidadePessoaDetractrosATN = quantidadePessoaDetractrosATN + 1
				armazenaDadosQuery['Detractors humano'] = quantidadePessoaDetractrosATN
			elif(i['NOTA'] >= 6 and i['NOTA'] <= 8):
				quantidadePessoaPassiveATN = quantidadePessoaPassiveATN + 1
				armazenaDadosQuery['Passives humano'] = quantidadePessoaPassiveATN
			elif(i['NOTA'] >= 9 and i['NOTA'] <= 10):
				quantidadePessoaPromotersATN = quantidadePessoaPromotersATN + 1
				armazenaDadosQuery['PH'] = quantidadePessoaPromotersATN
				print("Promotor",quantidadePessoaPromotersATN)

	armazenaDadosQuery['Resposta NPS Bot'] = 0
	armazenaDadosQuery['Respostas NPS humano'] = 0

	for i in rowsNps:
		
		if(i['flagNPS'] == 5):
			armazenaDadosQuery['Resposta NPS Bot'] = i['Quantidade de notas']
			print('NPS BOT ' ,armazenaDadosQuery['Resposta NPS Bot'] )
		elif(i['flagNPS'] == 4):
			armazenaDadosQuery['Respostas NPS humano'] = i['Quantidade de notas']
			print('NPS HUMANO ' ,armazenaDadosQuery['Respostas NPS humano'] )


	print(armazenaDadosQuery)

	return armazenaDadosQuery


def googleShsetsAPI():

	recuperaDictionary = querysMysql()

	# Chamada de acesso a api
	scope = ['https://spreadsheets.google.com/feeds']

	
	# Credenciamento Producao Linux
	credentials = ServiceAccountCredentials.from_json_keyfile_name('/exemplo/googleSheetsAPI/credentials_exemplo.json', scope)

	# Autorizando o credenciamento
	gc = gspread.authorize(credentials)		
	

	# Apontando o ID da planilha Producao
	wks = gc.open_by_key('KEY')

	worksheet = wks.get_worksheet(0)
	list_of_lists = worksheet.get_all_values()
	end_row = len(list_of_lists)


	i = 0
	coluna = 1
	linha = end_row + 1

	formulaJ = '=((J{0}-H{0})/SOMA(H{0};J{0}))*100'.format(linha)
	formulaO = '=((O{0}-M{0})/SOMA(M{0};O{0}))*100'.format(linha)
	formulaAssertividade = '=1-R{0}'.format(linha)
	formulaIDK = '=E{0}/C{0}'.format(linha)

	try:
		while(i < len(recuperaDictionary.items())):
			# Formulas 

			if(i == 6 and coluna == 7):
				print('Formula coluna J',formulaJ)
				worksheet.update_cell(linha, coluna ,formulaJ)
				coluna = 8
				i = 7

			if(i == 11 and coluna == 12):
				print('Formula coluna O',formulaO)
				worksheet.update_cell(linha, coluna,formulaO)
				coluna = 13
				i = 12

			if(i == 15 and coluna == 16):
				worksheet.update_cell(linha, coluna,"não apurado")
				coluna = 17
				i = 16

			if(i == 16 and coluna == 17):
				worksheet.update_cell(linha, coluna,formulaAssertividade)
				coluna = 18
				i = 17

			if(i == 17 and coluna == 18):
				worksheet.update_cell(linha, coluna,formulaIDK)
				coluna = 19
				i = 18


			#extend = True
			if(worksheet.cell(linha,coluna).value in list(recuperaDictionary.keys())[i]):
				print("Coluna : " , coluna , "Linha : " , i , list(recuperaDictionary.values())[i])
				worksheet.update_cell(linha,coluna,list(recuperaDictionary.values())[i])

			coluna = coluna + 1

			i = i + 1
	except IndexError:
		print('indice no array invalido')

googleShsetsAPI()

#contador = 0
#q = 7
#while(q > 1):

#	if(contador == 5):
#		print("Printed immediately.")
#		time.sleep(200)
#		print("Printed after 200 seconds.")
#		contador = 0
#
#	googleShsetsAPI()
#	date_now = datetime.datetime.now()
#
#	date_afterMidNight = date_now.replace(hour=0, minute=0, second=0)
#	date_beforeMidNight = date_now.replace(hour=23, minute=59, second=59)
#
#	one_days_ago = date_afterMidNight - datetime.timedelta(days=q)
#	one_days_ago_after_23hours = date_beforeMidNight - datetime.timedelta(days=q)
#
#	DT_TEMPLATE = one_days_ago.strftime("%d/%m/%Y")
#	DT_INI = one_days_ago.strftime("%Y-%m-%d %H:%M:%S")
#	DT_FIM = one_days_ago_after_23hours.strftime("%Y-%m-%d %H:%M:%S")
#
#	q = q - 1
#	contador = contador + 1