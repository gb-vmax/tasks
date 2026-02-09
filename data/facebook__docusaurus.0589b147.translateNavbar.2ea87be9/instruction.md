# Bug Report

### Describe the bug

When using nested navbar items with translations, the sub-items are not being translated correctly. Instead of using their own labels to look up translations, they're using the parent item's label, which causes all sub-items to display the same translated text or fall back to their original labels.

### Reproduction

```js
// i18n translation file
{
  "item.label.Products": "Produits",
  "item.label.Product A": "Produit A",
  "item.label.Product B": "Produit B"
}

// navbar config
{
  label: 'Products',
  items: [
    { label: 'Product A' },
    { label: 'Product B' }
  ]
}
```

**Expected:** Sub-items should display "Produit A" and "Produit B"

**Actual:** Both sub-items are trying to use the translation key `item.label.Products` (the parent's label) instead of their own keys, so they fall back to displaying "Product A" and "Product B" in English.

### Expected behavior

Each navbar sub-item should use its own label to look up the corresponding translation, not the parent item's label.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
