
from config.constants import IP_DVR1, IP_DVR2, IP_DVR4, IP_DVR5, IP_DVR6, MHDX_1208, MHDX_3016_C
from features import automation
from utilities import convertPDF, resizeIMG, sendMAIL

# INICIA PROCESSO DE AUTOMAÇÃO CHAMANDO A FUNÇÃO checkDvr( ip, quantidade câmeras, modelo do dvr);
automation.checkDvr(IP_DVR1, 6, MHDX_1208)
automation.checkDvr(IP_DVR2, 13, MHDX_3016_C)
automation.checkDvr(IP_DVR4, 13, MHDX_3016_C)
automation.checkDvr(IP_DVR5, 12, MHDX_3016_C)
automation.checkDvr(IP_DVR6, 13, MHDX_3016_C)

# REDIMENSIONA IMAGENS
resizeIMG.resize()

# CRIA UM ARQUIVO PDF A PARTIR DAS IMAGENS REDIMENSIONADAS
convertPDF.createPDF()

# ENVIA POR E-MAILS em um Array
sendMAIL.send(['boenojonasm@cfjl.com.br', 'hammesmaiconr@cfjl.com.br'])
