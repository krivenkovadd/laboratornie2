class SocialNetwork:
    """Базовый класс для социальных сетей."""

    def __init__(self, username: str, password: str):
        """
        Конструктор базового класса.

        :param username: Имя пользователя.
        :param password: Пароль пользователя.
        """
        self._username = username
        self._password = password

    def __str__(self) -> str:
        """
        Строковое представление объекта.

        :return: Строка с информацией о социальной сети и имени пользователя.
        """
        return f"Социальная сеть: {self.__class__.__name__}, Пользователь: {self._username}"

    def __repr__(self) -> str:
        """
        Представление объекта для отладки.

        :return: Строка с информацией о классе, имени пользователя и пароле.
        """
        return f"{self.__class__.__name__}(username={self._username!r}, password={self._password!r})"

    def post_message(self, message: str) -> None:
        """
        Метод для публикации сообщения в социальной сети.

        :param message: Текст сообщения.
        """
        print(f"Сообщение опубликовано: {message}")

    def _connect_to_server(self) -> None:
        """
        Приватный метод для подключения к серверу социальной сети.
        Инкапсулирован, так как является внутренней деталью реализации.
        """
        print("Подключение к серверу...")


class VK(SocialNetwork):
    """Класс для социальной сети VK."""

    def __init__(self, username: str, password: str, group: str):
        """
        Конструктор класса VK.

        :param username: Имя пользователя.
        :param password: Пароль пользователя.
        :param group: Группа пользователя.
        """
        super().__init__(username, password)
        self.group = group

    def post_message(self, message: str) -> None:
        """
        Перегруженный метод для публикации сообщения в VK.
        Добавляет указание группы пользователя при публикации.

        :param message: Текст сообщения.
        """
        self._connect_to_server()
        print(f"Сообщение опубликовано в группе {self.group}: {message}")

    def join_group(self, group_name: str) -> None:
        """
        Метод для вступления в группу VK.

        :param group_name: Название группы.
        """
        self._connect_to_server()
        print(f"Вы вступили в группу: {group_name}")


class Facebook(SocialNetwork):
    """Класс для социальной сети Facebook."""

    def __init__(self, username: str, password: str, email: str):
        """
        Конструктор класса Facebook.

        :param username: Имя пользователя.
        :param password: Пароль пользователя.
        :param email: Email пользователя.
        """
        super().__init__(username, password)
        self.email = email

    def post_photo(self, photo_path: str) -> None:
        """
        Метод для публикации фотографии в Facebook.

        :param photo_path: Путь к файлу фотографии.
        """
        self._connect_to_server()
        print(f"Фотография опубликована: {photo_path}")
