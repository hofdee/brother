"""Constants for Brother Printer library."""
ATTR_COUNTERS = "counters"
ATTR_FIRMWARE = "firmware"
ATTR_MAINTENANCE = "maintenance"
ATTR_MODEL = "model"
ATTR_NEXTCARE = "nextcare"
ATTR_SERIAL = "serial"
ATTR_STATUS = "status"

VAL_BW_COUNT = "b/w_count"
VAL_BELT_REMAIN = "belt_unit_remaining_life"
VAL_BELT_REMAIN_PAGES = "belt_unit_remaining_pages"
VAL_BLACK_COUNT = "black_count"
VAL_BLACK_TONER = "black_toner"
VAL_BLACK_TONER_REMAIN = "black_toner_remaining"
VAL_BLACK_TONER_STATUS = "black_toner_status"
VAL_COLOR_COUNT = "color_count"
VAL_CYAN_COUNT = "cyan_count"
VAL_CYAN_TONER = "cyan_toner"
VAL_CYAN_TONER_REMAIN = "cyan_toner_remaining"
VAL_DRUM_COUNT = "drum_count"
VAL_DRUM_REMAIN = "drum_remaining_life"
VAL_DRUM_REMAIN_PAGES = "drum_remaining_pages"
VAL_DRUM_STATUS = "drum_status"
VAL_FUSER_REMAIN = "fuser_remaining_life"
VAL_FUSER_REMAIN_PAGES = "fuser_unit_remaining_pages"
VAL_IMAGE_COUNT = "image_count"
VAL_LASER_REMAIN = "laser_remaining_life"
VAL_LASER_REMAIN_PAGES = "laser_unit_remaining_pages"
VAL_MAGENTA_COUNT = "magenta_count"
VAL_MAGENTA_TONER = "magenta_toner"
VAL_MAGENTA_TONER_REMAIN = "magenta_toner_remaining"
VAL_PF_1_REMAIN = "pf_kit_1_remaining_life"
VAL_PF_1_REMAIN_PAGES = "pf_kit_1_remaining_pages"
VAL_PF_MP_REMAIN = "pf_kit_mp_remaining_life"
VAL_PF_MP_REMAIN_PAGES = "pf_kit_mp_remaining_pages"
VAL_PRINTER_COUNT = "printer_count"
VAL_YELLOW_COUNT = "yellow_count"
VAL_YELLOW_TONER = "yellow_toner"
VAL_YELLOW_TONER_REMAIN = "yellow_toner_remaining"

OIDS = {
    ATTR_COUNTERS: "1.3.6.1.4.1.2435.2.3.9.4.2.1.5.5.10.0",
    ATTR_FIRMWARE: "1.3.6.1.4.1.2435.2.3.9.4.2.1.5.5.17.0",
    ATTR_MAINTENANCE: "1.3.6.1.4.1.2435.2.3.9.4.2.1.5.5.8.0",
    ATTR_MODEL: "1.3.6.1.4.1.2435.2.4.3.2435.5.13.3.0",
    ATTR_NEXTCARE: "1.3.6.1.4.1.2435.2.3.9.4.2.1.5.5.11.0",
    ATTR_SERIAL: "1.3.6.1.4.1.2435.2.3.9.4.2.1.5.5.1.0",
    ATTR_STATUS: "1.3.6.1.4.1.2435.2.3.9.4.2.1.5.4.5.2.0",
}

VALUES_COUNTERS = {
    "00": VAL_PRINTER_COUNT,
    "01": VAL_BW_COUNT,
    "02": VAL_COLOR_COUNT,
    "12": VAL_BLACK_COUNT,
    "13": VAL_CYAN_COUNT,
    "14": VAL_MAGENTA_COUNT,
    "15": VAL_YELLOW_COUNT,
    "16": VAL_IMAGE_COUNT,
}

VALUES_MAINTENANCE = {
    "11": VAL_DRUM_COUNT,
    "31": VAL_BLACK_TONER_STATUS,
    "41": VAL_DRUM_REMAIN,
    "63": VAL_DRUM_STATUS,
    "69": VAL_BELT_REMAIN,
    "6a": VAL_FUSER_REMAIN,
    "6b": VAL_LASER_REMAIN,
    "6c": VAL_PF_MP_REMAIN,
    "6d": VAL_PF_1_REMAIN,
    "6f": VAL_BLACK_TONER_REMAIN,
    "70": VAL_CYAN_TONER_REMAIN,
    "71": VAL_MAGENTA_TONER_REMAIN,
    "72": VAL_YELLOW_TONER_REMAIN,
    "81": VAL_BLACK_TONER,
    "82": VAL_CYAN_TONER,
    "83": VAL_MAGENTA_TONER,
    "84": VAL_YELLOW_TONER,
}

VALUES_NEXTCARE = {
    "73": VAL_LASER_REMAIN_PAGES,
    "77": VAL_PF_1_REMAIN_PAGES,
    "82": VAL_DRUM_REMAIN_PAGES,
    "86": VAL_PF_MP_REMAIN_PAGES,
    "88": VAL_BELT_REMAIN_PAGES,
    "89": VAL_FUSER_REMAIN_PAGES,
}

PERCENT_VALUES = [
    VAL_BELT_REMAIN,
    VAL_DRUM_REMAIN,
    VAL_FUSER_REMAIN,
    VAL_LASER_REMAIN,
    VAL_PF_1_REMAIN,
    VAL_PF_MP_REMAIN,
    VAL_BLACK_TONER_REMAIN,
    VAL_CYAN_TONER_REMAIN,
    VAL_MAGENTA_TONER_REMAIN,
    VAL_YELLOW_TONER_REMAIN,
]

OIDS_HEX = [OIDS[ATTR_COUNTERS], OIDS[ATTR_MAINTENANCE], OIDS[ATTR_NEXTCARE]]