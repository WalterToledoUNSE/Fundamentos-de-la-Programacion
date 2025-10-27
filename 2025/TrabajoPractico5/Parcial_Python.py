import numpy as np

TFECHA=np.dtype([
    ('dia',int),
    ('mes',int),
    ('anio',int)
])

TLOTE=np.dtype([
    ('codigoLote',int),
    ('nombre',"U50"),
    ('tipo','U1'),
    ('superficie',int),
    ('fecha',TFECHA),
    ('costoBaseHectarea',float),
    ('estado',int)
])
def cargaLote(L):
    dim=9
    L[0]=(100,"Productor 100","S",40,(12, 8,2025),8100,0)
    L[1]=(101,"Productor 101","M",30,( 1, 8,2025),7500,0)
    L[2]=(102,"Productor 102","T",22,(21, 8,2025),3250,0)
    L[3]=(103,"Productor 103","S",21,(19,10,2025),8100,0)
    L[4]=(104,"Productor 104","M",26,(12, 9,2025),7500,0)
    L[5]=(105,"Productor 105","T",10,(12, 5,2025),3250,0)
    L[6]=(106,"Productor 106","S",32,( 6, 3,2025),8100,0)
    L[7]=(107,"Productor 107","S",66,(12, 7,2025),8100,0)
    L[8]=(108,"Productor 108","M",58,(12, 4,2025),7500,0)
    L[8]=(109,"Productor 109","M",52,(12, 4,2025),7500,0)
    return dim

def mostrarLotes(L, dimL):
    for i in range(dimL):
        print("Código de Lote: ",L[i]['codigoLote'])
        print("Nombre del Productor: ",L[i]['nombre'])
        print("Tipo de Cultivo: ",L[i]['tipo'])
        print("Superficie Cultivada: ",L[i]['superficie'])
        print("Fecha de Siembra: ",L[i]['fecha'])
        print("Costo Base por Hectarea: ",L[i]['costoBaseHectarea'])
        print("Estado del Lote: ",L[i]['estado'])
        print(' ')

DIM_MAX = 20
lotes = np.empty(DIM_MAX,dtype=TLOTE)
dimL=cargaLote(lotes)
mostrarLotes(lotes, dimL)