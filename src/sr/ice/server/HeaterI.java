package sr.ice.server;

import com.zeroc.Ice.Current;
import home.DeviceOffException;
import home.DeviceState;
import home.Heater;
import home.InvalidValueException;

public class HeaterI extends AbstractDeviceI implements Heater {

    protected float temperature;

    public HeaterI(String name) {
        super(name);
        this.state = DeviceState.OFF;
        this.temperature = 21.0f;
    }

    @Override
    public float getTemperature(Current current) {
        return this.temperature;
    }

    @Override
    public void setTemperature(float value, Current current) throws DeviceOffException, InvalidValueException {
        if (this.state == DeviceState.ON){
            if (value < 15.0f || value > 30.0f){
                throw new InvalidValueException();
            }
            this.temperature = value;
        }
        else {
            throw new DeviceOffException();
        }
    }
}
