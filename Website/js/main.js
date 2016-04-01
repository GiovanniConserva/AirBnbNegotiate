$(document).ready(function(){
    
    $('.navbar-toggle').click(function(){
        $('.menu-btn').toggleClass("white");
    });
    
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
    
});