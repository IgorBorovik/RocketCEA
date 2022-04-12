import tempfile, os
from rocketcea.cea_obj import CEA_Obj, get_rocketcea_data_dir, set_rocketcea_data_dir

print( 'ROCKETCEA_DATA_DIR =', get_rocketcea_data_dir() )

with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)
    
    subdir = os.path.join( tmpdirname, 'cea w spaces' )
    os.mkdir( subdir )
    print( 'subdir =', subdir )
    print( 'os.path.exists(subdir) =', os.path.exists(subdir) )
    print()

    set_rocketcea_data_dir( subdir )
    #print( 'ROCKETCEA_DATA_DIR =', get_rocketcea_data_dir() )

    C = CEA_Obj( oxName='LOX', fuelName='LH2', make_debug_prints=True)
    Isp = C.get_Isp(Pc=100.0, MR=1.0, eps=40.0)
    print( Isp )

