import pytest

# 2. Параметризация фикстур и Косвенная параметризация (indirect)
# indirect=True позволяет передавать параметры из декоратора @pytest.mark.parametrize напрямую внутрь фикстуры.
# Это нужно, когда перед тестом объект необходимо как-то по-особому настроить или инициализировать в зависимости от нужд конкретного теста.

# Указываем indirect=["db_connection"], чтобы pytest понял:
# значение "sqlite" или "postgres" нужно отдать фикстуре, а не тесту напрямую!
@pytest.mark.parametrize("db_connection", ["sqlite", "postgres"], indirect=True)
def test_database_queries(db_connection):
    print(f"-> Выполнение запросов через: {db_connection}")
    assert "Соединение-" in db_connection

# 4. Динамическая параметризация во время исполнения тестов
# Обратите внимание, что сам тест выглядит чистым, на нем нет декоратора @pytest.mark.parametrize.
def test_dynamic_execution(dynamic_api_scenario):
    # Данные придут сюда автоматически благодаря хуку в conftest.py
    print(f"\n-> Запуск динамического сценария: {dynamic_api_scenario['id']}")
    print(f"-> Полезная нагрузка (Payload): {dynamic_api_scenario['payload']}")
    
    assert "Request" in dynamic_api_scenario['payload']

def test_environment_check(request):
    current_env = request.config.getoption("--env")
    print(f"requested_env = {current_env}")
    assert current_env in ["dev", "staging", "prod"]

def test_failed_example():
    print("This is failed test")
    assert False

# pytest -v -s --log-cli-level=DEBUG --tb=short
# pytest pytest_param_example_02.py -k "dynamic" -v -s

# TODO:
# 1) Написать тест для "API", который через indirect фикстуру меняет заголовки авторизации (User, Admin, Guest).
# 2) Написать динамическую параметризацию, которая сканирует указанную папку и генерирует тесты под каждый найденный там .txt или .json файл.
# 3) Сделать комбинаторный тест формы регистрации (Имя * Фамилия * Возраст) с красивыми кастомными ids.