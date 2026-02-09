# Bug Report

### Describe the bug

When using the `<Head>` component with `children` prop, the children are not being passed through to the underlying Helmet component. The component seems to be filtering out the children prop, which prevents adding head elements using the children pattern.

### Reproduction

```jsx
import Head from '@docusaurus/Head';

function MyComponent() {
  return (
    <Head>
      <meta name="description" content="My page description" />
      <title>My Page Title</title>
    </Head>
  );
}
```

The meta tags and title inside the `<Head>` component are not being rendered in the document head.

### Expected behavior

The `<Head>` component should accept children and render them in the document head, similar to how react-helmet-async's `<Helmet>` component works. The children should be passed through and properly rendered as head elements.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
