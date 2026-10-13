# TaskFlow

Невеликий REST API для управління завданнями. Лабораторна робота №1 з курсу
«Технології створення програмних продуктів».

## Вміст репозиторію
| Файл | Призначення |
|------|-------------|
| `TЗ.md` | Технічне завдання |
| `LIFECYCLE.md` | Обґрунтування моделі життєвого циклу (Scrum + GitFlow) |
| `VERSIONING.md` | SemVer і Git-стратегія |
| `RELEASE_TEMPLATE.md` | Шаблон release notes |
| `CHANGELOG.md` | Історія змін (Keep a Changelog) |
| `ACCEPTANCE_CHECKLIST.md` | Чекліст приймання фічі |
| `REPORT.md` | Підсумковий звіт |
| `.github/workflows/ci.yml` | CI: тести + автоматичний реліз за тегом |

## Запуск
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask --app app run
```

## API
| Метод | Шлях | Опис |
|-------|------|------|
| GET | `/health` | Стан і версія |
| POST | `/tasks` | Створити завдання `{"title": "..."}` |
| GET | `/tasks[?done=true\|false]` | Список / фільтр |
| PATCH | `/tasks/<id>/done` | Позначити виконаним |

```bash
curl -X POST localhost:5000/tasks -H "Content-Type: application/json" -d '{"title":"Звіт"}'
curl "localhost:5000/tasks?done=false"
```

## Перевірка
```bash
pytest -q                 # тести
git log --oneline --graph --all   # історія гілок
git tag -n                # теги релізів
```

## Модель життєвого циклу
Scrum зі спринтами по 1 тиждень + спрощений GitFlow + CI. Деталі — у [LIFECYCLE.md](LIFECYCLE.md).
