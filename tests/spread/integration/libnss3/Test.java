import java.io.ByteArrayInputStream;
import java.security.Security;
import sun.security.pkcs11.SunPKCS11;

public class Test {
    public static void main(String[] args){
        String config = "library=/usr/lib/x86_64-linux-gnu/nss/libsoftokn3.so" + "\n"
            + "name=\"Soft Token\"\n"
            + "slot=2\n"
            + "attributes=compatibility\n"
            + "allowSingleThreadedModules=true\n"
            + "showInfo=true\n"
            + "nssArgs=\"configdir='./conf' "
                        + "certPrefix='' "
                        + "keyPrefix='' "
                        + "secmod='secmod.db' "
                        + "flags='readOnly'\""
            + "\n";

        SunPKCS11 provider = new SunPKCS11(new ByteArrayInputStream(config.getBytes()));
        Security.insertProviderAt(provider, 1);
    }
}
