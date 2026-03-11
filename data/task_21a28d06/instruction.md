Hey, I need help updating some symbolic links in our localization setup. We have a translation system where each supported language has its own `.po` file, and we use symlinks so that our app always reads from a canonical path. Our project lives at `/home/user/i18n`.

Here's the current structure:

```
/home/user/i18n/
  locales/
    en_US/
      messages.po      ← actual file (English, the source)
    pt_BR/
      messages.po      ← actual file (Brazilian Portuguese)
    pt_PT/
      messages.po      ← actual file (European Portuguese)
    fr_FR/
      messages.po      ← actual file (French)
  active/
    english.po         ← currently a symlink, but pointing to the wrong file (en_US/messages.po is correct, but it's currently pointing to fr_FR/messages.po by mistake)
    portuguese.po      ← currently a broken symlink (points to a path that doesn't exist: ../locales/pt/messages.po)
    french.po          ← currently a symlink correctly pointing to ../locales/fr_FR/messages.po (leave this one alone)
```

I need you to fix the symlinks in the `/home/user/i18n/active/` directory:

1. **Fix `english.po`**: Remove the existing (wrong) symlink and create a new symlink at `/home/user/i18n/active/english.po` that points to `../locales/en_US/messages.po`.

2. **Fix `portuguese.po`**: Remove the existing broken symlink and create a new symlink at `/home/user/i18n/active/portuguese.po` that points to `../locales/pt_BR/messages.po`.

3. **Leave `french.po` untouched** — it's already correct.

After making the changes, please write a short verification report to `/home/user/i18n/symlink_report.txt`. The file must contain exactly the following format (fill in the actual link target paths by resolving what each symlink points to):

```
english.po -> ../locales/en_US/messages.po
french.po -> ../locales/fr_FR/messages.po
portuguese.po -> ../locales/pt_BR/messages.po
```

Each line must be in the format `<symlink_name> -> <target>` where the target is the relative path stored in the symlink (not the resolved absolute path). Lines must be in alphabetical order by symlink name. There should be no trailing spaces and no blank lines.
