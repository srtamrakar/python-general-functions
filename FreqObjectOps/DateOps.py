import pandas
from datetime import datetime
from typing import NoReturn, Optional, Union


class DateOps(object):
    def __init__(self) -> NoReturn:
        pass

    @classmethod
    def get_year(
        cls,
        date_entity: Union[str, datetime, pandas.Timestamp],
        date_format: str = "%Y-%m-%d",
    ) -> Optional[int]:
        if isinstance(date_entity, (datetime, pandas.Timestamp)) is True:
            return date_entity.year
        elif isinstance(date_entity, str) is True:
            try:
                date_entity = datetime.strptime(date_entity, date_format)
                return date_entity.year
            except ValueError:
                raise ValueError(f"Date should be in the format {date_format}")
        else:
            raise TypeError(f"Date type not supported")

    @classmethod
    def text_to_datetime(
        cls, text: str, date_format: str = "%Y-%m-%d"
    ) -> Optional[datetime]:
        if isinstance(text, str) is True:
            try:
                datetime_from_text = datetime.strptime(text, date_format)
                return datetime_from_text
            except ValueError:
                raise ValueError(f"Date should be in the format {date_format}")

    @classmethod
    def get_difference_in_year(
        cls,
        from_date: Union[str, datetime, pandas.Timestamp],
        to_date: Union[str, datetime, pandas.Timestamp] = datetime.today(),
        date_format: str = "%Y-%m-%d",
    ) -> Optional[int]:
        if isinstance(from_date, str) is True:
            from_date = cls.text_to_datetime(text=from_date, date_format=date_format)

        if isinstance(to_date, str) is True:
            to_date = cls.text_to_datetime(text=to_date, date_format=date_format)

        years_diff = to_date.year - from_date.year

        if to_date.month < from_date.month:
            years_diff -= 1
            return years_diff
        elif to_date.month == from_date.month and to_date.day < from_date.day:
            years_diff -= 1
            return years_diff
        else:
            return years_diff
