# Bug Report

### Describe the bug

The `useBaseUrl` hook is generating incorrect URLs. When I use `useBaseUrl()` to construct URLs in my Docusaurus site, the resulting URLs have the `siteUrl` and `baseUrl` in the wrong order, leading to broken links.

### Reproduction

```jsx
import useBaseUrl from '@docusaurus/useBaseUrl';

function MyComponent() {
  const url = useBaseUrl('/docs/intro');
  console.log(url); // Outputs incorrect URL with siteUrl and baseUrl swapped
  
  return <a href={url}>Link</a>;
}
```

With a config like:
```js
{
  url: 'https://example.com',
  baseUrl: '/myapp/',
}
```

The generated URL has the parameters in the wrong positions, causing navigation to fail.

### Expected behavior

The `useBaseUrl` hook should correctly combine the site URL and base URL to produce valid links that work properly for navigation.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
