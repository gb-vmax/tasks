# Bug Report

### Describe the bug

When extracting translations from source code files, the first file's translations are being completely skipped. Only translations from the second file onwards are being included in the final output.

### Reproduction

```js
// file1.js
translate({id: 'home.title', message: 'Home'})

// file2.js  
translate({id: 'about.title', message: 'About'})
```

After running translation extraction, only `about.title` appears in the translation files. The `home.title` translation is missing from the output.

### Expected behavior

All translation keys from all source code files should be extracted and included in the translation output, including translations from the first file.

### Additional context

This seems to affect the main source code files. The issue causes incomplete translation files to be generated, which means some parts of the site won't have translation support.

---
Repository: /testbed
