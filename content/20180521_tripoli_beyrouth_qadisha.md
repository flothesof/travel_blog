Title: Tripoli, Beyrouth, Qadisha, Saïda
Date: 2018-05-21 20:22
Category: Voyage
Tags: Liban
Slug: tripoli-beyrouth-qadisha-saida
Authors: Florian, Elida
Summary: 
gallery: {photo}Liban03

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.3.1/dist/leaflet.css"
integrity="sha512-Rksm5RenBEKSKFjgI3a41vrjkw4EVPlJ3+OiI65vTjIdo9brlAacEuKOiQ5OFh7cOI1bkDwLqdLw3Zg0cRJAAQ=="
crossorigin=""/>
<div id="mapid" style="height: 350px;"></div>

<!-- Make sure you put this AFTER Leaflet's CSS -->
<script src="https://unpkg.com/leaflet@1.3.1/dist/leaflet.js"
integrity="sha512-/Nsx9X4HebavoBvEBuyp3I7od5tA0UzAxs+j83KgC8PU0kgB4XiK4Lfe4y4cgBtaRJQEIFCW+oC506aPT2L1zw=="
crossorigin=""></script>
<script src='https://api.mapbox.com/mapbox.js/plugins/leaflet-omnivore/v0.2.0/leaflet-omnivore.min.js'></script>
<script type="">
	var mymap = new L.Map('mapid', {center: new L.LatLng(15., 2.3522),
									zoom: 2,
									worldCopyJump: true});
	mymap.zoomControl.setPosition('topright');
	layer = L.tileLayer('http://a.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png', {
    	attribution: '© Openstreetmap France | Données &copy; <a href="https://www.openstreetmap.org/copyright">les contributeurs OpenStreetMap</a>'});
	mymap.addLayer(layer);
	var runLayer = omnivore.kml('/maps/Liban_article_3.kml')
    .on('ready', function() {
        mymap.fitBounds(runLayer.getBounds());
        runLayer.eachLayer(function(layer) {
           layer.bindPopup(layer.feature.properties.name);
        });
    })
    .addTo(mymap);
</script>

La semaine dernière, nous avons poursuivi nos excursions depuis Beyrouth. 

La première a été la ville de Tripoli, au nord du Liban. On y trouve le château Saint Gilles, initialement construit par les croisés, en très bon état. Situé au sommet de la colline, il propose une belle vue sur la ville et la côte. Nous y avons également visité un hammam vieux de 800 ans et restauré depuis sa fermeture dans les années 1970. Après avoir traversé le dédale des ruelles du vieux souk, nous avons fini la journée dans une des institutions de la ville : la pâtisserie Hallab où on a pu déguster des douceurs locales...

{% figure responsive-image /images/20180521_tripoli.JPG Vue sur Tripoli depuis le château Saint Gilles. %}

Nous avons profité d'avoir un gîte à Beyrouth pour nous promener durant plusieurs journées dans la ville. Que retenir de la capitale du Liban ? Pour moi, c'est un mélange étonnant de routes serrées et de ruelles, de voitures trop nombreuses, de promenades en bord de mer, d'immeubles abandonnés, d'impacts de balles rebouchés ou non sur les façades, de blocs d'appartement modernes et de villas somptueuses. On peut noter que le centre ville a été reconstruit à neuf après les années de guerre civile (1975 - 1990) et a une allure atypique et très propre de ce fait. Nous avons également profité de l'agréable musée national qui nous a permis de couvrir du regard les millénaires d'histoire du Liban, et du musée de l'American University of Beirut qui est venu compléter cette parenthèse dans le passé. 

{% figure responsive-image /images/20180521_Rausche.JPG Selfie devant l'une des vues touristiques de Beyrouth : le rocher aux pigeons. %}

L'un des moments les plus agréables de cette semaine a été l'excursion dans la "vallée sainte de Qadisha". Cette vallée porte une longue histoire religieuse, ayant été tour à tour refuge de chrétiens persécutés ou d'ermites, avec de nombreuses caves creusées dans la roche ainsi que de nombreux monastères construits au fil des quinze derniers siècles. Nous avons eu la chance de la visiter en présence d'un guide français, "Monsieur Yves", qui nous a plus d'une fois surpris par la profondeur de son érudition et sa connaissance pointue du lieu. Il nous a emmené randonner dans la vallée, jusqu'à Hawqa où vit actuellement un ermite, puis jusqu'au couvent de Qannoubine où vivent encore deux religieuses. La marche est raide mais très belle et impressionnante. On a du mal à imaginer les conditions d'accès à ces sanctuaires il y a plusieurs centaines d'années, sans équipement si aménagements du sentier.

{% figure responsive-image /images/20180521_qadisha.JPG La végétation dans la vallée de Qadisha. %}

 Notre dernière excursion de la semaine nous a amené à Saïda, au sud de Beyrouth. A ce sujet, il est intéressant de noter que l'on se déplace facilement en bus au Liban, mais avec un certain nombre de différences par rapport aux bus que j'ai l'habitude de prendre : absence d'arrêts  officiels (on peut monter à partir du moment où on fait signe au chauffeur, y compris sur la bande d'arrêt d'urgence de l'autoroute), pas d'horaires définis, prix non affichés... A Saïda, nous avons trouvé une petite ville avec un souk typique, une citadelle marine de l'époque des croisés (encore eux !) ainsi qu'un musée du savon plutôt bien fait. Note pour plus tard : visiter une ville à prédominance musulmane le premier jour du Ramadan n'est pas une mince affaire lorsqu'il s'agit de se restaurer ;)

Enfin, nous avons également ajouté à la liste des sanctuaires visités celui de Saint Charbel, l'un des saints libanais les plus connus.

Bon, il commence à faire un peu trop chaud à Beyrouth, on retourne plus en altitude pour nos derniers jours ici :)