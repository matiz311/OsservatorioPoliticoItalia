# Osservatorio Politico Italia

Repository data-driven per ricostruire la storia dei governi della Repubblica italiana, collegare partiti, programmi, proposte, provvedimenti, attuazione e risultati osservabili.

## Obiettivo

Il progetto non assegna un voto complessivo a partiti o governi. Produce invece una scheda verificabile per ogni misura:

1. cosa era stato promesso o proposto;
2. chi ne rivendicava la paternità e con quale ruolo;
3. quale atto è stato approvato;
4. se e quanto è stato attuato;
5. quali risorse pubbliche sono state impiegate;
6. quali indicatori sono cambiati dopo l'intervento;
7. quali gruppi sociali, territori o settori sono stati interessati;
8. quali fattori esterni rendono difficile attribuire causalmente il cambiamento alla misura;
9. quali effetti inattesi o criticità sono documentati;
10. quali fonti sostengono ciascuna affermazione.

L'output finale deve permettere al lettore di distinguere **fatto**, **correlazione**, **valutazione istituzionale** e **inferenza causale**.

## Perimetro

- Periodo: Repubblica italiana, dal 1946 a oggi.
- MVP: 1994-oggi.
- Backfill: 1946-1994.
- Unità principali: governo, partito, misura, atto normativo, promessa, indicatore, fonte, contesto storico.

## Regola fondamentale di attribuzione

Una misura non viene automaticamente attribuita in egual misura a tutti i partiti che sostengono un governo. Si registrano separatamente:

- iniziativa governativa/parlamentare;
- ministro o ministero competente;
- proponenti e firmatari;
- posizione dei gruppi nelle votazioni, quando disponibile;
- appartenenza partitica nel periodo considerato;
- sostegno esterno o partecipazione diretta al governo;
- livello di evidenza disponibile sull'attribuzione politica.

## Struttura

```text
data/
  examples/          esempi compilati
  reference/         tassonomie e contesti storici
  sources/           catalogo delle fonti
schemas/             JSON Schema dei record
docs/                metodologia e policy editoriali
src/opitalia/         validazione e tooling
.github/workflows/    CI per validare i dati
```

## Fonti prioritarie

Le fonti istituzionali hanno priorità per fatti normativi, parlamentari, statistici e di finanza pubblica. Analisi accademiche e valutazioni indipendenti possono essere aggiunte per la causalità e gli effetti di medio-lungo periodo.

Vedi `docs/FONTI.md`.

## Avvio rapido

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -e .
python -m opitalia.validate
pytest
```

## Cosa NON fa il progetto

- Non converte automaticamente crescita del PIL, occupazione o altri indicatori in un giudizio politico complessivo.
- Non tratta il semplice “prima/dopo” come prova causale.
- Non usa dichiarazioni di partito come fonte sufficiente dell'effetto di una politica.
- Non attribuisce a un singolo governo fenomeni iniziati prima o determinati principalmente da shock esterni.
- Non nasconde dati contrari alla tesi iniziale del ricercatore.

## Roadmap

1. Anagrafe governi, partiti e coalizioni.
2. Import degli atti e degli iter parlamentari.
3. Collegamento programmi/promesse -> misure -> norme.
4. Stato di attuazione e decreti attuativi.
5. Serie storiche degli indicatori.
6. Contesti storici e shock esterni.
7. Schede web generate automaticamente.
8. Backfill 1946-1994.

## Comparazione costituzionale ed eredità normativa

Il progetto confronta ogni iniziativa e atto, quando le fonti lo consentono, con **tre riferimenti distinti**: testo originario della Costituzione (1948), testo applicabile alla data dell'atto e testo oggi vigente. Registra gli articoli pertinenti e le pronunce ufficiali della Corte, senza generare verdetti automatici di costituzionalità.

È inoltre prevista una **catena normativa tra governi**, che collega proposte, approvazione, attuazione, modifiche, rifinanziamenti e abrogazioni: chi eredita una misura non coincide necessariamente con chi l'ha ideata.

Vedi [Costituzione e continuità](docs/COSTITUZIONE_E_CONTINUITA.md) e lo schema [legal_lineage](schemas/legal_lineage.schema.json).

## Interfaccia web

L'interfaccia di esplorazione è in `site/` ed è progettata per GitHub Pages:

**https://matiz311.github.io/OsservatorioPoliticoItalia/**

Il workflow `.github/workflows/pages.yml` genera il catalogo JSON dai record YAML usando `scripts/build_site.py` e pubblica il sito. I file `data/examples/` sono intenzionalmente esclusi dalle statistiche: non vanno presentati come dati storici verificati.

Se Pages non è ancora abilitato, aprire **Settings → Pages → Build and deployment → Source: GitHub Actions**. La pubblicazione effettiva dipende dall'esito del workflow GitHub.

## Prima legislatura importata

Inserita una prima selezione verificata di **15 atti normativi**, **tre governi della I legislatura** (più il IV come antecedente in carica all'avvio), partiti, dati istituzionali ed elettorali e sei contesti storici. La selezione non è l'elenco completo delle norme del periodo. Vedi [dossier 1948–1953](docs/LEGISLATURA_I_1948_1953.md).
