# tennesseelabs.com

Marketing site for Tennessee Labs — applied AI studies and implementation for small
companies, specializing in medical devices and natural language processing.

Static HTML and CSS. No build step, no JavaScript, no dependencies beyond the
Google Fonts stylesheet (Newsreader, IBM Plex Sans, IBM Plex Mono).

```
index.html               the whole site
styles.css                tokens + layout
tennessee-labs-logo.svg   full lockup: mark + wordmark + tagline (fixed colors)
logo.svg                  the mark alone, standalone (fixed colors)
favicon.svg                the mark alone, on a paper tile, for 16px
CNAME                      custom domain for GitHub Pages
robots.txt
sitemap.xml
```

## The mark

A "T" built from a Tennessee state flag and a US flag set into its negative
space — ink black for the letterform, flag colors for the insets. Set beside a
rule and the "TENNESSEE LABS" wordmark plus the "AI FOR SMALL BUSINESSES"
tagline, it forms the full lockup in `tennessee-labs-logo.svg`.

Three versions, deliberately not one file:

- **Masthead** — the full lockup inlined in `index.html` (and `brief/index.html`),
  so it renders crisp at any size with no extra request.
- **`tennessee-labs-logo.svg`** — the full lockup as a standalone file, for
  anywhere the page can't be inlined (email signatures, slide decks, a README).
- **`logo.svg`** / **`favicon.svg`** — the mark alone, cropped tight, for square
  contexts (favicon, app icon, avatar). `favicon.svg` sits on a paper tile.

Colors are fixed hex values (flag red `#C8102E`/`#B22234`, flag blue
`#00205B`/`#3C3B6E`, ink `#201e1d`), not page tokens — the mark should look the
same wherever it's placed. Keep at least 8px of clear space around it, and
don't set the full lockup below about 120px wide — the tagline disappears
first, then the wordmark.

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
- **Both figures are synthetic and must stay that way.** Fig. 1's traces are
  hand-drawn SVG paths, not recordings; Fig. 2's note is invented. Never swap in
  real patient signals or text, de-identified or otherwise. The figures also must
  not be presented as output from a validated system — the caption says so, and
  it needs to keep saying so.
- The two figures are one clinical episode seen from each domain: Fig. 1 is the
  signal during the line placement, Fig. 2 is the note written after it. If you
  replace one, keep the link or drop it deliberately.
- Fig. 1's confidence values are illustrative. Don't quote them as performance.
- Colors live once in `:root`. The accent doubles as the P-wave stroke and the
  entity color for drugs; `--negated` grey plus a dashed stroke is the site's
  notation for *asserted absent or not resolvable*, used in both figures.
- Color is reserved for things that carry meaning. Adding decorative color breaks
  the premise.
