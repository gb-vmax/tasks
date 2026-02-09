# Bug Report

### Describe the bug

After a recent update, `useDocusaurusContext()` no longer returns the `siteConfig` property. When trying to access `siteConfig` from the context object, it returns `undefined` even though it should contain the site configuration.

### Reproduction

```js
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

function MyComponent() {
  const context = useDocusaurusContext();
  
  // This is now undefined
  console.log(context.siteConfig); // undefined
  
  // Expected to access site title and other config
  const siteTitle = context.siteConfig?.title; // Error: Cannot read property 'title' of undefined
}
```

### Expected behavior

The `useDocusaurusContext()` hook should return an object that includes the `siteConfig` property with all site configuration values (title, tagline, url, etc.). This was working in previous versions and is documented in the API reference.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
