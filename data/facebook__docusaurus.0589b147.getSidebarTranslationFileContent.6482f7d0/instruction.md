# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar translations in the docs plugin. It seems like the translatable sidebar items are not being included in the translation files anymore. Only non-translatable items are appearing in the generated translation JSON files.

### Reproduction

1. Set up a docs plugin with a sidebar containing translatable doc items
2. Generate translation files for the sidebar
3. Check the generated translation file content

Expected: Translatable sidebar doc items should be included in the translation files
Actual: Only non-translatable items are being included

### Expected behavior

When generating sidebar translation files, all items marked as `translatable: true` should be included in the translation output so they can be translated. Non-translatable items should be filtered out.

### Additional context

This is affecting our documentation localization workflow. The sidebar items that should be translatable are being excluded from the translation files, making it impossible to translate them properly.

---
Repository: /testbed
