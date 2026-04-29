package sr.ice.server;

import com.zeroc.Ice.Current;
import home.DeviceOffException;
import home.DeviceState;
import home.GroundHeater;
import home.InvalidValueException;

public class GroundHeaterI extends HeaterI implements GroundHeater {
    private String floorMaterial = "none";
    public GroundHeaterI(String name) {
        super(name);
    }

    @Override
    public void setFloorMaterial(String material, Current current) {
        this.floorMaterial = material;
        System.out.println(name + ": Zmieniono materiał podłogi na: " + material);
    }


    @Override
    public void setTemperature(float value, Current current) throws DeviceOffException, InvalidValueException {
        if (this.state != DeviceState.ON) {
            throw new DeviceOffException();
        }
        if (value < 18.0f || value > 28.0f){
            throw new InvalidValueException();
        }

        this.temperature = value;
        System.out.println(name + ": Temperatura grzejnika ustawiona na: " + value + "C");
    }
}
