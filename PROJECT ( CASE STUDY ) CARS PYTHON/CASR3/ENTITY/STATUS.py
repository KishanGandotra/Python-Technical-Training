class Status:
    def __init__(self, status_id: int, status_name: str):
        self.__status_id = status_id
        self.__status_name = status_name

    def get_status_id(self) -> int:
        return self.__status_id

    def set_status_id(self, status_id: int) -> None:
        self.__status_id = status_id

    def get_status_name(self) -> str:
        return self.__status_name

    def set_status_name(self, status_name: str) -> None:
        self.__status_name = status_name
