# Calculator CI/CD Project

Проект с автоматическими тестами для калькулятора, интегрированными в CI/CD через GitHub Actions.

## Структура проекта

- `calculator_class.py` - основной класс калькулятора
- `tests/test_calculator.py` - автоматические тесты
- `.github/workflows/run-tests.yml` - конфигурация CI/CD

## Локальный запуск тестов

```bash
pip install -r requirements.txt
pytest tests/ -v