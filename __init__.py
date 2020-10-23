# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import json
base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "Windows" + os.sep + "libs" + os.sep
sys.path.append(cur_path)
"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")

if module == "resize":
    from screen import ScreenRes

    resolution = GetParams("resolution")
    print(resolution)
    try:
        if resolution is not "" and resolution is not None:
            print('Changing resolution from: {}x{} to {}'.format(
                *ScreenRes.get(),
                resolution
            ))
            resolution = eval(resolution)
            print(resolution)
            ScreenRes.set(resolution[0], resolution[1])
        else:
            ScreenRes.set()  # Set defaults
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "getResolution":
    from screen import ScreenRes

    var_ = GetParams("var_")
    try:
        SetVar(var_, ScreenRes.get())

    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        PrintException()
        raise e