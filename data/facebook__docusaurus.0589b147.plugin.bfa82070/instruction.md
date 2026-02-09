# Bug Report

### Describe the bug

I'm experiencing an issue with the `<head>` component in MDX files. After a recent update, the `<head>` tag is no longer being properly transformed to the `<Head>` component. This is causing metadata and SEO tags to not render correctly in my documentation.

### Reproduction

Create an MDX file with a `<head>` block element:

```mdx
# My Page

<head>
  <meta name="description" content="My page description" />
  <title>Custom Title</title>
</head>

Some content here.
```

The `<head>` tag should be transformed to `<Head>` but it's not happening anymore. The metadata doesn't get applied to the page.

### Expected behavior

The `<head>` tag in MDX should be automatically transformed to the Docusaurus `<Head>` component so that metadata and SEO tags are properly rendered in the page head.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
