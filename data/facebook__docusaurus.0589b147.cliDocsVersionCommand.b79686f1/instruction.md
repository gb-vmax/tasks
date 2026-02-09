# Bug Report

### Describe the bug

When running the docs versioning command for a non-default locale, I'm getting an error saying no docs are found even though the docs directory exists and contains files. This seems to be backwards - it's throwing an error for localized versions but not for the default locale.

### Reproduction

1. Set up a Docusaurus site with i18n configured (e.g., default locale `en` and additional locale `fr`)
2. Add documentation files to the default locale docs directory
3. Try to create a new version using the CLI command
4. The command throws an error for the default locale instead of for missing localized docs

### Expected behavior

The command should throw an error if the **default locale** docs directory is missing or empty, and should skip or warn (not error) for non-default locales that don't have docs yet. Currently it seems to be doing the opposite.

### Additional context

Also noticed that new versions are being added to the end of the versions array instead of the beginning. This means the version order in `versions.json` is reversed from what it should be - newer versions should appear first in the list.

---
Repository: /testbed
