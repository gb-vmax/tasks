# Bug Report

### Describe the bug

Translation extraction is not working for `@docusaurus/Translate` imports. When using the `Translate` component or `translate` function in my code, the translations are not being extracted during the build process.

### Reproduction

```jsx
import Translate, {translate} from '@docusaurus/Translate';

function MyComponent() {
  return (
    <div>
      <Translate>Hello World</Translate>
      <p>{translate({message: 'Welcome'})}</p>
    </div>
  );
}
```

When building the site, the translation strings "Hello World" and "Welcome" are not being extracted to the translation files.

### Expected behavior

The translation extractor should detect and extract all strings wrapped in `<Translate>` components and `translate()` function calls, regardless of how they are imported.

### System Info

- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening recently. The translations worked fine before but now they're completely missing from the extracted translation files.

---
Repository: /testbed
