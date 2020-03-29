# Automatically generated by GPRPy
import gprpy.gprpy as gp
mygpr = gp.gprpyProfile()
mygpr.importdata('G3.gpr')
mygpr.adjProfile(5,158.46)
mygpr.truncateY(400)
mygpr.dewow(9999999)
mygpr.remMeanTrace(9999999)
mygpr.agcGain(100)
mygpr.setVelocity(0.11)
mygpr.fkMigration()
mygpr.topoCorrect('G3_Topo_3d.txt',delimiter='\t')
mygpr.printProfile('G3.pdf', color='bwr', contrast=3, yrng=[1200,1225], asp=1, dpi=600)
mygpr.exportVTK('G3',gpsinfo=mygpr.threeD,thickness=0,delimiter='\t',aspect=1,smooth=True, win_length=51, porder=3)

