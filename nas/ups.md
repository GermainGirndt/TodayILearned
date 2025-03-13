# UPS - Uninterrupt Power Supply

Eaton UPS Ellipse ECO 650 USB DIN (EL650USBDIN)

- Offline (standby) power supply: switches to battery power only when needed
- Lead-acid battery
  - 650 VA (Voltage-Amperes) / 400 W (Watts)
  - ~5-10 minutes typical runtime
  - Hot replacement is NOT (!) supported
- ~8-10ms (millisecond) delay during power cuts
- Surge protection (against voltage spikes), compliant with IEC 61643-1 standard.
- Circuit-Breaker reset button for power demand overload.

For being sure that the NAS won't abbrutly shutdown in case of power outages, you can use an UPS.

The UPS provides automatically a backup battery in case of power outages.

Besides that, it can emit an signal to inform the connected devices that the power outage occured and what's the current battery level.

By doing that, the connected devices can handle the signal and for instance enter standby mode and then shutdown completely.

## UPS - Eaton UPS Ellipse ECO 650 USB DIN

### Charge time

About 8 hours until full power.

### Power Outlets

3 "Master" outlets: battery + high voltage protection. For important master devices.

1 "Eco" outlets: high voltage protection. For less important peripherics.

### Setup

When connect to energy, the power button should automatically turn green.

After connected to energy and minimally charged, press the power button (which should be already green). By doing that, the battery can be used. Press the power button again to disable the battery use.

The Eco outlet can always be used, as long as the UPS is connected to the energy. In case of an outage, the Eco outlet does not receive energy.

### Integration with Synology NAS

Access your Synology NAS' page.

Then enter Control Panel > Hardware and Power > UPS.

Then select the desired configuration for handling the power outage signal. According to the information sign on this page, after the standby mode is entered, it can not longer be accessed and the green power light will blink continuously. After that, the NAS will automatically shutdown when the UPS has no energy.

The Synology NAS also serve as an UPS Server to other Synology NASes. By doing that, as soon as the NAS receive the power outage signal, it's going to broadcast to others, as configured. This is a good tool, for circunventing the fact that many UPS (as Eacon) do not support a network interface for broadcasting the signal to the devices in the LAN.
