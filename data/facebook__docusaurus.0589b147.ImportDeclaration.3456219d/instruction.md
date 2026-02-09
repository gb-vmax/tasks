# Bug Report

### Describe the bug

Translation extraction is not working correctly for files that import from `@docusaurus/Translate`. The `<Translate>` component and `translate()` function are not being detected, which causes translations to not be extracted from the source code.

### Reproduction

Create a React component that uses the translation features:

```jsx
import Translate, {translate} from '@docusaurus/Translate';

export default function MyComponent() {
  const label = translate({
    id: 'myComponent.label',
    message: 'Hello World',
  });

  return (
    <div>
      <Translate id="myComponent.title">Welcome</Translate>
      <p>{label}</p>
    </div>
  );
}
```

When running the translation extraction process, the translation strings are not being picked up from this file. The extracted translation files are missing the `myComponent.label` and `myComponent.title` entries.

### Expected behavior

The translation extractor should correctly identify imports from `@docusaurus/Translate` and extract all translation IDs and messages from both the `<Translate>` component and `translate()` function calls.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
