package sr.ice.server;
import com.zeroc.Ice.Current;
import home.*;

public class CameraI implements Camera {

    @Override
    public Coords getLocation(Current current) {
        return null;
    }

    @Override
    public CameraInfo getInfo(Current current) {
        return null;
    }

    @Override
    public void setPosition(float pan, float tilt, float zoom, Current current) throws DeviceOffException, InvalidValueException {

    }

    @Override
    public String getName(Current current) {
        return "";
    }

    @Override
    public DeviceState getState(Current current) {
        return null;
    }

    @Override
    public void turnOn(Current current) {

    }

    @Override
    public void turnOff(Current current) {

    }
}
