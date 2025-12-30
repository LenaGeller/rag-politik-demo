Eine RAG-basierte Analyse-App, die politische Fragen zu Regierung, SPD und CDU/CSU ausschließlich anhand offizieller Dokumente beantwortet.

Projektbeschreibung
RAG-basierte Politik-Analyse zu Regierung, SPD und CDU/CSU
Motivation und Zielsetzung

Politische Entscheidungen, Parteiprogramme und Koalitionsverträge sind zwar öffentlich zugänglich, sind jedoch lang, komplex formuliert und über viele Dokumente verteilt. In der öffentlichen Debatte dominieren daher oft verkürzte Darstellungen, Schlagzeilen oder ungeprüfte Behauptungen.

Ziel dieses Projekts war es, ein aufklärendes, niedrigschwelliges Informationssystem zu entwerfen, mit dem Nutzerinnen und Nutzer konkrete Fragen zur Politik der Bundesregierung sowie der Regierungsparteien SPD und CDU/CSU stellen können, ohne selbst umfangreiche Originaldokumente lesen zu müssen – aber dennoch ausschließlich auf Basis dieser offiziellen Texte.

Das System soll ermöglichen, sich eigenständig, quellenbasiert und ohne Meinungslenkung über politische Positionen, Maßnahmen und Spannungen zu informieren.

Projektfokus und Abgrenzung

Im Projekt wurde zuerst eine klare inhaltliche Begrenzung vorgenommen:

Regierung / Koalition

SPD

CDU/CSU

Diese Fokussierung diente dazu, die Architektur, die Dokumentenlogik und die Antwortqualität kontrolliert zu entwickeln und zu testen. Das Projekt ist konzeptionell erweiterbar, wurde aber absichtlich nicht auf alle Parteien oder Fraktionen ausgeweitet, um Qualität vor Vollständigkeit zu priorisieren.

Zentrale Idee: Strukturierte politische Fragen statt Volltextsuche

Der Kern des Projekts ist kein Chatbot im klassischen Sinne, sondern ein strukturierter Analyse-Assistent, der politische Fragen erkennt und entsprechend behandelt.

Das System unterscheidet u. a. zwischen:

Vergleichsfragen (z. B. Unterschiede zwischen Positionen einzelnen Parteien)

Prämissenfragen (z. B. „Ist das gerecht?“)

Maßnahmenfragen

Regierungsfragen

Konflikt- und Spannungsfragen

Je nach Fragetyp wird eine unterschiedliche Antwortlogik angewendet, um Verzerrungen zu vermeiden (z. B. keine Bewertung, wenn der Kontext keine erlaubt).

Technischer Ansatz (auf konzeptioneller Ebene)

Das Projekt basiert auf einer Retrieval-Augmented-Generation-Architektur (RAG):

Nutzung offizieller, frei zugänglicher Dokumente (Parteiprogramme, Koalitionsvertrag, Beschlussbücher, Anträge)

Vektorbasierte Dokumentensuche

Dokumentgewichtung und Re-Ranking nach politischer Relevanz

Strikte Kontextbindung: Antworten dürfen nur auf explizit enthaltenen Informationen beruhen

Keine wörtlichen Zitate, sondern klare Akteurszuordnung

Ein besonderer Fokus lag auf der Trennung unterschiedlicher Dokumenttypen und der Frage, wie politische Prioritäten algorithmisch berücksichtigt werden können.

Ergebnisse und Erkenntnisse

Das Projekt zeigt, dass ein RAG-System nicht nur zur Informationssuche, sondern auch zur politischen Einordnung und Strukturierung eingesetzt werden kann – sofern:

Fragemodi sauber erkannt werden

normative Bewertungen klar von beschreibenden Aussagen getrennt bleiben

Spannungen und Widersprüche nur dann benannt werden, wenn sie im Kontext belegbar sind

Im Vergleich zu generischen politischen Q&A-Systemen liegt die Stärke dieser App insbesondere in:

methodischer Transparenz

klarer Struktur

kontrollierter Verdichtung statt bloßer Zusammenfassung

Erweiterbarkeit

Das System ist bewusst modular angelegt und lässt sich perspektivisch erweitern, z. B. durch:

Einbindung weiterer Parteien und Fraktionen

Ausbau auf Landes- oder EU-Ebene

Follow-up-Fragen für längere Diskussionsverläufe

feinere Dokumentenklassifikation bei größerem Quellenbestand

Fazit

Dieses Projekt versteht sich als Experiment und Machbarkeitsnachweis, wie politische Aufklärung durch strukturierte KI-Systeme unterstützt werden kann – nicht als Ersatz für politische Urteilsbildung, sondern als Werkzeug für informierte Bürgerinnen und Bürger.