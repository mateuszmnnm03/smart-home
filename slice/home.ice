#ifndef HOME_ICE
#define HOME_ICE

module home
{
    enum DeviceState {ON, OFF, ERROR};
    enum CleaningMode {SILENT, NORMAL, TURBO};

    exception InvalidValueException {string message;};
    exception DeviceOffException {};

    struct Coords
    {
        float x;
        float y;
    };

    struct CameraInfo
    {
        Coords location;
        float pan;
        float tilt;
        float zoom;
    };

    struct CleanerInfo
    {
        Coords location;
        CleaningMode mode;
    };

    interface Device{
        idempotent string getName();
        idempotent DeviceState getState();
        void turnOn();
        void turnOff();
    };

    interface Camera extends Device{
        idempotent Coords getLocation();
        idempotent CameraInfo getInfo();
        void setPosition(float pan, float tilt, float zoom) throws InvalidValueException, DeviceOffException;
    };

    interface Heater extends Device{
        idempotent float getTemperature();
        void setTemperature(float value) throws InvalidValueException, DeviceOffException ;
    };

    interface Cleaner extends Device{
        idempotent CleaningMode getMode();
        idempotent Coords getLocation();
        void setMode(CleaningMode mode) throws DeviceOffException;
        void returnToBase() throws DeviceOffException ;
        void moveToLocation(Coords location) throws DeviceOffException, InvalidValueException ;
    };

    interface GroundHeater extends Heater  // ogrzewanie podlogowe
    {
        void setFloorMaterial(string material);
    };

    interface Radiator extends Heater // kaloryfer
    {
        void setFanSpeed(int speed) throws InvalidValueException ;
    };
};

#endif