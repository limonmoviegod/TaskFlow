# Політика версіонування

## 1. Семантичне версіонування (SemVer 2.0.0)
Формат: **MAJOR.MINOR.PATCH** (наприклад, `1.2.3`).

| Частина | Коли збільшується | Приклад |
|---------|-------------------|---------|
| MAJOR | Несумісні (зламні) зміни API | `1.4.2 → 2.0.0` (змінено формат відповіді `/tasks`) |
| MINOR | Нова функціональність, сумісна зі старою | `1.0.0 → 1.1.0` (додано збереження в SQLite) |
| PATCH | Виправлення помилок без зміни API | `1.1.0 → 1.1.1` (виправлено помилку 500 при порожньому тілі) |

Правила:
- до `1.0.0` (версії `0.y.z`) API вважається нестабільним;
- після збільшення MAJOR скидаються MINOR і PATCH; після збільшення MINOR скидається PATCH;
- кожен реліз має git-тег `vX.Y.Z` і запис у `CHANGELOG.md`;
- pre-release: `1.1.0-rc.1`, `1.1.0-beta.2`.

## 2. Git-стратегія: спрощений GitFlow
| Гілка | Призначення | Створюється з | Зливається в |
|-------|-------------|---------------|--------------|
| `main` | Лише стабільні релізи (кожен коміт — тег) | — | — |
| `develop` | Інтеграція готових фіч | `main` | — |
| `feature/*` | Одна фіча — одна гілка | `develop` | `develop` |
| `release/X.Y.Z` | Підготовка релізу (версія, CHANGELOG, фікси) | `develop` | `main` і `develop` |
| `hotfix/*` | Термінові виправлення production | `main` | `main` і `develop` |

```
main     ●────────────────────────●(v1.0.0)──────●(v1.0.1)
          \                      /               /
develop    ●──●───────●──────●───●───────────────●
              \      /  \   /     \             /
feature/*      ●────●    ●─●       hotfix/*────●
```

## 3. Угода про коміти (Conventional Commits)
`type(scope): опис` — `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, `ci`.
- `fix` → PATCH, `feat` → MINOR, `feat!` / `BREAKING CHANGE:` → MAJOR.

## 4. Команди
```bash
# Нова фіча
git checkout -b feature/add-login develop
git add . && git commit -m "feat(auth): add login endpoint"
git push origin feature/add-login
# після code review
git checkout develop
git merge --no-ff feature/add-login
git push origin develop

# Реліз
git checkout -b release/1.0.0 develop
# оновити версію та CHANGELOG
git checkout main && git merge --no-ff release/1.0.0
git tag -a v1.0.0 -m "Release 1.0.0"
git push origin main v1.0.0
git checkout develop && git merge --no-ff release/1.0.0

# Hotfix
git checkout -b hotfix/fix-crash main
git commit -am "fix(tasks): handle empty body"
git checkout main && git merge --no-ff hotfix/fix-crash
git tag -a v1.0.1 -m "Release 1.0.1"
git checkout develop && git merge --no-ff hotfix/fix-crash
```

## 5. Процес релізу
1. Усі фічі спринту злиті в `develop`, CI зелений.
2. Створити `release/X.Y.Z`, підняти версію в `app/__init__.py`, оновити `CHANGELOG.md`.
3. Пройти `ACCEPTANCE_CHECKLIST.md`.
4. Злити в `main`, поставити тег, злити назад у `develop`.
5. Тег запускає GitHub Actions, що створює реліз з артефактом.
