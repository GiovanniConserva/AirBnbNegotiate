$(document).ready(function () {

    $('.navbar-toggle').click(function () {
        $('.menu-btn').toggleClass("white");
    });

    // Search bar

    $('[data-toggle="tooltip"]').tooltip();

    $('.check-in').datetimepicker({
        format: 'll',
        //minDate: moment()
    });
    $('.check-out').datetimepicker({
        format: 'll',
        useCurrent: false //Important! See issue #1075
    });
    $(".check-in").on("dp.show", function (e) {
        $(this).data("DateTimePicker").minDate(moment());
    });
    $(".check-out").on("dp.show", function (e) {
        $(this).data("DateTimePicker").minDate(moment());
    });
    $(".check-in").on("dp.change", function (e) {
        $('.check-out').data("DateTimePicker").minDate(e.date);
    });
    $(".check-out").on("dp.change", function (e) {
        $('.check-in').data("DateTimePicker").maxDate(e.date);
    });
    
    // Collapse filter
    $('.filters-btn').click(function(){
        $('.filters').toggleClass('hidden-xs');
    });
    
    // Slider
    
    $(".price-range").slider({});
    $(".price-range").on("slide", function(slideEvt) {
        $(".low-value").text(slideEvt.value[0]);
        $(".high-value").text(slideEvt.value[1]);
    });
    $(".price-range").on("slideStop", function(slideEvt) {
        $(".low-value").text(slideEvt.value[0]);
        $(".high-value").text(slideEvt.value[1]);
    });

});