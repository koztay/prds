$(document).ready(function(){

    //bootstrap carousel (slider)
    var $item = $('.carousel .item');
    $item.eq(0).addClass('active');

    $('.carousel img.background').each(function() {
      var $src = $(this).attr('src');
      var $color = $(this).attr('data-color');
      $(this).parent().css({
        'background-image' : 'url(' + $src + ')',
        'background-color' : $color
      });
      $(this).remove();
    });

    $("#owl-demo").owlCarousel({
        navigation : false, // Show next and prev buttons
        slideSpeed : 300,
        paginationSpeed : 400,
        singleItem:true
    });

     // Contact Map
    if ($("#map").length > 0)
    {
        var map;

        map = new GMaps({
            el: "#map",
            lat: 45.494447,
            lng: -73.5697587,
            scrollwheel: false,
            zoom: 14,
            zoomControl: true,
            panControl: false,
            streetViewControl: false,
            mapTypeControl: false,
            overviewMapControl: false,
            clickable: false
        });

        var image = "";
        map.addMarker({
            lat: 45.494447,
            lng: -73.5697587,
            icon: "img/marker.png",
            animation: google.maps.Animation.DROP,
            verticalAlign: "bottom",
            horizontalAlign: "center",
            backgroundColor: "#d3cfcf"
        });

        var styles = [
            {
                "featureType": "road",
                "stylers": [
                    {"color": "#ffffff"}
                ]
            }, {
                "featureType": "water",
                "stylers": [
                    {"color": "#f2f2f2"}
                ]
            }, {
                "featureType": "landscape",
                "stylers": [
                    {"color": "#f2f2f2"}
                ]
            }, {
                "elementType": "labels.text.fill",
                "stylers": [
                    {"color": "#2d2d2d"}
                ]
            }, {
                "featureType": "poi",
                "stylers": [
                    {"color": "#f2f2f2"}
                ]
            }, {
                "elementType": "labels.text",
                "stylers": [
                    {"saturation": 1},
                    {"weight": 0.1},
                    {"color": "#b1b1b1"}
                ]
            }

        ];

        map.addStyle({
            styledMapName: "Styled Map",
            styles: styles,
            mapTypeId: "map_style"
        });

        map.setStyle("map_style");
    }

    //Animated conter
    $('.timer').appear(function(){
        var count = $(this);
        $.each($(count), function(i){
            var dataTo = $(this).attr("data-to");
            var dataSpeed = $(this).attr("data-speed");
            var dataRefreshInterval = $(this).attr("data-refresh-interval");
            count.countTo({
                from: 0,
                to: dataTo,
                speed: dataSpeed,
                refreshInterval: dataRefreshInterval,
            });
        });
    });

    //portfolio mixitup
    $('#portfolio').mixItUp();

    //nav scroll
    $('a').on('click', function() {
        var scrollAnchor = $(this).attr('data-scroll'),
            scrollPoint = $('[data-anchor="' + scrollAnchor + '"]').offset().top -1;
        $('body,html').animate({
            scrollTop: scrollPoint
        }, 500);
        return false;
    });

});
