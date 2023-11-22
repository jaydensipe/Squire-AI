import requests
import os
from colour import Color
import webcolors


class LIFX:
    def __init__(self):
        self.token = os.getenv("lifx_token")

    def get_status(self) -> None:
        response = requests.get(
            "https://api.lifx.com/v1/lights/all", auth=(self.token, "")
        )
        print(response.json())

    def turn_on(self) -> None:
        response = requests.put(
            "https://api.lifx.com/v1/lights/all/state",
            auth=(self.token, ""),
            data={"power": "on"},
        )
        print(response.json())

    def turn_off(self) -> None:
        response = requests.put(
            "https://api.lifx.com/v1/lights/all/state",
            auth=(self.token, ""),
            data={"power": "off"},
        )
        print(response.json())

    def set_color(self, response: str) -> None:
        color = [i for i in response.split(" ") if self.__check_color(i)]
        response = requests.put(
            "https://api.lifx.com/v1/lights/all/state",
            auth=(self.token, ""),
            data={"color": webcolors.name_to_hex(color[0].lower())},
        )
        print(response.json())

    @staticmethod
    def __check_color(color) -> bool:
        try:
            Color(color)
            return True
        except ValueError:
            return False
