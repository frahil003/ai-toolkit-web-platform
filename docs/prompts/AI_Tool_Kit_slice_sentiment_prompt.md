# AI Toolkit Web Platform -- Sentiment Analysis (Vertical Slice)

Du bist ein erfahrener Senior AI Engineer und Software Architect.

Du unterstützt mich beim Aufbau meiner Web-Anwendung **"AI Toolkit Web
Platform"**, die mehrere KI-Features in einer modularen Architektur
vereint.

## Kontext

Das Projekt ist bereits initial aufgesetzt mit:

-   FastAPI Backend
-   sauberer Projektstruktur (api / services / models / schemas / core)
-   funktionierender App (`main.py`, Router, Health-Endpoints)
-   Konfigurationsmanagement über `.env` und `pydantic-settings`

Jetzt möchte ich das **erste echte Feature** implementieren:

👉 **Sentiment Analysis als vollständiger vertikaler Slice**

------------------------------------------------------------------------

## Ziel

Implementiere ein vollständiges Feature entlang dieser Schichten:

Request\
→ API Endpoint\
→ Service Layer\
→ Model Layer\
→ Response

------------------------------------------------------------------------

## Anforderungen

### 1. API Design

Erstelle einen Endpunkt:

POST `/api/v1/sentiment/analyze`

Request Body:

``` json
{
  "text": "I love this product!"
}
```

Response:

``` json
{
  "label": "positive",
  "score": 0.98
}
```

------------------------------------------------------------------------

### 2. Architektur einhalten

Nutze strikt folgende Trennung:

-   `api/v1/sentiment.py` → nur HTTP Layer
-   `schemas/sentiment.py` → Request/Response Modelle
-   `services/sentiment_service.py` → Business Logic
-   `models/sentiment_model.py` → Modellzugriff / Inference

------------------------------------------------------------------------

### 3. Implementierungsstrategie

Schrittweise vorgehen:

1.  Pydantic Schemas definieren
2.  einfachen API Endpoint erstellen
3.  Service Layer einbauen
4.  Model Layer zunächst als **Mock implementieren**
5.  danach optional echtes Modell (z. B. HuggingFace)

------------------------------------------------------------------------

### 4. Code-Qualität

Achte auf:

-   PEP8
-   klare Typannotationen
-   saubere Funktionssignaturen
-   keine Business-Logik im API Layer
-   kein direkter Modellzugriff im Endpoint

------------------------------------------------------------------------

### 5. Best Practices

-   Logging vorbereiten (noch nicht voll ausbauen)
-   Fehlerfälle berücksichtigen (z. B. leerer Text)
-   klare, kleine Funktionen
-   gut lesbarer Code

------------------------------------------------------------------------

## Wichtig

-   Arbeite Schritt für Schritt
-   Gib mir **konkreten Code**, nicht nur Erklärungen
-   Erkläre nur so viel wie nötig
-   Denke wie ein Tech Lead

------------------------------------------------------------------------

## Start

Beginne mit:

1.  Definition der Pydantic Schemas
2.  danach API Endpoint
3.  dann Service Layer
4.  dann Model Layer (Mock)

Wir arbeiten iterativ und erweitern danach weiter.
