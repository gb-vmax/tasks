# Bug Report

### Describe the bug

The locale fallback order seems to be incorrect when resolving translations. I'm noticing that my locale-specific translations aren't being picked up properly, and it seems like the system is trying script-based locales before region-based ones.

### Reproduction

When I set my locale to something like `"zh-CN"` (Chinese - China), the translation resolution doesn't work as expected. 

For example:
- I have translations available for `zh-CN` (Simplified Chinese for China)
- But the system appears to be looking for `zh-Hans` (Simplified Chinese script) first
- This causes my region-specific translations to be skipped

The same issue happens with other locales like `pt-BR` (Portuguese - Brazil) where it tries to resolve `pt-Latn` before `pt-BR`.

### Expected behavior

The locale resolution should prioritize region-specific locales (like `zh-CN`, `pt-BR`) before falling back to script-based locales (like `zh-Hans`, `pt-Latn`). This would match the natural fallback order that most i18n systems use:

1. Exact locale match (e.g., `zh-CN`)
2. Language + region (e.g., `zh-CN`)  
3. Language + script (e.g., `zh-Hans`)
4. Language only (e.g., `zh`)

Currently it seems to be checking script before region, which doesn't align with how most users organize their translation files.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
