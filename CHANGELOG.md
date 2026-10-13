# Changelog
Формат — [Keep a Changelog](https://keepachangelog.com/uk/1.1.0/), версії — [SemVer](https://semver.org/lang/uk/).

## [Unreleased]

## [1.0.0] — 2026-10-27
### Added
- `GET /health` — стан і версія сервісу.
- `POST /tasks` і `GET /tasks` — створення та перегляд завдань.
- Фільтр `GET /tasks?done=true|false`.
- `PATCH /tasks/<id>/done` — позначення завдання виконаним.
- CI (GitHub Actions) з автоматичним релізом за тегом.

[Unreleased]: https://github.com/<user>/taskflow/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/<user>/taskflow/releases/tag/v1.0.0
