# Costituzione, legislazione e continuità tra governi

## Obiettivo
Per ogni DDL, decreto-legge, decreto legislativo, legge ordinaria, legge costituzionale e altro atto pertinente, ricostruire: origine, iter, versioni, norme precedenti interessate, basi costituzionali e successiva attuazione. Il confronto con la Costituzione **non** genera automaticamente un verdetto di legittimità.

## Tre versioni da confrontare
1. **Testo costituzionale originario**: Costituzione promulgata il 27 dicembre 1947, in vigore dal 1 gennaio 1948. È il riferimento storico e non il parametro giuridico esclusivo per giudicare un atto successivo.
2. **Testo vigente alla data rilevante**: per ogni atto registrare la versione della Costituzione applicabile al momento dell'approvazione, dell'entrata in vigore e, se necessario, del giudizio.
3. **Testo oggi vigente**: utile per capire modifiche e discontinuità, mai sostituto retroattivo del testo dell'epoca.

L'analisi segnala gli articoli potenzialmente pertinenti e gli scostamenti documentati. Solo decisioni giurisdizionali e atti ufficiali permettono di riportare dichiarazioni di illegittimità, abrogazioni e relativi effetti giuridici. Evitare di equiparare una proposta a una legge in vigore.

## Stati distinti per il rapporto costituzionale
- `not_reviewed`: non ancora esaminato;
- `articles_mapped`: possibili articoli interessati, senza giudizio;
- `constitutional_question_raised`: questione sollevata, con riferimenti;
- `court_decision_available`: pronuncia ufficiale disponibile, con dispositivo ed esito testuale;
- `not_applicable`: motivare perché.

**Non** dedurre “costituzionale” dall'assenza di pronunce; non dedurre “incostituzionale” dall'esistenza di una questione pendente. Registrare anche pronunce interpretative, inammissibilità, rigetti, annullamenti parziali e successivi interventi normativi, conservando le espressioni della Corte.

## Eredità legislativa dei governi precedenti
Per ogni atto collegare gli atti antecedenti e successivi con relazioni tipizzate:
- `implements`: attua una norma precedente;
- `amends`: modifica un atto;
- `repeals`: abroga espressamente;
- `converts`: converte un decreto-legge;
- `delegated_by`: è adottato sulla base di delega;
- `extends`: proroga;
- `refinances`: rifinanzia;
- `continues_program`: prosecuzione documentata di un programma;
- `replaces`: sostituzione espressa;
- `cites`: richiamo senza rapporto causale documentato.

Ogni collegamento deve avere fonte, data e, quando opportuno, articolo/comma. Il governo che **propone**, quello sotto cui il Parlamento **approva**, quello che **attua**, e quello che **modifica** possono essere diversi. Non assegnare automaticamente l'atto a uno solo dei governi.

## Algoritmo iniziale
1. Recuperare testo originario, versioni successive e metadati da Normattiva e Gazzetta Ufficiale.
2. Ricostruire iniziativa, firmatari, commissioni, voti e iter da Camera/Senato.
3. Identificare citazioni normative e collegamenti espliciti tra norme; sottoporre i collegamenti non univoci a verifica umana.
4. Mappare gli articoli costituzionali pertinenti nelle tre versioni temporali.
5. Incrociare norme e parametri con i dataset ufficiali della Corte costituzionale.
6. Documentare il passaggio tra governi e attribuire responsabilità per fase.
7. Integrare osservazioni statistiche e valutazioni ex post: non inferire causalità dal solo cambiamento.
8. Conservare versioni, fonti consultate, metodo di estrazione e rettifiche.

## Limiti di copertura
L'obiettivo è la copertura progressiva, non una pretesa di completezza immediata. Normattiva rende ricostruibili le modifiche **esplicite**; le abrogazioni implicite richiedono interpretazione e non devono essere inventate da un parser. Iniziative legislative non approvate richiedono dataset parlamentari e non vanno cercate solo in Normattiva. Gli atti di livello secondario e le leggi regionali necessitano fonti e perimetri dedicati.

## Fonti ufficiali
- Senato, *La storia della nostra Costituzione*: https://www.senato.it/CESUS/2026/Costituzione/
- Camera, testo costituzionale e versioni precedenti: https://leg15.camera.it/cost_reg_funz/345/copertina.asp
- Corte costituzionale, Open Data: https://dati.cortecostituzionale.it/
- Normattiva, multivigenza: https://www.normattiva.it/staticPage/faq
