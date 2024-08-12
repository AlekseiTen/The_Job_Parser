from abc import ABC, abstractmethod
import requests
from vacancy import Vacancy


class Parser(ABC):
    """
    Абстрактный класс для работы с API
    """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        pass


# ip адреса 10 компания в виде словаря
employers_ids = {
    108780: 'СКАУТ Разработчик Системы',
    3432635: 'ООО EVOS',
    9196211: 'JFoRecruitment',
    6000512: 'ООО Долсо',
    656481: 'Biglion',
    1577237: 'ООО Эрвез',
    5879545: 'ООО Фаст Софт',
    10882430: 'Лаборатория айти',
    2437802: 'ООО Леон',
    1740: 'Яндекс'
}


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом
    """
    employers_data = employers_ids

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '',
                       'employer_id': '',
                       'page': 0,
                       'only_with_salary': True,
                       'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword: str):
        """загружает данные c АПИ по определенным параметрам"""
        self.params['text'] = keyword
        self.params['employer_id'] = self.employers_data
        while self.params.get('page') != 10:
            response = requests.get(self.url, headers=self.__headers, params=self.params)
            response.raise_for_status()
            vacancy = response.json()['items']
            self.vacancies.extend(vacancy)
            self.params['page'] += 1
            print(self.vacancies)
        #return self.vacancies

    def parse_vacancies(self, vacancies: list[dict]) -> list[dict]:
        """ Метод фильтрует с API по заданным ключам и возвращает список словарей """

        items = []
        for i in vacancies:
            vacancy_id = i.get('id')
            vacancy_name = i.get('name')
            vacancy_url = i.get('alternate_url')

            salary_dict = i.get('salary')
            salary_from = salary_dict.get('from')
            if salary_from is None:
                salary_from = 0

            snippet_dict = i.get('snippet')
            snippet_requirement = snippet_dict.get('requirement')
            if snippet_requirement:
                snippet_requirement = snippet_requirement.replace('<highlighttext>', '').replace('</highlighttext>', '')
            else:
                snippet_requirement = 'нет требований'

            employer = i.get('employer')
            employer_id = employer.get('id')
            employer_name = employer.get('name')

            vacancy_object = Vacancy(vacancy_id, vacancy_name, vacancy_url, salary_from, snippet_requirement,
                                     employer_id, employer_name)



            items.append(vacancy_object)
        return items


if __name__ == "__main__":
    hh_api = HH()
    load_vac = hh_api.load_vacancies('a')
    #parse = hh_api.parse_vacancies(load_vac)
    #print(parse, sep='\n')

