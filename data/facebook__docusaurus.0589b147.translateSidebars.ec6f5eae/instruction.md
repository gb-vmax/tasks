# Bug Report

### Describe the bug

After a recent update, the sidebar translations are not working correctly. The translated sidebars are being returned as an array instead of an object with sidebar names as keys. This breaks the sidebar structure and causes the documentation to fail rendering properly.

### Reproduction

When using multiple sidebars with translations:

```js
// Original sidebar structure
{
  tutorialSidebar: [...items],
  apiSidebar: [...items]
}

// After translation, it returns an array instead:
[
  [...items],
  [...items]
]
```

The sidebar names are lost in the translation process, which means the application can't properly map sidebars to their respective names.

### Expected behavior

The `translateSidebars` function should preserve the original object structure with sidebar names as keys, returning something like:

```js
{
  tutorialSidebar: [...translatedItems],
  apiSidebar: [...translatedItems]
}
```

Instead of an array of sidebar items.

### Additional context

This appears to affect any documentation site using multiple named sidebars with i18n translations enabled. The sidebar configuration stops working because the mapping between sidebar names and their content is lost.

---
Repository: /testbed
