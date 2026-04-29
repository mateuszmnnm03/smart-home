package sr.ice.server;

import com.zeroc.Ice.Current;
import home.Device;
import home.DeviceState;

public class AbstractDeviceI implements Device {
    protected final String name;
    protected DeviceState state;

    public AbstractDeviceI(String name) {
        this.name = name;
    }

    @Override
    public String getName(Current current) {
        return this.name;
    }

    @Override
    public DeviceState getState(Current current) {
        return this.state;
    }

    @Override
    public void turnOn(Current current) {
        this.state = DeviceState.ON;
    }

    @Override
    public void turnOff(Current current) {
        this.state = DeviceState.OFF;
    }
}
