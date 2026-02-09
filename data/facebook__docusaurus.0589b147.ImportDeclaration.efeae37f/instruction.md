# Bug Report

### Describe the bug

Translation extraction is not working for my Docusaurus site. When I use the `Translate` component or the `translate()` function in my React components, the translations are not being extracted properly.

### Reproduction

```jsx
import Translate from '@docusaurus/Translate';
import {translate} from '@docusaurus/Translate';

function MyComponent() {
  const label = translate({
    id: 'homepage.title',
    message: 'Welcome to my site',
  });

  return (
    <div>
      <h1>{label}</h1>
      <Translate id="homepage.subtitle">
        This is a subtitle
      </Translate>
    </div>
  );
}
```

When I try to extract translations from this component, nothing gets extracted. The translation files remain empty or don't include these strings.

### Expected behavior

The translation extractor should detect both the `Translate` component and the `translate()` function calls and extract the translation IDs and messages into the translation JSON files.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This used to work fine before, but recently stopped detecting translations in my components. Not sure what changed but it's blocking our i18n efforts.

---
Repository: /testbed
