package sr.ice.server;
import com.zeroc.Ice.Current;
import home.*;

public class CameraI extends AbstractDeviceI implements Camera {
    private CameraInfo info;

    public CameraI(String name, Coords location) {
        super(name);
        this.state = DeviceState.OFF;
        this.info = new CameraInfo(location, 0.0f, 0.0f, 1.0f);
    }

    @Override
    public Coords getLocation(Current current) {
        return this.info.location;
    }

    @Override
    public CameraInfo getInfo(Current current) {
        return this.info;
    }

    @Override
    public void setPosition(float pan, float tilt, float zoom, Current current) throws DeviceOffException, InvalidValueException {
        if(this.state == DeviceState.ON){
            if (pan < 0.0f || pan > 360.0f || tilt < -90.0f || tilt > 90.0f || zoom < 1.0f || zoom > 10.0f) {
                throw new InvalidValueException();
            }
            this.info.pan = pan;
            this.info.tilt = tilt;
            this.info.zoom = zoom;

            System.out.println(name + ": Pozycja ustawiona na Pan=" + pan + ", Tilt=" + tilt + ", Zoom=" + zoom);
        }
        else{
            throw new DeviceOffException();
        }
    }
}
