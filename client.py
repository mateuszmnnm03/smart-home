import Ice
import sys
import home

def print_menu(devices):
    print("\nDOSTĘPNE URZĄDZENIA")
    for i, dev_id in enumerate(devices):
        print(f"{i + 1}. {dev_id}")
    print("0. Wyjście")
    return input("Wybierz numer urządzenia: ")

def handle_camera(camera):
    print(f"\nObsługa kamery: {camera.getName()}")
    print("1. Włącz | 2. Wyłącz | 3. Ustaw pozycję | 4. Pobierz info")
    choice = input("Wybór: ")
    try:
        if choice == "1": camera.turnOn()
        elif choice == "2": camera.turnOff()
        elif choice == "3":
            p = float(input("Pan: "))
            t = float(input("Tilt: "))
            z = float(input("Zoom: "))
            camera.setPosition(p, t, z)
        elif choice == "4":
            info = camera.getInfo()
            print(f"Pozycja: {info.location.x}, {info.location.y} | PTZ: {info.pan}, {info.tilt}, {info.zoom}")
    except (home.DeviceOffException, home.InvalidValueException) as e:
        print(f"BŁĄD: {type(e).__name__}")

def handle_cleaner(cleaner):
    print(f"\nObsługa odkurzacza: {cleaner.getName()}")
    print("1. Włącz | 2. Wyłącz | 3. Pobierz tryb | 4. Ustaw tryb | 5. Pobierz lokalizację | 6. Ustaw lokalizację | 7. Wróć do bazy")
    choice = input("Wybór: ")
    try:
        if choice == "1": cleaner.turnOn()
        elif choice == "2": cleaner.turnOff()
        elif choice == "3":
            mode = cleaner.getMode()
            print(f"Tryb: {mode}")
        elif choice == "4":
            print("Dostępne tryby: 0-Silent, 1-Normal, 2-Turbo")
            m = int(input("Tryb: "))
            mode_enum = home.CleaningMode.valueOf(m) 
            cleaner.setMode(mode_enum)
            print("Tryb zmieniony.")
        elif choice == "5":
            loc = cleaner.getLocation()
            print(f"Lokalizacja: x = {loc.x}, y = {loc.y}")
        elif choice == "6":
            x = int(input("X: "))
            y = int(input("Y: "))
            cleaner.moveToLocation(home.Coords(x, y))
        elif choice == "7":
            cleaner.returnToBase()
    except (home.DeviceOffException, home.InvalidValueException) as e:
        print(f"BŁĄD: {type(e).__name__}")

    

def handle_heater(heater):
    print(f"\nObsługa grzejnika: {heater.getName()}")
    print("1. Włącz | 2. Wyłącz | 3. Ustaw temperaturę")
    if hasattr(home, 'RadiatorPrx') and home.RadiatorPrx.checkedCast(heater):
        print("4. Ustaw wentylator (Radiator)")
    if hasattr(home, 'GroundHeaterPrx') and home.GroundHeaterPrx.checkedCast(heater):
        print("5. Ustaw materiał podłogi (GroundHeater)")

    choice = input("Wybór: ")
    try:
        if choice == "1": heater.turnOn()
        elif choice == "2": heater.turnOff()
        elif choice == "3":
            temp = float(input("Temperatura: "))
            heater.setTemperature(temp)
        elif choice == "4":
            rad = home.RadiatorPrx.checkedCast(heater)
            rad.setFanSpeed(int(input("Prędkość (0-3): ")))
        elif choice == "5":
            gh = home.GroundHeaterPrx.checkedCast(heater)
            gh.setFloorMaterial(input("Materiał: "))
    except Exception as e:
        print(f"BŁĄD: {e}")

def main():
    with Ice.initialize([]) as communicator:
        device_ids = ["cam1", "cam2", "heater1", "heater2", "cleaner1", "cleaner2"]
        port = 10011

        while True:
            choice = print_menu(device_ids)
            if choice == "0": 
                break

            try:
                selected_id = device_ids[int(choice) - 1]
                proxy_str = f"{selected_id}:tcp -p {port}"
                base = communicator.stringToProxy(proxy_str)

                if home.CameraPrx.checkedCast(base):
                    handle_camera(home.CameraPrx.uncheckedCast(base))
                elif home.HeaterPrx.checkedCast(base):
                    handle_heater(home.HeaterPrx.uncheckedCast(base))
                elif home.CleanerPrx.checkedCast(base):
                    handle_cleaner(home.CleanerPrx.uncheckedCast(base))
                else:
                    print("Nieobsługiwany typ urządzenia.")

            except Exception as e:
                print(f"Błąd połączenia: {e}")

if __name__ == "__main__":
    main()