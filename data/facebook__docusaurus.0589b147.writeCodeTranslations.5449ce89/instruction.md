# Bug Report

### Describe the bug

I'm experiencing an issue with code translations where the translation file content is not being written correctly. When trying to write code translations, it seems like the wrong data is being passed to the file writer, resulting in corrupted or incorrect translation files.

### Reproduction

```js
const context = {
  siteDir: '/path/to/site',
  i18n: {
    currentLocale: 'en',
    locales: ['en', 'fr']
  }
}

const content = {
  'component.button.label': {
    message: 'Click me',
    description: 'Button label'
  }
}

const options = {
  messagePrefix: 'prefix'
}

await writeCodeTranslations(context, content, options)
// Expected: translation file with proper content
// Actual: file contains context object instead of translation messages
```

### Expected behavior

The `writeCodeTranslations` function should write the provided translation content to the appropriate file. The translation file should contain the messages and descriptions passed in the `content` parameter.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
