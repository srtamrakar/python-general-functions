import pandas
from datetime import datetime
from typing import NoReturn, Optional, Union


class DateOps(object):
    def __init__(self) -> NoReturn:
        pass

    @classmethod
    def get_year(
        cls,
        date_entity: Union[str, datetime, pandas._libs.tslib.Timestamp] = None,
        date_format: str = None,
    ) -> Optional[int]:
        """
        :param date_entity: str | datetime | pandas._libs.tslib.Timestamp
            an object representing date
        :param date_format: str
            date format, in case type(date_entity) == str
        :return:
            year from date as int
        """
        if date_entity is None:
            return None
        if date_format is None:
            date_format = "%Y-%m-%d"

        if isinstance(date_entity, (datetime, pandas._libs.tslib.Timestamp)) is True:
            return date_entity.year

        if isinstance(date_entity, str) is True:
            try:
                date_entity = datetime.strptime(date_entity, date_format)
            except ValueError:
                raise ValueError("Date should be in the format {0}".format(date_format))

            return date_entity.year

        return None

    @classmethod
    def text_to_datetime(cls, text: str = None, date_format: str = None) -> Optional[datetime]:
        """
        :param text: str
            string representation of a date
        :param date_format: str
            format of a date
        :return:
            datetime object of corresponding date
        """
        if date_format is None:
            date_format = "%Y-%m-%d"
        if isinstance(text, str) is True:
            try:
                datetime_from_text = datetime.strptime(text, date_format)
                return datetime_from_text
            except ValueError:
                raise ValueError("Date should be in the format {0}".format(date_format))
        return None

    @classmethod
    def get_difference_in_year(
        cls,
        from_date: Union[str, datetime, pandas._libs.tslib.Timestamp] = None,
        to_date: Union[str, datetime, pandas._libs.tslib.Timestamp] = None,
        date_format: str = None,
    ) -> Optional[int]:
        """
        :param from_date: str | datetime | pandas.*.Timestamp
            start date
        :param to_date:
            end date
        :param date_format:
            date format, in case type(date_entity) == str
        :return:
            difference between two dates as int
        """
        if from_date is None:
            return None

        if to_date is None:
            to_date = datetime.today()

        if (
            isinstance(from_date, (datetime, pandas._libs.tslib.Timestamp, str))
            is False
        ):
            return None

        if isinstance(to_date, (datetime, pandas._libs.tslib.Timestamp, str)) is False:
            return None

        if isinstance(from_date, str) is True:
            from_date = cls.text_to_datetime(text=from_date, date_format=date_format)

        if isinstance(to_date, str) is True:
            to_date = cls.text_to_datetime(text=to_date, date_format=date_format)

        years_diff = to_date.year - from_date.year

        if to_date.month < from_date.month:
            years_diff -= 1
            return years_diff

        if to_date.month == from_date.month and to_date.day < from_date.day:
            years_diff -= 1
            return years_diff

        return years_diff
