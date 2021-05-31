from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "aloe_harvester aloe_timelord_launcher aloe_timelord aloe_farmer aloe_full_node aloe_wallet".split(),
    "node": "aloe_full_node".split(),
    "harvester": "aloe_harvester".split(),
    "farmer": "aloe_harvester aloe_farmer aloe_full_node aloe_wallet".split(),
    "farmer-no-wallet": "aloe_harvester aloe_farmer aloe_full_node".split(),
    "farmer-only": "aloe_farmer".split(),
    "timelord": "aloe_timelord_launcher aloe_timelord aloe_full_node".split(),
    "timelord-only": "aloe_timelord".split(),
    "timelord-launcher-only": "aloe_timelord_launcher".split(),
    "wallet": "aloe_wallet aloe_full_node".split(),
    "wallet-only": "aloe_wallet".split(),
    "introducer": "aloe_introducer".split(),
    "simulator": "aloe_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
