# Bug Report

### Describe the bug

The `translate()` function is not extracting translations correctly when passed an object with `message`, `id`, and `description` properties. The translation extraction seems to fail silently or produces incorrect results.

### Reproduction

```js
// This translation is not being extracted properly
translate({
  message: "Welcome to the site",
  id: "homepage.welcome",
  description: "Greeting message on homepage"
})
```

When using the translate function with an object argument (as documented), the translations don't get extracted during the build process. The function should accept an object with `message`, `id`, and optional `description` fields, but it appears to be checking for the wrong type.

### Expected behavior

The translation extractor should properly handle object arguments passed to `translate()` and extract them into the translation files. The object format should work as intended:

```js
translate({
  message: "text to translate",
  id: "unique.translation.id",
  description: "context for translators"
})
```

### Additional context

This seems to have broken recently. The extractor is supposed to evaluate the first argument and extract the translation metadata, but something in the type checking logic appears to be wrong.

---
Repository: /testbed
