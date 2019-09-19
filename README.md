# FinancialSentiments

Le domaine de l'analyse de sentiments dans les textes a pris beaucoup d'intérêt ces dernières années grâce au succès et aux bonnes performances des classificateurs. Les chercheurs et développeurs ont commencé par l'analyse de sentiments dans des domaines classiques tels que les commentaires sur les films, les produits de commerce, les hôtels, restaurants, etc. Aujourd'hui, nous témoignons un intérêt plus focalisé sur des domaines plus difficiles tels que les débats politiques et la finance et l'économie politique.

Dans ce projet, il s'agit de faire un tour sur les technologies récentes de machine learning utilisées pour résoudre cette problématique, et de les appliquer dans le domaine du marché financier du FOREX dans le but de suivre la tendance haussière et baissière dans les pairs de devises (par exemple USD/CHF et EUR/USD).

Un corpus (ensemble de texte) copieux extrait depuis Reuters et Bloomberg sera mise à disposition pour l'entrainement. Les Tweet de D. Trump ainsi que les rapports de la FED des Etats-Unis seront mise en analyse durant ce projet.

L'objectif ultime est de développer un classificateur "maison" qui permettrai de collecter et préparer les sources textuelles (posts et articles publiés sur Reuters, Bloomberg, Twitter (seulement D. Trump) et quelques canaux financiers spécialisés) puis d'en générer un sentiment (entre 0 et 1) d'une période de trading (une heure, une demi journée, journée, semaine, ...) et relatif à un sujet (par exemple Brexit, échanges commerciaux avec la Chine, ....)

Ce classificateur, avec d'autres en cours de développement, sera intégré dans un outil de prédiction du taux change.