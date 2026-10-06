# PROMPT PRO CLAUDE CODE — Rozšíření a úprava webu u-cerhu.cz podle SEO plánu

> Tento dokument slouží jako kompletní zadání pro Claude Code. Vychází z dokumentu
> „u-cerhu.cz — Kompletní Keyword Cluster, URL architektura a Link-Building systém"
> (30. 8. 2026), navazujícího na SEO audit ze stejného data. Cílem je do existujícího
> statického webu (HTML/CSS/JS) doplnit nové stránky, upravit URL strukturu a zajistit
> interní prolinkování podle pillar–cluster modelu — **bez zásahu do link-buildingu**
> (ten se řeší mimo web, viz kap. 6 zdrojového dokumentu, a není součástí tohoto promptu).

---

## 0. Než začneš — průzkum existujícího webu

Web u-cerhu.cz už existuje a běží na statickém HTML/CSS/JS. **Nikdy nezačínej psát nové
stránky, dokud nezmapuješ, jak je postavený stávající web.** Konkrétně:

1. Projdi adresářovou strukturu repozitáře a zjisti, jak jsou organizované existující
   stránky (ploché soubory `nazev.html` vs. složky s `index.html`, např. `/svatby/index.html`).
2. Najdi a popiš si sdílené komponenty: hlavičku/navigaci, patičku, případné
   includes/partials nebo build systém (statický generátor? čisté HTML s kopírovaným
   kódem?).
3. Zjisti, jak web řeší CSS (jeden globální soubor? SCSS? utility třídy?) a jak
   pojmenovává třídy a sekce — nové stránky musí vizuálně a strukturně sedět k
   stávajícím, ne vypadat jako cizí vložený blok.
4. Najdi existující `sitemap.xml` a `robots.txt` — nové URL do nich bude potřeba doplnit
   (viz kap. 6 tohoto promptu).
5. Zkontroluj, jestli již existuje stránka `/svatby/` (nebo její ekvivalent, např.
   `svatby.html`). Pokud ano, jde o **úpravu obsahu existující stránky** (přidat
   klíčová slova z kap. 1, ne založit duplicitní stránku). Pokud stránka jako pilíř
   ještě neexistuje, založ ji nově podle specifikace v kap. 2.
6. Zjisti aktuální URL patterns (trailing slash, `.html` přípona, česká diakritika v
   URL ano/ne) a **striktně se jich drž** i u nových stránek, aby architektura byla
   konzistentní.

Pokud cokoliv z výše uvedeného není z repozitáře jednoznačné, **zeptej se uživatele**
dřív, než začneš generovat soubory — chybná struktura URL by musela vyvolat později
redirecty a zbytečně komplikovat SEO.

---

## 1. Princip, který nesmí být porušen: kanibalizace klíčových slov

Fráze **svatby**, **svatby Český ráj**, **svatební statek**, **svatební místo**,
**prostory na svatbu** cílí VŠECHNY na jednu jedinou stránku `/svatby/` (pilíř). Nikdy
nevytvářej pro tyto fráze samostatné podstránky ani duplicitní obsah — musí se
přirozeně objevit v title, H1, H2 a textu pilíře, ne se rozmělnit do víc URL.

Naproti tomu lokalita (Mladá Boleslav, Liberec), produkt (catering) a informační dotazy
(jak naplánovat svatbu, kolik stojí svatba) mají jasně odlišný vyhledávací záměr → **ty
dostávají vlastní URL** jako cluster stránky, které se zpětně odkazují na pilíř.

---

## 2. Cílová URL architektura

```
u-cerhu.cz/
├── /svatby/                                        ← PILÍŘ
│   ├── /svatby/svatby-mlada-boleslav/              ← lokální cluster
│   ├── /svatby/svatby-liberec/                     ← lokální cluster
│   └── /svatby/svatebni-catering/                  ← produktový cluster
├── /ubytovani/                                     ← PILÍŘ (už navržen v auditu)
├── /oslavy-a-vyroci/                               ← nová služba
├── /pribeh/                                        ← beze změny
├── /galerie/                                       ← beze změny
├── /okoli-cesky-raj/                               ← PILÍŘ (turistika)
│   └── /okoli-cesky-raj/zricenina-hradu-valecov/   ← cluster podstránka
├── /magazin/                                       ← nový blogový hub (rozcestník)
│   ├── /magazin/jak-naplanovat-svatbu-na-statku/
│   ├── /magazin/kolik-stoji-svatba-cesky-raj/
│   └── /magazin/svatebni-fotograf-cesky-raj/
└── /kontakt/                                       ← beze změny
```

**Úkol:** vytvoř tuto strukturu jako novou (chybějící) nebo uprav existující stránky tak,
aby odpovídaly. Pokud některá z cílových URL koliduje s jinou stávající URL na webu,
zastav se a nahlas to uživateli — needeš vytvořit duplicitu.

---

## 3. Specifikace jednotlivých stránek

Pro každou stránku níže platí: **použij přesně dodaný title, H1 a meta description**
(neuprav je stylisticky, jsou navržené na míru délce a klíčovým slovům). Obsahovou
osnovu rozpracuj do plnohodnotného textu v tónu a slovníku, který odpovídá stávajícímu
obsahu webu (nekopíruj cizí formulace, ale drž se stejné úrovně formálnosti/vřelosti
jako zbytek webu). Nikde nevymýšlej konkrétní fakta (ceny, kapacity, počty realizací),
která nejsou podložená obsahem webu nebo tímto zadáním — pokud chybí, vlož zřetelně
označený placeholder `[DOPLNIT: ...]` a uveď to v závěrečném shrnutí.

### 3.1 `/svatby/` (úprava existující pilířové stránky, ne nová stránka)

- **Title:** `Svatba na statku v Českém ráji | U Cerhů`
- **H1:** `Svatební statek U Cerhů — svatby v srdci Českého ráje`
- **Meta description:** `Exkluzivní svatební místo v Kněžmostě. Jedna svatba na víkend, celý statek jen pro vás. Prostory pro obřad, hostinu i ubytování hostů.`
- **Povinná klíčová slova v textu (přirozeně, ne mechanicky):** svatby, svatby Český
  ráj, svatební statek, svatební místo, prostory na svatbu.
- **Interní odkazy, které stránka MUSÍ obsahovat** (viz kap. 5):
  - odkaz na `/svatby/svatby-mlada-boleslav/` a `/svatby/svatby-liberec/` s
    konverzačním textem typu „Svatbu plánujete z Mladé Boleslavi? Podívejte se, jak
    snadno se k nám dostanete →"
  - odkaz na `/svatby/svatebni-catering/`
  - odkaz na `/ubytovani/`

### 3.2 `/svatby/svatby-mlada-boleslav/` (nová stránka)

- **Title:** `Svatby Mladá Boleslav — statek 20 min od města | U Cerhů`
- **H1:** `Svatba nedaleko Mladé Boleslavi — statek U Cerhů`
- **Meta description:** `Hledáte svatební místo poblíž Mladé Boleslavi? Historický statek U Cerhů je vzdálen jen cca 20 minut a nabízí exkluzivitu i ubytování.`
- **Osnova obsahu:**
  1. Úvod — proč je statek dobrá volba pro páry z Mladé Boleslavi (vzdálenost,
     dostupnost)
  2. Co statek nabízí (stručné shrnutí, ne duplicita celého pilíře — 1 odstavec)
  3. Doprava/vzdálenost od Mladé Boleslavi (orientační čas, případně trasa)
  4. CTA + textový odkaz zpět na `/svatby/` s anchor textem typu „prohlédněte si celý
     svatební areál"

### 3.3 `/svatby/svatby-liberec/` (nová stránka)

- **Title:** `Svatby Liberec — svatební statek 35 min od města | U Cerhů`
- **H1:** `Svatba pro páry z Liberce na statku U Cerhů`
- **Meta description:** `Svatební statek U Cerhů leží cca 35 minut od Liberce, v srdci Českého ráje. Klidné místo, exkluzivita a ubytování pro hosty.`
- **Osnova obsahu:** stejná struktura jako 3.2, přizpůsobená Liberci (vzdálenost cca 35
  min).

### 3.4 `/svatby/svatebni-catering/` (nová stránka)

- **Title:** `Svatební catering a menu | U Cerhů, Český ráj`
- **H1:** `Svatební catering přímo v areálu statku`
- **Meta description:** `Profesionální kuchyně na statku, top kuchaři a partnerské cateringy, které areál dobře znají. Ukázky svatebních menu a catering na míru vaší hostině.`
- **Osnova obsahu:**
  1. Úvod — catering přímo v areálu, profesionální kuchyně
  2. Top kuchaři a partnerské cateringy (Luciz Catering, Familia Catering, Pavel Vedral
     a další) — degustace se nenabízí, klient potvrdil 09/2026, neuvádět
  3. Ukázky svatebních menu — 2–3 kompletní příklady (předkrm/hlavní chod/dezert, raut
     varianta) — `[DOPLNIT: konkrétní chody]`, pokud nejsou v podkladech
  4. Speciální diety (bezlepkové, veganské)
  5. CTA → poptávkový formulář / odkaz zpět na `/svatby/`
- **Důležité:** catering zajišťují doporučení partneři (potvrzeno klientem 09/2026) a
  stránka to transparentně uvádí. Odkazy na weby partnerů zatím nejsou — navázání
  spolupráce/backlinku je mimo scope tohoto promptu, viz kap. 6 zdrojového dokumentu.

### 3.5 `/oslavy-a-vyroci/` (nová stránka, nová služba)

- **Title:** `Oslavy výročí a rodinné oslavy | U Cerhů`
- **H1:** `Oslavte výročí nebo rodinnou událost na statku U Cerhů`
- **Meta description:** `Statek U Cerhů není jen pro svatby — pronajměte si celý areál i na oslavu výročí, kulatiny nebo rodinné setkání v Českém ráji.`
- **Osnova obsahu:**
  1. Úvod — areál není jen pro svatby
  2. Typy oslav (výročí svatby, kulatiny, rodinné sjezdy)
  3. Kapacita a možnosti ubytování hostů (odkaz na `/ubytovani/`)
  4. Fotky z realizovaných akcí — `[DOPLNIT: fotky, pokud existují]`
  5. CTA → `/kontakt/`

### 3.6 `/magazin/` (nový blogový hub/rozcestník)

- Rozcestníková stránka se seznamem (kartami) 3 článků níže. Nemá vlastní zadanou
  title/H1/meta v podkladech — navrhni je konzistentně s ostatními (formát:
  `Magazín | U Cerhů`, H1 `Magazín U Cerhů — rady a tipy ke svatbě v Českém ráji`),
  a **uveď to uživateli ke schválení**, protože nejde o hodnotu ze zdrojového dokumentu.

### 3.7 `/magazin/jak-naplanovat-svatbu-na-statku/` (nová stránka)

- **Title:** `Jak naplánovat svatbu na statku — průvodce | U Cerhů`
- **H1:** `Jak naplánovat svatbu na statku krok za krokem`
- **Meta description:** `Praktický průvodce plánováním svatby na venkovském statku — od výběru termínu přes catering až po ubytování hostů.`
- **Osnova obsahu:**
  1. Časová osa přípravy (12, 6, 3, 1 měsíc před svatbou)
  2. Výběr místa — na co se ptát majitele areálu
  3. Catering, výzdoba, ubytování hostů — checklist
  4. Odkaz na konkrétní nabídku U Cerhů jako příklad „ready-to-use" řešení (odkaz na
     `/svatby/`)

### 3.8 `/magazin/kolik-stoji-svatba-cesky-raj/` (nová stránka)

- **Title:** `Kolik stojí svatba v Českém ráji? | U Cerhů`
- **H1:** `Kolik stojí svatba v Českém ráji — reálné ceny`
- **Meta description:** `Přehled orientačních nákladů na svatbu v Českém ráji — pronájem místa, catering, ubytování hostů a další položky rozpočtu.`
- **Osnova obsahu:**
  1. Hlavní položky rozpočtu (pronájem místa, catering, foto, výzdoba, hudba)
  2. Orientační rozmezí cen v regionu Český ráj — **obecně za region, ne jen U Cerhů**
     — `[DOPLNIT: reálná čísla nebo rozmezí od klienta/z trhu]`
  3. Jak exkluzivní pronájem celého areálu (žádné sdílení víkendu) ovlivňuje rozpočet
  4. Odkaz na ceník U Cerhů jako konkrétní referenci — **cena 45 000–75 000 Kč** (uveď
     přesně tuto hodnotu, je dána zdrojovým dokumentem; pokud se liší od aktuálního
     ceníku na webu, uprav podle webu a uprav i tuto poznámku)

### 3.9 `/magazin/svatebni-fotograf-cesky-raj/` (nová stránka)

- **Title:** `Svatební fotograf v Českém ráji — tipy a doporučení`
- **H1:** `Jak vybrat svatebního fotografa v Českém ráji`
- **Meta description:** `Na co si dát pozor při výběru svatebního fotografa a tipy na fotografy, kteří znají prostředí Českého ráje i statek U Cerhů.`
- **Osnova obsahu:**
  1. Na co se zaměřit při výběru fotografa (styl, zkušenost s venkovními obřady)
  2. Nejfotogeničtější místa přímo v areálu a okolí — prolinkuj na
     `/okoli-cesky-raj/zricenina-hradu-valecov/`
  3. Seznam/doporučení fotografů, kteří na statku už fotili — `[DOPLNIT: konkrétní
     jména/weby fotografů od klienta]`. Bez potvrzených jmen nevymýšlej fotografy ani
     jejich reference.

### 3.10 `/okoli-cesky-raj/zricenina-hradu-valecov/` (nová podstránka)

- **Title:** `Zřícenina hradu Valečov — 3 km od statku U Cerhů`
- **H1:** `Zřícenina hradu Valečov — výlet od statku U Cerhů`
- **Meta description:** `Největší skalní hrad v ČR jen 3 km od statku U Cerhů. Tip na výlet nebo net svatební fotografii pro novomanžele.`
  *(Pozn.: v podkladu je „net svatební fotografii" — pravděpodobně překlep, ověř s
  uživatelem, zda nemá být „tip na svatební fotografii"; než se potvrdí, ponech
  formulaci beze změny.)*
- **Osnova obsahu:**
  1. Základní info o hradu (vzdálenost 3 km, historie, „největší skalní hrad v ČR")
  2. Tip na výlet pro svatební hosty / novomanžele na svatební cestu
  3. Fotografická lokace pro svatební fotografy — prolinkuj na
     `/magazin/svatebni-fotograf-cesky-raj/`
- Tato stránka spadá pod pilíř `/okoli-cesky-raj/` — pokud tento pilíř ještě
  neexistuje, uprav nebo zjisti, jestli existuje ekvivalentní sekce „Okolí" na webu a
  vytvoř podle ní vnoření.

---

## 4. Pravidla interního prolinkování (povinná, kontroluj u každé stránky)

1. Každá cluster stránka (lokální varianty, catering, magazín) **musí** obsahovat
   minimálně jeden textový odkaz zpět na svůj pilíř (`/svatby/`) s přirozeným anchor
   textem — ne generické „klikněte zde".
2. Pilíř `/svatby/` **musí** odkazovat na všechny své clustery (viz 3.1).
3. Magazínové články **musí** křížově odkazovat na `/svatby/` i
   `/svatby/svatebni-catering/`, protože jsou přirozeným „dalším krokem" pro čtenáře.
4. `/magazin/svatebni-fotograf-cesky-raj/` a `/okoli-cesky-raj/zricenina-hradu-valecov/`
   se musí odkazovat navzájem.
5. Po dokončení všech stránek projdi kompletní prolinkování a ověř, že žádná nová
   stránka není „osiřelá" (bez příchozího interního odkazu ze žádné jiné stránky) —
   to by SEO hodnotu clusteru oslabilo.

---

## 5. Technické požadavky

- **Konzistence designu:** nové stránky musí použít existující header/nav, footer,
  typografii, barvy a grid/layout patterns webu. Neimportuj nové CSS frameworky ani
  neměň vizuální styl.
- **Responzivita:** nové stránky musí fungovat stejně dobře na mobilu jako stávající
  stránky webu — ověř na stejných breakpointech, jaké web už používá.
- **Sémantické HTML:** jedno `<h1>` na stránku (přesně podle zadání výše), logická
  hierarchie `<h2>`/`<h3>` pro podsekce z obsahových osnov.
- **Meta tagy:** doplň `<title>` a `<meta name="description">` přesně podle zadání.
  Pokud web používá i Open Graph tagy (`og:title`, `og:description`, `og:image`) na
  ostatních stránkách, dodrž stejný vzor i zde.
- **`sitemap.xml`:** přidej všechny nové URL.
- **`robots.txt`:** zkontroluj, že nic z nového obsahu není nechtěně blokované.
- **Redirecty:** pokud se v rámci úpravy `/svatby/` mění jakákoliv stávající URL
  (např. přesun obsahu, změna cesty), nastav 301 redirect ze staré URL na novou —
  needeš ztratit stávající SEO hodnotu.
- **Breadcrumbs / navigace:** pokud web má navigační menu, zvaž, kde se nové sekce
  (`/oslavy-a-vyroci/`, `/magazin/`) objeví v hlavní navigaci — nezůstat jen jako
  „osiřelé" podstránky bez cesty z menu.

---

## 6. Fázový postup (podle harmonogramu ze zdrojového dokumentu)

Implementuj v tomto pořadí, po fázích, a po každé fázi krátce shrň, co bylo hotovo:

1. **Fáze 1** — uprav pilíře `/svatby/` a `/ubytovani/` (zapracuj klíčová slova do
   H1/H2/textu, `/ubytovani/` uprav jen pokud je v repozitáři jako placeholder/needit; pokud
   je hotová dle staršího auditu, jen ověř soulad s tímto zadáním).
2. **Fáze 2** — přidej cluster stránky: `/svatby/svatby-mlada-boleslav/`,
   `/svatby/svatby-liberec/`, `/svatby/svatebni-catering/`.
3. **Fáze 3** — spusť `/oslavy-a-vyroci/` jako novou nabídku.
4. **Fáze 4** — rozjeď `/magazin/` se 3 úvodními články.
5. **Fáze 5** — doplň `/okoli-cesky-raj/zricenina-hradu-valecov/` a propoj s článkem o
   fotografech.
6. **Fáze 6** — projdi celé prolinkování podle kap. 4, aktualizuj `sitemap.xml`.

*(Link-building z kap. 6 zdrojového dokumentu je mimo tuto implementaci — týká se
externích webů, ne kódu tohoto repozitáře.)*

---

## 7. Kontrolní seznam před dokončením (projdi před nahlášením hotovo)

- [ ] Žádná nová URL neduplikuje záměr jiné (zkontrolováno proti kap. 1 — kanibalizace)
- [ ] Každá cluster stránka má odkaz na svůj pilíř a naopak
- [ ] Title/meta description jsou unikátní pro každou URL a odpovídají zadání v kap. 3
- [ ] Přesně jeden `<h1>` na stránku, odpovídá zadání
- [ ] Interní odkazy používají popisný anchor text (ne „klikněte zde")
- [ ] Nové stránky přidané do `sitemap.xml`
- [ ] Nové stránky vizuálně a strukturně sedí ke stávajícímu designu webu
- [ ] Responzivita ověřena
- [ ] Všechna místa označená `[DOPLNIT: ...]` jsou sepsaná v závěrečném souhrnu pro
      klienta — žádné vymyšlené fakty nezůstaly v textu bez označení
- [ ] Pokud se měnila jakákoliv stávající URL, jsou nastavené 301 redirecty

---

## 8. Co NENÍ součástí tohoto promptu

- Samotný link-building (oslovování portálů, blogů, fotografů — kap. 6 zdrojového
  dokumentu) — to je manuální/obchodní aktivita mimo repozitář.
- Zadávání do Collabimu / sledování pozic (kap. 7, bod 7 zdrojového dokumentu).
- Odeslání sitemap do Google Search Console (technicky mimo repozitář, ale
  připomeň to uživateli po dokončení implementace).