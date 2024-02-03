class IncidentType:
    def __init__(self, type_id: int, type_name: str):
        self.__type_id = type_id
        self.__type_name = type_name

    def get_type_id(self) -> int:
        return self.__type_id

    def set_type_id(self, type_id: int) -> None:
        self.__type_id = type_id

    def get_type_name(self) -> str:
        return self.__type_name

    def set_type_name(self, type_name: str) -> None:
        self.__type_name = type_name
