# Metodologia

## 1. Separare quattro domande diverse

Per ogni misura il progetto risponde separatamente a:

1. **Promessa/proposta** — che cosa era stato dichiarato prima dell'approvazione?
2. **Produzione normativa** — che cosa è stato effettivamente approvato?
3. **Attuazione** — la norma è diventata operativa, con quali decreti, risorse e tempi?
4. **Risultati** — che cosa è cambiato negli indicatori rilevanti e quanto è credibile un nesso causale?

Confondere questi quattro piani produce valutazioni scorrette.

## 2. Nessun punteggio unico

Il repository non produce un voto generale per partito o governo. Un indicatore economico può migliorare mentre peggiorano distribuzione, finanza pubblica o accesso a un servizio. Aggregare tutto in un numero richiederebbe pesi politici o morali non oggettivi.

La UI può invece mostrare una matrice di effetti con valori, intervalli, popolazioni interessate e fonti.

## 3. Stato di una misura

Valori ammessi:

- `announced`
- `proposed`
- `parliamentary_process`
- `approved`
- `partially_implemented`
- `implemented`
- `repealed`
- `expired`
- `blocked`

Lo stato deve essere accompagnato dalla data e dalla fonte.

## 4. Attribuzione politica

Ogni record può contenere più attori, ciascuno con un ruolo:

- `government_collective`
- `prime_minister`
- `minister`
- `party_proponent`
- `parliamentary_group`
- `first_signatory`
- `coalition_partner`
- `external_support`

L'attribuzione è accompagnata da `evidence_basis`, non da un punteggio di merito.

## 5. Effetti e causalità

Ogni indicatore deve riportare almeno:

- periodo di baseline;
- periodo osservato;
- valore iniziale e finale;
- unità di misura;
- popolazione interessata;
- eventuale target esplicito;
- fonte;
- disegno di valutazione.

`evaluation_design` può assumere:

- `descriptive_before_after`
- `official_ex_post_evaluation`
- `difference_in_differences`
- `synthetic_control`
- `regression_discontinuity`
- `instrumental_variables`
- `randomized_evaluation`
- `structural_model`
- `systematic_review`
- `other`

Un semplice prima/dopo va descritto come correlazione temporale, non come effetto causale.

## 6. Benefici e costi distribuiti

Gli effetti devono essere disaggregati quando le fonti lo consentono:

- famiglie per fascia di reddito;
- età;
- area geografica;
- lavoratori/occupati/disoccupati;
- imprese per dimensione o settore;
- contribuenti;
- utenti di servizi pubblici;
- finanza pubblica corrente e futura.

Non è corretto scrivere “vantaggio per gli italiani” quando una misura produce vincitori e perdenti identificabili.

## 7. Contesto storico

Gli shock esterni sono record di prima classe e possono essere collegati a più governi. Esempi: crisi economiche internazionali, shock petroliferi, pandemie, guerre, transizioni monetarie, vincoli europei, calamità, mutamenti demografici.

La percezione pubblica non viene inferita dagli indicatori economici. Quando rilevante, deve essere documentata con sondaggi, risultati elettorali, studi storici o serie di fiducia disponibili per il periodo.

## 8. Contraddittorio delle fonti

Per le questioni controverse, il record deve poter contenere:

- valutazioni istituzionali;
- studi accademici;
- analisi indipendenti;
- contestazioni metodologiche.

Il progetto conserva risultati discordanti invece di forzarli in una singola conclusione.

## 9. Regola editoriale

Ogni frase fattuale destinata alla scheda finale deve essere riconducibile a una fonte identificabile. Le inferenze devono essere etichettate come tali.
