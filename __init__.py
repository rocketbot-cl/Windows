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
        print(ScreenRes.get_modes())
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

if module == "getUserName":
    import user

    try:
        username = user.get_username()
        var_ = GetParams("var_")
        SetVar(var_, username)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "lockWindows":
    from screen import ScreenRes

    try:
        print("Se ha bloqueado su pantalla!")
        ScreenRes.lock_windows()
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "isLoggedIn":
    import user

    try:
        var_ = GetParams("var_")
        is_logged_in = user.is_logged_in()
        SetVar(var_, is_logged_in)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "maximizeWindow":
    import window

    title = GetParams("title")
    try:
        window.maximize_window(title)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "restoreWindow":
    import window

    title = GetParams("title")
    try:
        window.restore_window(title)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "minimizeWindow":
    import window

    title = GetParams("title")
    try:
        window.minimize_window(title)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "listWindows":
    
    
    try:
        import win32gui

        varToSaveIn = GetParams("varToSaveIn")
        checkHandles = GetParams("checkHandles")
        varFilter = GetParams("varFilter")

        handleInfo = []

        def winEnumHandler(hwnd, ctx):
                    global handleInfo
                    if win32gui.IsWindowVisible(hwnd):
                        handleInfo.append((hwnd, win32gui.GetWindowText(hwnd)))

        win32gui.EnumWindows(winEnumHandler, None)

        finalHandleInfo = []

        for h in handleInfo:
            # h is each handle
            # h[0] => each number of the handle
            # h[1] => each name (str) of the handle
            
            if (checkHandles == 'True'):
                    if (h[1] != ''):
                        if (varFilter):
                            result = h[1].find(varFilter)
                            if (result > -1):
                                finalHandleInfo.append(h)
                        else:
                            finalHandleInfo.append(h)
            else:
                print(checkHandles)
                if (h[1] != ''):
                    if (varFilter):
                        result = h[1].find(varFilter)
                        print(result)
                        if (result > -1):
                            finalHandleInfo.append(h[1])
                    else:
                        finalHandleInfo.append(h[1])

        SetVar(varToSaveIn, finalHandleInfo)

    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "setForeground":
    try:
        import win32gui
        title = GetParams("title")
        def set_window_to_foreground(title):
            import win32gui
            import win32con
            import win32com
            try:
                handle = win32gui.FindWindow(None, title)
                if not handle:
                    raise Exception('Could not find a window with title "{}"'.format(title))

                win32gui.ShowWindow(handle, win32con.SW_SHOWMAXIMIZED)
                shell = win32com.client.Dispatch("WScript.Shell")
                shell.SendKeys('%')
                win32gui.SetForegroundWindow(handle)
            except Exception as ex:
                raise ex
        set_window_to_foreground(title)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        PrintException()
        raise e
if module == "findWindow":
    import window

    title = GetParams("title")
    try:
        window_title = window.find_window_title(title)
        var_ = GetParams("var_")
        SetVar(var_, window_title)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "getServiceStatus":
    import service_windows

    title = GetParams("title")
    try:
        service_status = service_windows.get_service_status(title)
        var_ = GetParams("var_")
        SetVar(var_, service_status)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "startService":
    import service_windows

    title = GetParams("title")
    try:
        service_status = service_windows.get_service_status(title)
        if service_status != "running":
            service_windows.start_service(title)
            service_status = service_windows.get_service_status(title)
        var_ = GetParams("var_")
        SetVar(var_, service_status)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "stopService":
    import service_windows

    title = GetParams("title")
    try:
        service_status = service_windows.get_service_status(title)
        if service_status == "running":
            service_windows.stop_service(title)
            service_status = service_windows.get_service_status(title)
        var_ = GetParams("var_")
        SetVar(var_, service_status)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "moveWindow":
    title = GetParams("title")
    coord = GetParams("coordinates")
    size = GetParams("size")

    import win32gui

    handle = win32gui.FindWindow(None, "Note (98.260.00) From (0.3.250.00)")
    if not size:
        rect = win32gui.GetWindowRect(handle)
        w = rect[2] - rect[0]
        h = rect[3] - rect[1]
    else:
        w, h = eval(size)
    if coord:
        x, y = eval(coord)
    else:
        x, y = (0, 0)

    win32gui.MoveWindow(handle, x, y, w, h, True)




