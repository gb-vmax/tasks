# Bug Report

### Describe the bug

I'm experiencing an issue with translation extraction where some translations are being lost or not properly merged when extracting from multiple source code files. It seems like the first file's translations are being skipped and the merge order might be reversed, causing translations to be overwritten incorrectly.

### Reproduction

1. Create multiple source code files with translations
2. Ensure the first file has unique translation keys
3. Run the translation extraction
4. Check the output - translations from the first file are missing

For example, if I have:
- `file1.js` with translation key `"hello": "Hello"`
- `file2.js` with translation key `"goodbye": "Goodbye"`

After extraction, only the translations from `file2.js` appear in the output. The translations from `file1.js` are completely missing.

Additionally, if there are duplicate keys across files, the wrong translation seems to be kept (earlier files overwrite later ones instead of the other way around).

### Expected behavior

All translation keys from all source files should be included in the extracted translation file. When duplicate keys exist, translations from later files should take precedence over earlier ones (or at least maintain consistent behavior).

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
