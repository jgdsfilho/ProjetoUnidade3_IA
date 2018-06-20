import numpy as np
import vrep
import sys
import time


# Encerra conexoes previas
vrep.simxFinish(-1)

# Faz a conexao com o Vrep
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)  # Connect to V-REP

# Verifica se a conexao foi efetiva
if clientID != -1:
    print("Conectado ao VRep!!  Obaaaaa!!!")
    vrep.simxAddStatusbarMessage(clientID, "Conexao estabelecida!", vrep.simx_opmode_buffer)

else:
    print("Nao conectado ao VRep!!!")
    sys.exit("Xau!!")

#Instancia objetos no Python para os handlers
codErro, ref = vrep.simxGetObjectHandle(clientID, 'ref', vrep.simx_opmode_oneshot)

codErro, dummy = vrep.simxGetObjectHandle(clientID, 'dummy', vrep.simx_opmode_oneshot)

codErro, pioneerColDetect = vrep.simxGetCollisionHandle(clientID, 'pioneerColDetect', vrep.simx_opmode_oneshot)

codErro, pioneerDistDetect = vrep.simxGetDistanceHandle(clientID, 'pioneerDistDetect', vrep.simx_opmode_oneshot)

# codErro, obstaculos = vrep.simxGetCollectionHandle(clientID, 'obstaculos', vrep.simx_opmode_oneshot)

codErro, robo = vrep.simxGetObjectHandle(clientID, 'Pionee_p3dx', vrep.simx_opmode_oneshot)

codErro, chao = vrep.simxGetObjectHandle(clientID, 'ResizableFloor_5_25', vrep.simx_opmode_oneshot)

posicao = vrep.simxGetObjectPosition(clientID,robo, -1, vrep.simx_opmode_buffer)
angulos = vrep.simxGetObjectOrientation(clientID, robo, -1, vrep.simx_opmode_buffer)
#distancia = vrep.simxReadDistance(clientID, pioneerDistDetect,
                                  #operationMode=vrep.simx_opmode_blocking)

time.sleep(3)
print posicao



codErroPosicao = vrep.simxSetObjectPosition(clientID, robo, ref, [1, 1, 1],
                           vrep.simx_opmode_buffer)
time.sleep(3)

print codErroPosicao

# print posicao
#print angulos[1][1]
#print distancia[1]