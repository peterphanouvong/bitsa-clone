(function ($) {
 "use strict";
	

/*----------------------------
 Navbar nav
------------------------------ */
    var menu_btn = $('.menu-btn');
    menu_btn.on("click", function () {
        $(this).toggleClass("active");
        $(".icon-header").toggleClass("active");
    });
/*---------------------
 TOP Menu Stick
--------------------- */
var s = $(window);
  var sticky_id = $("#sticker");
  s.on('scroll',function() {    
    var scroll = s.scrollTop();
    if (scroll < 300) {
      sticky_id.removeClass("stick");
    }else{
      sticky_id.addClass("stick");
    }
  });
/*---------------------
  venobox
--------------------- */
    var veno_box = $('.venobox');
    veno_box.venobox();
	
/*--------------------------
preloader
---------------------------- */	
	$(window).on('load',function(){
		var pre_loader = $('#preloader')
	pre_loader.fadeOut('slow',function(){$(this).remove();});
	});	
/*----------------------------
 jQuery MeanMenu
------------------------------ */
    var mean_menu = $('nav#dropdown');
    mean_menu.meanmenu();

/*--------------------------
 scrollUp
---------------------------- */
	$.scrollUp({
		scrollText: '<i class="fa fa-angle-up"></i>',
		easingType: 'linear',
		scrollSpeed: 900,
		animation: 'fade'
	});
	
/*----------------------------
 isotope active
------------------------------ */
	// portfolio start
    $(window).on("load",function() {
        var $container = $('.portfolio-content');
        $container.isotope({
            filter: '*',
            animationOptions: {
                duration: 750,
                easing: 'linear',
                queue: false
            }
        });
        $('.portfolio-menu li a').on("click", function() {
            $('.portfolio-menu li a.active').removeClass('active');
            $(this).addClass('active');
            var selector = $(this).attr('data-filter');
            $container.isotope({
                filter: selector,
                animationOptions: {
                    duration: 750,
                    easing: 'linear',
                    queue: false
                }
            });
            return false;
        });

    });
    //portfolio end
/*----------------------------
 isotope for events
------------------------------ */
	// portfolio start
    $(window).on("load",function() {
        var $container = $('.portfolio-content-events');
        $container.isotope({
            filter: '.all',
            animationOptions: {
                duration: 750,
                easing: 'linear',
                queue: false
            }
        });
        $('.all').css('position', 'relative');
        $('.portfolio-menu li a').on("click", function() {
            $('.portfolio-menu li a.active').removeClass('active');
            $(this).addClass('active');
            var selector = $(this).attr('data-filter');
            $container.isotope({
                filter: selector,
                animationOptions: {
                    duration: 750,
                    easing: 'linear',
                    queue: false
                }
            });
            $(selector).css('position', 'relative');
            return false;
        });

    });
    //portfolio end

/*--------------------------
isotope for our team 
---------------------------- */
//isotope for ourteam
$(window).on("load", function () {
    var $container = $('.portfolio-content-ourteam');
    $container.isotope({
        filter: '.2020',
        animationOptions: {
            duration: 750,
            easing: 'linear',
            queue: false
        }
    });
    $('.2020').css('position', 'relative');
    $('.portfolio-menu li a').on("click", function () {
        $('.portfolio-menu li a.active').removeClass('active');
        $(this).addClass('active');
        var selector = $(this).attr('data-filter');
        $container.isotope({
            filter: selector,
            animationOptions: {
                duration: 750,
                easing: 'linear',
                queue: false
            }
        });
        $(selector).css('position', 'relative');
        return false;
    });
});

//end of isotope for ourteam

/*--------------------------
    bitsa mag isotope
---------------------------- */
$(window).on("load", function () {
    var $container = $('.BITSA-mag');
    $container.isotope({
        filter: '.2019',
        animationOptions: {
            duration: 750,
            easing: 'linear',
            queue: false
        }
    });
    $('.2019').css('position', 'relative');
    $('.2019').css('height', 'auto');
    
    $('.portfolio-menu li a').on("click", function () {
        $('.portfolio-menu li a.active').removeClass('active');
        $(this).addClass('active');
        var selector = $(this).attr('data-filter');
        $container.isotope({
            filter: selector,
            animationOptions: {
                duration: 750,
                easing: 'linear',
                queue: false
            }
        });
        $(selector).css('position', 'relative');
        return false;
    });

});




/*--------------------------
     slider carousel
---------------------------- */
    $('.intro-carousel').owlCarousel({
        loop:true,
        nav:true,		
        autoplay:false,
        dots:false,
        navText: ["<i class='icon icon-chevron-left'></i>","<i class='icon icon-chevron-right'></i>"],
        responsive:{
            0:{
                items:1
            },
            600:{
                items:1
            },
            1000:{
                items:1
            }
        }
    });

/*---------------------
 Testimonial carousel
---------------------*/
    var test_carousel = $('.testimonial-carousel');
    test_carousel.owlCarousel({
        loop:true,
        nav:false,
        dots:true,
		margin:50,
        autoplay:true,
        responsive:{
            0:{
                items:1
            },
            768:{
                items:2
            },
            1000:{
                items:2
            }
        }
    });
/*--------------------------
     Project carousel
---------------------------- */

    $('.project-carousel').owlCarousel({
        loop:true,
        nav:true,		
        autoplay:true,
        dots:false,
        navText: ["<i class='icon icon-chevron-left'></i>","<i class='icon icon-chevron-right'></i>"],
        responsive:{
            0:{
                items:1
            },
            600:{
                items:1
            },
            1000:{
                items:1
            }
        }
    });
/*----------------------------
  brand-carousel-carousel
------------------------------ */  
    $('.brand-carousel').owlCarousel({
        loop:true,
        margin:30,
        nav:false,		
        autoplay:true,
        dots:false,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:3
            },
            1000:{
                items:6
            }
        }
    });
/*--------------------------
     preloader
---------------------------- */	
    $(window).on('load',function(){
        $('#preloader').fadeOut('slow',function(){$(this).remove();});
    });
	
/*--------------------------
     contact-from
---------------------------- */
    $("#contactForm").on("submit", function (event) {
        if (event.isDefaultPrevented()) {
            // handle the invalid form...
            formError();
            submitMSG(false, "Did you fill in the form properly?");
        } else {
            // everything looks good!
            event.preventDefault();
            submitForm();
        }
    });
    function submitForm(){
        // Initiate Variables With Form Content
        var name = $("#name").val();
        var email = $("#email").val();
        var msg_subject = $("#msg_subject").val();
        var message = $("#message").val();


        $.ajax({
            type: "POST",
            url: "assets/contact.php",
            data: "name=" + name + "&email=" + email + "&msg_subject=" + msg_subject + "&message=" + message,
            success : function(text){
                if (text == "success"){
                    formSuccess();
                } else {
                    formError();
                    submitMSG(false,text);
                }
            }
        });
    }

    function formSuccess(){
        $("#contactForm")[0].reset();
        submitMSG(true, "Message Submitted!")
    }

    function formError(){
        $("#contactForm").removeClass().addClass('shake animated').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function(){
            $(this).removeClass();
        });
    }

    function submitMSG(valid, msg){
        if(valid){
            var msgClasses = "h3 text-center tada animated text-success";
        } else {
            var msgClasses = "h3 text-center text-danger";
        }
        $("#msgSubmit").removeClass().addClass(msgClasses).text(msg);
    }
    
	
/*----------------------------
   Typed Text
------------------------------ */
    var content = $(".typed_text");

    $(function() {
        content.typed({
            strings: ["Web Development.", "Graphic Design.", "Social Marketing."],
            typeSpeed: 100,
            loop: true,
        });
    });		

})(jQuery); 

/*----------------------------
    FORM
------------------------------ */
function insert_value() {
    var name = $("#name").val();
    var zID = $("#zID").val();
    alert($("#zID").val());
    if ($("#zID").val().charAt(0) !== 'z') {
        alert("ZID Must Start with z");
    }
    var email = $("#email").val();
    var degree = other_degree_value();
    var yearOfStudy = $("#yearOfStudy").val();
    var isArcMember = $("#isArcMember").val();
    var includeML = $("#includeML").val();
    var url = script_url + "?callback-ctrlq&name=" + name + "&zID=" + zID + "&email=" + email + "&degree=" + degree + "&yearOfStudy=" + yearOfStudy + "&isArcMember=" + isArcMember + "&includeML=" + includeML + "&action=insert";

    // if (var_degree === "Other"){
    //     var degree = $("#otherDegree").val();
    // }
    // else{
    //     var degree = $("#degree option:selected").val();
    // }
    //alert(url);
    var request = jQuery.ajax({
        crossDomain: true,
        url: url,
        method: "GET",
        dataType: "jsonp"
    });
    document.getElementById("form").reset();
    $("#otherDegree").hide();
    ctrlq();
    $(".content-section").hide();
    $("#Registered").show();


}
function ctrlq(e) {
    // alert("Congrats! Registered Successfully")
}
$(document).ready(function () {
    $("#degree").on("change", function () {
        if ($(this).val() === "Other") {
            $("#otherDegree").show();
        }
        else {
            $("#otherDegree").hide();
            $("#dergeeInput").hide();
        }
    });
});

function other_degree_value() {
    if ($("#degree").val() === "Other") {
        var degree = $("#otherDegree").val();
    }
    else {
        var degree = $("#degree option:selected").val();
    }

    return degree;
}
(jQuery);

//I dont know about the script_url stuff so i didnt put it in the main function
// this comment is by ALI
var script_url = "https://script.google.com/a/bitsa.org.au/macros/s/AKfycbyE_iz-YoWObGPKwZPdX4I8L5uvnHQwWQzkz6V1/exec";

/*----------------------------
FORM
------------------------------ */
function insert_value() {
var name = $("#name").val();
var zID = $("#zID").val();
//  
var email = $("#email").val();
var degree = other_degree_value();
var yearOfStudy = $("#yearOfStudy").val();
var isArcMember = $("#isArcMember").val();
var includeML = $("#includeML").val();
var url = script_url + "?callback-ctrlq&name=" + name + "&zID=" + zID + "&email=" + email + "&degree=" + degree + "&yearOfStudy=" + yearOfStudy + "&isArcMember=" + isArcMember + "&includeML=" + includeML + "&action=insert";

// if (var_degree === "Other"){
//     var degree = $("#otherDegree").val();
// }
// else{
//     var degree = $("#degree option:selected").val();
// }
//alert(url);
// Above is debugging scripts used

//ALI - i tried adding a statement to make sure a z is added before ur zid numbers
// if ($("#zID").val().charAt(0) !== 'z') {
//     alert("zID Must Start with z");
// } else {
var request = jQuery.ajax({
    crossDomain: true,
    url: url,
    method: "GET",
    dataType: "jsonp"
});
document.getElementById("form").reset();
$("#otherDegree").hide();
ctrlq();
$(".content-section").hide();
$("#Registered").show();
//}

}
// function ctrlq(e) {
// alert("Congrats! Registered Successfully")
// }
$(document).ready(function () {
$("#degree").on("change", function () {
    if ($(this).val() === "Other") {
        $("#otherDegree").show();
    }
    else {
        $("#otherDegree").hide();
        $("#dergeeInput").hide();
    }
});
});

function other_degree_value() {
if ($("#degree").val() === "Other") {
    var degree = $("#otherDegree").val();
}
else {
    var degree = $("#degree option:selected").val();
}

return degree;
}