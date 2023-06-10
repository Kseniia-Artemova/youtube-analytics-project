from src.channel import YouTube
from src.utils import find_value


class Video(YouTube):
    """Класс для ютуб-видео"""

    def __init__(self, video_id: str) -> None:
        """Экземпляр инициализируется по id видео. Дальше все данные будут подтягиваться по API."""
        # noinspection PyMissingConstructor

        self._video_id = video_id

        try:
            self.set_atr()

        except IndexError:

            self._title = None
            self._url = None
            self._views_count = None
            self._like_count = None

    @property
    def video_id(self) -> str:
        return self._video_id

    @video_id.setter
    def video_id(self, video_id: str):
        self._video_id = video_id

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str):
        self._title = title

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, url: str):
        self._url = url

    @property
    def views_count(self) -> str:
        return self._views_count

    @views_count.setter
    def views_count(self, views_count: str):
        self._views_count = views_count

    @property
    def like_count(self) -> str:
        return self._like_count

    @like_count.setter
    def like_count(self, likes_count: str):
        self._like_count = likes_count

    def get_info(self) -> dict:
        """Получает данные о видео по его id"""

        manager = self.get_service()

        video_info = manager.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                           id=self.video_id
                                           ).execute()
        return video_info

    def set_atr(self) -> None:
        """
        Устанавливает значения основных атрибутов объекта
        на основании полученных по id данных видео
        """

        video_info = self.get_info()

        self.title = video_info['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/watch?v={self.video_id}'
        self.views_count = video_info['items'][0]['statistics']['viewCount']
        self.like_count = video_info['items'][0]['statistics']['likeCount']

    def __str__(self) -> str:
        """Возвращает строку в формате: `<название_видео>`"""

        return f"{self.title}"


class PLVideo(Video):
    """Класс для ютуб-видео, принимающий также id плейлиста"""

    def __init__(self, video_id: str, video_pl: str) -> None:
        super().__init__(video_id)
        self._video_pl = video_pl