# CLAUDE.md — Projektová pravidla: Web U Cerhů

> Tento soubor je závazný pro celou dobu životnosti projektu.
> Claude Code ho čte automaticky při každém spuštění v tomto adresáři.
> Pravidla jsou psána česky/anglicky dle kontextu.

---

## 1. Identita projektu

| Položka | Hodnota |
|---|---|
| **Projekt** | Web statku U Cerhů — svatební místo & ubytování |
| **Soubor** | `index.html` (single-file SPA) |
| **Vlastník** | Jiří Bartoň, Na Rynku 7, 294 02 Kněžmost |
| **Telefon** | +420 605 971 109 |
| **Email** | jiri_barton@centrum.cz |
| **Domain** | ucerhu.cz |
| **GPS** | 50.4892°N, 15.0383°E |
| **Instagram** | https://www.instagram.com/ucerhu/ |
| **Facebook** | https://www.facebook.com/profile.php?id=100064278752605 |

---

## 2. Technický stack — ZÁVAZNÝ

```
HTML5 (sémantický)  +  Tailwind CSS (CDN)  +  Vanilla JavaScript
```

- **Žádné frameworky** (React, Vue, Angular…) — projekt je single-file HTML.
- **Žádné npm závislosti** ve výstupu — vše přes CDN.
- **Žádné `// TODO` placeholdery** — každý úsek musí být plně implementován.
- Tailwind loaded via: `<script src="https://cdn.tailwindcss.com"></script>`
- Fonty přes Google Fonts CDN:
  - Headings: **Playfair Display** (serif)
  - Body: **Inter** nebo **Montserrat** (sans-serif)

---

## 3. Architektura souboru

Projekt je **jediný soubor `index.html`**. Struktura dokumentu:

```
<head>
  ├── <meta> SEO + OG tagy
  ├── <title>
  ├── Schema.org JSON-LD (WeddingVenue + LocalBusiness)
  ├── Google Fonts link
  └── Tailwind CDN + inline <style> pro custom CSS

<body>
  ├── <header> — sticky nav + hamburger
  ├── <main>
  │   ├── #hero         — fullscreen hero + logo watermark
  │   ├── #pribeh       — Příběh & Historie (rok 1590, r. 1907)
  │   ├── #svatby       — Svatby & Kapacity (hlavní konverzní sekce)
  │   ├── #ubytovani    — Ubytování (23 lůžek, pokoje + apartmány)
  │   ├── #terminy      — Volné termíny 2026 (JS kalendář)
  │   ├── #galerie      — Foto galerie (Unsplash placeholdery)
  │   ├── #reference    — Recenze novomanželů
  │   └── #okoli        — Dostupnost & atrakce v okolí
  └── <footer>
      ├── SEO lokální hub text
      ├── Kontaktní formulář
      └── Sociální sítě + Google Maps iframe placeholder
```

---

## 4. Design system — ZÁVAZNÝ

### Barvy

```css
--color-bg:        #FDFBF7;  /* Primary Background — Cream/Warm Off-White */
--color-text:      #1E293B;  /* Primary Text — Deep Slate */
--color-text-dark: #0F172A;  /* Headings — Charcoal */
--color-accent:    #606C38;  /* Sage Green (primary accent) */
--color-accent-2:  #A3B18A;  /* Light Sage (secondary) */
--color-gold:      #D4AF37;  /* Muted Gold (highlights, CTA hover) */
```

### Logo symbol „Přeškrtnutý kruh"

Inline SVG zobrazující přeškrtnutý kruh (stylizované U, C, ů, most).
Použití na **třech místech** — tato pravidla nesmí být porušena:

1. **Hero sekce** — velký watermark na pozadí (opacity ~0.06)
2. **Oddělovač sekcí** — elegantní SVG divider mezi sekcemi
3. **Hover micro-animace** — rotace/rozsvícení na interaktivních prvcích

### Typografie

```css
font-family headings: 'Playfair Display', serif
font-family body:     'Inter', sans-serif  (fallback: 'Montserrat')
```

---

## 5. SEO pravidla — ZÁVAZNÁ

### `<title>`
```
U Cerhů | Exkluzivní svatební místo a ubytování v Českém ráji
```

### `<meta name="description">`
Must highlight: volné termíny 2026, prémiový historický statek, dostupnost z Prahy a Mladé Boleslavi. Max 160 znaků.

### Target keywords — přirozeně zapracovat do H1–H3, alt tagů a `<strong>`:
- Svatby Český ráj
- Ubytování Český ráj
- Svatební místo Mladá Boleslav
- Svatba Turnov
- Svatební stodola Jičín
- Romantická svatba Sobotka
- Statek na svatbu Kněžmost
- Pronájem areálu na svatbu Mnichovo Hradiště

### Schema.org JSON-LD v `<head>`
Typy: `WeddingVenue` + `LocalBusiness`
Povinné fieldy: `name`, `address` (PostalAddress), `telephone`, `email`, `url`, `geo` (GeoCoordinates), `openingHours`, `sameAs` (Instagram, Facebook).

---

## 6. Povinné copy — NESMÍ BÝT MĚNĚNO

Tyto textové bloky musí být zachovány doslova při každé úpravě:

### Storytelling hook (sekce Příběh):
> „Přes čtyři staletí pevné zdi statku. Přes století vůně poctivé kuchyně a smích hostů. Od roku 1907 píšeme příběh rodinné pohostinnosti bez jediného přerušení. Vítejte U Cerhů – na místě, kde se historie prolíná s vaším novým začátkem."

### SEO lokální hub (footer):
> „Hledáte dokonalé svatební místo v Českém ráji? Historický statek U Cerhů v Kněžmostě je ideálně dostupný z Mladé Boleslavi (15 min), Mnichova Hradiště (12 min), Jičína (30 min), Sobotky (20 min), Turnova (30 min) i Prahy (55 min)."

### Valečov copy (sekce Okolí):
> „Statek U Cerhů leží na hranici Českého ráje – od hradu Valečov vás dělí jen 3 km pěší turistické trasy."

---

## 7. Kapacity & data — ZÁVAZNÁ referenční tabulka

### Ubytování — 23 lůžek celkem

| Název | Lůžka | Poznámka |
|---|---|---|
| Pokoj 1 (hlavní budova) | 4 | Vlastní sociální zařízení, prémiové vybavení |
| Pokoj 2 (hlavní budova) | 4 | Vlastní sociální zařízení, prémiové vybavení |
| Pokoj 3 (hlavní budova) | 5 | Vlastní sociální zařízení, prémiové vybavení |
| Apartmán 1 (prázdninový domek) | 5 | Plně vybavená kuchyňka, soc. zařízení — **NOVÉ** |
| Apartmán 2 (prázdninový domek) | 5 | Plně vybavená kuchyňka, soc. zařízení — **NOVÉ** |
| **Celkem** | **23** | |

### Svatební kapacity

- Hosté: **max 100 osob**
- Exkluzivita: **1 svatba = celý víkend** (absolutní soukromí)
- Prostory: Hlavní sál, Stodola, Dvůr, Terasa, Ubytovací část

### Dostupnost z Kněžmostu

| Město | Vzdálenost | Čas |
|---|---|---|
| Mladá Boleslav | ~11 km | 15 min |
| Mnichovo Hradiště | ~10 km | 12 min |
| Sobotka | ~15 km | 20 min |
| Turnov | ~25 km | 30 min |
| Jičín | ~25 km | 30 min |
| Praha | ~75 km | 55 min |

---

## 8. JavaScript komponenty

### Komponenta: Kalendář volných termínů 2026

- Zobrazit: červen – září 2026
- Styl: vizuální grid s barevným kódováním
  - 🟥 Obsazeno (většina sobot)
  - 🟩 Volný termín (poslední 2–3 soboty)
- Urgency messaging: _„Poslední volné prázdninové termíny pro sezónu 2026"_
- Souboty jsou primární termíny, zobrazit všechny 4 měsíce.

### Komponenta: Navigace

- Sticky header s průhledností → solid po scrollu (JS scroll listener)
- Hamburger menu pro mobile (animace ≥ CSS transition)
- Hladký scroll na anchor sekce (`scroll-behavior: smooth` nebo JS)
- Aktivní stav nav položky dle aktuální sekce (IntersectionObserver)
- **Sticky CTA button**: `"Rezervovat termín 2026"` — vždy viditelný, barva zlatá/sage

---

## 9. UX & přístupnost — WCAG AA

- Všechny obrázky musí mít popisný `alt` text (v češtině, s target keywords).
- Kontrastní poměr textu: min 4.5:1 (AA standard).
- Keyboard navigace: fokus stavy na všech interaktivních prvcích.
- Semantické HTML5 elementy: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`, `<address>`.
- `aria-label` na ikonách bez textu, hamburger menu, sociálních odkazech.
- Skip-to-content link jako první prvek v `<body>`.

---

## 10. Galerie — pravidla pro placeholder obrázky

Zdroj: **Unsplash** (svobodné licence, bez atribuce).
Query terms pro sémanticky relevantní obrázky:

| Slot | Unsplash query |
|---|---|
| Hero | `rustic-wedding-venue` |
| Příběh | `old-farmhouse-countryside` |
| Svatby | `wedding-barn-reception` |
| Ubytování | `cozy-countryside-room` |
| Galerie 1 | `wedding-ceremony-outdoor` |
| Galerie 2 | `rustic-wedding-decoration` |
| Galerie 3 | `wedding-banquet-table` |
| Galerie 4 | `bohemian-paradise-czech` |
| Okolí | `czech-paradise-rocks` |

Format URL: `https://images.unsplash.com/photo-{ID}?w=800&q=80`

---

## 11. Cenová politika — ZÁVAZNÉ zobrazení

Ceny **nikdy nezobrazovat** jako pevné číslo.
Vždy použít CTA variantu:

- Ubytování: _„Ceny na vyžádání — kontaktujte nás"_
- Pronájem areálu na svatbu: _„Cena pronájmu na vyžádání — rádi vám připravíme nabídku na míru"_

---

## 12. Klíčové prodejní argumenty (USPs)

Vždy zobrazovat jako icon grid nebo bullet list v sekci Svatby:

1. **Exkluzivita** — 1 svatba = celý areál jen váš
2. **Ubytování přímo v areálu** (23 lůžek)
3. **Venkovní i vnitřní obřad**
4. **Historický statek s duší od r. 1590**
5. **3 generace rodinné pohostinnosti**
6. **Parkování zdarma** v areálu / u areálu
7. **WiFi v celém areálu** zdarma
8. **Plně bezbariérový přístup**
9. **Domácí mazlíčci vítáni**

---

## 13. Workflow pro změny

### Před každou úpravou:
1. Přečti tento `CLAUDE.md` celý.
2. Zkontroluj, zda úprava neporušuje povinné copy (sekce 6).
3. Zkontroluj, zda zůstávají správné kontaktní údaje (sekce 1).

### Při přidávání nové sekce/komponenty:
1. Drž se design systému (sekce 4) — barvy, fonty, logo.
2. Přidej sémantický HTML5 element s `id` pro scroll-navigaci.
3. Přidej odpovídající nav item s anchor linkem.
4. Zkontroluj WCAG AA (sekce 9).

### Při SEO úpravách:
1. Title tag nesmí být zkracován ani přeformulován.
2. Schema.org JSON-LD vždy aktualizuj při změně kontaktů/kapacit.
3. Target keywords z sekce 5 musí zůstat zastoupeny v H1–H3.

### Zakázané operace:
- ❌ Nezavádět npm / node_modules do projektu
- ❌ Nerozdělovat projekt na více souborů (musí zůstat single-file)
- ❌ Neměnit povinné copy bloky (sekce 6)
- ❌ Neuvádět pevné ceny (sekce 11)
- ❌ Neodstraňovat Schema.org JSON-LD
- ❌ Nepoužívat generické `alt=""` na obrázky

---

## 14. Git commit konvence

```
feat(sekce):  přidání nové sekce nebo komponenty
fix(copy):    oprava textu, překlepu
seo:          změna metadat, structured data, keywords
style:        vizuální úpravy bez změny funkce
content:      aktualizace termínů, kapacit, kontaktů
a11y:         úpravy přístupnosti (WCAG)
```

Příklad: `content(terminy): aktualizace volných sobot září 2026`

---

## 15. Kontextová poznámka pro Claude Code

Tento projekt je **marketingový web malého rodinného podniku**. Priorita je:

1. **Konverze** (kontaktní formulář, CTA tlačítko rezervace)
2. **Lokální SEO** (Kněžmost, Český ráj, okolní města)
3. **Důvěryhodnost** (historie, rodinné hodnoty, recenze)
4. **Mobilní UX** (většina návštěvníků přichází z mobilu)

Při pochybnostech vždy preferuj: jednoduchost, čitelnost, rychlost načítání.