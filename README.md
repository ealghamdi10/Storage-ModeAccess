# Stockage mode d’accès
## Objectif 1  
le but de ce TP est d’appréhender différents modes d’accès de stockage de données. Cela 
va de la mémoire RAM, au cloud en passant par le système de fichier. Chacun des différents types de 
stockage proposant des caractéristiques et contraintes différentes en termes de latence, bande 
passante, robustesse, sécurité et coût. 
Afin de mieux comparer les performances, vous allez écrire un programme python qui pour chacun 
des cas (RAM, système de fichiers, et stockage cloud) récupère des données depuis une source et les 
écrit dans l’espace de stockage. Vous mettrez en place une métrique pour mesurer le temps 
d’écriture. 
Vous ferez de même pour la lecture des données, vous récupérerez les données depuis l’espace de 
stockage et le stockerez dans tableau de bytes. Vous mettrez en place une métrique pour mesurer le 
temps d’écriture. 
Pour vérifier que les données ont bien été stockées, puis récupérer vous pouvez manipuler des 
données d’images que vous afficherez pour valider la non-corruption.   
## Objectif 2  
Le but est de comprendre comment optimiser son système de stockage 
Plus le stockage est rapide plus il est cher … de ce constat est né 2 idées : 
Le cache : toutes les données sont stockées sur un stockage maitre (lent), quand elles sont lues, elles 
sont répliquées sur un stockage plus rapide (appelé cache). La politique de remplacement des 
données du cache peut être défini par l’administrateur du système. En général, il y a 2 grandes 
méthodes : 
Least Recently Used (LRU) : les données les plus anciennement utilisées depuis le cache sont 
supprimées en premier du cache 
Least Frequently Used (LFU) : les données les moins fréquemment utilisées sont supprimées en 
premier 
Le tiering : de façon statique, l’administrateur décide où place quelle donnée. En général les données 
les plus utilisées sont stockées sur du stockage rapide, et les moins utilisées sur le stockage plus lent. 
Des mécanismes de migration automatique de données entre les différents espaces de stockage 
peuvent être mis en place. On parle alors d’auto-tiering. Tout comme pour le cache, ces mécanismes 
de migration peuvent être basés la dernière date d’utilisation de la donnée ou la fréquence 
d’utilisation.  
## pré-requis   
installer la librairie boto 
```
pip3 install boto
```
installer la librairie PIL  
```
pip3 install pillow
```
installer la librairie memcache  
```
pip3 install python-memcached
```
Service AWS S3  
- **Credentials**  
## les étapes :
- [systemfile.py](https://github.com/ealghamdi10/Storage-AccessMode/blob/master/systemfile.py)  
- [memcache.py](https://github.com/ealghamdi10/Storage-AccessMode/blob/master/memcache.py)  
- [awss3.py](https://github.com/ealghamdi10/Storage-AccessMode/blob/master/awss3.py)  
- [replication.py](https://github.com/ealghamdi10/Storage-AccessMode/blob/master/replication.py)  
- [tiering.py](https://github.com/ealghamdi10/Storage-AccessMode/blob/master/tiering.py)  
- [cache2level.py](https://github.com/ealghamdi10/Storage-AccessMode/blob/master/cache2level.py)  
### Ce fichier python exécutera tous les scripts :  
- [full.py](https://github.com/ealghamdi10/Storage-AccessMode/blob/master/full.py)