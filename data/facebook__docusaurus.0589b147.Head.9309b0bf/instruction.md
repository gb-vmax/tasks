# Bug Report

### Describe the bug

The `<Head>` component is no longer rendering children properly. When I try to add meta tags or other elements as children to the `<Head>` component, they don't appear in the document head.

### Reproduction

```jsx
import Head from '@docusaurus/Head';

function MyComponent() {
  return (
    <Head>
      <meta name="description" content="My page description" />
      <link rel="canonical" href="https://example.com" />
    </Head>
  );
}
```

### Expected behavior

The meta tags and other elements passed as children should be rendered in the document `<head>`. Previously this worked fine, but now the children are being ignored and don't appear in the DOM.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
