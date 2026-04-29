package sr.ice.server;
import com.zeroc.Ice.Communicator;
import com.zeroc.Ice.Identity;
import com.zeroc.Ice.ObjectAdapter;
import com.zeroc.Ice.Util;
import com.zeroc.Ice.InitializationException;
import home.Coords;

public class Server {

    public static void main(String[] args){
        String configFile = (args.length > 0) ? args[0] : "server2.config";
        try (Communicator communicator = Util.initialize(args, "server.config")) {

            ObjectAdapter adapter = communicator.createObjectAdapter("SmartHomeAdapter");

            adapter.add(new CameraI("Kamera Salon", new Coords(0, 0)), Util.stringToIdentity("cam1"));
            adapter.add(new CameraI("Kamera Wejscie", new Coords(50, 50)), Util.stringToIdentity("cam2"));

            adapter.add(new RadiatorI("Grzejnik Sypialnia"), Util.stringToIdentity("heater1"));
            adapter.add(new GroundHeaterI("Ogrzewanie Salon"), Util.stringToIdentity("heater2"));

            adapter.add(new CleanerI("Roomba Parter", new Coords(0,0)), Util.stringToIdentity("cleaner1"));
            adapter.add(new CleanerI("Roomba Pietro", new Coords(10,10)), Util.stringToIdentity("cleaner2"));

            adapter.activate();
            System.out.println("Serwer Smart Home wystartowal!");
            communicator.waitForShutdown();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
