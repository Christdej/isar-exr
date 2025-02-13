from enum import Enum


class AwakeStatus(str, Enum):
    Awake = "AWAKE"
    Asleep = "ASLEEP"
    WakingUp = "WAKING_UP"
    GoingToSleep = "GOING_TO_SLEEP"


class ChargingState(str, Enum):
    Discharging = "DISCHARGING"
    Charging = "CHARGING"
    Charged = "CHARGED"


class ChargerType(str, Enum):
    NotConnected = "NOT_CONNECTED"
    WiredCharger = "WIRED_CHARGER"
    WirelessCharger = "WIRELESS_CHARGER"
