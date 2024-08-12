class Vacancy:
    """Класс для организации данных по вакансиям в удобном виде. хранит в себе полезные атрибуты по вакансиям"""

    def __init__(self, id: str | int, name: str, alternate_url: str, salary: int, requirement: str, employer_id: str, employer_name: str):
        """ Конструктор класса """

        self.id = id
        self.name = name
        self.employer_id = employer_id
        self.employer_name = employer_name
        self.alternate_url = alternate_url
        self.salary = salary
        self.requirement = requirement

    def __lt__(self, other):
        """ Метод сравнения зарплат """
        # if self.salary is not None and other.salary is not None:
        return self.salary < other.salary

    def __str__(self):
        """ Строковое представление вакансии """

        return (f'ID вакансии: {self.id}\n'
                f'ID компании: {self.employer_id}\n'
                f'Наименование компании: {self.employer_name}\n'
                f'Наименование вакансии: - {self.name}\n'
                f'Ссылка на вакансию {self.alternate_url}\n'
                f'Зарплата от - {self.salary},\n'
                f'Краткое описание: {self.requirement}\n')


if __name__ == "__main__":
    test_inst = Vacancy('12312', 'python', 'dasdasxvsda', 100, 'вообще пофиг', 740, 'яндекс')
    print(test_inst)
