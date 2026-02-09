Exercices - 04_api

1) Auth headers
- Lire un token depuis API_TOKEN et construire les headers.
- Ajouter un header Accept.

2) REST URL
- Parser une URL avec urlparse.
- Afficher schema, domaine, chemin, params.

3) Retry
- Implementer un retry avec backoff exponentiel.
- Simuler une fonction qui echoue 2 fois.

4) Rate limiting
- Implementer un rate limiter simple pour 3 req/s.
- Simuler 6 requetes.

5) Errors
- Creer 2 exceptions: ClientError, ServerError.
- Lever selon un code HTTP donne.

6) Logging
- Configurer un logger et ecrire 3 logs de niveaux differents.

7) Client API
- Ecrire un mini client qui appelle un endpoint GET.
- Ajouter gestion 429 et 5xx (retry simple).

