package sr.ice.server;

import com.zeroc.Ice.Current;
import home.*;

public class CleanerI extends AbstractDeviceI implements Cleaner {

    private CleaningMode mode;
    private Coords location;
    private final Coords baseLocation;

    public CleanerI(String name, Coords baseLocation){
        super(name);
        this.mode = CleaningMode.NORMAL;
        this.location = baseLocation;
        this.baseLocation = baseLocation;
        this.state = DeviceState.OFF;
    }

    @Override
    public CleaningMode getMode(Current current) {
        return this.mode;
    }

    @Override
    public Coords getLocation(Current current) {
        return this.location;
    }

    @Override
    public void setMode(CleaningMode mode, Current current) throws DeviceOffException {
        if (this.state == DeviceState.ON) {
            this.mode = mode;
            System.out.println(this.name + ": Tryb ustawiony na " + mode + ".");
            return;
        }
        throw new DeviceOffException();

    }

    @Override
    public void returnToBase(Current current) throws DeviceOffException {
        if (this.state == DeviceState.ON){
            this.location = this.baseLocation;
            System.out.println(this.name + ": Powrót do bazy");
            return;
        }
        throw new DeviceOffException();
    }

    @Override
    public void moveToLocation(Coords location, Current current) throws DeviceOffException, InvalidValueException {
        if (this.state == DeviceState.ON){
            if (location.x < 0 || location.y < 0){
                throw new InvalidValueException();
            }
            this.location = location;
            System.out.println(this.name + ": Przesunięto do: x = " + location.x + ", y = " + location.y +".");
        }
        else {
            throw new DeviceOffException();
        }
    }
}
