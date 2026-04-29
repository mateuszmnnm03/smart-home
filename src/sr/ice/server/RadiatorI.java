package sr.ice.server;

import com.zeroc.Ice.Current;
import home.DeviceOffException;
import home.DeviceState;
import home.InvalidValueException;
import home.Radiator;

public class RadiatorI extends HeaterI implements Radiator {
    private int fanSpeed = 0;
    public RadiatorI(String name) {
        super(name);
    }

    @Override
    public void setFanSpeed(int speed, Current current) throws InvalidValueException, DeviceOffException {
        if (this.state != DeviceState.ON) {
            throw new DeviceOffException();
        }
        if (speed < 0 || speed > 3) {
            throw new InvalidValueException();
        }
        this.fanSpeed = speed;
        System.out.println(name + ": Prędkość wentylatora ustawiona na: " + speed);
    }

    @Override
    public void setTemperature(float value, Current current) throws DeviceOffException, InvalidValueException {
        if (this.state != DeviceState.ON) {
            throw new DeviceOffException();
        }
        if (value < 10.0f || value > 45.0f) {
            throw new InvalidValueException();
        }

        this.temperature = value;
        System.out.println(name + ": Temperatura grzejnika ustawiona na: " + value + "C");
    }
}
