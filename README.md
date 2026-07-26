# tennesseelabs.com

Marketing site for Tennessee Labs — applied AI studies and implementation for small
companies, specializing in medical devices and natural language processing.

Static HTML and CSS. No build step, no JavaScript, no dependencies beyond the
Google Fonts stylesheet (Newsreader, IBM Plex Sans, IBM Plex Mono).

```
index.html     the whole site
styles.css     tokens + layout
logo.svg       the mark, standalone (fixed colors)
favicon.svg    the mark on a paper tile, weights bumped for 16px
CNAME          custom domain for GitHub Pages
robots.txt
sitemap.xml
```

## The mark

A line of text with a bracket marking a span beneath it — the same gesture as
Fig. 1, and the notation NLP uses to mark constituents. Ink for the text, accent
blue for the bracket.

Three versions, deliberately not one file:

- **Masthead** — inlined in `index.html` so the text stroke inherits
  `currentColor` and the bracket picks up `--accent`.
- **`logo.svg`** — same geometry with fixed hex values, for anywhere the page's
  CSS can't reach (email signatures, slide decks, a README).
- **`favicon.svg`** — heavier strokes and a longer bracket. The masthead weights
  turn to mush at 16px; this is optically corrected, not scaled.

Keep at least 8px of clear space around the mark, and don't set it below 16px —
the bracket arms close up. On dark backgrounds, use paper for the text stroke and
lighten the bracket to about `#6ea8c8`; the 
`#1d5c7f` blue goes muddy against `#16181a`.

## Local preview

```sh
python3 -m http.server 8000    # then open http://localhost:8000
```

## Deploying on GitHub Pages

1. Settings → Pages → Source: **Deploy from a branch**, branch `main`, folder `/ (root)`.
2. Point DNS at GitHub, then set the custom domain to `tennesseelabs.com` and
   tick **Enforce HTTPS** once the certificate is issued (can take up to an hour).

DNS records at the registrar:

| Type  | Name  | Value                 |
|-------|-------|-----------------------|
| A     | `@`   | `185.199.108.153`     |
| A     | `@`   | `185.199.109.153`     |
| A     | `@`   | `185.199.110.153`     |
| A     | `@`   | `185.199.111.153`     |
| CNAME | `www` | `tacolopo.github.io.` |

## Editing notes

- Contact address `hello@tennesseelabs.com` appears in `index.html` once, in the
  contact section.
- The annotated note in Fig. 1 is synthetic. If it is ever replaced, the
  replacement must also be synthetic — never real patient text, de-identified or
  otherwise.
- Entity colors are defined once in `:root` and reused by both the annotation
  underlines and the legend swatches. Changing a color in one place changes both.
- Color is reserved for things that carry meaning (entity types, the accent rule
  on section labels). Adding decorative color breaks the premise.
