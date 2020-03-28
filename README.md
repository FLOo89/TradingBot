# TradingBot : Trading algorithmique sur cryptomonnaies

## Description

Ce projet consiste en la conception d'un bot qui se connectera à une plateforme de trading où il assurera le pilotage d'un portefeuille de cryptomonnaies, exécutant des ordres d'achat et de vente.

Les cryptomonnaies ont acquis une forte popularité durant les récentes années, en tant qu'instruments financiers novateurs et faciles à utiliser, et beaucoup d'acteurs de la Fintech proposent maintenant des applications, Frameworks, et librairi
es pour les manipuler. Il existe également de nombreuses plateformes où les cryptomonnaies peuvent être échangées, achetées et vendues avec des monnaies traditionnelles.

Le [trading algorithmique](https://en.wikipedia.org/wiki/Algorithmic_trading) a également connu une forte adoption et représente maintenant la majorité des transactions financières conduites sur les marchés internationaux.
Plusieurs outils peuvent être utilisés pour concevoir un bot qui se connecte à une plateforme de change de cryptomonnaie et conduire du trading algorithmique automatisé.
Plusieurs aspects peuvent être abordés séparément ou conjointement :

### Infrastructure
  
D’une part, l’infrastructure qui permettra au bot de mettre en œuvre le trading : Il s’agira d’intégrer 2 composants :

- Un connecteur capable de communiquer avec une plateforme de change pour consulter le cours, son portefeuille et placer des ordres. Le projet [Xchange](https://github.com/knowm/XChange) constitue une référence et supporte de nombreuses plateformes. Ecrit en Java, il peut être facilement porté en .Net/c# grâce à la librairie [IKVM](https://www.ikvm.net).
- Un moteur capable de faire tourner le bot et d’exécuter des stratégies. La librairie [Lean](https://www.quantconnect.com/lean/) et le [repository associé](https://github.com/QuantConnect/Lean) constituent un bon candidat dans plusieurs langages.


### Stratégies

La stratégie de trading à proprement parlé, basée ou non sur l’apprentissage et le deep learning.

- On pourra s’imprégner de connaissances générales, par exemple via ce [subreddit](https://www.reddit.com/r/algotrading/)
- Un certain nombre de stratégies sont fournies en [csharp](https://github.com/QuantConnect/Lean/tree/master/Algorithm.CSharp) ou en [Python](https://github.com/QuantConnect/Lean) avec la librairie Lean comme par exemple [cet exemple](https://github.com/QuantConnect/Lean/blob/master/Algorithm.Python/KerasNeuralNetworkAlgorithm.py) utilisant la
librairie de Deep Learning Keras


## Deep learning

Pour des articles sur le trading à l’aide de réseaux de neurones, on pourra consulter cet article pour une approche simple et péd
agogique, et pour des exemples plus aboutis:

- Cette librairie constitue sans doute la plus complète avec de nombreux modèles
- Ce tutoriel tu ou celui-là pour des approches plus récentes et complexes sous CNTK. Les librairies suivantes ont l’air assez abouties:
- Cette librairie documente un unique modèle assez complexe



