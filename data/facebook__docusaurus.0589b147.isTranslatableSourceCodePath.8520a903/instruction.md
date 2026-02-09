# Bug Report

### Describe the bug

Translation extraction is not working for source code files. It seems like files with translatable extensions (`.js`, `.jsx`, `.ts`, `.tsx`) are not being detected properly, which means their translation strings are not being extracted.

### Reproduction

1. Create a React component file with translation calls (e.g., `MyComponent.tsx`)
2. Add some translatable text using the `<Translate>` component or `translate()` function
3. Run the translation extraction process
4. Check the generated translation files

**Expected:** Translation strings from `.tsx` (and other valid source code extensions) should be extracted

**Actual:** Translation strings are not being extracted from these files

### Example

```tsx
// src/components/MyComponent.tsx
import Translate from '@docusaurus/Translate';

export default function MyComponent() {
  return (
    <div>
      <Translate id="my.translation.id">Hello World</Translate>
    </div>
  );
}
```

The translation ID `my.translation.id` should be extracted but isn't showing up in the translation files.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is blocking our i18n implementation. Any help would be appreciated!

---
Repository: /testbed
