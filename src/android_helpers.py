from typing import Dict, List

from kvdroid.tools import toast
from kvdroid.tools.lang import device_lang
from kvdroid.tools.contact import get_contact_details
from plyer import sms


class Android_Helpers:
    """To be used on Android."""

    def get_ph_book(self) -> Dict[str, List[str]]:
        """
        Get phone book from device.

        Returns:
            Dict[str, List[str]]: Dict[contact name, List[of phone no's]].
        """
        return get_contact_details("phone_book")

    def show_toast(self, text: str) -> None:
        """
        Show toast message onto device.

        Args:
            text (str): message to be shown.
        """
        toast(text)

    def send_sms(self, tel: str, msg: str) -> None:
        """
        Send sms from device.

        Args:
            tel (str): receiver phone number
            msg (str): message to be sent
        """
        sms.send(recipient=tel, message=msg)

    def check_lang() -> str:
        """
        Detect device default language.

        Returns:
            str: returns os lang in LA_la format
        """
        return device_lang()
