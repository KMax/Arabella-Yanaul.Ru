/**
 * User: Maxim Kolchin
 * Date: 22.12.2010
 * Time: 22:46:38
 */

$(document).ready(function() {
    $('#coin-slider').coinslider(
        {
        width: 850,
        height: 300,
        spw: 3,
        sph: 5,
        navigation: true,
        delay: 5000,
        links: false,
        effect: 'rain',
        titleSpeed: 500,
        sDelay: 50,
        opacity: 0.4
        });
});

