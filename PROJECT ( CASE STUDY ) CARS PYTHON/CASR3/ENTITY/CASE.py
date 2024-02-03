class Case:
    def __init__(self, case_id: int, case_description: str, incidents: list):
        self.__case_id = case_id
        self.__case_description = case_description
        self.__incidents = incidents

    def get_case_id(self) -> int:
        return self.__case_id

    def set_case_id(self, case_id: int) -> None:
        self.__case_id = case_id

    def get_case_description(self) -> str:
        return self.__case_description

    def set_case_description(self, case_description: str) -> None:
        self.__case_description = case_description

    def get_incidents(self) -> list:
        return self.__incidents

    def set_incidents(self, incidents: list) -> None:
        self.__incidents = incidents
